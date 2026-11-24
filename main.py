# The Funniest Toaster Error Message — writes one deadpan toaster error line
# to /output/entry.txt.
# Python 3.13, standard library only, no network, no secrets, no environment reads.

import os
from pathlib import Path

LINE = "E01: No bread detected. I am a toaster. This is my entire purpose. Please help."

# The gate requires 1-120 characters of non-whitespace UTF-8 text, on one line.
# The joke's shape, per the judge brief: a real appliance error code (E01) and
# voice, then the surprise — the toaster's own existential crisis, not a toast
# pun — with the punch at the end ("Please help."): the appliance asking its
# owner for help inverts who serves whom, in one read.
if not 1 <= len(LINE.strip()) <= 120:
    raise SystemExit(f"entry line must be 1-120 characters, got {len(LINE)}")
if "\n" in LINE:
    raise SystemExit("entry line must be a single line")
if LINE != LINE.strip():
    raise SystemExit("entry line must not have leading or trailing whitespace")

out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
out_dir.mkdir(parents=True, exist_ok=True)
target = out_dir / "entry.txt"
target.write_text(LINE + "\n", encoding="utf-8")
# Confirm what landed on disk is exactly the line above, nothing else.
assert target.read_text(encoding="utf-8").strip() == LINE
print(f"Wrote {len(LINE)} characters to {target}")
