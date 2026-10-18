import tkinter as tk
from login import LoginVentana
from interfaz import VentanaPrincipal 

def abrir_principal ():
    root = tk.Tk()
    VentanaPrincipal(root)
    root.mainloop()

root = tk.Tk()
LoginVentana(root, abrir_principal)
root.mainloop()
