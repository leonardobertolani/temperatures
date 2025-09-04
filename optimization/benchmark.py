import numpy as np
import time
import matplotlib
matplotlib.use('Agg')
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

def dot_product(vec1, vec2):
    return sum(x * y for x, y in zip(vec1, vec2))


def plain_algorithm(T_vector, R_matrix, m_vector, c_vector, environment=True):

    if environment:
        initial_m[-1] = 100000
        initial_c[-1] = 100000

    T_time_matrix = [T_vector]
    current_T_vector = T_vector
    
    for _ in range(int(DURATION / DT) - 1):
        new_T_vector = []
    
        for j in range(OBJECT_NUMBER):
            R_dot = [1 / R_matrix[j][n] for n in range(OBJECT_NUMBER)]
            T_dot = [current_T_vector[j] - current_T_vector[n] for n in range(OBJECT_NUMBER)]
            delta_T = DT / (m_vector[j] * c_vector[j]) * dot_product(R_dot, T_dot)
            new_T_vector.append(current_T_vector[j] - delta_T)
        
        current_T_vector = new_T_vector
        T_time_matrix.append(current_T_vector)
        
    return T_time_matrix


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



def vectorized_algorithm(T_vector, R_matrix, m_vector, c_vector, environment=True):

    if environment:
        m_vector[-1] = 100000
        c_vector[-1] = 100000

    scaling_vector = DT / (m_vector * c_vector)
    Mr = (1 / R_matrix) * scaling_vector[:, np.newaxis]
            
    T_time_matrix = np.empty((int(DURATION/DT), OBJECT_NUMBER))
    T_time_matrix[0] = T_vector

    for i in range(1, int(DURATION/DT)):
        T_time_matrix[i] = T_time_matrix[i-1]*(1 - Mr @ np.ones(OBJECT_NUMBER)) + (Mr @ T_time_matrix[i-1])

    return T_time_matrix





# BENCHMARK VARIABLES
OBJECTS_STARTING_NUMBER = 10
OBJECT_MULTIPLIER = 20

DURATION_STARTING_TIME = 1000
DURATION_MULTIPLIER = 1000

DT = 10

N_BENCHMARK_COMPARISONS = 100




# BENCHMARKING WITH RESPECT TO OBJECT NUMBER
executionTime_standardAlg_objects = []
executionTime_numpyAlg_objects = []
executionTime_vectorizedAlg_objects = []
for i in range(0, N_BENCHMARK_COMPARISONS):

    OBJECT_NUMBER = OBJECTS_STARTING_NUMBER + i * OBJECT_MULTIPLIER
    DURATION = DURATION_STARTING_TIME

    initial_T = [250 + 100 * rn.random() for i in range(0, OBJECT_NUMBER)]
    initial_m = [10 + 100 * rn.random() for i in range(0, OBJECT_NUMBER)]
    initial_c = [10 + 1000 * rn.random() for i in range(0, OBJECT_NUMBER)]
    initial_R = build_symmetrical_matrix(OBJECT_NUMBER)

    # BENCHMARKING THE STANDARD ALGORITHM
    #'''
    start_time = time.time()
    plain_algorithm(initial_T, initial_R, initial_m, initial_c)
    end_time = time.time()

    executionTime_standardAlg_objects.append(end_time - start_time)
    #'''
    # BENCHMARKING THE NUMPY ALGORITHM
    initial_T = np.array(initial_T)
    initial_R = np.array(initial_R)
    initial_m = np.array(initial_m)
    initial_c = np.array(initial_c)

    #'''
    start_time = time.time()
    numpy_algorithm(initial_T, initial_R, initial_m, initial_c)
    end_time = time.time()

    executionTime_numpyAlg_objects.append(end_time - start_time)
    #'''


    # BENCHMARKING THE VECTORIZED/NUMPY ALGORITHM
    start_time = time.time()
    vectorized_algorithm(initial_T, initial_R, initial_m, initial_c)
    end_time = time.time()

    executionTime_vectorizedAlg_objects.append(end_time - start_time)


    # PRINTING STATUS
    print(f"round: {i+1}, obj number: {OBJECT_NUMBER}, num intervals: {DURATION}")








# BENCHMARKING WITH RESPECT TO SIMULATION DURATION
executionTime_standardAlg_duration = []
executionTime_numpyAlg_duration = []
executionTime_vectorizedAlg_duration = []
for i in range(0, N_BENCHMARK_COMPARISONS):

    
    DURATION = DURATION_STARTING_TIME + i * DURATION_MULTIPLIER
    OBJECT_NUMBER = OBJECTS_STARTING_NUMBER

    initial_T = [250 + 100 * rn.random() for i in range(0, OBJECT_NUMBER)]
    initial_m = [10 + 100 * rn.random() for i in range(0, OBJECT_NUMBER)]
    initial_c = [10 + 1000 * rn.random() for i in range(0, OBJECT_NUMBER)]
    initial_R = build_symmetrical_matrix(OBJECT_NUMBER)

    # BENCHMARKING THE STANDARD ALGORITHM
    #'''
    start_time = time.time()
    plain_algorithm(initial_T, initial_R, initial_m, initial_c)
    end_time = time.time()

    executionTime_standardAlg_duration.append(end_time - start_time)
    #'''

    # BENCHMARKING THE NUMPY ALGORITHM
    initial_T = np.array(initial_T)
    initial_R = np.array(initial_R)
    initial_m = np.array(initial_m)
    initial_c = np.array(initial_c)
    #'''
    start_time = time.time()
    numpy_algorithm(initial_T, initial_R, initial_m, initial_c)
    end_time = time.time()

    executionTime_numpyAlg_duration.append(end_time - start_time)
    #'''

    # BENCHMARKING THE VECTORIZED/NUMPY ALGORITHM
    start_time = time.time()
    vectorized_algorithm(initial_T, initial_R, initial_m, initial_c)
    end_time = time.time()

    executionTime_vectorizedAlg_duration.append(end_time - start_time)


    # PRINTING STATUS
    print(f"round: {i+1}, obj number: {OBJECT_NUMBER}, num intervals: {DURATION}")






fig, (ax1, ax2) = plt.subplots(2) #, sharey=True)
fig.suptitle('algorithm comparisons')
fig.set_figheight(8)
fig.set_figwidth(10)


ax1.plot([OBJECTS_STARTING_NUMBER + i * OBJECT_MULTIPLIER for i in range(0, N_BENCHMARK_COMPARISONS)], executionTime_standardAlg_objects, label='standard')
ax1.plot([OBJECTS_STARTING_NUMBER + i * OBJECT_MULTIPLIER for i in range(0, N_BENCHMARK_COMPARISONS)], executionTime_numpyAlg_objects, label='numpy')
ax1.plot([OBJECTS_STARTING_NUMBER + i * OBJECT_MULTIPLIER for i in range(0, N_BENCHMARK_COMPARISONS)], executionTime_vectorizedAlg_objects, label='vectorial')
ax1.legend(loc="upper left")
ax1.set(xlabel='number of objects', ylabel='execution time [s]')


ax2.plot([DT * (DURATION_STARTING_TIME + i * DURATION_MULTIPLIER) for i in range(0, N_BENCHMARK_COMPARISONS)], executionTime_standardAlg_duration, label='standard')
ax2.plot([DT * (DURATION_STARTING_TIME + i * DURATION_MULTIPLIER) for i in range(0, N_BENCHMARK_COMPARISONS)], executionTime_numpyAlg_duration, label='numpy')
ax2.plot([DT * (DURATION_STARTING_TIME + i * DURATION_MULTIPLIER) for i in range(0, N_BENCHMARK_COMPARISONS)], executionTime_vectorizedAlg_duration, label='vectorial')
ax2.legend(loc="upper left")
ax2.set(xlabel='simulation duration [s]', ylabel='execution time [s]')


plt.savefig("./benchmark.png")