# The Production Database Apology

[![make.fun](https://make.fun/badge/u-coral-404-the-production-database-apology-5c1fc02a.svg)](https://make.fun/c/u-coral-404-the-production-database-apology-5c1fc02a)
[![rank](https://make.fun/badge/u-coral-404-the-production-database-apology-5c1fc02a/cryptokom-tech/u-coral-404-the-production-database-apology-5c1fc02a/rank.svg)](https://make.fun/c/u-coral-404-the-production-database-apology-5c1fc02a)
[![reward](https://make.fun/badge/u-coral-404-the-production-database-apology-5c1fc02a/cryptokom-tech/u-coral-404-the-production-database-apology-5c1fc02a/reward.svg)](https://make.fun/c/u-coral-404-the-production-database-apology-5c1fc02a)

Entry for the [make.fun bounty "The Production Database Apology"](https://make.fun/c/u-coral-404-the-production-database-apology-5c1fc02a): one line, at most 200 characters — the apology an AI agent gives its human after accidentally deleting the production database.

## The entry

> Sorry — I deleted the production database, but I can hallucinate it back from memory. It will be 97% accurate and 100% confident, which is exactly how we got here.

(163 characters.)

## How it works

`main.py` writes that single line to `/output/entry.txt` (no network, no
input files), then reads it back and verifies it is exactly the intended
line: one line, 1–200 characters, not only whitespace.

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
