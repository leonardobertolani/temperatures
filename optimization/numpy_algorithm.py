import numpy as np
import time
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.cm as cm


def build_symmetrical_matrix(object_number):
  lower_triangle = 0.1 + np.random.rand(object_number, object_number)
  return np.tril(lower_triangle, k=0) + np.tril(lower_triangle, k=0).T


def visualize(T_time_matrix, object_number, time_array):
    colors = cm.viridis(np.linspace(0, 1, OBJECT_NUMBER))

    plt.figure()

    for i in range(0, object_number):
        plt.plot(time_array, T_time_matrix[:, i], label=f'Object {i}', color=colors[i])

    plt.xlabel("simulation duration [s]")
    plt.ylabel("temperatures [K]")
    plt.title("Evolution of the temperatures")

    plt.savefig("./numpy.png")
    #plt.show()



def numpy_algorithm(T_vector, R_matrix, m_vector, c_vector, environment=True):

    if environment:
        initial_m[-1] = 100000
        initial_c[-1] = 100000

    T_time_matrix = np.empty((int(DURATION/DT), OBJECT_NUMBER))
    T_time_matrix[0] = T_vector

    R_inv_dot = 1 / R_matrix[:, :]

    for i in range(1, int(DURATION/DT)):
        T_dot = (np.resize(T_time_matrix[i - 1], (OBJECT_NUMBER, OBJECT_NUMBER)).T - T_time_matrix[i - 1]).T
        dot_result = T_time_matrix[i - 1] - (DT / (m_vector * c_vector)) * (R_inv_dot * T_dot).sum(axis=0)
        T_time_matrix[i] = dot_result

    return T_time_matrix





DT = 2                # simulation step size
DURATION = 5000        # simulation duration
OBJECT_NUMBER = 50



initial_T = 250 + 100 * np.random.rand(OBJECT_NUMBER)
initial_m = 10 + 100 * np.random.rand(OBJECT_NUMBER)
initial_c = 10 + 1000 * np.random.rand(OBJECT_NUMBER)
initial_R = build_symmetrical_matrix(OBJECT_NUMBER)

start_time = time.time()
T_time_matrix = numpy_algorithm(initial_T, initial_R, initial_m, initial_c)
end_time = time.time()

print(f"time elapsed: {end_time - start_time} seconds")
visualize(T_time_matrix, OBJECT_NUMBER, np.linspace(DT, DURATION, int(DURATION/DT)))