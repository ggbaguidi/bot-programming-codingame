# Mad Pod Racing - Bot Programming

This is a bot programming game for [CodinGame](https://www.codingame.com/multiplayer/bot-programming/mad-pod-racing) where you control a pod in a race against other bots. Your goal is to be the first to complete all the laps of the circuit.

## Learning Objectives

* **Trajectory Calculation:**  Learn to calculate efficient paths for your pod to reach checkpoints.
* **Collision Avoidance:**  Implement strategies to avoid collisions with other pods.
* **Speed and Inertia:**  Understand how speed and inertia affect your pod's movement.
* **AI and Strategy:**  Develop tactics to optimize your pod's performance and win the race.

## Gameplay Basics

The game is played on a rectangular map with checkpoints scattered throughout. Your pod needs to pass through each checkpoint in the correct order to complete a lap.

* You control your pod by specifying its target coordinates and thrust level.
* The thrust level determines your pod's acceleration (0-100).
* You can use a one-time boost for extra speed.
* Pods have a circular force field that activates in case of collisions.

## Provided Code

This directory contains the Python code for your bot. The code defines functions for:

* `compute_target`: Calculates the target point for your pod to reach the next checkpoint efficiently, considering opponent location.
* `compute_thrust`: Determines the thrust level based on the distance and angle to the next checkpoint.
* `main`: The main loop that continuously reads input, calculates target and thrust, and outputs commands for your pod.

### Running Your Bot

1. Sign up for a CodinGame account (if you haven't already).
2. Create a new bot for the Mad Pod Racing challenge.
3. Copy and paste the provided Python code into your bot's code editor.
4. Run your bot and watch it race against other bots!

## Improvement Ideas

* Fine-tune the target calculation to account for sharper corners or obstacles.
* Develop strategies for using shield rams offensively or defensively.
* Experiment with different boost timings for optimal performance.

This code provides a solid foundation for your Mad Pod Racing bot. With further development and strategic thinking, you can create a champion pod that dominates the racecourse!
