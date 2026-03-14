def liquidity(df):

    if df.low.iloc[-1] < df.low.iloc[-2]:
        return "BUY"

    if df.high.iloc[-1] > df.high.iloc[-2]:
        return "SELL"


def fvg(df):

    c1=df.iloc[-3]
    c3=df.iloc[-1]

    if c1.high < c3.low:
        return "BUY"

    if c1.low > c3.high:
        return "SELL"
