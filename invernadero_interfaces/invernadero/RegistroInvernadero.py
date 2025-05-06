import tkinter as tk
from tkinter import ttk

class RegistroFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="white")
        self.master = master

        # Encabezado
        encabezado = tk.Frame(self, bg="#73b84b", height=40)
        encabezado.pack(fill="x")
        tk.Label(encabezado, text="🪶  Vivero vital", bg="#73b84b", fg="black", font=("Arial", 13, "bold")).pack(side="left", padx=10)

        # Contenedor central
        cuerpo = tk.Frame(self, bg="white")
        cuerpo.pack(pady=20, padx=20, fill="both", expand=True)

        # Sección izquierda: formulario
        formulario = tk.Frame(cuerpo, bg="white")
        formulario.pack(side="left", padx=20, pady=10)

        campos = [
            "Nombre del invernadero",
            "Superficie (m²)",
            "Tipo de cultivo",
            "Fecha de creación", 
            "Responsable del invernadero", 
            "Capacidad de producción",
            "Sistema de riego"
        ]

        self.entradas = {}

        for i, etiqueta in enumerate(campos):
            tk.Label(formulario, text=etiqueta, bg="white", anchor="w").grid(row=i, column=0, sticky="w", pady=5)
            
            if etiqueta in ["Tipo de cultivo", "Sistema de riego"]:
                combo = ttk.Combobox(formulario, state="readonly", values=["Manual", "Automatizado", "Por goteo"] if etiqueta == "Sistema de riego" else ["Flores", "Hortalizas", "Frutas"])
                combo.grid(row=i, column=1, pady=5, padx=5, sticky="ew")
                self.entradas[etiqueta] = combo
            else:
                entry = tk.Entry(formulario, bg="#fdf4cd")
                entry.grid(row=i, column=1, pady=5, padx=5, sticky="ew")
                self.entradas[etiqueta] = entry

        formulario.columnconfigure(1, weight=1)

        # Botones Guardar / Cancelar
        botones = tk.Frame(formulario, bg="white")
        botones.grid(row=len(campos), column=0, columnspan=2, pady=15)

        tk.Button(botones, text="Guardar", bg="green", fg="white", font=("Arial", 10, "bold"), width=10, command=self.guardar_invernadero).pack(side="left", padx=10)
        tk.Button(botones, text="Cancelar", bg="red", fg="white", font=("Arial", 10, "bold"), width=10, command=self.cancelar).pack(side="left", padx=10)

        # Sección derecha: imagen
        imagen = tk.Label(cuerpo, text="[Imagen del invernadero]", bg="white", width=40, height=20, relief="solid")
        imagen.pack(side="right", padx=30)

        # Pie de página
        pie = tk.Frame(self, bg="#fbc14a", height=30)
        pie.pack(side="bottom", fill="x")

        tk.Label(pie, text="Registrar invernadero", bg="#fbc14a", font=("Arial", 10, "bold")).pack(side="left", padx=10)
        tk.Button(pie, text="Regresar", bg="lightgreen", font=("Arial", 9), command=lambda: self.master.cambiar_frame(__import__('Menu').MenuFrame)).pack(side="right", padx=10)

    def guardar_invernadero(self):
        # Aquí luego puedes implementar la lógica para guardar en base de datos o lista
        print("Invernadero guardado (simulado)")

    def cancelar(self):
        for entrada in self.entradas.values():
            if isinstance(entrada, tk.Entry):
                entrada.delete(0, tk.END)
            elif isinstance(entrada, ttk.Combobox):
                entrada.set('')
