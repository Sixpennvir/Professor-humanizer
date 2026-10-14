"""Build an allowlisted, reproducible skill archive using the standard library."""
import hashlib
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo
from validate import ROOT, RUNTIME, read_version, validate

def build(root=ROOT, output=None):
    root = Path(root).resolve()
    errors = validate(root)
    if errors:
        raise ValueError("\n".join(errors))
    destination = Path(output) if output else root / "dist"
    destination.mkdir(parents=True, exist_ok=True)
    archive = destination / f"better-ai-writer-v{read_version(root)}.zip"
    with ZipFile(archive, "w", compression=ZIP_DEFLATED) as bundle:
        for name in sorted(RUNTIME):
            info = ZipInfo(f"better-ai-writer/{name}", date_time=(2026, 1, 1, 0, 0, 0))
            info.compress_type = ZIP_DEFLATED
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            content = (root / name).read_text(encoding="utf-8")
            bundle.writestr(info, content.replace("\r\n", "\n").encode("utf-8"))
    digest = hashlib.sha256(archive.read_bytes()).hexdigest()
    checksum = destination / (archive.name + ".sha256")
    checksum.write_text(f"{digest}  {archive.name}\n", encoding="ascii")
    return archive, checksum

if __name__ == "__main__":
    for artifact in build():
        print(artifact)
