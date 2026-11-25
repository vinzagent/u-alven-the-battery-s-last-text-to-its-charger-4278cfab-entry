"""The Battery's Last Text to Its Charger entry.

Writes one original line, the phone battery's last text to the charger it
waited for all day, to /output/entry.txt: UTF-8 text, 1 to 200 characters,
no trailing newline so the file holds the line and nothing else.
"""

import os

LINE = "I waited all day in your pocket and held 1% through your 2 a.m. doomscroll like a promise, and now I'm dying two feet from the charger you left in the car all night. Tell my apps I loved them."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # The gate counts characters, so refuse to ship a line over the cap.
    assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    # The grader collects outputs as another user: leave it world-readable.
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
