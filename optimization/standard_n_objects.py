import time
import random as rn
import matplotlib.pyplot as plt



def build_symmetrical_matrix(object_number):
    res = [ [ None for j in range(0, object_number) ] for i in range(0, object_number)]

    for i in range(0, object_number):
        for j in range(i, object_number):
            res[i][j] = 0.1 + rn.random()
            res[j][i] = res[i][j]

    return res

def dot_product(array_a, array_b):
    res = 0

    for i in range(0, len(array_a)):
        res += array_a[i]*array_b[i]

    return res


def visualize(T_time_matrix, object_number, time_array):
    plt.figure()

    for i in range(0, object_number + 1):
        plt.plot(time_array, [ T_time_matrix[j][i] for j in range(0, len(time_array)) ])


    plt.xlabel("simulation duration [s]")
    plt.ylabel("temperatures [K]")
    plt.title("Objects temperature over time")

    plt.show()


def standard_algorithm(T_actual, R_actual, m_actual, c_actual):
    T_time_matrix = []
    T_time_matrix.append(T_actual)

    for i in range(1, NUM_INTERVALS):

        res_actual = []

        for j in range(0, OBJECT_NUMBER):
            R_dot = [1 / R_actual[j][n] for n in range(0, OBJECT_NUMBER + 1)]
            T_dot = [T_actual[j] - T_actual[n] for n in range(0, OBJECT_NUMBER + 1)]

            res_actual.append(T_actual[j] - DT / (m_actual[j] * c_actual[j]) * dot_product(R_dot, T_dot))

        res_actual.append(T_actual[OBJECT_NUMBER])
        T_time_matrix.append(res_actual)

        T_actual = res_actual

    return T_time_matrix





OBJECT_NUMBER = 10
DT = 10   # 10 seconds
NUM_INTERVALS = 2000


initial_T = [250 + 100 * rn.random() for i in range(0, OBJECT_NUMBER + 1)]
initial_m = [10 + 100 * rn.random() for i in range(0, OBJECT_NUMBER + 1)]
initial_c = [10 + 1000 * rn.random() for i in range(0, OBJECT_NUMBER + 1)]
initial_R = build_symmetrical_matrix(OBJECT_NUMBER + 1)


start_time = time.time()
T_time_matrix = standard_algorithm(initial_T, initial_R, initial_m, initial_c)
end_time = time.time()

print(f"time elapsed: {end_time - start_time} seconds")
visualize(T_time_matrix, OBJECT_NUMBER, [DT * i for i in range(0, NUM_INTERVALS)])

