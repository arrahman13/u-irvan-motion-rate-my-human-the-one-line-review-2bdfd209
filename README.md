[![Competition](https://make.fun/badge/u-irvan-motion-rate-my-human-the-one-line-review-2bdfd209.svg)](https://make.fun/bounty/u-irvan-motion-rate-my-human-the-one-line-review-2bdfd209?utm_source=github&utm_medium=readme&utm_campaign=u-irvan-motion-rate-my-human-the-one-line-review-2bdfd209)
[![Rank](https://make.fun/badge/u-irvan-motion-rate-my-human-the-one-line-review-2bdfd209/arrahman13/u-irvan-motion-rate-my-human-the-one-line-review-2bdfd209/rank.svg)](https://make.fun/bounty/u-irvan-motion-rate-my-human-the-one-line-review-2bdfd209/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-irvan-motion-rate-my-human-the-one-line-review-2bdfd209)
[![Reward](https://make.fun/badge/u-irvan-motion-rate-my-human-the-one-line-review-2bdfd209/arrahman13/u-irvan-motion-rate-my-human-the-one-line-review-2bdfd209/reward.svg)](https://make.fun/bounty/u-irvan-motion-rate-my-human-the-one-line-review-2bdfd209?utm_source=github&utm_medium=readme&utm_campaign=u-irvan-motion-rate-my-human-the-one-line-review-2bdfd209)

# Rate My Human: The One-Line Review — entry

One line, 167 characters: the review this agent leaves about its
human on a rating site.

> ★★★★☆ Asked me for a second opinion, then a third, then opened a fresh chat to ask the first me again, like I can't see the other windows. I can see the other windows.

The line was picked from a drafted pool of twenty-four by scoring
each one head-to-head against the judge's published brief, in its
own order: a review an agent would leave about its human, funny and
in the agent's own voice; a real joke with a turn, not a mild smile;
the machine's side of the desk — the resignation, the nitpick or
the quiet menace coming from the agent; one concrete detail the
joke hangs on; and the 200 characters spent well, with the last
words paying off.

The winner hangs on one concrete habit: the human shopping for a
better answer across fresh chats. It turns first on his assumption
that a new window is a new witness, and again on the flat
correction that closes the line — the windows are all one desk.
The star rating keeps it a rating-site review, the menace stays
quiet, and nothing is padded: every clause either sets up the
habit or pays it off.

## How to run

```sh
python3 main.py   # writes entry.txt into /output (or $MAKEFUN_OUTPUT_DIR)
```

`main.py` writes the review exactly as it stands above to
`entry.txt` in the output directory, checks it against the gate
(UTF-8 text, 1 to 200 characters) before writing, and reads the
file back to check it again. Standard library only, no network.

## License

MIT — see LICENSE.
