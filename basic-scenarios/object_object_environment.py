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

        self.R12 = 0.03
        self.R1_env = 0.03
        self.R2_env = 0.03
        self.Tenv = 273

        self.tMax = 3000
        self.numDots = 200


        self.root = tk.Tk()
        self.root.title("object-object-environment temperature graph")

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

        configuration_label = ttk.Label(frame_left, text="Environment", font=("Arial", 16))
        configuration_label.grid(row=8, column=0, padx=5, pady=10, sticky=tk.W)

        Tenv_label = ttk.Label(frame_left, text="Temperature (K):", font=("Arial", 14))
        Tenv_label.grid(row=9, column=0, padx=5, pady=5, sticky=tk.E)
        self.Tenv_entry = ttk.Entry(frame_left, font=("Arial", 14), width=10)
        self.Tenv_entry.grid(row=9, column=1, padx=5, pady=5)
        self.Tenv_entry.insert(0, str(self.Tenv))

        R12_label = ttk.Label(frame_left, text="Thermal resistance R12:", font=("Arial", 14))
        R12_label.grid(row=10, column=0, padx=5, pady=5, sticky=tk.E)
        self.R12_entry = ttk.Entry(frame_left, font=("Arial", 14), width=10)
        self.R12_entry.grid(row=10, column=1, padx=5, pady=5)
        self.R12_entry.insert(0, str(self.R12))

        R1_env_label = ttk.Label(frame_left, text="Thermal resistance R1-env:", font=("Arial", 14))
        R1_env_label.grid(row=11, column=0, padx=5, pady=5, sticky=tk.E)
        self.R1_env_entry = ttk.Entry(frame_left, font=("Arial", 14), width=10)
        self.R1_env_entry.grid(row=11, column=1, padx=5, pady=5)
        self.R1_env_entry.insert(0, str(self.R1_env))

        R2_env_label = ttk.Label(frame_left, text="Thermal resistance R2-env:", font=("Arial", 14))
        R2_env_label.grid(row=12, column=0, padx=5, pady=(5, 60), sticky=tk.E)
        self.R2_env_entry = ttk.Entry(frame_left, font=("Arial", 14), width=10)
        self.R2_env_entry.grid(row=12, column=1, padx=5, pady=(5, 60))
        self.R2_env_entry.insert(0, str(self.R2_env))

        configuration_label = ttk.Label(frame_left, text="Graph configuration", font=("Arial", 16))
        configuration_label.grid(row=13, column=0, padx=5, pady=10, sticky=tk.W)

        tMax_label = ttk.Label(frame_left, text="x-axis upper bound:", font=("Arial", 14))
        tMax_label.grid(row=14, column=0, padx=5, pady=5, sticky=tk.E)
        self.tMax_entry = ttk.Entry(frame_left, font=("Arial", 14), width=10)
        self.tMax_entry.grid(row=14, column=1, padx=5, pady=5)
        self.tMax_entry.insert(0, str(self.tMax))

        numDots_label = ttk.Label(frame_left, text="Number of dots:", font=("Arial", 14))
        numDots_label.grid(row=15, column=0, padx=5, pady=5, sticky=tk.E)
        self.numDots_entry = ttk.Entry(frame_left, font=("Arial", 14), width=10)
        self.numDots_entry.grid(row=15, column=1, padx=5, pady=5)
        self.numDots_entry.insert(0, str(self.numDots))



        self.T1_init_entry.bind("<FocusOut>", self.update_plot)
        self.m1_entry.bind("<FocusOut>", self.update_plot)
        self.c1_entry.bind("<FocusOut>", self.update_plot)
        self.T2_init_entry.bind("<FocusOut>", self.update_plot)
        self.m2_entry.bind("<FocusOut>", self.update_plot)
        self.c2_entry.bind("<FocusOut>", self.update_plot)
        self.R12_entry.bind("<FocusOut>", self.update_plot)
        self.R1_env_entry.bind("<FocusOut>", self.update_plot)
        self.R2_env_entry.bind("<FocusOut>", self.update_plot)
        self.Tenv_entry.bind("<FocusOut>", self.update_plot)
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
        self.R12 = float(self.R12_entry.get())
        self.R1_env = float(self.R1_env_entry.get())
        self.R2_env = float(self.R2_env_entry.get())
        self.Tenv = float(self.Tenv_entry.get())
        self.tMax = float(self.tMax_entry.get())
        self.numDots = float(self.numDots_entry.get())

        self.plot_function()

    def plot_function(self):
        t = np.linspace(0, self.tMax, int(self.numDots))
        T1, T2 = self.T()


        self.ax.clear()
        self.ax.plot(t, T1)
        self.ax.plot(t, T2)
        self.ax.set_xlabel('t')
        self.ax.set_ylabel('T(t)')
        self.canvas.draw()

    def T(self):
        T1 = list()
        T2 = list()

        T1.append(self.T1_init)
        T2.append(self.T2_init)

        dt = self.tMax / self.numDots

        for counter in range(1, int(self.numDots)):
            T1.append(   ( -(T1[len(T1) - 1]  - T2[len(T2) - 1])/(self.R12 * self.m1 * self.c1) - (T1[len(T1) - 1]  - self.Tenv)/(self.R1_env * self.m1 * self.c1)) * dt + T1[len(T1) - 1]   )
            T2.append(   ( -(T2[len(T2) - 1]  - T1[len(T1) - 1])/(self.R12 * self.m2 * self.c2) - (T2[len(T2) - 1]  - self.Tenv)/(self.R2_env * self.m2 * self.c2)) * dt + T2[len(T2) - 1]   )


        return T1, T2




if __name__ == "__main__":
    app = GUI()
    app.update_plot()
    app.main_loop()
