from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit.classical import expr
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import numpy as np
from math import pi
from enum import Enum

"""
Method that takes in a quantum circuit, a basis, and a bit, and applies the 
corresponding gates

Method that takes in a quantum circuit and a basis, applies the corresponding
gates, the measures and returns the recieved bit
"""

qr = QuantumRegister(1)
cr = ClassicalRegister(1)
qc = QuantumCircuit(qr, cr)
key_length = 16

class Basis(Enum):
    ZERO = 1
    PLUS = 2

for i in range(key_length):
    pass

def send(qc : QuantumCircuit, basis : Basis, bit : int ):
    if bit == 1:
        qc.x(0)
    if basis == Basis.PLUS:
        qc.h(0)

    pass

def recieve(qc, basis : Basis) -> int:
    if basis == Basis.PLUS:
        qc.h(0)
    qc.measure(0, cr[0])
    sim = AerSimulator()
    result = sim.run(qc).result()
    counts = result.get_counts()
    bit = -1
    if len(counts) == 1:
        bit = int(counts.most_frequent())
    else:
        for c in counts: # take result of first shot then exit loop
            bit = int(c)
            break
    #print(counts)
    print(bit)
    qc.reset(0)
    #print(len(counts))

    """
    bit = expr.lift(cr[0])
    with qc.if_test(bit):
        print("1")
    pass
    """
for i in range(key_length):
    send(qc, Basis.ZERO, 1)
    recieve(qc, Basis.PLUS)