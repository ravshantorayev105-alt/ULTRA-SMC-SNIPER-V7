df = get_data(pair,"5min",API_KEY)

price = df.close.iloc[-1]

sl,tp = calc(price)

text=f"""
ULTRA SMC SNIPER

PAIR: {pair}
TYPE: {lq}

ENTRY: {price}
SL: {sl}
TP: {tp}
"""
