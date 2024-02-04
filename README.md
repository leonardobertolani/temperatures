The scripts in this repo deals with some basic thermodynamics, displaying the rate of change in temperature of objects over time. Every script deal with a different problem:
- *object_environment.py*: this script plot the temperature / time graph of an object cooling or heating in a steady temperature environment.
- *object_object.py*: this script plot the temperature / time graph of two object transfering heat to each other. The heat transfer is only between the two object, no environment is considered.


## object_environment.py

Let's consider an object of mass $m$, temperature $T_{init}$ and thermal coefficient $c$ surrounded by an environment with a steady temperature $T_{env}$ and with a thermal resistance $R$ between them. 
From this, it is possible to analytically find the temperature function $T(t)$ of the object, that is, find the rate of change in temperature over time. Actually, it's exponential.

To find it, let us consider a system with the properties we provided. It doesn't matter if the object is cooler or hotter than the environment, physics works both ways :)

Given that, let us quantify the total heat transfered by the object or to the object in a very small period of time $dt$:

$Q_{total} = m \cdot c \cdot (T(t + dt) - T(t))$

Now, we can think of the total heat exchanged as the total heat power released in the $dt$ interval:

$Q_{total} = \dot{Q}_{total} \cdot dt = m \cdot c \cdot (T(t + dt) - T(t))$

Then, from the electro-thermal analogy we can express the heat power using the temperature of the environment $T_{env}$, the temperature of the object at that time $T(t)$, and the thermal resistance $R$ facing between them:

$-\frac{T(t) - T_{env}}{R} dt = m \cdot c \cdot (T(t + dt) - T(t))$

The - sign is fundamental to maintain the equivalence (for example, suppose the object is cooling: in that case $T(t) - T_{env} > 0$ but $T(t + dt) - T(t) < 0$ and so the - is fundamental so balance the equation.
If the object is warming it goes the other way round).

Finally, we can divide both terms by $dt$: the $dt$ in the left term cancels out, while in the right term we recognize the derivative of function $T(t)$:

$-\frac{T(t) - T_{env}}{R} = m \cdot c \cdot \frac{(T(t + dt) - T(t))}{dt} = m \cdot c \cdot \frac{dT(t)}{dt}$

 We eventually obtained this beautiful linear differential equation for the temperature function! In the end it should look like this:

 $\frac{dT(t)}{dt} + \frac{1}{R \cdot m \cdot c}T(t) = \frac{T_{env}}{R \cdot m \cdot c}$

Remembering that $T(0) = T_{init}$ we find the following result:

$T(t) = (T_{init} - T_{env})e^{-\frac{1}{R \cdot m \cdot c}t} + T_{env}$

 This function goes to $T_{env}$ when time goes to infinity, and equals $T_{init}$ at the starting point $T(0)$. It seems to work fine! 

 The object_environment.py python script uses this analytical result to plot the $T(t)$ graph of a general object, wrapping it into a Tkinter GUI that let you play with the properties of the system.
