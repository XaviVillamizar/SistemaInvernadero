import tkinter as tk
from tkinter import ttk, messagebox, Toplevel
from conexion import obtener_conexion


class ControlFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="#f0f0f0")
        self.master = master
        self.invernaderos = []
        self.crear_encabezado()
        self.crear_lista()

    def cargar_invernaderos(self):
        conexion = obtener_conexion()
        cursor = conexion.cursor(dictionary=True)
        cursor.execute("SELECT * FROM invernaderos")
        self.invernaderos = cursor.fetchall()
        conexion.close()

    def crear_encabezado(self):
        encabezado = tk.Frame(self, bg="#7ac142", height=40)
        encabezado.pack(fill=tk.X)
        tk.Label(encabezado, text="Vivero vital", bg="#7ac142", fg="black", font=("Arial", 14, "bold")).pack(side=tk.LEFT, padx=10)

    def crear_lista(self):
        self.cargar_invernaderos()
        contenedor = tk.Frame(self, bg="#ffffff")
        contenedor.pack(fill=tk.BOTH, expand=True)

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

        pie = tk.Frame(self, bg="#f9c349", height=40)
        pie.pack(fill=tk.X, side=tk.BOTTOM)
        tk.Button(pie, text="Regresar", bg="green", fg="white", command=lambda: self.master.cambiar_frame(__import__('Menu').MenuFrame)).pack(side=tk.LEFT, padx=10, pady=5)
        tk.Label(pie, text="Control invernadero", bg="#f9c349", font=("Arial", 12, "bold")).pack(side=tk.RIGHT, padx=10)

    def agregar_fila_invernadero(self, contenedor, invernadero):
        fila = tk.Frame(contenedor, bg="#ffffff", pady=5)
        fila.pack(fill=tk.X, padx=20)
        tk.Label(fila, text=invernadero["nombre"], width=25, bg="#e0e0e0", font=("Arial", 10, "bold")).pack(side=tk.LEFT)
        tk.Label(fila, text=invernadero["estado"], width=12, bg="#f3f7c0", font=("Arial", 10, "bold")).pack(side=tk.LEFT, padx=5)

        tk.Button(fila, text="Editar", width=10, bg="#f7f7b0", command=lambda inv=invernadero: self.ventana_edicion(inv)).pack(side=tk.LEFT, padx=2)
        tk.Button(fila, text="Eliminar", width=10, bg="#f7f7b0", command=lambda inv=invernadero: self.eliminar_invernadero(inv, fila)).pack(side=tk.LEFT, padx=2)
        tk.Button(fila, text="Ver Detalles", width=12, bg="#ffdb6d", command=lambda inv=invernadero: self.ventana_detalles(inv)).pack(side=tk.LEFT, padx=2)

    def eliminar_invernadero(self, invernadero, fila_frame):
        confirmacion = messagebox.askyesno("Confirmar", f"¿Eliminar invernadero '{invernadero['nombre']}'?")
        if confirmacion:
            conexion = obtener_conexion()
            cursor = conexion.cursor()
            cursor.execute("DELETE FROM invernaderos WHERE id = %s", (invernadero['id'],))
            conexion.commit()
            conexion.close()
            fila_frame.destroy()
            messagebox.showinfo("Eliminado", "Invernadero eliminado correctamente.")

    def ventana_detalles(self, invernadero):
        detalles_win = Toplevel(self)
        detalles_win.title(f"Detalles de {invernadero['nombre']}")
        detalles_win.geometry("400x300")
        detalles_win.config(bg="white")

        campos = {
            "Nombre": invernadero["nombre"],
            "Superficie (m²)": invernadero["superficie"],
            "Tipo de cultivo": invernadero["tipo_cultivo"],
            "Fecha de creación": invernadero["fecha_creacion"],
            "Responsable": invernadero["responsable"],
            "Capacidad": invernadero["capacidad"],
            "Sistema de riego": invernadero["sistema_riego"],
            "Estado": invernadero["estado"]
        }

        for i, (key, value) in enumerate(campos.items()):
            tk.Label(detalles_win, text=f"{key}:", anchor="w", font=("Arial", 10, "bold"), bg="white").grid(row=i, column=0, sticky="w", padx=10, pady=5)
            tk.Label(detalles_win, text=str(value), anchor="w", bg="white", font=("Arial", 10)).grid(row=i, column=1, sticky="w", padx=5)

    def ventana_edicion(self, invernadero):
        edit_win = Toplevel(self)
        edit_win.title("Editar Invernadero")
        edit_win.geometry("400x400")
        edit_win.config(bg="white")

        campos = [
            "nombre", "superficie", "tipo_cultivo", "fecha_creacion",
            "responsable", "capacidad", "sistema_riego", "estado"
        ]

        entradas = {}

        for i, campo in enumerate(campos):
            tk.Label(edit_win, text=campo.replace("_", " ").capitalize(), bg="white").grid(row=i, column=0, sticky="w", padx=10, pady=5)
            entrada = tk.Entry(edit_win)
            entrada.insert(0, str(invernadero[campo]))
            entrada.grid(row=i, column=1, padx=5)
            entradas[campo] = entrada

        def guardar_cambios():
            try:
                datos_actualizados = {k: v.get() for k, v in entradas.items()}
                conexion = obtener_conexion()
                cursor = conexion.cursor()
                cursor.execute("""
                    UPDATE invernaderos SET
                        nombre = %s,
                        superficie = %s,
                        tipo_cultivo = %s,
                        fecha_creacion = %s,
                        responsable = %s,
                        capacidad = %s,
                        sistema_riego = %s,
                        estado = %s
                    WHERE id = %s
                """, (
                    datos_actualizados["nombre"],
                    float(datos_actualizados["superficie"]),
                    datos_actualizados["tipo_cultivo"],
                    datos_actualizados["fecha_creacion"],
                    datos_actualizados["responsable"],
                    int(datos_actualizados["capacidad"]),
                    datos_actualizados["sistema_riego"],
                    datos_actualizados["estado"],
                    invernadero["id"]
                ))
                conexion.commit()
                conexion.close()
                messagebox.showinfo("Éxito", "Invernadero actualizado correctamente.")
                edit_win.destroy()
                self.master.cambiar_frame(ControlFrame)  # Refrescar lista
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo actualizar: {e}")

        tk.Button(edit_win, text="Guardar cambios", bg="green", fg="white", command=guardar_cambios).grid(row=len(campos), column=0, columnspan=2, pady=20)

