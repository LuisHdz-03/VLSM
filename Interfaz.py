import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from VLSM import Logica


class Ventana:
    def __init__(self, root):
        self.root = root
        self.root.title("VLSM")

        ancho_ventana = 500
        alto_ventana = 600

        self.root.update_idletasks()
        x, y = self.root.winfo_x(), self.root.winfo_y()

        nuevo_ancho = 900
        self.root.geometry(f"{nuevo_ancho}x{alto_ventana}+{x}+{y}")

        self.panel = tk.Frame(self.root, bg="#123142")
        self.panel.place(relwidth=1.0, relheight=1.0)

        self.labels(self.panel, "Ingrese la direccion IP", 20, 80, ("Arial", 15))
        self.labels(
            self.panel, "Ingrese la cantidad\nde departamentos", 20, 140, ("Arial", 15)
        )

        self.entries = []
        self.device_counts = []  
        self.text(self.panel, 300, 80, 18, ("Arial", 20))
        self.text(self.panel, 300, 140, 18, ("Arial", 20))

        self.current_dep = 1
        self.departamentos = 0

        self.label = tk.Label(
            self.panel,
            text=f"Ingrese la cantidad\nde dispositivos\ndel departamento {self.current_dep}:",
            bg="#e9f0c9",
            font=("Arial", 15),
        )
        self.label.place(x=20, y=220)

        self.entry = tk.Entry(self.panel, width=18, font=("Arial", 20))
        self.entry.place(x=300, y=220)

        self.button = tk.Button(self.panel, text="Siguiente", command=self.cambioLabel)
        self.button.place(x=300, y=260)

        self.tree = ttk.Treeview(
            self.panel,
            columns=(
                "Departamento",
                "Dispositivos",
                "IP Inicial",
                "IP Final",
                "Máscara",
            ),
            show="headings",
        )
        self.tree.heading("Departamento", text="Departamento")
        self.tree.heading("Dispositivos", text="Dispositivos")
        self.tree.heading("IP Inicial", text="IP Inicial")
        self.tree.heading("IP Final", text="IP Final")
        self.tree.heading("Máscara", text="Máscara")
        self.tree.place(x=20, y=320, width=800, height=200)

        self.tree.column("Departamento", width=100, anchor="center")
        self.tree.column("Dispositivos", width=100, anchor="center")
        self.tree.column("IP Inicial", width=150, anchor="center")
        self.tree.column("IP Final", width=150, anchor="center")
        self.tree.column("Máscara", width=100, anchor="center")

        self.logica = Logica()

        self.clear_button = tk.Button(self.panel, text="Limpiar", command=self.limpiar)
        self.clear_button.place(x=400, y=260)

    def labels(self, parent, text, x, y, font):
        label = tk.Label(parent, text=text, bg="#e9f0c9", font=font)
        label.place(x=x, y=y)

    def text(self, parent, x, y, Width, fuente):
        entry = tk.Entry(parent, width=Width, font=fuente)
        entry.place(x=x, y=y)
        self.entries.append(entry)

    def cambioLabel(self):
        if self.current_dep == 1:
            if len(self.entries) < 2:
                messagebox.showerror(
                    "Error",
                    "Por favor, ingrese la dirección IP y la cantidad de departamentos.",
                )
                return
            try:
                self.departamentos = int(self.entries[1].get())
            except ValueError:
                messagebox.showerror(
                    "Error",
                    "Por favor, ingrese un número válido para la cantidad de departamentos.",
                )
                return

        try:
            dispositivos = int(self.entry.get())
        except ValueError:
            messagebox.showerror(
                "Error",
                f"Por favor, ingrese un número válido para la cantidad de dispositivos del departamento {self.current_dep}.",
            )
            return

        self.device_counts.append(dispositivos)

        self.entry.delete(0, tk.END)

        self.current_dep += 1
        if self.current_dep <= self.departamentos:
            self.label.config(
                text=f"Ingrese la cantidad\nde dispositivos\ndel departamento {self.current_dep}:"
            )
        else:
            self.label.config(text="Todos los departamentos\nhan sido ingresados.")
            self.entry.config(state="disabled")
            self.button.config(state="disabled")

            direccion_ip = self.entries[0].get()
            subnets = self.logica.calculate_vlsm(direccion_ip, self.device_counts)

            if isinstance(subnets, str):

                messagebox.showerror("Error", subnets)
            else:

                for idx, subnet in enumerate(subnets):
                    self.tree.insert(
                        "",
                        "end",
                        values=(
                            f"Departamento {idx + 1}",
                            subnet["total_hosts"],
                            subnet["first_ip"],
                            subnet["last_ip"],
                            f"/{subnet['prefix_length']}",
                        ),
                    )

    def limpiar(self):

        for entry in self.entries:
            entry.delete(0, tk.END)
        self.entries.clear()
        self.device_counts.clear()

        for item in self.tree.get_children():
            self.tree.delete(item)

        self.current_dep = 1
        self.departamentos = 0

        self.label.config(
            text=f"Ingrese la cantidad\nde dispositivos\ndel departamento {self.current_dep}:"
        )
        self.entry.config(state="normal")
        self.button.config(state="normal")

        self.text(self.panel, 300, 80, 18, ("Arial", 20))
        self.text(self.panel, 300, 140, 18, ("Arial", 20))


if __name__ == "__main__":
    root = tk.Tk()
    ventana = Ventana(root)
    root.mainloop()
