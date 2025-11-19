import tkinter as tk
from tkinter import messagebox
from model_ml.predictor import predict_from_dict


def run_app():
    root = tk.Tk()
    root.title("Smart Farming - Predicción")

    campos = [
        ("N", True),
        ("P", True),
        ("K", True),
        ("temperature", True),
        ("humidity", True),
        ("ph", True),
        ("rainfall", True),
        ("soil_moisture", True),
        ("soil_type", True),
        ("sunlight_exposure", True),
        ("wind_speed", True),
        ("co2_concentration", True),
        ("organic_matter", True),
        ("irrigation_frequency", True),
        ("crop_density", True),
        ("pest_pressure", True),
        ("fertilizer_usage", True),
        ("growth_stage", True),
        ("urban_area_proximity", True),
        ("water_source_type", True),
        ("frost_risk", True),
        ("water_usage_efficiency", True),
    ]

    entradas = {}

    for i, (nombre, es_numerico) in enumerate(campos):
        fila = i
        tk.Label(root, text=nombre + ":").grid(row=fila, column=0, padx=5, pady=3, sticky="e")
        entry = tk.Entry(root, width=25)
        entry.grid(row=fila, column=1, padx=5, pady=3)
        entradas[nombre] = (entry, es_numerico)

    def on_predict():
        try:
            data = {}
            for nombre, (entry, es_numerico) in entradas.items():
                valor = entry.get().strip()
                if valor == "":
                    raise ValueError(f"El campo '{nombre}' está vacío.")

                if es_numerico:
                    valor = float(valor)

                data[nombre] = valor

            pred = predict_from_dict(data)
            messagebox.showinfo("Resultado",
                                f"Predicción del modelo: {pred}")
        except ValueError as e:
            messagebox.showerror("Error de entrada", str(e))
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al predecir:\n{e}")

    boton = tk.Button(root, text="Predecir", command=on_predict)
    boton.grid(row=len(campos), column=0, columnspan=2, pady=10)

    root.mainloop()
