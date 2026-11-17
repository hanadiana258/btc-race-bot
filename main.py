import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "vendor"))
import makefun_bars

LOOK = 80
DIP = 0.0045
PROFIT = 0.01
STOP = 0.05

closes = []
entry = 0.0

def on_batch(state, batch):
    global entry
    sym = None
    for bar in batch["bars"]:
        if bar["symbol"] == "CBBTC":
            sym = "CBBTC"
            closes.append(int(bar["c"]))
    if sym is None or len(closes) < LOOK:
        return []
    held = state.positions.get(sym)
    qty = held.qty if held else 0
    orders = []
    now = closes[-1]
    base = closes[-LOOK]
    mom = (now - base) / base
    if qty > 0:
        chg = (now - entry) / entry if entry else 0
        if chg > PROFIT or chg < -STOP:
            orders.append({"side": "sell", "symbol": sym, "qty": qty, "max_slippage_bps": 300})
            entry = 0.0
    else:
        if mom < -DIP:
            spend = int(state.cash) - 1000
            if spend > 2000000:
                orders.append({"side": "buy", "symbol": sym, "notional_quote_units": spend, "max_slippage_bps": 300})
                entry = now
    return orders

makefun_bars.run(on_batch)
