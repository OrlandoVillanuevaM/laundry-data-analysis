import pandas as pd

df = pd.read_csv("data/clean_usage_cycles.csv")

def chatbot():
    print("🤖 Chatbot de Lavandería (escribe 'salir' para terminar)\n")

    while True:
        pregunta = input("Pregunta: ").lower()

        if pregunta == "salir":
            print("👋 Hasta luego")
            break

        elif "ciclos" in pregunta:
            print("Total ciclos:", len(df))

        elif "ingresos" in pregunta:
            print("Ingresos totales:", round(df["price"].sum(), 2))

        elif "hora pico" in pregunta:
            peak = df.groupby("hour").size().idxmax()
            print(f"La hora pico es: {peak}:00")

        elif "usuarios" in pregunta:
            print("Usuarios únicos:", df["resident_id"].nunique())

        else:
            print("No entiendo esa pregunta aún 🤔")

chatbot()
