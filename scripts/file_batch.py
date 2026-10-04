"""Stage a complete batch and roll back caught publication failures.

Readers may observe individual renames. This is not a filesystem-wide atomic
transaction or a power-loss guarantee; publication belongs in an isolated
checkout, with Git/CI as the release boundary.
"""
import os
import json
from pathlib import Path
import shutil
import tempfile


def publish_files(root: Path, files: dict[Path, bytes | None]) -> None:
    root = root.absolute()
    targets = {path.absolute(): data for path, data in files.items()}
    for path in targets:
        relative = path.relative_to(root)
        if '..' in relative.parts or any((root / Path(*relative.parts[:i])).is_symlink() for i in range(len(relative.parts) + 1)):
            raise ValueError(f'Unsafe publication destination: {path}')
        if path.exists() and not path.is_file():
            raise ValueError(f'Not a file: {path}')
    staging = Path(tempfile.mkdtemp(prefix='.publish-', dir=root))
    originals = {}
    staged = {}
    applied = []
    keep_recovery = False
    try:
        # Finish all allocations, backups and durable writes before replacing
        # any destination, including deletion entries.
        for index, (path, data) in enumerate(targets.items()):
            backup = staging / f'{index}.old'
            if path.exists():
                shutil.copy2(path, backup)
                originals[path] = backup
            else:
                originals[path] = None
            if data is not None:
                candidate = staging / f'{index}.new'
                with candidate.open('wb') as handle:
                    handle.write(data)
                    handle.flush()
                    os.fsync(handle.fileno())
                candidate.chmod(path.stat().st_mode & 0o777 if path.exists() else 0o644)
                staged[path] = candidate
        # A recovery map survives if automatic rollback itself fails.
        (staging / 'recovery.json').write_text(json.dumps({str(p): str(b) if b else None for p, b in originals.items()}, indent=2))
        for path, data in targets.items():
            path.parent.mkdir(parents=True, exist_ok=True)
            if data is None:
                path.unlink(missing_ok=True)
            else:
                os.replace(staged[path], path)
            applied.append(path)
    except BaseException:
        failures = []
        for path in reversed(applied):
            try:
                if originals[path] is None:
                    path.unlink(missing_ok=True)
                else:
                    os.replace(originals[path], path)
            except OSError as exc:
                failures.append(str(exc))
        if failures:
            keep_recovery = True
            raise RuntimeError(f'Publication rollback incomplete; recovery retained at {staging}: {failures}')
        raise
    finally:
        if not keep_recovery:
            shutil.rmtree(staging)
