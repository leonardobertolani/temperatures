import time
import random as rn
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt



def build_symmetrical_matrix(object_number):
    res = [ [ None for j in range(0, object_number) ] for i in range(0, object_number)]

    for i in range(0, object_number):
        for j in range(i, object_number):
            res[i][j] = 0.1 + rn.random()
            res[j][i] = res[i][j]

    return res


def dot_product(vec1, vec2):
    return sum(x * y for x, y in zip(vec1, vec2))



def visualize(T_time_matrix, object_number, time_array):
    plt.figure()

    for i in range(0, object_number):
        plt.plot(time_array, [ T_time_matrix[j][i] for j in range(0, len(time_array)) ])


    plt.xlabel("simulation duration [s]")
    plt.ylabel("temperatures [K]")
    plt.title("Evolution of the temperatures")

    plt.savefig("./standard.png")
    #plt.show()


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





OBJECT_NUMBER = 50
DT = 2              # simulation step size
DURATION = 5000     # simulation duration


initial_T = [250 + 100 * rn.random() for i in range(0, OBJECT_NUMBER)]
initial_m = [10 + 100 * rn.random() for i in range(0, OBJECT_NUMBER)]
initial_c = [10 + 1000 * rn.random() for i in range(0, OBJECT_NUMBER)]
initial_R = build_symmetrical_matrix(OBJECT_NUMBER)


start_time = time.time()
T_time_matrix = plain_algorithm(initial_T, initial_R, initial_m, initial_c)
end_time = time.time()

print(f"time elapsed: {end_time - start_time} seconds")
visualize(T_time_matrix, OBJECT_NUMBER, [i for i in range(0, DURATION, DT)])

