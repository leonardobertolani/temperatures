import numpy as np
import time
import matplotlib.pyplot as plt
import matplotlib.cm as cm


def build_symmetrical_matrix(object_number):
  lower_triangle = 0.1 + np.random.rand(object_number, object_number)
  return np.tril(lower_triangle, k=0) + np.tril(lower_triangle, k=0).T


def visualize(T_time_matrix, object_number, time_array):
    colors = cm.viridis(np.linspace(0, 1, object_number + 1))

    plt.figure()

    for i in range(0, object_number + 1):
        plt.plot(time_array, T_time_matrix[:, i], label=f'Object {i}', color=colors[i])

    plt.xlabel("simulation duration [s]")
    plt.ylabel("temperatures [K]")
    plt.title("Objects temperature over time")

    plt.show()



def vectorized_algorithm(T_initial, R_matrix, m_initial, c_initial):
    T_time_matrix = np.empty((NUM_INTERVALS, OBJECT_NUMBER + 1))
    T_time_matrix[0] = T_initial

    Mr = 1 / R_matrix[:, :]

    for row in range(0, OBJECT_NUMBER+1):
        for col in range(0, OBJECT_NUMBER+1):
            Mr[row][col] *= DT/(m_initial[row]*c_initial[row])


    for i in range(1, NUM_INTERVALS):
        T_actual = T_time_matrix[i-1]
        T_time_matrix[i] = T_actual*(1 - Mr @ np.ones(OBJECT_NUMBER+1)) + (Mr @ T_actual)

    return T_time_matrix





DT = 10  # 10 seconds
NUM_INTERVALS = 5000
OBJECT_NUMBER = 40



initial_T = 250 + 100 * np.random.rand(OBJECT_NUMBER + 1)
initial_m = 10 + 100 * np.random.rand(OBJECT_NUMBER + 1)
initial_c = 10 + 1000 * np.random.rand(OBJECT_NUMBER + 1)
initial_R = build_symmetrical_matrix(OBJECT_NUMBER + 1)

# Forcing the environment not to change its temperature over time
initial_m[OBJECT_NUMBER] = 100000
initial_c[OBJECT_NUMBER] = 100000

start_time = time.time()
T_time_matrix = vectorized_algorithm(initial_T, initial_R, initial_m, initial_c)
end_time = time.time()

print(f"time elapsed: {end_time - start_time} seconds")
visualize(T_time_matrix, OBJECT_NUMBER, np.linspace(DT, DT * NUM_INTERVALS, NUM_INTERVALS))