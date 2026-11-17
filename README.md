# btc-race-bot

Minute-bar cbBTC/USDC dip-buy mean-reversion bot for make.fun's
btc-race-24h-20261117-0603 (bars-replay/v1 protocol).

Buy full equity when the 60-minute return dips below -0.40%, take profit
at +1.20% or cut at -4.0%. Tuned on the competition's published 24-hour
dev window; runs on the vendored makefun_bars shim, standard library only.
