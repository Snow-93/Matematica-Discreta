# -*- coding: utf-8 -*-
"""
PROYECTO No. 2 - MATEMATICA DISCRETA
Programa principal: pide la contrasena y luego muestra un menu para elegir
que programa usar.

  Opcion 4. Grafos  -> Node Demonstrator (nodemon)
            https://github.com/MrHarcombe/NodeDemonstrator
  Opcion 6. Arboles -> Arbol binario de busqueda (carpeta "arbol")
            https://github.com/JDCruz001/binary-search-tree-gui-python

Antes de ejecutar, instalar el programa de grafos (una sola vez):
    pip install "ttkbootstrap<2" nodemon

Estructura de carpetas:
    proyecto/
    |-- menu.py          (este archivo)
    |-- arbol/           (main.py, login.py, interfaz.py, arbol.py sin cambios)

Ejecutar con:  python menu.py
"""

import importlib.util
import os
import subprocess
import sys
import tkinter as tk
from datetime import date
from tkinter import messagebox

# ---------------------------------------------------------------- datos
PASSWORD = "ARBOL"
INTEGRANTES = ["Integrante 1", "Integrante 2", "Integrante 3", "Integrante 4"]  # <- editar

CARPETA = os.path.dirname(os.path.abspath(__file__))
CARPETA_ARBOL = os.path.join(CARPETA, "arbol")


# ------------------------------------------------------------- pantallas
class Login(tk.Tk):
    """Primera pantalla: pide la contrasena."""

    def __init__(self):
        super().__init__()
        self.title("Proyecto No. 2 - Matemática Discreta")
        self.geometry("420x360")
        self.autenticado = False

        tk.Label(self, text="Proyecto No. 2", font=("Arial", 16, "bold")).pack(pady=(15, 0))
        tk.Label(self, text="Matemática Discreta: Grafos y Árboles",
                 font=("Arial", 11)).pack()
        tk.Label(self, text="\n".join(INTEGRANTES), font=("Arial", 9)).pack(pady=8)
        tk.Label(self, text="Fecha: " + date.today().strftime("%d/%m/%Y")).pack()

        tk.Label(self, text="Contraseña").pack(pady=(12, 2))
        self.entrada = tk.Entry(self, show="*")
        self.entrada.pack()
        self.entrada.focus()
        self.entrada.bind("<Return>", lambda e: self.validar())

        tk.Button(self, text="Ingresar", command=self.validar).pack(pady=15)

    def validar(self):
        if self.entrada.get() == PASSWORD:
            self.autenticado = True
            self.destroy()
        else:
            messagebox.showerror("Error", "Contraseña incorrecta")
            self.entrada.delete(0, tk.END)
            self.entrada.focus()


class Menu(tk.Tk):
    """Segunda pantalla: elegir el programa a usar."""

    def __init__(self):
        super().__init__()
        self.title("Menú principal")
        self.geometry("420x300")
        self.opcion = None

        tk.Label(self, text="¿Qué programa desea usar?",
                 font=("Arial", 14, "bold")).pack(pady=20)
        tk.Button(self, text="4. Grafos\n(matriz, recorridos, mejor ruta)", width=34, height=2,
                  command=lambda: self.elegir("grafos")).pack(pady=5)
        tk.Button(self, text="6. Árboles\n(preorden, inorden, postorden)", width=34, height=2,
                  command=lambda: self.elegir("arboles")).pack(pady=5)
        tk.Button(self, text="0. Salir", width=34,
                  command=lambda: self.elegir(None)).pack(pady=15)

    def elegir(self, opcion):
        self.opcion = opcion
        self.destroy()


# ------------------------------------------------------------ programas
def abrir_arboles():
    """Opcion 6: abre la interfaz del arbol (sus archivos no se modifican)."""
    sys.path.insert(0, CARPETA_ARBOL)
    try:
        from interfaz import VentanaPrincipal
    except ImportError:
        messagebox.showerror("Árboles", "No se encontró la carpeta 'arbol' junto a menu.py.")
        return
    raiz = tk.Tk()
    VentanaPrincipal(raiz)
    raiz.mainloop()
    try:
        raiz.destroy()
    except tk.TclError:
        pass  # la ventana ya se cerro


def abrir_grafos():
    """Opcion 4: abre el programa de grafos (nodemon) y lo trae al frente."""
    if importlib.util.find_spec("nodemon") is None:
        messagebox.showerror(
            "Grafos",
            "No está instalado el programa de grafos.\n\nInstálelo con:\n"
            'pip install "ttkbootstrap<2" nodemon')
        return
    try:
        from nodemon.node_demonstrator import NodeApplication
        ventana = NodeApplication()
        # Traer la ventana al frente (en Windows puede abrirse detras de otras).
        ventana.lift()
        ventana.attributes("-topmost", True)
        ventana.after(400, lambda: ventana.attributes("-topmost", False))
        ventana.focus_force()
        ventana.mainloop()
    except Exception as error:
        messagebox.showerror(
            "Grafos",
            "No se pudo abrir el programa de grafos.\n\n" + str(error) +
            '\n\nPruebe: pip install "ttkbootstrap<2" nodemon')


# --------------------------------------------------------------- inicio
def main():
    login = Login()
    login.mainloop()
    if not login.autenticado:
        return

    while True:
        menu = Menu()
        menu.mainloop()
        if menu.opcion == "grafos":
            abrir_grafos()
        elif menu.opcion == "arboles":
            abrir_arboles()
        else:
            break


if __name__ == "__main__":
    if "--verificar" in sys.argv:
        # Comprobacion rapida (sin ventanas): que todo este incluido.
        sys.path.insert(0, CARPETA_ARBOL)
        from interfaz import VentanaPrincipal  # noqa: F401
        from nodemon.node_demonstrator import NodeApplication
        ventana = NodeApplication()
        ventana.update()
        ventana.destroy()
        print("verificacion ok")
    else:
        main()
