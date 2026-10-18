import tkinter as tk
from tkinter import messagebox
from arbol import ArbolNodos


class VentanaPrincipal:
    def __init__(self,root):
        self.root = root
        self.root.title("Arbol Binario de Búsqueda")
        self.root.geometry("1100x700")

        self.arbol = ArbolNodos()

        frame_superior = tk.Frame(root)
        frame_superior.pack(pady=10)

        self.entry_codigo = tk.Entry(frame_superior, width=10)
        self.entry_codigo.grid(row=0, column=0, padx=5)

        tk.Button(frame_superior, text="Agregar Nodo",
                  command=self.registrar).grid(row=0, column=1, padx=5)
        
        tk.Button(frame_superior, text="Buscar Nodo",
                  command=self.buscar).grid(row=0, column=2, padx=5)
        
        tk.Button(frame_superior, text="Limpiar",
                  command=self.limpiar).grid(row=0, column=3, padx=5)
        
        tk.Button(frame_superior, text="Salir",
                  command=root.quit).grid(row=0, column=4, padx=5)
        
        self.canvas = tk.Canvas(root, width=1000, height=420, bg="white")
        self.canvas.pack(pady=10)

        frame_recorridos = tk.Frame(root)
        frame_recorridos.pack(pady=10)

        tk.Label(frame_recorridos, text="Preorden").grid(row=0, column=0)
        tk.Label(frame_recorridos, text="Inorden").grid(row=0, column=1)
        tk.Label(frame_recorridos, text="Posorden").grid(row=0, column=2)

        self.preorden_txt = tk.Text(frame_recorridos, width= 40, height= 2)
        self.preorden_txt.grid(row=1, column=0, padx=10, pady=5)

        self.inorden_txt = tk.Text(frame_recorridos, width= 40, height= 2)
        self.inorden_txt.grid(row=1, column=1, padx=10, pady=5)

        self.postorden_txt = tk.Text(frame_recorridos, width= 40, height= 2)
        self.postorden_txt.grid(row=1, column=2, padx=10, pady=5)

    
    def registrar(self):
        try:
            codigo=int(self.entry_codigo.get())
            self.arbol.insertar(codigo)
            self.actualizar_interfaz()
        except ValueError:
            messagebox.showerror("Error","Ingrese un numero entero")
        except Exception as e:
            messagebox.showerror("Error",str(e))

                       
    def buscar(self):
        try:
            codigo = int(self.entry_codigo.get())
            if self.arbol.buscar(codigo):
                messagebox.showinfo("Buscar Nodo",f" Valor {codigo} si existe")
            else:
                messagebox.showwarning("Buscar Nodo",f"valor {codigo} no existe en el arbol")
        except ValueError:
            messagebox.showerror("Error","ingrese un numero entero")
    def limpiar(self):
        self.arbol.limpiar()
        self.actualizar_interfaz()

    def actualizar_interfaz(self):
        self.canvas.delete("all")
        self.dibujar_arbol(self.arbol.raiz, 500, 30, 250)

        self.preorden_txt.delete("1.0", tk.END)
        self.preorden_txt.insert("1.0", ", ".join(map(str, self.arbol.preorden())))


        self.inorden_txt.delete("1.0", tk.END)
        self.inorden_txt.insert("1.0",", ".join(map(str, self.arbol.inorden())))

        self.postorden_txt.delete("1.0", tk.END)
        self.postorden_txt.insert("1.0",", ".join(map(str, self.arbol.postorden())))

    def dibujar_arbol(self, nodo, x, y, espacio):
        if nodo is None:
            return
        
        radio = 20

        if nodo.izq:
            self.canvas.create_line(x, y, x - espacio, y + 80)
            self.dibujar_arbol(nodo.izq, x - espacio, y + 80, espacio // 2)

        if nodo.der:
            self.canvas.create_line(x, y, x + espacio, y + 80)
            self.dibujar_arbol(nodo.der, x + espacio, y + 80, espacio // 2)    

        self.canvas.create_oval(x-radio, y-radio, x+radio, y+radio, fill="lightblue")
        self.canvas.create_text(x, y, text=str(nodo.codigo))    
        
