# Temperatures

With this repo I'd like to show you some of my (very simple) results about my study of thermodynamics. In particular, I analitically studied the way temperature of objects change over time, and I built some basic GUI interfaces with python to plot the results I found. The problems I analyzed go for a crescent way of difficulty, and the repo ends with a general solution I came up with that comprehend all the possible situations. Hope it could be interesting :)

## Table of Contents
- [Tackling the problem](#tackling-the-problem)
  - [First problem: single object and the environment](#first-problem-single-object-and-the-environment)
  - [Second problem: two objects without environment](#second-problem-two-objects-without-environment)
  - [Third problem: two objects and the environment](#third-problem-two-objects-and-the-environment)
  - [A more general way](#a-more-general-way)
- [Optimizing the solution](#optimizing-the-solution)
  - [First approach: standard python](#firts-approach:standard-python)
  - [Second approach: numpy](#second-approach:numpy)


# Tackling the problem
The problem of determining the temperature variation of a body over time can be quite complicated. Let us therefore make a few preliminary remarks: first, we will consider free evolution systems, i.e. systems that evolve freely once the initial conditions are fixed.
Furthermore, we will consider temperature as the only function of time, all other variables being independent of any other quantity.

We will therefore tackle the problem of determining the temperature function with an increasing degree of difficulty: we will start from a simple case, for which the analytical solution is easily calculable, then to an intermediate one, for which the analytical solution is already more complex, and finally
we will find a way to generalise the calculation and find any solution numerically.



## First problem: single object and the environment

Let's consider an object of mass $m$, temperature $T_{init}$ and specific heat $c$ surrounded by an environment with a steady temperature $T_{env}$ and with a thermal resistance $R$ between them. 
From this, we would like to find the temperature function $T(t)$ of the object as time passes, that is, find the rate of change in temperature over time. Actually, it's exponential.

To find it, let us consider a system with the properties we provided. It doesn't matter if the object is cooler or hotter than the environment, physics works both ways :)

<p align="center">
  <img width="596" alt="image" src="https://github.com/leonardobertolani/temperatures/assets/102794282/df7a909f-f8de-4c36-b26b-96dd548bf111"/>
</p>

Given that, let us quantify the total heat transfered by the object or to the object in a very small period of time $dt$:

$$Q_{total} = m \cdot c \cdot (T(t + dt) - T(t))$$

Now, we can think of the total heat exchanged as the total heat power released in the $dt$ interval:

$$Q_{total} = \dot{Q}_{total} \cdot dt = m \cdot c \cdot (T(t + dt) - T(t))$$

Then, from the electro-thermal analogy we can express the heat power using the temperature of the environment $T_{env}$, the temperature of the object at that time $T(t)$, and the thermal resistance $R$ facing between them:

$$-\frac{T(t) - T_{env}}{R} \cdot dt = m \cdot c \cdot (T(t + dt) - T(t))$$

The - sign is fundamental to maintain the equivalence (for example, suppose the object is cooling: in that case $T(t) - T_{env} > 0$ but $T(t + dt) - T(t) < 0$ and so the - is fundamental to balance the equation.
If the object is warming it goes the other way round).

Finally, we can divide both terms by $dt$: the $dt$ in the left term cancels out, while in the right term we recognize the derivative of function $T(t)$:

$$-\frac{T(t) - T_{env}}{R} = m \cdot c \cdot \frac{(T(t + dt) - T(t))}{dt} = m \cdot c \cdot \frac{dT(t)}{dt}$$

We eventually obtain this beautiful linear differential equation for the temperature function! In the end it should look like this:

$$\frac{dT(t)}{dt} + \frac{1}{R \cdot m \cdot c}T(t) = \frac{T_{env}}{R \cdot m \cdot c}$$

Remembering that $T(0) = T_{init}$ we find the following result:

$$T(t) = (T_{init} - T_{env})e^{-\frac{1}{R \cdot m \cdot c}t} + T_{env}$$

This function goes to $T_{env}$ when time goes to infinity, and equals $T_{init}$ at the starting point $T(0)$. It seems to work fine! 

Starting from this analytical solution I wrote the `object_environment.py` python script, that simply reads the properties of the system from some input-boxes and then plot the curve of the function.








## Second problem: two objects without environment

Let's consider two objects of mass $m1$ and $m2$, temperature $T^1_{init}$ $T^2_{init}$ and specific heat $c_1$ and $c_2$, surrounded by an adiabatic environment (no environment transfer of heat happens) and with a thermal resistence $R$ between the two objects. We would like to discover the rate of change in temperature of the two objects.

<p align="center">
<img width="596" alt="image" src="https://github.com/leonardobertolani/temperatures/assets/102794282/bd9a5a47-122d-4e2f-9ba3-1ee9ee8c923a">
</p>

### The equivalence temperature

First of all, it can be usefull to find the equivalence temperature $T_{eq}$, that is the temperature that the two objects will reach at equilibrium, once all the heat will have been transfered. From this point of view, the equivalence temperature can be found by comparing the total heat exchanges of the two objects untill they reach that temperature:

$$
  Q_{12} = - Q_{21} \implies m_1 \cdot c_1 \cdot (T^1_{init} -  T_{eq}) = - m_2 \cdot c_2 \cdot (T^2_{init} -  T_{eq})
$$

From here we have

$$
  T_{eq} = \frac{m_1 \cdot c_1 \cdot T^1_{init} + m_2 \cdot c_2 \cdot T^2_{init}}{m_1 \cdot c_1 + m_2 \cdot c_2}
$$

As we can see, the equivalence temperature seems to be the weighted average of the initial objects temperatures, with the weights expressed by the product $m \cdot c$.


### The relation between temperature curves

Now let's understand what happens to our system after a really short period of time $dt$. The amount of heat that the two objects will have been transfered equals to

$$
  Q_{tot} = m_1 \cdot c_1 \cdot (T_1(t + dt) - T_1(t)) = - m_2 \cdot c_2 \cdot (T_2(t + dt) - T_2(t))
$$

with the - sign balancing the equation (in fact, when one temperature increases and its difference is positive, the other decreases and its difference is negative). From here we divide both terms by $dt$ and we obtain the following:

$$
  m_1 \cdot c_1 \cdot \frac{dT_1(t)}{dt} = - m_2 \cdot c_2 \cdot \frac{dT_2(t)}{dt}
$$

$$
  \frac{dT_1(t)}{dt} = - \frac{m_2 \cdot c_2}{m_1 \cdot c_1} \cdot \frac{dT_2(t)}{dt}
$$

Then we integrate both sides of the equation and we obtain:

$$
  T_1(t) = - \frac{m_2 \cdot c_2}{m_1 \cdot c_1} \cdot T_2(t) + c
$$

This final result shows that $T_1(t)$ and $T_2(t)$ are pretty much the same function, except for a coefficient and a constant term. This result is reasonable, because the heat exchanged by the objects over time is the same, so the way one temperature function increases should match the way the other temperature function decreases. The constant term $c$ can be found remembering that for time going to infinity bot functions equals $T_{eq}$, and so:

$$
  T_{eq} = - \frac{m_2 \cdot c_2}{m_1 \cdot c_1} \cdot T_{eq} + c \qquad t \to\infty
$$

$$
  c = T_{eq} \cdot (1 + \frac{m_2 \cdot c_2}{m_1 \cdot c_1})
$$

$$
  c = \frac{m_1 \cdot c_1 \cdot T^1_{init} + m_2 \cdot c_2 \cdot T^2_{init}}{m_1 \cdot c_1 + m_2 \cdot c_2} \cdot (\frac{m_1 \cdot c_1 + m_2 \cdot c_2}{m_1 \cdot c_1})
$$

$$
  c = \frac{m_1 \cdot c_1 \cdot T^1_{init} + m_2 \cdot c_2 \cdot T^2_{init}}{m_1 \cdot c_1} = T^1_{init} + \frac{m_2 \cdot c_2}{m_1 \cdot c_1} \cdot T^2_{init}
$$

The equation can eventually be written as:

$$
  T_1(t) = - \frac{m_2 \cdot c_2}{m_1 \cdot c_1} \cdot T_2(t) + c = - \frac{m_2 \cdot c_2}{m_1 \cdot c_1} \cdot T_2(t) + T^1_{init} + \frac{m_2 \cdot c_2}{m_1 \cdot c_1} \cdot T^2_{init}
$$

and, of course

$$
T_2(t) = - \frac{m_1 \cdot c_1}{m_2 \cdot c_2} \cdot (T_1(t) - c) = - \frac{m_1 \cdot c_1}{m_2 \cdot c_2} \cdot (T_1(t) - T^1_{init} - \frac{m_2 \cdot c_2}{m_1 \cdot c_1} \cdot T^2_{init})
$$


### The differential equation
Finally, let's rewrite the previous equation using the electro-thermal analogy: the amount of heat transfered in a $dt$ interval can be expressed also by the difference in temperature at time $t$ between the object and by the thermal resistence $R$. 

$$
Q_{tot} = m_1 \cdot c_1 \cdot (T_1(t + dt) - T_1(t)) = - m_2 \cdot c_2 \cdot (T_2(t + dt) - T_2(t)) = - \frac{T_1(t) - T_2(t)}{R} \cdot dt
$$

Now, let's focus on the second and the fourth term

$$
m_1 \cdot c_1 \cdot (T_1(t + dt) - T_1(t)) = - \frac{T_1(t) - T_2(t)}{R} \cdot dt
$$

As we seen, the functions $T_1(t)$ can be expressed in terms of the function $T_2(t)$, and vice-versa. From the previous result we can go on and write:

$$
m_1 \cdot c_1 \cdot (T_1(t + dt) - T_1(t)) = - \frac{T_1(t) - T_2(t)}{R} \cdot dt
$$

$$
m_1 \cdot c_1 \cdot \frac{dT_1(t)}{dt} = - \frac{T_1(t) - T_2(t)}{R}
$$

$$
m_1 \cdot c_1 \cdot \frac{dT_1(t)}{dt} = - \frac{1}{R} \cdot T_1(t) - \frac{m_1 \cdot c_1}{m_2 \cdot c_2 \cdot R} \cdot T_1(t) + \frac{m_1 \cdot c_1 \cdot c}{m_2 \cdot c_2 \cdot R}
$$

$$
m_1 \cdot c_1 \cdot \frac{dT_1(t)}{dt} = - \frac{m_1 \cdot c_1 + m_2 \cdot c_2}{m_2 \cdot c_2 \cdot R} \cdot T_1(t) + \frac{m_1 \cdot c_1 \cdot c}{m_2 \cdot c_2 \cdot R}
$$

$$
\frac{dT_1(t)}{dt} + \frac{m_1 \cdot c_1 + m_2 \cdot c_2}{m_1 \cdot c_1 \cdot m_2 \cdot c_2 \cdot R} \cdot T_1(t) = \frac{c}{m_2 \cdot c_2 \cdot R}
$$

This is the linear differential equation that governs the $T_1(t)$ temperature curve. By solving it and indicating with $\gamma = \frac{m_1 \cdot c_1 + m_2 \cdot c_2}{m_1 \cdot c_1 \cdot m_2 \cdot c_2 \cdot R}$ we obtain the following

$$
  T_1(t) = e^{-\gamma t} (c_1 + \frac{c}{m_2 \cdot c_2 \cdot R} \cdot \frac{1}{\gamma} \cdot e^{\gamma t}) =  c_1 \cdot e^{-\gamma t} + \frac{c}{m_2 \cdot c_2 \cdot R \cdot \gamma} = c_1 \cdot e^{-\gamma t} + T_{eq}
$$

Note that the the term $\frac{c}{m_2 \cdot c_2 \cdot R \cdot \gamma}$ perfectly equals the $T_{eq}$ term that we calculated before. This is obvious: with $t$ going to infinity we expect the temperature of the system approaching $T_{eq}$, and this is what happens in the formula. The last costant $c_1$ can be found remembering that $T_1(0) = T^1_{init}$, leading to these final functions:

$$
  T_1(t) = (T^1_{init} - T_{eq}) \cdot e^{-\gamma t} + T_{eq}
$$

$$
  T_2(t) = (T^2_{init} - T_{eq}) \cdot e^{-\gamma t} + T_{eq}
$$

These results have been applied in the `object_object.py` script. A simple GUI wraps the graph and add some input-boxes to let you play around with different scenarios.








## Third problem: two objects and the environment

For the third problem, let's consider two objects of mass $m1$ and $m2$, temperature $T^1_{init}$ $T^2_{init}$ and specific heat $c_1$ and $c_2$, surrounded by an environment with a steady temperature $T_{env}$. The thermal resistance between the two objects is $R_{12}$, between the first object and the environment is $R_{1-env}$ and between the second object and the environment is $R_{2-env}$.


<p align="center">
<img width="593" alt="image" src="https://github.com/leonardobertolani/temperatures/assets/102794282/89ffea7a-0797-4346-a3e0-6fd5a4af990f">
</p>


From here, it's very difficult to find an analytical solution for the temperature curves of the objects, since the system is too complicated. Anyway, we can opt for an iterative solution! Like before, let us describe the total heat exchanged by the first object in a small period of time $dt$:

$$
Q_{total} = m_1 \cdot c_1 \cdot (T_1(t + dt) - T_1(t))
$$

Again, we can think of the total heat transfered as the total heat power released in the $dt$ interval, so:

$$
Q_{total} = \dot{Q}_{total} \cdot dt = m_1 \cdot c_1 \cdot (T_1(t + dt) - T_1(t))
$$

Now, the heat power that is being exchanged during the $dt$ interval is the sum of the heat power transfered from oject 1 through di environment and the heat power transfered from object 1 through object 2. 
Thus, by using the electro-thermal analogy we conclude that:

$$
-(\frac{T_1(t) - T_2(t)}{R_{12}} + \frac{T_1(t) - T_{env}}{R_{1-env}}) \cdot dt = m_1 \cdot c_1 \cdot (T_1(t + dt) - T_1(t))
$$

The - sign is fundamental to maintain the equivalence (for example, suppose $T_1(t) > T_2(t) > T_{env}$: in that case $T_1(t) - T_2(t) > 0$ and $T_1(t) - T_{env} > 0$ but $T_1(t + dt) - T_1(t) < 0$ and so the - is fundamental so balance the equation).

From this equation we notice that we can derive the temperature of the object at time $t + dt$ given the state of the system at time $t$, in fact:

$$T_1(t + dt) = T_1(t) - (\frac{T_1(t) - T_2(t)}{R_{12} \cdot m_1 \cdot c_1} + \frac{T_1(t) - T_{env}}{R_{1-env} \cdot m_1 \cdot c_1}) \cdot dt$$

For example, after the first $dt$ interval the temperature would become:

$$
T_1(0 + dt) = T_1(dt)= T_1(0) - (\frac{T_1(0) - T_2(0)}{R_{12} \cdot m_1 \cdot c_1} + \frac{T_1(0) - T_{env}}{R_{1-env} \cdot m_1 \cdot c_1}) \cdot dt = T^1_{init} - (\frac{T^1_{init} - T^2_{init}}{R_{12} \cdot m_1 \cdot c_1} + \frac{T^1_{init} - T_{env}}{R_{1-env} \cdot m_1 \cdot c_1}) \cdot dt
$$

We can see that by iterating this formula over and over again and by storing each time the values computed we are able to build the temperature curve of the object. Obviously, all the temperatures of the system must be updated over time, so to be able to build the $T_1(t)$ temperature curve is necessary to build the $T_2(t)$ temperature curve at the same time. This idea is applied in the `object_object_environment.py` script, and seems to work pretty well.









## A more general way
As seen in the previous paragraph about the `object_object_environment.py` script, it is not always necessary to compute a differential equation to plot the graph of different objects in the system. By using the iterative approach, the only difficulty is writing the first equation correctly and then plugging it into a script that builds a function step by step. 

For example, suppose we have $N$ objects with different masses, specific heats, and temperatures, all linked together, surrounded by the same environment. The temperature equation for, let's say, object 1 would simply be:

$$
-(\frac{T_1(t) - T_2(t)}{R_{12}} + \frac{T_1(t) - T_3(t)}{R_{13}} + \ldots + \frac{T_1(t) - T_N(t)}{R_{1N}} + \frac{T_1(t) - T_{env}}{R_{1-env}}) \cdot dt = m_1 \cdot c_1 \cdot (T_1(t + dt) - T_1(t))
$$

So, the temperature of object 1 at time $t + dt$ can be determined by the state of the system at time $t$ as:

$$
T_1(t + dt) = T_1(t) - (\frac{T_1(t) - T_2(t)}{R_{12} \cdot m_1 \cdot c_1} + \frac{T_1(t) - T_3(t)}{R_{13} \cdot m_1 \cdot c_1} + \ldots + \frac{T_1(t) - T_N(t)}{R_{1N} \cdot m_1 \cdot c_1} + \frac{T_1(t) - T_{env}}{R_{1-env} \cdot m_1 \cdot c_1}) \cdot dt
$$

Not every object should exchange heat with all others. For instance, object 1 may directly exchange heat with objects 2 and 4 but not with objects 3 and 5. We can represent these objects and their thermal interactions through a weighted graph, where each node symbolizes an object and each edge represents a connection between two objects, with the weight indicating thermal resistances.

<p align="center">
<img width="595" alt="image" src="https://github.com/leonardobertolani/temperatures/assets/102794282/9807af79-4f09-44a8-87e2-ac215c8cedfc">
</p>

This concept presents a more **scalable** and **efficient** approach to the problem of finding the temperature variations over time, and represent the generalization of the previous exercises.









# Optimizing the solution
Now that we have established a general criterion for studying the free evolution
of the system over time, let us try different algorithmic approaches to calculate its evolution.

As we have seen, the numerical strategy found consists in using the state of the system
at time $t$ to determine the future situation after a very short time instant $dt$. In fact, for what 
we have deduced, the temperature of a generic object $i \in N$ with mass $m_i$ and specific heat $c_i$, connected to a set $J \subset N$ of objects ${1, ..., j}$ via thermal resistances
$R_{ij}$, can be calculated as

$$
T_i(t + dt) = T_i(t) - (\frac{T_i(t) - T_1(t)}{R_{i1} \cdot m_i \cdot c_i} + \frac{T_i(t) - T_1(t)}{R_{i2} \cdot m_i \cdot c_i} + \ldots + \frac{T_i(t) - T_N(t)}{R_{iN} \cdot m_i \cdot c_i} + \frac{T_i(t) - T_{env}}{R_{i-env} \cdot m_i \cdot c_i}) \cdot dt
$$

where $\forall i \in N, R_{ii} = 1$ by our convention.

The situation can therefore be represented in this way

{picture of the network}

From here, we easily realise that the computation to be performed at each layer is nothing more than a scalar product between the vector of temperatures of the objects at instant $t$ and the vector of thermal resistances of 
that object with respect to all the others. In effect, we observe that

$$
T_i(t + dt) = T_i(t) - (\frac{T_i(t) - T_1(t)}{R_{i1} \cdot m_i \cdot c_i} + \frac{T_i(t) - T_1(t)}{R_{i2} \cdot m_i \cdot c_i} + \ldots + \frac{T_i(t) - T_N(t)}{R_{iN} \cdot m_i \cdot c_i} + \frac{T_i(t) - T_{env}}{R_{i-env} \cdot m_i \cdot c_i}) \cdot dt
$$

$$
T_i(t + dt) = T_i(t) - ( \ \sum_{j=1}^{N}\frac{T_i(t) - T_j(t)}{R_{ij} \cdot m_i \cdot c_i} + \frac{T_i(t) - T_{env}}{R_{i-env} \cdot m_i \cdot c_i} \ ) \cdot dt
$$

$$
T_i(t + dt) = T_i(t) - \frac{dt}{m_i \cdot c_i} ( \ \sum_{j=1}^{N}\frac{1}{R_{ij}} \cdot (T_i(t) - T_j(t)) + \frac{T_i(t) - T_{env}}{R_{i-env}} \ )
$$

The summation we have extracted represents a scalar product between the vector of the normalised temperatures with respect to object $i$ and the vector
of the inverse of the thermal resistances with respect to object $i$. Furthermore, we realise that the heat contribution given by the environment has the same mathematical structure as the other objects, therefore we can treat the environment as an object to all intents and purposes and include it in the summation, but remembering that its temperature must remain constant,
and thus imposing that $m_{env} = \infty$ and $c_{env} = \infty$.

$$
T_i(t + dt) = T_i(t) - \frac{dt}{m_i \cdot c_i} ( \ \sum_{j=1}^{N + 1}\frac{1}{R_{ij}} \cdot (T_i(t) - T_j(t)) \ ) \quad , \quad T_{env} = c
$$

The presence of a scalar product has an important advantage: it allows algorithmic optimization techniques to be implemented, since many calculations can be parallelized
by modern processors.
This will therefore be the mathematical structure that we will implement via software, in order to determine the algorithmic approach that best optimize the vector calculation and thus the solution to our problem.



## First approach: standard python
The first way we can try to implement the equation above is by using the python standard library. This approach, that we will call standard, is implemented in the `standard_dot.py` file, under the `optimization` directory, where a little GUI helps us to visualize the temperature trend of the objects.

