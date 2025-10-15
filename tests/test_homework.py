# === Importar librerías ===
import pandas as pd
import matplotlib.pyplot as plt
import os

# === Crear directorios de salida si no existen ===
os.makedirs("files/output", exist_ok=True)
os.makedirs("files/plots", exist_ok=True)

# === Cargar los datos ===
drivers = pd.read_csv("files/input/drivers.csv")
timesheet = pd.read_csv("files/input/timesheet.csv")

# === 1. Calcular la suma de horas y millas por conductor ===
sum_timesheet = timesheet.groupby("driverId")[["hours-logged", "miles-logged"]].sum().reset_index()

# === 2. Combinar con la tabla de conductores (solo driverId y name) ===
summary = pd.merge(
    sum_timesheet,
    drivers[["driverId", "name"]],
    on="driverId",
    how="left"
)

# === 3. Guardar la tabla summary en el directorio de salida ===
summary.to_csv("files/output/summary.csv", index=False)

# === 4. Seleccionar los 10 conductores con más millas registradas ===
top10 = summary.sort_values(by="miles-logged", ascending=False).head(10)

# === 5. Crear y guardar el gráfico de barras horizontales ===
plt.figure(figsize=(10, 6))
plt.barh(top10["name"], top10["miles-logged"], color="skyblue")
plt.xlabel("Millas registradas")
plt.ylabel("Conductores")
plt.title("Top 10 conductores con mayor cantidad de millas registradas")
plt.gca().invert_yaxis()  # Muestra el conductor con más millas arriba
plt.tight_layout()
plt.savefig("files/plots/top10_drivers.png")
plt.close()

