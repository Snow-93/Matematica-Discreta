import tkinter as tk
from tkinter import messagebox
from datetime import date 

class LoginVentana:
    def __init__(self, root, abrir_principal):
        self.root = root
        self.abrir_principal = abrir_principal

        self.root.title("Fase4_ JuanCruz")
        self.root.geometry("400x300")

        tk.Label(root, text="Aplicacion:Arboles Binarios.",
                 font=("Arial",14)).pack(pady=10)
        
        
        tk.Label(root,text = "Estudiante:Juan David Cruz").pack()
        
        fecha_hoy = date.today().strftime("%d/%m/%Y")
        tk.Label(root, text=f"Fecha: {fecha_hoy}").pack(pady=5)

        tk.Label(root,text="Contraseña").pack(pady=10)

        self.entry_password = tk.Entry(root, show="-")
        self.entry_password.pack()

        tk.Button(root, text="Ingresar", command=self.validar).pack(pady=20)
    
    def validar(self):
     if self.entry_password.get() == "ARBOL":
        self.root.destroy()
        self.abrir_principal()
     else:
        messagebox.showerror("Error","Contrasena incorrecta")
        self.entry_password.delete(0, tk.END)
        self.entry_password.focus()

