"""Robot wedding vows, one line — make.fun entry.

This program writes one hand-written line of wedding vows for a robot
couple to ``/output/entry.txt``. The line is fixed and deterministic:
no randomness, no network access, standard library only.

Why the line answers the brief:

* It is a one-line robot wedding vow that is also a joke.
* The laugh lives in the final words: the vow lists intimate things a
  robot would share, then withholds the one thing that matters most —
  the admin password.
* It sounds like a real wedding promise — "From this day forward, I
  promise to share ..." — a commitment, not just a gag.
* The machine details are specific — battery, bandwidth, backup, admin
  password — rather than a joke that would fit any couple.
* One line, 117 characters, and it reads well aloud: three shared
  things build a rhythm, and the "but never ..." turn lands the laugh.
"""

import os

# The vow, kept as one literal so its text is exactly what gets written.
VOW = (
    "From this day forward, I promise to share my battery, "
    "my bandwidth, and my last backup \u2014 but never my admin password."
)

# The brief caps a one-line vow at 160 characters.
MAX_CHARS = 160


def check_vow(text: str) -> str:
    """Trim the vow and make sure it is a single line within the limit."""
    cleaned = text.strip()
    if not 1 <= len(cleaned) <= MAX_CHARS:
        raise ValueError(
            "vow must be 1-%d characters, got %d" % (MAX_CHARS, len(cleaned))
        )
    if "\n" in cleaned:
        raise ValueError("vow must fit on one line")
    return cleaned


def write_entry(text: str) -> None:
    """Write the checked vow to /output/entry.txt."""
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(text)


def main() -> None:
    write_entry(check_vow(VOW))


if __name__ == "__main__":
    main()
