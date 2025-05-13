import tkinter as tk
from PIL import Image, ImageTk
from RegistroInvernadero import RegistroFrame
from ControlInvernadero import ControlFrame
import os

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

        boton_color = "#fdf4cd"
        texto_color = "#444"

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

        # Imagen decorativa
        ruta_imagen = os.path.join(os.path.dirname(__file__), "9c19392a-d0ce-48d6-b11b-f3320bd29e55.png")
        try:
            imagen = Image.open(ruta_imagen)
            imagen = imagen.resize((400, 250))
            self.foto = ImageTk.PhotoImage(imagen)
            lbl_imagen = tk.Label(self, image=self.foto, bg="white", relief="solid", bd=1)
            lbl_imagen.pack(pady=30)
        except Exception as e:
            tk.Label(self, text=f"aqui van imagenes", bg="white", fg="red").pack(pady=30)

        # Pie de página
        pie = tk.Frame(self, bg="#fbc14a", height=20)
        pie.pack(side="bottom", fill="x")
