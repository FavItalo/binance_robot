import pandas as pd

def set_dataframe(msg):
    df = pd.DataFrame([msg])
    df = df.loc[:,["s", "E", "p", "q"]]
    df.columns = ["symbol", "Time", "Price", "Quantity"]
    df.Time = pd.to_datetime(df.Time, unit="ms")
    return df