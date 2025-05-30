import tkinter as tk
from tkinter import messagebox
from Menu import MenuFrame
from conexion import obtener_conexion

class LoginFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="white")
        self.master = master

        tk.Label(self, text="Iniciar Sesión", bg="#fdf4cd", fg="#f4a300", font=("Arial", 18, "bold")).pack(pady=20)

        self.entry_usuario = tk.Entry(self, font=("Arial", 12))
        self.entry_usuario.pack(pady=10)

        self.entry_contraseña = tk.Entry(self, font=("Arial", 12), show="•")
        self.entry_contraseña.pack(pady=10)

        tk.Button(self, text="Confirmar", bg="#4CAF50", fg="white", font=("Arial", 10, "bold"),
                  command=self.verificar_credenciales).pack(pady=15)

        tk.Frame(self, bg="#fbc14a", height=20).pack(side="bottom", fill="x")

    def verificar_credenciales(self):
        usuario = self.entry_usuario.get()
        contraseña = self.entry_contraseña.get()

        conexion = obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE nombre_usuario = %s AND contraseña = %s", (usuario, contraseña))
        resultado = cursor.fetchone()
        conexion.close()

        if resultado:
            messagebox.showinfo("Éxito", "Inicio de sesión correcto.")
            self.master.cambiar_frame(MenuFrame)
        else:
            messagebox.showerror("Error", "Credenciales incorrectas.")
