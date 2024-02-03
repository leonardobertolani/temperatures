import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class RaffreddamentoGUI:

    def __init__(self):

        self.T0 = 293
        self.Tamb = 278
        self.m = 27
        self.c = 1005
        self.R = 0.033
        self.Qentr = 200
        self.Qusc = 0
        self.tMax = 3000
        self.numDots = 200

        # Creazione dell'interfaccia grafica
        self.root = tk.Tk()
        self.root.title("Temperature")

        # Creazione degli entry widgets per i coefficienti
        T0_label = ttk.Label(self.root, text="T iniziale (K):", font=("Arial", 16))
        T0_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.E)
        self.T0_entry = ttk.Entry(self.root, font=("Arial", 16), width=10, justify="left")
        self.T0_entry.grid(row=0, column=1, padx=5, pady=5)
        self.T0_entry.insert(0, str(self.T0))


        Tamb_label = ttk.Label(self.root, text="T ambiente (K):", font=("Arial", 16))
        Tamb_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.E)
        self.Tamb_entry = ttk.Entry(self.root, font=("Arial", 16), width=10, justify="left")
        self.Tamb_entry.grid(row=1, column=1, padx=5, pady=5)
        self.Tamb_entry.insert(0, str(self.Tamb))


        m_label = ttk.Label(self.root, text="massa:", font=("Arial", 16))
        m_label.grid(row=2, column=0, padx=5, pady=5, sticky=tk.E)
        self.m_entry = ttk.Entry(self.root, font=("Arial", 16), width=10)
        self.m_entry.grid(row=2, column=1, padx=5, pady=5)
        self.m_entry.insert(0, str(self.m))


        c_label = ttk.Label(self.root, text="calore specifico:", font=("Arial", 16))
        c_label.grid(row=3, column=0, padx=5, pady=5, sticky=tk.E)
        self.c_entry = ttk.Entry(self.root, font=("Arial", 16), width=10)
        self.c_entry.grid(row=3, column=1, padx=5, pady=5)
        self.c_entry.insert(0, str(self.c))


        R_label = ttk.Label(self.root, text="Resistenza termica totale:", font=("Arial", 16))
        R_label.grid(row=4, column=0, padx=5, pady=5, sticky=tk.E)
        self.R_entry = ttk.Entry(self.root, font=("Arial", 16), width=10)
        self.R_entry.grid(row=4, column=1, padx=5, pady=5)
        self.R_entry.insert(0, str(self.R))


        Qentr_label = ttk.Label(self.root, text="Potenza entrante:", font=("Arial", 16))
        Qentr_label.grid(row=5, column=0, padx=5, pady=5, sticky=tk.E)
        self.Qentr_entry = ttk.Entry(self.root, font=("Arial", 16), width=10)
        self.Qentr_entry.grid(row=5, column=1, padx=5, pady=5)
        self.Qentr_entry.insert(0, str(self.Qentr))


        Qusc_label = ttk.Label(self.root, text="Potenza uscente:", font=("Arial", 16))
        Qusc_label.grid(row=6, column=0, padx=5, pady=5, sticky=tk.E)
        self.Qusc_entry = ttk.Entry(self.root, font=("Arial", 16), width=10)
        self.Qusc_entry.grid(row=6, column=1, padx=5, pady=5)
        self.Qusc_entry.insert(0, str(self.Qusc))


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
        self.T0_entry.bind("<FocusOut>", self.update_plot)
        self.Tamb_entry.bind("<FocusOut>", self.update_plot)
        self.m_entry.bind("<FocusOut>", self.update_plot)
        self.c_entry.bind("<FocusOut>", self.update_plot)
        self.R_entry.bind("<FocusOut>", self.update_plot)
        self.Qentr_entry.bind("<FocusOut>", self.update_plot)
        self.Qusc_entry.bind("<FocusOut>", self.update_plot)
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
        self.T0 = float(self.T0_entry.get())
        self.Tamb = float(self.Tamb_entry.get())
        self.m = float(self.m_entry.get())
        self.c = float(self.c_entry.get())
        self.R = float(self.R_entry.get())
        self.Qentr = float(self.Qentr_entry.get())
        self.Qusc = float(self.Qusc_entry.get())
        self.tMax = float(self.tMax_entry.get())
        self.numDots = float(self.numDots_entry.get())


        self.plot_function()




    def plot_function(self):
        t = np.linspace(0, self.tMax, int(self.numDots))
        T = self.T(t)
        #Tricors = self.Tricorsiva()


        self.ax.clear()
        self.ax.plot(t, T)
        #self.ax.plot(t, Tricors)
        self.ax.set_xlabel('t')
        self.ax.set_ylabel('T(t)')
        self.ax.set_title(f'$T(t) = (T_0 - T_{{amb}} - \\dot{{Q}}_{{entrata}} \\cdot R + \\dot{{Q}}_{{uscita restante}} \\cdot R) e^{{-\\frac{{1}}{{R \cdot m \cdot c}} \cdot t}} + T_{{amb}} + \\dot{{Q}}_{{entrata}} \\cdot R - \\dot{{Q}}_{{uscita restante}} \\cdot R$', fontsize=16)
        self.canvas.draw()



    def T(self, t):
        return (self.T0 - self.Tamb - self.Qentr * self.R + self.Qusc * self.R) * np.exp(-1 / (self.R * self.m * self.c) * t) + self.Tamb + self.Qentr * self.R - self.Qusc * self.R


    def Tricorsiva(self):
        T = list()
        T.append(self.T0)

        dt = self.tMax / self.numDots

        for counter in range(1, int(self.numDots)):
            T.append( ( (-T[len(T) - 1] + self.Tamb)/(self.R * self.m * self.c) + self.Qentr / (self.m*self.c) - self.Qusc / (self.m * self.c) ) * dt + T[len(T) - 1])

        return T



if __name__ == "__main__":
    app = RaffreddamentoGUI()
    app.update_plot()
    app.main_loop()
