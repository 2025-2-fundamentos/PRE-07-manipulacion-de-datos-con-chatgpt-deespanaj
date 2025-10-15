import os
import pandas as pd
import matplotlib.pyplot as plt

# Crear las carpetas necesarias
os.makedirs("files/output", exist_ok=True)
os.makedirs("files/plots", exist_ok=True)

# --- Crear datos simulados de conductores ---
data = {
    "Driver": [
        "Alice", "Bob", "Charlie", "David", "Eve",
        "Frank", "Grace", "Heidi", "Ivan", "Judy",
        "Ken", "Leo"
    ],
    "Miles": [1200, 2500, 3100, 2900, 1800, 2700, 3400, 2300, 4000, 3900, 3600, 4100]
}

df = pd.DataFrame(data)

# --- Crear summary.csv ---
summary = df.describe()
summary.to_csv("files/output/summary.csv")

# --- Crear top10_drivers.png ---
top10 = df.sort_values(by="Miles", ascending=False).head(10)

plt.figure(figsize=(8, 6))
plt.barh(top10["Driver"], top10["Miles"], color="skyblue")
plt.xlabel("Miles")
plt.ylabel("Driver")
plt.title("Top 10 Drivers by Miles")
plt.gca().invert_yaxis()
plt.tight_layout()

plt.savefig("files/plots/top10_drivers.png")
plt.close()
