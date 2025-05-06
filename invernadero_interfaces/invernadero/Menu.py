import tkinter as tk
from RegistroInvernadero import RegistroFrame
from ControlInvernadero import ControlFrame

class MenuFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="white")
        self.master = master

        # Encabezado verde
        encabezado = tk.Frame(self, bg="#73b84b", height=40)
        encabezado.pack(fill="x")
        lbl_encabezado = tk.Label(encabezado, text="   🪶  Vivero vital", bg="#73b84b", fg="black", font=("Arial", 12, "bold"))
        lbl_encabezado.pack(side="left", padx=10)

        # Espacio
        tk.Label(self, bg="white").pack(pady=10)

        # Contenedor de botones
        frame_botones = tk.Frame(self, bg="white")
        frame_botones.pack()

        # Estilo de botones
        boton_color = "#fdf4cd"
        texto_color = "#444"

        # Botones con sus acciones
        botones = [
            ("Registrar invernaderos", lambda: self.master.cambiar_frame(RegistroFrame)),
            ("Control invernaderos", lambda: self.master.cambiar_frame(ControlFrame)),
            ("Control de humedad", None),
            ("Control de piso", None),
            ("Enfermedades", None)
        ]

        for texto, comando in botones:
            btn = tk.Button(frame_botones, text=texto, bg=boton_color, fg=texto_color, font=("Arial", 10, "bold"),
                            relief="solid", borderwidth=1, padx=10, pady=5, command=comando)
            btn.pack(side="left", padx=5)

        # Pie de página amarillo
        pie = tk.Frame(self, bg="#fbc14a", height=20)
        pie.pack(side="bottom", fill="x")



