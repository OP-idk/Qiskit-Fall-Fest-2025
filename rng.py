from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import numpy as np
from math import pi

num_outcomes = 129 
n = int(np.ceil(np.log2(num_outcomes)))
qc = QuantumCircuit(n, n)

qc.h(range(n))
qc.measure(range(n), range(n))

sim = AerSimulator()
result = sim.run(qc).result()
counts = result.get_counts()
plot_histogram(counts)
#print(counts)

# First entry in counts array within the given range will be the result of the
# first valid shot which will be random every time
random_number = -1
random_number_int = -1
for count in counts:
    temp_int = int(count, 2)
    if temp_int < num_outcomes:
        random_number = count
        random_number_int = temp_int
        break
    print("    Invalid Generation: " + str(count) + " | " + str(temp_int))

print("Range: 0 to " + str(num_outcomes - 1))
print("Num Qubits: " + str(n))
print("Actual range: 0 to " + str((2 ** n) - 1))
print("Generated Binary: " + str(random_number))
print("Generated Integer: " + str(random_number_int))
