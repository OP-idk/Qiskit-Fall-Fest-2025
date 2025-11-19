# Qiskit Fall Fest 2025 Submission
My submission to the 2025 Qiskit Fall Fest Challenges

Challenges Completed:
- Cryptography
- Random Number Generator

Note: Neither of my solutions are set up to run on real quantum hardware yet, they currently just use the qiskit AerSimulator

## start.sh
Bash script that sets up the virtual environment and installs the needed packages

## rng.py
Generates a random number between `0` and `num_outputs - 1`. Accounts for values of `num_outputs` that are not powers of 2

## bb84.py
Implementation of the BB84 Quantum Key Distribution algorithm. The value of `evesdropper` determines if an evesdropper is present in the interaction.
