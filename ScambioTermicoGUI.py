import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class ScambioTermicoGUI:

    def __init__(self):
        self.T1_init = 300
        self.m1 = 20
        self.c1 = 1005

        self.T2_init = 280
        self.m2 = 20
        self.c2 = 1005

        self.R = 0.03

        self.Teq = (self.m1*self.c1*self.T1_init + self.m2*self.c2*self.T2_init)/(self.m1*self.c1 + self.m2*self.c2)
        self.gamma = (self.m1*self.c1 + self.m2*self.c2)/(self.m1*self.c1*self.m2*self.c2*self.R)
        self.tMax = 3000
        self.numDots = 200


        # Creazione dell'interfaccia grafica
        self.root = tk.Tk()
        self.root.title("Temperature")

        # Creazione degli entry widgets per i coefficienti
        T1_init_label = ttk.Label(self.root, text="T1 iniziale (K):", font=("Arial", 16))
        T1_init_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.E)
        self.T1_init_entry = ttk.Entry(self.root, font=("Arial", 16), width=10, justify="left")
        self.T1_init_entry.grid(row=0, column=1, padx=5, pady=5)
        self.T1_init_entry.insert(0, str(self.T1_init))

        m1_label = ttk.Label(self.root, text="massa 1:", font=("Arial", 16))
        m1_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.E)
        self.m1_entry = ttk.Entry(self.root, font=("Arial", 16), width=10, justify="left")
        self.m1_entry.grid(row=1, column=1, padx=5, pady=5)
        self.m1_entry.insert(0, str(self.m1))

        c1_label = ttk.Label(self.root, text="calore specifico 1:", font=("Arial", 16))
        c1_label.grid(row=2, column=0, padx=5, pady=5, sticky=tk.E)
        self.c1_entry = ttk.Entry(self.root, font=("Arial", 16), width=10)
        self.c1_entry.grid(row=2, column=1, padx=5, pady=5)
        self.c1_entry.insert(0, str(self.c1))

        T2_init_label = ttk.Label(self.root, text="T2 iniziale (K):", font=("Arial", 16))
        T2_init_label.grid(row=3, column=0, padx=5, pady=5, sticky=tk.E)
        self.T2_init_entry = ttk.Entry(self.root, font=("Arial", 16), width=10, justify="left")
        self.T2_init_entry.grid(row=3, column=1, padx=5, pady=5)
        self.T2_init_entry.insert(0, str(self.T2_init))

        m2_label = ttk.Label(self.root, text="massa 2", font=("Arial", 16))
        m2_label.grid(row=4, column=0, padx=5, pady=5, sticky=tk.E)
        self.m2_entry = ttk.Entry(self.root, font=("Arial", 16), width=10, justify="left")
        self.m2_entry.grid(row=4, column=1, padx=5, pady=5)
        self.m2_entry.insert(0, str(self.m2))

        c2_label = ttk.Label(self.root, text="calore specifico 2:", font=("Arial", 16))
        c2_label.grid(row=5, column=0, padx=5, pady=5, sticky=tk.E)
        self.c2_entry = ttk.Entry(self.root, font=("Arial", 16), width=10)
        self.c2_entry.grid(row=5, column=1, padx=5, pady=5)
        self.c2_entry.insert(0, str(self.c2))

        R_label = ttk.Label(self.root, text="Resistenza termica:", font=("Arial", 16))
        R_label.grid(row=6, column=0, padx=5, pady=5, sticky=tk.E)
        self.R_entry = ttk.Entry(self.root, font=("Arial", 16), width=10)
        self.R_entry.grid(row=6, column=1, padx=5, pady=5)
        self.R_entry.insert(0, str(self.R))

        tMax_label = ttk.Label(self.root, text="estremo superiore:", font=("Arial", 16))
        tMax_label.grid(row=7, column=0, padx=5, pady=5, sticky=tk.E)
        self.tMax_entry = ttk.Entry(self.root, font=("Arial", 16), width=10)
        self.tMax_entry.grid(row=7, column=1, padx=5, pady=5)
        self.tMax_entry.insert(0, str(self.tMax))

        numDots_label = ttk.Label(self.root, text="numero di punti:", font=("Arial", 16))
        numDots_label.grid(row=8, column=0, padx=5, pady=5, sticky=tk.E)
        self.numDots_entry = ttk.Entry(self.root, font=("Arial", 16), width=10)
        self.numDots_entry.grid(row=8, column=1, padx=5, pady=5)
        self.numDots_entry.insert(0, str(self.numDots))



        # Aggiunta della funzione di aggiornamento al cambio di valore
        self.T1_init_entry.bind("<FocusOut>", self.update_plot)
        self.m1_entry.bind("<FocusOut>", self.update_plot)
        self.c1_entry.bind("<FocusOut>", self.update_plot)
        self.T2_init_entry.bind("<FocusOut>", self.update_plot)
        self.m2_entry.bind("<FocusOut>", self.update_plot)
        self.c2_entry.bind("<FocusOut>", self.update_plot)
        self.R_entry.bind("<FocusOut>", self.update_plot)
        self.tMax_entry.bind("<FocusOut>", self.update_plot)
        self.numDots_entry.bind("<FocusOut>", self.update_plot)

        # Creazione di un grafico vuoto
        fig, self.ax = plt.subplots(figsize=(12, 10))
        self.canvas = FigureCanvasTkAgg(fig, master=self.root)
        canvas_widget = self.canvas.get_tk_widget()
        canvas_widget.grid(row=0, column=2, rowspan=9, padx=50, pady=50)

    def main_loop(self):
        self.root.mainloop()

    def update_plot(self, *args):
        self.T1_init = float(self.T1_init_entry.get())
        self.m1 = float(self.m1_entry.get())
        self.c1 = float(self.c1_entry.get())
        self.T2_init = float(self.T2_init_entry.get())
        self.m2 = float(self.m2_entry.get())
        self.c2 = float(self.c2_entry.get())
        self.R = float(self.R_entry.get())
        self.tMax = float(self.tMax_entry.get())
        self.numDots = float(self.numDots_entry.get())

        self.Teq = (self.m1 * self.c1 * self.T1_init + self.m2 * self.c2 * self.T2_init) / (self.m1 * self.c1 + self.m2 * self.c2)
        self.gamma = (self.m1 * self.c1 + self.m2 * self.c2) / (self.m1 * self.c1 * self.m2 * self.c2 * self.R)

        self.plot_function()

    def plot_function(self):
        t = np.linspace(0, self.tMax, int(self.numDots))
        T1 = self.T(t, self.T1_init)
        T2 = self.T(t, self.T2_init)
        #Tricors = self.Tricorsiva()


        self.ax.clear()
        self.ax.plot(t, T1)
        self.ax.plot(t, T2)
        #self.ax.plot(t, Tricors)
        self.ax.set_xlabel('t')
        self.ax.set_ylabel('T(t)')
        self.ax.set_title(
            f'$T(t) = (T_{{inizio}} - T_{{equilibrio}}) e^{{-\\frac{{m_2 \cdot c_2 + m_1 \cdot c_1}}{{m_1 \cdot c_1 \cdot m_2 \cdot c_2 \cdot R}} \cdot t}} + T_{{equilibrio}}$',
            fontsize=16)
        self.canvas.draw()

    def T(self, t, T_init):
        return (T_init - self.Teq) * np.exp(-self.gamma * t) + self.Teq

    def Tricorsiva(self):
        T = list()
        T.append(self.T0)

        dt = self.tMax / self.numDots

        for counter in range(1, int(self.numDots)):
            T.append(((-T[len(T) - 1] + self.Tamb) / (self.R * self.m * self.c) + self.Qentr / (
                        self.m * self.c) - self.Qusc / (self.m * self.c)) * dt + T[len(T) - 1])

        return T


if __name__ == "__main__":
    app = ScambioTermicoGUI()
    app.update_plot()
    app.main_loop()
