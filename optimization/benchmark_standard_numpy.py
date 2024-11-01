import numpy as np
import time
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import random as rn



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


def numpy_algorithm(T_actual, R_actual, m_actual, c_actual):
    T_time_matrix = np.empty((NUM_INTERVALS, OBJECT_NUMBER + 1))
    T_time_matrix[0] = T_actual

    R_inv_dot = 1 / R_actual[:, :]

    for i in range(1, NUM_INTERVALS):

        T_dot = np.resize(T_time_matrix[i - 1], (OBJECT_NUMBER + 1, OBJECT_NUMBER + 1)).T - T_time_matrix[i - 1]
        dot_result = T_time_matrix[i - 1] - (DT / (m_actual * c_actual)) * np.diag(R_inv_dot @ T_dot.T)
        T_time_matrix[i] = dot_result

    return T_time_matrix


def vectorized_algorithm(T_initial, Mr):
    T_time_matrix = np.empty((NUM_INTERVALS, OBJECT_NUMBER + 1))
    T_time_matrix[0] = T_initial


    for i in range(1, NUM_INTERVALS):
        T_actual = T_time_matrix[i-1]
        T_time_matrix[i] = T_actual*(1 - Mr @ np.ones(OBJECT_NUMBER+1)) + (Mr @ T_actual)

    return T_time_matrix






# BENCHMARK VARIABLES
OBJECTS_STARTING_NUMBER = 10
OBJECT_MULTIPLIER = 10

DURATION_STARTING_TIME = 1000
DURATION_MULTIPLIER = 1000

DT = 10  # 10 seconds

COMPARISON_NUM = 30




# BENCHMARKING WITH RESPECT TO OBJECT NUMBER
executionTime_standardAlg_objects = []
executionTime_numpyAlg_objects = []
executionTime_vectorizedAlg_objects = []
for i in range(0, COMPARISON_NUM):

    # BENCHMARKING THE STANDARD ALGORITHM
    OBJECT_NUMBER = OBJECTS_STARTING_NUMBER + i * OBJECT_MULTIPLIER
    NUM_INTERVALS = DURATION_STARTING_TIME

    initial_T = [250 + 100 * rn.random() for i in range(0, OBJECT_NUMBER + 1)]
    initial_m = [10 + 100 * rn.random() for i in range(0, OBJECT_NUMBER + 1)]
    initial_c = [10 + 1000 * rn.random() for i in range(0, OBJECT_NUMBER + 1)]
    initial_R = build_symmetrical_matrix(OBJECT_NUMBER + 1)

    '''
    start_time = time.time()
    standard_algorithm(initial_T, initial_R, initial_m, initial_c)
    end_time = time.time()

    executionTime_standardAlg_objects.append(end_time - start_time)
    '''
    # BENCHMARKING THE NUMPY ALGORITHM
    initial_T = np.array(initial_T)
    initial_R = np.array(initial_R)
    initial_m = np.array(initial_m)
    initial_c = np.array(initial_c)

    # Forcing the environment not to change its temperature over time
    initial_m[OBJECT_NUMBER] = 100000
    initial_c[OBJECT_NUMBER] = 100000

    start_time = time.time()
    numpy_algorithm(initial_T, initial_R, initial_m, initial_c)
    end_time = time.time()

    executionTime_numpyAlg_objects.append(end_time - start_time)



    #BENCHMARKING THE VECTORIZED/NUMPY ALGORITHM

    Mr = 1 / initial_R[:, :]

    for row in range(0, OBJECT_NUMBER + 1):
        for col in range(0, OBJECT_NUMBER + 1):
            Mr[row][col] *= DT / (initial_m[row] * initial_c[row])

    start_time = time.time()
    vectorized_algorithm(initial_T, Mr)
    end_time = time.time()

    executionTime_vectorizedAlg_objects.append(end_time - start_time)


    # PRINTING STATUS
    print(f"round: {i+1}, obj number: {OBJECT_NUMBER}, num intervals: {NUM_INTERVALS}")








# BENCHMARKING WITH RESPECT TO SIMULATION DURATION
executionTime_standardAlg_duration = []
executionTime_numpyAlg_duration = []
executionTime_vectorizedAlg_duration = []
for i in range(0, COMPARISON_NUM):

    # BENCHMARKING THE STANDARD ALGORITHM
    NUM_INTERVALS = DURATION_STARTING_TIME + i * DURATION_MULTIPLIER
    OBJECT_NUMBER = OBJECTS_STARTING_NUMBER

    initial_T = [250 + 100 * rn.random() for i in range(0, OBJECT_NUMBER + 1)]
    initial_m = [10 + 100 * rn.random() for i in range(0, OBJECT_NUMBER + 1)]
    initial_c = [10 + 1000 * rn.random() for i in range(0, OBJECT_NUMBER + 1)]
    initial_R = build_symmetrical_matrix(OBJECT_NUMBER + 1)

    '''
    start_time = time.time()
    standard_algorithm(initial_T, initial_R, initial_m, initial_c)
    end_time = time.time()

    executionTime_standardAlg_duration.append(end_time - start_time)
    '''

    # BENCHMARKING THE NUMPY ALGORITHM
    initial_T = np.array(initial_T)
    initial_R = np.array(initial_R)
    initial_m = np.array(initial_m)
    initial_c = np.array(initial_c)

    # Forcing the environment not to change its temperature over time
    initial_m[OBJECT_NUMBER] = 100000
    initial_c[OBJECT_NUMBER] = 100000

    start_time = time.time()
    numpy_algorithm(initial_T, initial_R, initial_m, initial_c)
    end_time = time.time()

    executionTime_numpyAlg_duration.append(end_time - start_time)



    # BENCHMARKING THE VECTORIZED/NUMPY ALGORITHM

    Mr = 1 / initial_R[:, :]

    for row in range(0, OBJECT_NUMBER + 1):
        for col in range(0, OBJECT_NUMBER + 1):
            Mr[row][col] *= DT / (initial_m[row] * initial_c[row])

    start_time = time.time()
    vectorized_algorithm(initial_T, Mr)
    end_time = time.time()

    executionTime_vectorizedAlg_duration.append(end_time - start_time)


    # PRINTING STATUS
    print(f"round: {i+1}, obj number: {OBJECT_NUMBER}, num intervals: {NUM_INTERVALS}")






fig, (ax1, ax2) = plt.subplots(2) #, sharey=True)
fig.suptitle('Numpy benchmark')


#ax1.plot([OBJECTS_STARTING_NUMBER + i * OBJECT_MULTIPLIER for i in range(0, COMPARISON_NUM)], executionTime_standardAlg_objects, label='standard')
ax1.plot([OBJECTS_STARTING_NUMBER + i * OBJECT_MULTIPLIER for i in range(0, COMPARISON_NUM)], executionTime_numpyAlg_objects, label='numpy')
ax1.plot([OBJECTS_STARTING_NUMBER + i * OBJECT_MULTIPLIER for i in range(0, COMPARISON_NUM)], executionTime_vectorizedAlg_objects, label='vect')
ax1.legend(loc="upper left")
ax1.set(xlabel='number of objects', ylabel='execution time [s]')


#ax2.plot([DT * (DURATION_STARTING_TIME + i * DURATION_MULTIPLIER) for i in range(0, COMPARISON_NUM)], executionTime_standardAlg_duration, label='standard')
ax2.plot([DT * (DURATION_STARTING_TIME + i * DURATION_MULTIPLIER) for i in range(0, COMPARISON_NUM)], executionTime_numpyAlg_duration, label='numpy')
ax2.plot([DT * (DURATION_STARTING_TIME + i * DURATION_MULTIPLIER) for i in range(0, COMPARISON_NUM)], executionTime_vectorizedAlg_duration, label='vect')
ax2.legend(loc="upper left")
ax2.set(xlabel='simulation interval duration [s]', ylabel='execution time [s]')


plt.show()