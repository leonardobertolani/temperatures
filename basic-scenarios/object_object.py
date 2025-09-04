import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class GUI:

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


        self.root = tk.Tk()
        self.root.title("object-object temperature graph")

        self.root.geometry("1500x900")
        self.root.minsize(1200, 700)

        frame_left = ttk.Frame(self.root, padding=(10, 10, 20, 10))
        frame_left.grid(row=0, column=0, sticky=(tk.N, tk.S, tk.E, tk.W))

        first_object_label = ttk.Label(frame_left, text="First object", font=("Arial", 16))
        first_object_label.grid(row=0, column=0, padx=0, pady=10, sticky=tk.W)

        T1_init_label = ttk.Label(frame_left, text="Temperature (K):", font=("Arial", 14))
        T1_init_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.E)
        self.T1_init_entry = ttk.Entry(frame_left, font=("Arial", 14), width=10, justify="left")
        self.T1_init_entry.grid(row=1, column=1, padx=5, pady=5)
        self.T1_init_entry.insert(0, str(self.T1_init))

        m1_label = ttk.Label(frame_left, text="mass:", font=("Arial", 14))
        m1_label.grid(row=2, column=0, padx=5, pady=5, sticky=tk.E)
        self.m1_entry = ttk.Entry(frame_left, font=("Arial", 14), width=10, justify="left")
        self.m1_entry.grid(row=2, column=1, padx=5, pady=5)
        self.m1_entry.insert(0, str(self.m1))

        c1_label = ttk.Label(frame_left, text="specific heat:", font=("Arial", 14))
        c1_label.grid(row=3, column=0, padx=5, pady=(5, 60), sticky=tk.E)
        self.c1_entry = ttk.Entry(frame_left, font=("Arial", 14), width=10)
        self.c1_entry.grid(row=3, column=1, padx=5, pady=(5, 60))
        self.c1_entry.insert(0, str(self.c1))

        second_object_label = ttk.Label(frame_left, text="Second object", font=("Arial", 16))
        second_object_label.grid(row=4, column=0, padx=5, pady=10, sticky=tk.W)

        T2_init_label = ttk.Label(frame_left, text="Temperature (K):", font=("Arial", 14))
        T2_init_label.grid(row=5, column=0, padx=5, pady=5, sticky=tk.E)
        self.T2_init_entry = ttk.Entry(frame_left, font=("Arial", 14), width=10, justify="left")
        self.T2_init_entry.grid(row=5, column=1, padx=5, pady=5)
        self.T2_init_entry.insert(0, str(self.T2_init))

        m2_label = ttk.Label(frame_left, text="mass", font=("Arial", 14))
        m2_label.grid(row=6, column=0, padx=5, pady=5, sticky=tk.E)
        self.m2_entry = ttk.Entry(frame_left, font=("Arial", 14), width=10, justify="left")
        self.m2_entry.grid(row=6, column=1, padx=5, pady=5)
        self.m2_entry.insert(0, str(self.m2))

        c2_label = ttk.Label(frame_left, text="specific heat:", font=("Arial", 14))
        c2_label.grid(row=7, column=0, padx=5, pady=(5, 60), sticky=tk.E)
        self.c2_entry = ttk.Entry(frame_left, font=("Arial", 14), width=10)
        self.c2_entry.grid(row=7, column=1, padx=5, pady=(5, 60))
        self.c2_entry.insert(0, str(self.c2))

        R_label = ttk.Label(frame_left, text="Thermal resistance:", font=("Arial", 14))
        R_label.grid(row=8, column=0, padx=5, pady=(5, 60), sticky=tk.W)
        self.R_entry = ttk.Entry(frame_left, font=("Arial", 14), width=10)
        self.R_entry.grid(row=8, column=1, padx=5, pady=(5, 60))
        self.R_entry.insert(0, str(self.R))

        configuration_label = ttk.Label(frame_left, text="Graph configuration", font=("Arial", 16))
        configuration_label.grid(row=9, column=0, padx=5, pady=10, sticky=tk.W)

        tMax_label = ttk.Label(frame_left, text="x-axis upper bound:", font=("Arial", 14))
        tMax_label.grid(row=10, column=0, padx=5, pady=5, sticky=tk.E)
        self.tMax_entry = ttk.Entry(frame_left, font=("Arial", 14), width=10)
        self.tMax_entry.grid(row=10, column=1, padx=5, pady=5)
        self.tMax_entry.insert(0, str(self.tMax))

        numDots_label = ttk.Label(frame_left, text="Number of dots:", font=("Arial", 14))
        numDots_label.grid(row=11, column=0, padx=5, pady=5, sticky=tk.E)
        self.numDots_entry = ttk.Entry(frame_left, font=("Arial", 14), width=10)
        self.numDots_entry.grid(row=11, column=1, padx=5, pady=5)
        self.numDots_entry.insert(0, str(self.numDots))



        self.T1_init_entry.bind("<FocusOut>", self.update_plot)
        self.m1_entry.bind("<FocusOut>", self.update_plot)
        self.c1_entry.bind("<FocusOut>", self.update_plot)
        self.T2_init_entry.bind("<FocusOut>", self.update_plot)
        self.m2_entry.bind("<FocusOut>", self.update_plot)
        self.c2_entry.bind("<FocusOut>", self.update_plot)
        self.R_entry.bind("<FocusOut>", self.update_plot)
        self.tMax_entry.bind("<FocusOut>", self.update_plot)
        self.numDots_entry.bind("<FocusOut>", self.update_plot)

        frame_left.grid_columnconfigure(1, minsize=100)

        frame_right = ttk.Frame(self.root, padding=(20, 10, 10, 10))
        frame_right.grid(row=0, column=1, sticky=(tk.N, tk.S, tk.E, tk.W))


        fig, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(fig, master=frame_right)
        canvas_widget = self.canvas.get_tk_widget()
        canvas_widget.grid(row=0, column=0, padx=5, pady=5, sticky=(tk.N, tk.S, tk.E, tk.W))

        self.root.columnconfigure(0, weight=0)
        self.root.columnconfigure(1, weight=1)
        self.root.rowconfigure(0, weight=1)

        frame_left.columnconfigure(1, weight=1)
        frame_right.columnconfigure(0, weight=1)
        frame_right.rowconfigure(0, weight=1)

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


        self.ax.clear()
        self.ax.plot(t, T1)
        self.ax.plot(t, T2)
        self.ax.set_xlabel('t')
        self.ax.set_ylabel('T(t)')
        self.ax.set_title(
            f'$T(t) = (T_{{init}} - T_{{eq}}) e^{{-\\frac{{m_2 \cdot c_2 + m_1 \cdot c_1}}{{m_1 \cdot c_1 \cdot m_2 \cdot c_2 \cdot R}} \cdot t}} + T_{{eq}}$',
            fontsize=16)
        self.canvas.draw()

    def T(self, t, T_init):
        return (T_init - self.Teq) * np.exp(-self.gamma * t) + self.Teq



if __name__ == "__main__":
    app = GUI()
    app.update_plot()
    app.main_loop()
