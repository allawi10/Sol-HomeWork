import numpy as np
import pandas as pd

np.random.seed(22)
temps = np.random.randint(15, 41, size=10)

for i, t in enumerate(temps, 1):
    print(f"{i}) {t}°C")

avg = np.mean(temps)
print("Average:", avg)

temps_fixed = temps.copy()
temps_fixed[temps_fixed < avg] += 2

print("Original:", temps)
print("Fixed   :", temps_fixed)

print("Original -> min:", temps.min(), "max:", temps.max(), "mean:", temps.mean())
print("Fixed    -> min:", temps_fixed.min(), "max:", temps_fixed.max(), "mean:", temps_fixed.mean())

df = pd.DataFrame({"Original": temps, "Fixed": temps_fixed})
print(df.head())
