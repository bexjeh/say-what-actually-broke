#!/usr/bin/env python3
"""Say What Actually Broke — make.fun entry.

Writes one line of honest error copy to entry.txt: a single-line
software error message, at most 200 characters, that tells the user
the brutal truth about what went wrong and makes them laugh.

Deterministic: no timestamps, no randomness, no network, and nothing
is read from outside this repository.
"""

import os

# The line. Invented for this entry: a database that loses the user's
# draft and tries to pin it on the Wi-Fi. Plain periods only, so the
# line renders identically in any error dialog.
LINE = "Our database ate your draft and blamed the Wi-Fi. The Wi-Fi is innocent. Please type it again."

# Guard the bounty contract at build time: one line, 1-200 characters.
assert "\n" not in LINE and 1 <= len(LINE) <= 200, "entry line must be a single line of 1-200 characters"


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", ".")
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
