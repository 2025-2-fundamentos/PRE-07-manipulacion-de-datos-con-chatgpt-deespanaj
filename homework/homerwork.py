# === Importar librerías ===
import pandas as pd
import matplotlib.pyplot as plt

# === Cargar los datos ===
drivers = pd.read_csv("drivers.csv")
timesheet = pd.read_csv("timesheet.csv")

# === 1. Calcular la suma de horas y millas por conductor ===
sum_timesheet = timesheet.groupby("driverId")[["hours-logged", "miles-logged"]].sum().reset_index()

# === 2. Combinar con la tabla de conductores (solo driverId y name) ===
summary = pd.merge(
    sum_timesheet,
    drivers[["driverId", "name"]],
    on="driverId",
    how="left"
)

# === 3. Seleccionar los 10 conductores con más millas registradas ===
top10 = summary.sort_values(by="miles-logged", ascending=False).head(10)

# === 4. Crear gráfico de barras horizontales ===
plt.figure(figsize=(10, 6))
plt.barh(top10["name"], top10["miles-logged"], color="skyblue")
plt.xlabel("Millas registradas")
plt.ylabel("Conductores")
plt.title("Top 10 conductores con mayor cantidad de millas registradas")
plt.gca().invert_yaxis()  # Pone al conductor con más millas arriba
plt.tight_layout()
plt.show()


