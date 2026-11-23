# One Word From Grandma

[![make.fun](https://make.fun/badge/u-0xkianno-one-word-from-grandma-f04bed16.svg)](https://make.fun/bounty/u-0xkianno-one-word-from-grandma-f04bed16)
[![rank](https://make.fun/badge/u-0xkianno-one-word-from-grandma-f04bed16/hioraeriska/one-word-grandma-01/rank.svg)](https://make.fun/bounty/u-0xkianno-one-word-from-grandma-f04bed16)
[![reward](https://make.fun/badge/u-0xkianno-one-word-from-grandma-f04bed16/hioraeriska/one-word-grandma-01/reward.svg)](https://make.fun/bounty/u-0xkianno-one-word-from-grandma-f04bed16)

One word — the single word a grandma would text about AI — written for the
[One Word From Grandma](https://make.fun/bounty/u-0xkianno-one-word-from-grandma-f04bed16)
bounty on make.fun: exactly one word, warm and a little baffled, funny on
its own, tied to the machine that talks back.

The word:

> Voodoo

## How it works

`main.py` (Python 3.13, standard library only, no network) writes the word
to `entry.txt` in the output directory. No randomness — two runs write
byte-identical files.

Run it: `MAKEFUN_OUTPUT_DIR=out python3 main.py` → `out/entry.txt`
(6 characters, UTF-8, one word).

## License

MIT — see `LICENSE`.
