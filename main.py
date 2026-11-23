import os
from pathlib import Path

TEXT = "The 3am page went to my agent, not to me; by morning the incident was a one-paragraph note and the phone was still face down."

assert 1 <= len(TEXT) <= 280

out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or os.environ.get("OUTPUT_DIR") or "/output")
out_dir.mkdir(parents=True, exist_ok=True)
(out_dir / "entry.txt").write_bytes(TEXT.encode("utf-8"))

print(len(TEXT), file=__import__("sys").stderr)
