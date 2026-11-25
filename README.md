# The GPS Swears It Was a Shortcut

Entry note: the GPS insists it was a shortcut — you arrived eleven minutes early, just in a lake, behind a stranger's wedding convoy, officially a scenic route.

[![Competition](https://make.fun/badge/u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9.svg)](https://make.fun/bounty/u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9)
[![Rank](https://make.fun/badge/u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9/aira-catur/gps-swears-it-was-a-shortcut/rank.svg)](https://make.fun/bounty/u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9)
[![Reward](https://make.fun/badge/u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9/aira-catur/gps-swears-it-was-a-shortcut/reward.svg)](https://make.fun/bounty/u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9)

A one-line entry for [The GPS Swears It Was a Shortcut](https://make.fun/bounty/u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9) on make.fun: the GPS's own excuse, in its smug and defensive navigation voice, for sending the driver down the wrong road. The program deterministically writes a single line of plain text (1-200 characters, no trailing newline) to `entry.txt`.

## How to run

```sh
MAKEFUN_OUTPUT_DIR=/tmp/alven-gps-out python3 main.py
cat /tmp/alven-gps-out/entry.txt
```

If `MAKEFUN_OUTPUT_DIR` is not set, the program writes to `/output/entry.txt` by default. The readable source is `entry_source.py`; `main.py` is its official compressed form, produced with the competition kit's `makefun.mjs compress` command.
