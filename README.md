Three-Body problem
A small Python project where I explore how three bodies interact through gravity.

I started this project to understand the three-body problem through simulation rather than just reading about it. The idea is to give three bodies initial positions and velocities, let gravity influence their motion, and see how their trajectories develop over time.

It's a work in progress, and I plan to improve both the simulation and my understanding of the physics behind it as I learn more.

What it currently does
Simulates the gravitational interactions between three bodies in two dimensions.
Animates their movement using Python and Matplotlib.
Displays trails showing their recent trajectories.
Provides several starting configurations, including random initial conditions and a few predefined systems.
Allows users to enter their own initial positions and velocities.
Offers several figure-size presets for the visualization.
Built with
Python
NumPy
Matplotlib
Getting started

You'll need Python installed on your computer.

Install the required libraries:

pip install numpy matplotlib

How it works

The simulation calculates the gravitational acceleration of each body based on the positions of the other two bodies.

It then updates the velocities and positions in small time steps and uses Matplotlib to animate the resulting motion.

The current implementation uses a simple numerical integration method. The accuracy of the results depends on factors such as the time step, initial conditions, and how closely the bodies approach one another.

Things I want to explore next
Improve the numerical integration method.
Investigate energy conservation and numerical errors.
Explore how different initial conditions affect the motion.
Improve the visualization and simulation controls.
Compare the simulated motion with known solutions of the three-body problem.
Progress

This project is an ongoing learning exercise. I'll update the code as I experiment with different approaches, understand the physics more deeply, and improve the implementation.

Feedback and suggestions are welcome.
