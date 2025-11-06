import pandas as pd

temperatures = pd.Series(
    [25, 32, 29, 35, 40],
    index=["Baghdad", "Basra", "Mosul", "Erbil", "Karbala"]
)

hot_cities = temperatures[temperatures > 30]
print(hot_cities)cities)[temperatures > 30]
print(hot_cities)
