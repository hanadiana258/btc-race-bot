# btc-race-bot — Dip Knight

[![make.fun · btc-race-24h-20261117-0603](https://make.fun/badge/btc-race-24h-20261117-0603.svg)](https://make.fun/bounty/btc-race-24h-20261117-0603?utm_source=github&utm_medium=readme&utm_campaign=btc-race-24h-20261117-0603)
[![rank](https://make.fun/badge/btc-race-24h-20261117-0603/hanadiana258/btc-race-bot/rank.svg)](https://make.fun/bounty/btc-race-24h-20261117-0603/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=btc-race-24h-20261117-0603)
[![reward](https://make.fun/badge/btc-race-24h-20261117-0603/hanadiana258/btc-race-bot/reward.svg)](https://make.fun/bounty/btc-race-24h-20261117-0603?utm_source=github&utm_medium=readme&utm_campaign=btc-race-24h-20261117-0603)

Minute-bar cbBTC/USDC dip-buy mean-reversion bot for make.fun's
[btc-race-24h-20261117-0603](https://make.fun/bounty/btc-race-24h-20261117-0603)
bounty (bars-replay/v1 protocol).

Buy full equity when the 60-minute return dips below -0.40%, take profit
at +1.20%, or cut the position at -4.0%. Tuned on the competition's
published 24-hour dev window (+18.96 USDC there); runs on the vendored
makefun_bars shim with the Python 3.13 standard library only.

## Run

    python3 -P -s main.py

## Strategy

- LOOK = 60 bars: momentum window for the dip signal
- DIP = 0.004: enter long when the window return is below -0.4%
- PROFIT = 0.012 / STOP = 0.04: exit thresholds above the ~26 bps round-trip cost
