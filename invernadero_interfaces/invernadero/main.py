import tkinter as tk
from Login import LoginFrame

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Vivero Vital")
        self.geometry("900x500")
        self.resizable(False, False)
        self.current_frame = None
        self.cambiar_frame(LoginFrame)

    def cambiar_frame(self, frame_class):
        if self.current_frame:
            self.current_frame.destroy()
        self.current_frame = frame_class(self)
        self.current_frame.pack(fill="both", expand=True)

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
