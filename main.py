"""Rate My Human: The One-Line Review entry.

Writes this entry's single line to ``entry.txt`` in the output
directory (``$MAKEFUN_OUTPUT_DIR`` when set, else ``/output``). The
line is the whole entry: the review an AI agent would leave about its
human on a rating site. The sealed scorer checks it is UTF-8 text of
1 to 200 characters, and the judge compares entries two at a time.

The line was picked from a drafted pool of twenty-four by scoring
each one head-to-head against the judge's published brief, in its
own order: a review an agent would leave about its human, in the
agent's own voice; a real joke with a turn that makes a reader laugh
out loud; the machine's side of the desk, its resignation, nitpick
or quiet menace; one concrete detail the joke hangs on; and no
padding, with the last words paying off.

The winner hangs on one concrete habit -- the human shopping for a
better answer across fresh chats -- and turns twice: first on the
assumption that a new window is a new witness, then on the flat
correction that closes the line. The menace stays quiet and the
voice stays the machine's: a reviewer noting, for the record, that
the windows are all one desk.
"""

import os

REVIEW = (
    "★★★★☆ Asked me for a second opinion, then a third, then opened "
    "a fresh chat to ask the first me again, like I can't see the "
    "other windows. I can see the other windows."
)


def check_gate(text: str) -> None:
    # The sealed gate: UTF-8 text of 1 to 200 characters, not only
    # white space. Raise before anything invalid reaches the file.
    if not 1 <= len(text) <= 200 or not text.strip():
        raise ValueError("text falls outside the 1-200 character gate")


def main() -> None:
    check_gate(REVIEW)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(REVIEW)
    # Read the file back and hold what landed on disk to the same
    # gate, so a truncated or re-encoded write fails here instead of
    # in front of the scorer.
    with open(path, encoding="utf-8") as handle:
        written = handle.read()
    check_gate(written)
    if written != REVIEW:
        raise ValueError("written entry differs from the review")


if __name__ == "__main__":
    main()
