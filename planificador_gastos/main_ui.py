import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import Calendar
from gasto import Gasto
from planificador import Planificador

 # Cambiar a tu región si es necesario

class PlanificadorUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Planificador de Gastos")

        self.planificador = Planificador(1000.0)  # Presupuesto inicial

        # Etiquetas y entradas
        ttk.Label(root, text="Nombre:").grid(row=0, column=0)
        self.nombre_entry = ttk.Entry(root)
        self.nombre_entry.grid(row=0, column=1)

        ttk.Label(root, text="Categoría:").grid(row=1, column=0)
        self.categorias = [
            "Ahorro",
            "Comida",
            "Casa",
            "Gastos varios",
            "Ocio",
            "Salud",
            "Suscripciones",
        ]
        self.categoria_combo = ttk.Combobox(
            root, values=self.categorias, state="readonly"
        )
        self.categoria_combo.grid(row=1, column=1)

        ttk.Label(root, text="Cantidad:").grid(row=2, column=0)
        self.cantidad_entry = ttk.Entry(root)
        self.cantidad_entry.grid(row=2, column=1)

        ttk.Label(root, text="Fecha:").grid(row=3, column=0)
        self.fecha_calendario = Calendar(
            root,
            date_pattern="dd/mm/yyyy",
            foreground="blue",  # Color de las letras
            background="white",  # Fondo del calendario
            headersforeground="red",  # Color de los nombres de los días
            selectforeground="orange",  # Color del texto de la fecha seleccionada
            selectbackground="black",  # Fondo de la fecha seleccionada
        )
        self.fecha_calendario.grid(row=3, column=1)

        # Botón para agregar gasto
        self.agregar_btn = ttk.Button(
            root, text="Agregar Gasto", command=self.agregar_gasto
        )
        self.agregar_btn.grid(row=4, column=0, columnspan=2)

        # Tabla de gastos
        self.tree = ttk.Treeview(
            root, columns=("Nombre", "Categoría", "Cantidad", "Fecha"), show="headings"
        )
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Categoría", text="Categoría")
        self.tree.heading("Cantidad", text="Cantidad")
        self.tree.heading("Fecha", text="Fecha")
        self.tree.grid(row=5, column=0, columnspan=2)

        # Agregar divisiones visibles
        self.tree.grid_rowconfigure(0, weight=1)
        self.tree.grid_columnconfigure(0, weight=1)
        
        # Configurar alineación a la derecha
        self.tree.column("Nombre", anchor="e")
        self.tree.column("Categoría", anchor="e")
        self.tree.column("Cantidad", anchor="e")
        self.tree.column("Fecha", anchor="e")

        # Presupuesto disponible
        self.presupuesto_label = ttk.Label(
            root, text=f"Presupuesto disponible: ${self.planificador.presupuesto:.2f}"
        )
        self.presupuesto_label.grid(row=6, column=0, columnspan=2)

    def agregar_gasto(self):
        try:
            nombre = self.nombre_entry.get()
            categoria = self.categoria_combo.get()
            cantidad = float(self.cantidad_entry.get())
            fecha = self.fecha_calendario.get_date()

            if not nombre or not categoria or not fecha:
                messagebox.showerror("Error", "Todos los campos son obligatorios")
                return

            nuevo_gasto = Gasto(nombre, categoria, cantidad, fecha)
            self.planificador.agregar_gasto(nuevo_gasto)

            self.tree.insert("", tk.END, values=(nombre, categoria, f"${cantidad:,.2f} MXN", fecha))
            self.actualizar_presupuesto()

        except ValueError:
            messagebox.showerror("Error", "La cantidad debe ser un número válido")

    def actualizar_presupuesto(self):
        total_gastos = sum(g.get_cantidad() for g in self.planificador.lista_gastos)
        presupuesto_disponible = self.planificador.presupuesto - total_gastos
        self.presupuesto_label.config(
            text=f"Presupuesto disponible: ${presupuesto_disponible:.2f}"
        )

if __name__ == "__main__":
    root = tk.Tk()
    app = PlanificadorUI(root)
    root.mainloop()
