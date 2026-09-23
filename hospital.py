import tkinter as tk
from tkinter import messagebox
import random

def generar_cita():
    # Genera un folio y un horario simulado para la cita
    folio = random.randint(1000, 9999)
    return f"Cita Asignada: Hoy a las 16:30 hrs"

def calcular_diagnostico():
    try:
        nombre = entry_nombre.get().strip()
        edad = int(entry_edad.get().strip())
        oxigeno = float(entry_oxigeno.get().strip())
        fc = int(entry_fc.get().strip())
        pa = entry_pa.get().strip()
        peso = float(entry_peso.get().strip())
        talla = float(entry_talla.get().strip())
        imc = peso / (talla ** 2)

        if imc < 18.5:
            estado_peso = "Bajo peso"
        elif 18.5 <= imc < 25.0:
            estado_peso = "Peso normal"
        elif 25.0 <= imc < 30.0:
            estado_peso = "Sobrepeso"
        else:
            estado_peso = "Obesidad"

        diagnostico_texto = (
            f"--- REPORTE MÉDICO DE DIAGNÓSTICO ---\n\n"
            f"Paciente: {nombre} | Edad: {edad} años\n"
            f"Signos Vitales:\n"
            f"  • SpO2 (Oxígeno): {oxigeno}%\n"
            f"  • Frecuencia Cardíaca: {fc} bpm\n"
            f"  • Presión Arterial: {pa} mmHg\n"
            f"  • Peso: {peso} kg | Talla: {talla} m\n\n"
            f"Evaluación Antropométrica:\n"
            f"  • IMC: {imc:.2f} kg/m²\n"
            f"  • Diagnóstico de peso: {estado_peso.upper()}"
        )

        lbl_diagnostico.config(text=diagnostico_texto, fg="#1e3d59")

    except ValueError:
        messagebox.showerror(
            "Error de entrada", 
            "Por favor, ingresa datos válidos en todos los campos.\n"
            "Asegúrate de poner la talla en metros (ej. 1.70) y valores numéricos correctos."
        )

root = tk.Tk()
root.title("Sistema de Diagnóstico Hospitalario")
root.geometry("520x650")
root.resizable(False, False)
root.configure(bg="#f5f7fa")

frame_superior = tk.Frame(root, bg="#1e3d59", pady=10)
frame_superior.pack(fill="x")

lbl_cita = tk.Label(
    frame_superior, 
    text=generar_cita(), 
    font=("Arial", 12, "bold"), 
    bg="#1e3d59", 
    fg="#ffffff"
)
lbl_cita.pack()

frame_medio = tk.LabelFrame(
    root, 
    text=" Datos del Paciente y Signos Vitales ", 
    font=("Arial", 10, "bold"),
    bg="#f5f7fa", 
    padx=15, 
    pady=15
)
frame_medio.pack(padx=20, pady=15, fill="x")

campos = [
    ("Nombre completo:", 0),
    ("Edad (años):", 1),
    ("Saturación de Oxígeno SpO2 (%):", 2),
    ("Frecuencia Cardíaca (bpm):", 3),
    ("Presión Arterial (ej. 120/80):", 4),
    ("Peso (kg):", 5),
    ("Talla / Estatura (m, ej. 1.70):", 6)
]

entries = {}

for texto, fila in campos:
    lbl = tk.Label(frame_medio, text=texto, anchor="w", bg="#f5f7fa", font=("Arial", 9))
    lbl.grid(row=fila, column=0, sticky="w", pady=4)
    
    ent = tk.Entry(frame_medio, font=("Arial", 9), width=25)
    ent.grid(row=fila, column=1, sticky="e", pady=4, padx=(10, 0))
    entries[texto] = ent


entry_nombre = entries["Nombre completo:"]
entry_edad = entries["Edad (años):"]
entry_oxigeno = entries["Saturación de Oxígeno SpO2 (%):"]
entry_fc = entries["Frecuencia Cardíaca (bpm):"]
entry_pa = entries["Presión Arterial (ej. 120/80):"]
entry_peso = entries["Peso (kg):"]
entry_talla = entries["Talla / Estatura (m, ej. 1.70):"]

entry_edad.insert(0, "15")
entry_peso.insert(0, "120")
entry_talla.insert(0, "1.70")

btn_enviar = tk.Button(
    root, 
    text="Generar Diagnóstico", 
    command=calcular_diagnostico,
    bg="#17b978", 
    fg="white", 
    font=("Arial", 11, "bold"),
    padx=10, 
    pady=5,
    cursor="hand2"
)
btn_enviar.pack(pady=5)


frame_inferior = tk.Frame(root, bg="#f5f7fa", pady=10)
frame_inferior.pack(fill="both", expand=True, padx=20)

lbl_diagnostico = tk.Label(
    frame_inferior, 
    text="Completa la información y presiona 'Generar Diagnóstico'", 
    font=("Arial", 10), 
    bg="#ffffff", 
    fg="#555555",
    relief="solid", 
    bd=1, 
    justify="left", 
    anchor="nw",
    padx=10, 
    pady=10
)
lbl_diagnostico.pack(fill="both", expand=True)

root.mainloop()
