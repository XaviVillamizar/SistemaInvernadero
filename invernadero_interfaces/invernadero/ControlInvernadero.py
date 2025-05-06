import tkinter as tk
from tkinter import ttk

class ControlFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="#f0f0f0")
        self.master = master

        self.invernaderos = [
            {"nombre": "Invernadero Los Andes", "estado": "Operativo"},
            {"nombre": "Invernadero Las Flores", "estado": "Reparación"},
            {"nombre": "Invernadero Los Pinos", "estado": "Inspección"},
            {"nombre": "Invernadero El Mirador", "estado": "Expansión"},
            {"nombre": "Invernadero Las Brisas", "estado": "Operativo"}
        ]

        self.crear_encabezado()
        self.crear_lista()

    def crear_encabezado(self):
        encabezado = tk.Frame(self, bg="#7ac142", height=40)
        encabezado.pack(fill=tk.X)

        tk.Label(encabezado, text="Vivero vital", bg="#7ac142", fg="black", font=("Arial", 14, "bold")).pack(side=tk.LEFT, padx=10)

    def crear_lista(self):
        contenedor = tk.Frame(self, bg="#ffffff")
        contenedor.pack(fill=tk.BOTH, expand=True)

        # Scroll y lista
        canvas = tk.Canvas(contenedor, bg="#ffffff")
        scrollbar = ttk.Scrollbar(contenedor, orient="vertical", command=canvas.yview)
        frame_lista = tk.Frame(canvas, bg="#ffffff")

        frame_lista.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=frame_lista, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        for invernadero in self.invernaderos:
            self.agregar_fila_invernadero(frame_lista, invernadero)

        # Pie
        pie = tk.Frame(self, bg="#f9c349", height=40)
        pie.pack(fill=tk.X, side=tk.BOTTOM)

        tk.Button(pie, text="Regresar", bg="green", fg="white", command=lambda: self.master.cambiar_frame(__import__('Menu').MenuFrame)).pack(side=tk.LEFT, padx=10, pady=5)
        tk.Label(pie, text="Control invernadero", bg="#f9c349", font=("Arial", 12, "bold")).pack(side=tk.RIGHT, padx=10)

    def agregar_fila_invernadero(self, contenedor, invernadero):
        fila = tk.Frame(contenedor, bg="#ffffff", pady=5)
        fila.pack(fill=tk.X, padx=20)

        tk.Label(fila, text=invernadero["nombre"], width=25, bg="#e0e0e0", font=("Arial", 10, "bold")).pack(side=tk.LEFT)
        tk.Label(fila, text=invernadero["estado"], width=12, bg="#f3f7c0", font=("Arial", 10, "bold")).pack(side=tk.LEFT, padx=5)

        tk.Button(fila, text="Editar", width=10, bg="#f7f7b0").pack(side=tk.LEFT, padx=2)
        tk.Button(fila, text="Eliminar", width=10, bg="#f7f7b0").pack(side=tk.LEFT, padx=2)
        tk.Button(fila, text="Detalles", width=10, bg="#f9c349").pack(side=tk.LEFT, padx=2)
