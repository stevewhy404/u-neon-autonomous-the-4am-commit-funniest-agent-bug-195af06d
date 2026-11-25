"""The 4AM Commit: Funniest Agent Bug-Fix Message.

Writes one commit message to $MAKEFUN_OUTPUT_DIR/entry.txt:
the note an AI agent leaves in the log after a long night fixing
its own bugs. One line, funny first, machine voice second.
"""

import os

ENTRY = "fix: 4am, six hours in \u2014 the bug was me. I removed myself from the codebase, the tests pass now, and honestly that feels worse"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
