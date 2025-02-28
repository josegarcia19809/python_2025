import tkinter as tk
from tkinter import ttk, messagebox
from gasto import Gasto
from planificador import Planificador


class AppGastos:
    def __init__(self, root):
        self.root = root
        self.root.title("Planificador de Gastos")
        self.planificador = Planificador(1000.0)  # Presupuesto inicial

        # Etiquetas y campos de entrada
        ttk.Label(root, text="Nombre del Gasto:").grid(row=0, column=0, padx=5, pady=5)
        self.entry_nombre = ttk.Entry(root)
        self.entry_nombre.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(root, text="Tipo de Gasto:").grid(row=1, column=0, padx=5, pady=5)
        self.entry_tipo = ttk.Entry(root)
        self.entry_tipo.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(root, text="Cantidad:").grid(row=2, column=0, padx=5, pady=5)
        self.entry_cantidad = ttk.Entry(root)
        self.entry_cantidad.grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(root, text="Fecha (DD/MM/AAAA):").grid(row=3, column=0, padx=5, pady=5)
        self.entry_fecha = ttk.Entry(root)
        self.entry_fecha.grid(row=3, column=1, padx=5, pady=5)

        # Botón para agregar gasto
        self.boton_agregar = ttk.Button(root, text="Agregar Gasto",
                                        command=self.agregar_gasto)
        self.boton_agregar.grid(row=4, column=0, columnspan=2, padx=5, pady=10)

        # Botón para mostrar gastos
        self.boton_mostrar = ttk.Button(root, text="Mostrar Gastos",
                                        command=self.mostrar_gastos)
        self.boton_mostrar.grid(row=5, column=0, columnspan=2, padx=5, pady=10)

        # Etiquetas de resumen
        self.label_presupuesto = ttk.Label(root, text="Presupuesto Disponible: $1000")
        self.label_presupuesto.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

        self.label_porcentaje = ttk.Label(root, text="Porcentaje Gastado: 0%")
        self.label_porcentaje.grid(row=7, column=0, columnspan=2, padx=5, pady=5)

        # Área de texto para mostrar gastos
        self.texto_gastos = tk.Text(root, height=10, width=50)
        self.texto_gastos.grid(row=8, column=0, columnspan=2, padx=5, pady=10)

    def agregar_gasto(self):
        nombre = self.entry_nombre.get()
        tipo = self.entry_tipo.get()
        cantidad = self.entry_cantidad.get()
        fecha = self.entry_fecha.get()

        # Validación
        try:
            cantidad = float(cantidad)
            if nombre and tipo and fecha:
                gasto = Gasto(nombre, tipo, cantidad, fecha)
                self.planificador.agregar_gasto(gasto)

                messagebox.showinfo("Éxito", "Gasto agregado correctamente")
                self.actualizar_presupuesto()
            else:
                messagebox.showwarning("Error", "Todos los campos son obligatorios")
        except ValueError:
            messagebox.showerror("Error", "La cantidad debe ser un número")

    def mostrar_gastos(self):
        self.texto_gastos.delete("1.0", tk.END)
        if not self.planificador.lista_gastos:
            self.texto_gastos.insert(tk.END, "No hay gastos registrados\n")
        else:
            for gasto in self.planificador.lista_gastos:
                self.texto_gastos.insert(tk.END, gasto.mostrar_info() + "\n")

    def actualizar_presupuesto(self):
        presupuesto_disp = self.planificador.obtener_presupuesto_disponible()
        porcentaje_gastado = self.planificador.obtener_porcentaje_gastado()

        self.label_presupuesto.config(
            text=f"Presupuesto Disponible: ${presupuesto_disp:.2f}")
        self.label_porcentaje.config(
            text=f"Porcentaje Gastado: {porcentaje_gastado:.2f}%")


# Ejecutar aplicación
root = tk.Tk()
app = AppGastos(root)
root.mainloop()
