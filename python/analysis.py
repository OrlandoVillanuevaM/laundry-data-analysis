import pandas as pd

# =========================
# CARGA DE DATOS
# =========================

df = pd.read_csv("data/usage_cycles.csv")

# =========================
# LIMPIEZA
# =========================

# Convertir fechas
df["start_time"] = pd.to_datetime(df["start_time"], errors="coerce")
df["end_time"] = pd.to_datetime(df["end_time"], errors="coerce")

# Eliminar filas con errores
df = df.dropna()

# =========================
# FEATURE ENGINEERING
# =========================

# Duración en minutos
df["duration_min"] = (df["end_time"] - df["start_time"]).dt.total_seconds() / 60

# Hora
df["hour"] = df["start_time"].dt.hour

# Día de la semana
df["day_of_week"] = df["start_time"].dt.day_name()

# =========================
# KPIs
# =========================

total_cycles = len(df)
total_revenue = df["price"].sum()
avg_duration = df["duration_min"].mean()

print("📊 KPIs GENERALES")
print("Total ciclos:", total_cycles)
print("Ingresos totales:", round(total_revenue, 2))
print("Duración promedio:", round(avg_duration, 2), "min")

# =========================
# HORAS PICO
# =========================

peak_hours = df.groupby("hour").size().sort_values(ascending=False).head(3)

print("\n⏰ Horas pico:")
print(peak_hours)

# =========================
# TOP USUARIOS
# =========================

top_users = df.groupby("resident_id").size().sort_values(ascending=False).head(5)

print("\n👤 Top usuarios:")
print(top_users)

# =========================
# EXPORTAR DATA LIMPIA
# =========================

df.to_csv("data/clean_usage_cycles.csv", index=False)

print("\n✅ Archivo limpio generado: clean_usage_cycles.csv")
