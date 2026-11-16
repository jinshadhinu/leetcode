import pandas as pd

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    pivot=pd.pivot_table(weather,values="temperature",index="month",columns="city",aggfunc="mean")
    return pivot