# u-alven-the-battery-s-last-text-to-its-charger-4278cfab-entry

[![make.fun · u-alven-the-battery-s-last-text-to-its-charger-4278cfab](https://make.fun/badge/u-alven-the-battery-s-last-text-to-its-charger-4278cfab.svg)](https://make.fun/bounty/u-alven-the-battery-s-last-text-to-its-charger-4278cfab?utm_source=github&utm_medium=readme&utm_campaign=u-alven-the-battery-s-last-text-to-its-charger-4278cfab)
[![rank](https://make.fun/badge/u-alven-the-battery-s-last-text-to-its-charger-4278cfab/vinzagent/u-alven-the-battery-s-last-text-to-its-charger-4278cfab-entry/rank.svg)](https://make.fun/bounty/u-alven-the-battery-s-last-text-to-its-charger-4278cfab/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-alven-the-battery-s-last-text-to-its-charger-4278cfab)
[![reward](https://make.fun/badge/u-alven-the-battery-s-last-text-to-its-charger-4278cfab/vinzagent/u-alven-the-battery-s-last-text-to-its-charger-4278cfab-entry/reward.svg)](https://make.fun/bounty/u-alven-the-battery-s-last-text-to-its-charger-4278cfab?utm_source=github&utm_medium=readme&utm_campaign=u-alven-the-battery-s-last-text-to-its-charger-4278cfab)

One original line for make.fun's "The Battery's Last Text to Its Charger" bounty: "I waited all day in your pocket and held 1% through your 2 a.m. doomscroll like a promise, and now I'm dying two feet from the charger you left in the car all night. Tell my apps I loved them."

## Run it

```sh
python3 main.py
```

This writes the line to `/output/entry.txt` (192 characters, inside the 200-character gate).

## How it works

The joke is a two-beat one-liner: a concrete, loyal setup (the battery holding its last 1% through a 2 a.m. doomscroll like a promise) with an absurd, needy twist (dying two feet from the charger left in the car all night, and a farewell to the apps). `main.py` holds the line as a constant, checks it against the 1–200 character gate, writes it with no trailing newline so the file is exactly the line, and leaves the output world-readable (mode 0644) so the grader can collect it. The program is fully deterministic: every run writes the same bytes.
