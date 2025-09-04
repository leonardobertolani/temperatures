import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class GUI:

    def __init__(self):

        self.T_init = 293
        self.Tenv = 278
        self.m = 27
        self.c = 1005
        self.R = 0.033
        self.tMax = 3000
        self.numDots = 200


        self.root = tk.Tk()
        self.root.title("object-environment temperature graph")

        self.root.geometry("1500x900")
        self.root.minsize(1200, 700)

        frame_left = ttk.Frame(self.root, padding=(10, 10, 20, 10))
        frame_left.grid(row=0, column=0, sticky=(tk.N, tk.S, tk.E, tk.W))

        object_label = ttk.Label(frame_left, text="Object", font=("Arial", 16))
        object_label.grid(row=0, column=0, padx=0, pady=10, sticky=tk.W)

        T_init_label = ttk.Label(frame_left, text="Temperature (K):", font=("Arial", 14))
        T_init_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.E)
        self.T_init_entry = ttk.Entry(frame_left, font=("Arial", 14), width=10, justify="left")
        self.T_init_entry.grid(row=1, column=1, padx=5, pady=5)
        self.T_init_entry.insert(0, str(self.T_init))

        m_label = ttk.Label(frame_left, text="mass:", font=("Arial", 14))
        m_label.grid(row=2, column=0, padx=5, pady=5, sticky=tk.E)
        self.m_entry = ttk.Entry(frame_left, font=("Arial", 14), width=10, justify="left")
        self.m_entry.grid(row=2, column=1, padx=5, pady=5)
        self.m_entry.insert(0, str(self.m))

        c_label = ttk.Label(frame_left, text="specific heat:", font=("Arial", 14))
        c_label.grid(row=3, column=0, padx=5, pady=(5, 60), sticky=tk.E)
        self.c_entry = ttk.Entry(frame_left, font=("Arial", 14), width=10)
        self.c_entry.grid(row=3, column=1, padx=5, pady=(5, 60))
        self.c_entry.insert(0, str(self.c))

        configuration_label = ttk.Label(frame_left, text="Environment", font=("Arial", 16))
        configuration_label.grid(row=4, column=0, padx=5, pady=10, sticky=tk.W)

        Tenv_label = ttk.Label(frame_left, text="Temperature (K):", font=("Arial", 14))
        Tenv_label.grid(row=5, column=0, padx=5, pady=5, sticky=tk.E)
        self.Tenv_entry = ttk.Entry(frame_left, font=("Arial", 14), width=10)
        self.Tenv_entry.grid(row=5, column=1, padx=5, pady=5)
        self.Tenv_entry.insert(0, str(self.Tenv))

        R_label = ttk.Label(frame_left, text="Thermal resistance:", font=("Arial", 14))
        R_label.grid(row=6, column=0, padx=5, pady=(5, 60), sticky=tk.E)
        self.R_entry = ttk.Entry(frame_left, font=("Arial", 14), width=10)
        self.R_entry.grid(row=6, column=1, padx=5, pady=(5, 60))
        self.R_entry.insert(0, str(self.R))

        configuration_label = ttk.Label(frame_left, text="Graph configuration", font=("Arial", 16))
        configuration_label.grid(row=7, column=0, padx=5, pady=10, sticky=tk.W)

        tMax_label = ttk.Label(frame_left, text="x-axis upper bound:", font=("Arial", 14))
        tMax_label.grid(row=8, column=0, padx=5, pady=5, sticky=tk.E)
        self.tMax_entry = ttk.Entry(frame_left, font=("Arial", 14), width=10)
        self.tMax_entry.grid(row=8, column=1, padx=5, pady=5)
        self.tMax_entry.insert(0, str(self.tMax))

        numDots_label = ttk.Label(frame_left, text="Number of dots:", font=("Arial", 14))
        numDots_label.grid(row=9, column=0, padx=5, pady=5, sticky=tk.E)
        self.numDots_entry = ttk.Entry(frame_left, font=("Arial", 14), width=10)
        self.numDots_entry.grid(row=9, column=1, padx=5, pady=5)
        self.numDots_entry.insert(0, str(self.numDots))



        self.T_init_entry.bind("<FocusOut>", self.update_plot)
        self.Tenv_entry.bind("<FocusOut>", self.update_plot)
        self.m_entry.bind("<FocusOut>", self.update_plot)
        self.c_entry.bind("<FocusOut>", self.update_plot)
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
        self.T_init = float(self.T_init_entry.get())
        self.Tenv = float(self.Tenv_entry.get())
        self.m = float(self.m_entry.get())
        self.c = float(self.c_entry.get())
        self.R = float(self.R_entry.get())
        self.tMax = float(self.tMax_entry.get())
        self.numDots = float(self.numDots_entry.get())


        self.plot_function()




    def plot_function(self):
        t = np.linspace(0, self.tMax, int(self.numDots))
        T = self.T(t)


        self.ax.clear()
        self.ax.plot(t, T)
        self.ax.set_xlabel('t')
        self.ax.set_ylabel('T(t)')
        self.ax.set_title(f'$T(t) = (T_{{init}} - T_{{env}}) e^{{-\\frac{{1}}{{R \cdot m \cdot c}} \cdot t}} + T_{{env}}$', fontsize=16)
        self.canvas.draw()



    def T(self, t):
        return (self.T_init - self.Tenv) * np.exp(-1 / (self.R * self.m * self.c) * t) + self.Tenv


    def Titerative(self):
        T = list()
        T.append(self.T_init)

        dt = self.tMax / self.numDots

        for counter in range(1, int(self.numDots)):
            T.append( ( (-T[len(T) - 1] + self.Tenv)/(self.R * self.m * self.c) ) * dt + T[len(T) - 1])

        return T



if __name__ == "__main__":
    app = GUI()
    app.update_plot()
    app.main_loop()
