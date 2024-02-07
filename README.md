# Temperatures

The scripts in this repo deal with some basic thermodynamics, displaying the rate of change in temperature of objects over time. Every script deal with a different problem:
- *object_environment.py*: this script plot the temperature / time graph of an object cooling or heating in a steady temperature environment.
- *object_object.py*: this script plot the temperature / time graph of two object at different temperatures transfering heat to each other. The heat transfer is only between the two object, no environment is considered.
- *object_object_environment.py* : this script plot the temperature / time graph of two object at different temperatures transfering heat to each other, surrounded by a steady temperature environment. 




## object_environment.py


Let's consider an object of mass $m$, temperature $T_{init}$ and specific heat $c$ surrounded by an environment with a steady temperature $T_{env}$ and with a thermal resistance $R$ between them. 
From this, it is possible to analytically find the temperature function $T(t)$ of the object, that is, find the rate of change in temperature over time. Actually, it's exponential.

To find it, let us consider a system with the properties we provided. It doesn't matter if the object is cooler or hotter than the environment, physics works both ways :)

Given that, let us quantify the total heat transfered by the object or to the object in a very small period of time $dt$:

$$Q_{total} = m \cdot c \cdot (T(t + dt) - T(t))$$

Now, we can think of the total heat exchanged as the total heat power released in the $dt$ interval:

$$Q_{total} = \dot{Q}_{total} \cdot dt = m \cdot c \cdot (T(t + dt) - T(t))$$

Then, from the electro-thermal analogy we can express the heat power using the temperature of the environment $T_{env}$, the temperature of the object at that time $T(t)$, and the thermal resistance $R$ facing between them:

$$-\frac{T(t) - T_{env}}{R} \cdot dt = m \cdot c \cdot (T(t + dt) - T(t))$$

The - sign is fundamental to maintain the equivalence (for example, suppose the object is cooling: in that case $T(t) - T_{env} > 0$ but $T(t + dt) - T(t) < 0$ and so the - is fundamental so balance the equation.
If the object is warming it goes the other way round).

Finally, we can divide both terms by $dt$: the $dt$ in the left term cancels out, while in the right term we recognize the derivative of function $T(t)$:

$$-\frac{T(t) - T_{env}}{R} = m \cdot c \cdot \frac{(T(t + dt) - T(t))}{dt} = m \cdot c \cdot \frac{dT(t)}{dt}$$

We eventually obtained this beautiful linear differential equation for the temperature function! In the end it should look like this:

$$\frac{dT(t)}{dt} + \frac{1}{R \cdot m \cdot c}T(t) = \frac{T_{env}}{R \cdot m \cdot c}$$

Remembering that $T(0) = T_{init}$ we find the following result:

$$T(t) = (T_{init} - T_{env})e^{-\frac{1}{R \cdot m \cdot c}t} + T_{env}$$

This function goes to $T_{env}$ when time goes to infinity, and equals $T_{init}$ at the starting point $T(0)$. It seems to work fine! 

The *object_environment.py* python script uses this analytical result to plot the $T(t)$ graph of a general object, wrapping it into a Tkinter GUI that let you play with the properties of the system.




## object_object_environment.py

Let's consider two objects of mass $m1$ and $m2$, temperature $T^1_{init}$ $T^2_{init}$ and specific heat $c_1$ and $c_2$, surrounded by an environment with a steady temperature $T_{env}$. The thermal resistance between the
two objects is $R_{12}$, between the first object and the environment is $R_{1-env}$ and between the second object and the environment is $R_{2-env}$.

From here, an analytical solution for the temperature diagram could be very difficult to calculate, since the system is too complicated. Anyway, we can opt for an iterative solution! Let us describe the total heat exchanged by the first object in a small period of time $dt$ as:

$$Q_{total} = m_1 \cdot c_1 \cdot (T_1(t + dt) - T_1(t))$$

Again, we can think of the total heat transfered as the total heat power released in the $dt$ interval, so:

$$Q_{total} = \dot{Q}_{total} \cdot dt = m_1 \cdot c_1 \cdot (T_1(t + dt) - T_1(t))$$

Now, the heat power that is being exchanged during the $dt$ interval is the sum of the heat power transfered from oject 1 through di environment and the heat power transfered from object 1 through object 2. 
Thus, by using the electro-thermal analogy we can conclude that:

$$-(\frac{T_1(t) - T_2(t)}{R_{12}} + \frac{T_1(t) - T_{env}}{R_{1-env}}) \cdot dt = m_1 \cdot c_1 \cdot (T_1(t + dt) - T_1(t))$$

The - sign is fundamental to maintain the equivalence (for example, suppose $T_1(t) > T_2(t) > T_{env}$: in that case $T_1(t) - T_2(t) > 0$ and $T_1(t) - T_{env} > 0$ but $T_1(t + dt) - T_1(t) < 0$ and so the - is fundamental so balance the equation).

From this equation we can calculate the temperature of the object at time $t + dt$ given the temperature of the system at time $t$:

$$T_1(t + dt) = T_1(t) - (\frac{T_1(t) - T_2(t)}{R_{12} \cdot m_1 \cdot c_1} + \frac{T_1(t) - T_{env}}{R_{1-env} \cdot m_1 \cdot c_1}) \cdot dt$$

For example, after the first $dt$ interval the temperature would be:

$$T_1(0 + dt) = T_1(0) - (\frac{T_1(0) - T_2(0)}{R_{12} \cdot m_1 \cdot c_1} + \frac{T_1(0) - T_{env}}{R_{1-env} \cdot m_1 \cdot c_1}) \cdot dt = T^1_{init} - (\frac{T^1_{init} - T^2_{init}}{R_{12} \cdot m_1 \cdot c_1} + \frac{T^1_{init} - T_{env}}{R_{1-env} \cdot m_1 \cdot c_1}) \cdot dt$$

By iterating this formula over and over again it is possible to build the temperature graph of the object. This rule is applied in the object_object_environment.py script, and seems to work pretty well.



