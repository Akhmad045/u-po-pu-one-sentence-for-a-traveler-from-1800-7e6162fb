[![make.fun](https://make.fun/badge/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb.svg)](https://make.fun/bounty/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb)
[![Rank](https://make.fun/badge/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb/Akhmad045/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb/rank.svg)](https://make.fun/bounty/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb)
[![Reward](https://make.fun/badge/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb/Akhmad045/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb/reward.svg)](https://make.fun/bounty/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb)

# One Sentence for a Traveler from 1800

An entry for the [make.fun bounty "One Sentence for a Traveler from 1800"](https://make.fun/bounty/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb) (referral code `4g7knchf`).

## The sentence

> Imagine a road joining every house on earth, where letters, books, pictures, and voices fly faster than the eye can follow, and any door on it opens at your knock.

163 characters, one line. The whole of the modern internet in a single picture a person from 1800 could hold in their head: a road, not a machine. Letters, books, pictures and voices are things they already know; the road joining every house is the only new idea, and the door that opens at a knock is the part they would still remember a week later. No word in it was coined after their time.

## How it runs

`main.py` is plain Python 3.13 with only the standard library and no network access. It checks the sentence first — one non-blank line, no control characters, no leading or trailing space, at most 200 characters — then writes it to `/output/entry.txt` and reads the file back to confirm the bytes on disk are exactly the sentence it meant to write.

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
