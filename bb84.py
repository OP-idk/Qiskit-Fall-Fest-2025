from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit.classical import expr
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import numpy as np
from math import pi
from enum import Enum
import random as rng

key_length = 32
check_length = 8

evesdropper = True

a_bits = []
a_bases = []
a_key = []

b_bits = []
b_bases = []
b_key = []

qr = QuantumRegister(1)
cr = ClassicalRegister(1)
qc = QuantumCircuit(qr, cr)

class Basis(Enum):
    ZERO = 1
    PLUS = 2

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
    #print(bit)
    qc.reset(0)
    return bit

# Actual Algorithm
for i in range(key_length):
    # Alice: Send
    a_rand_basis = rng.choice([Basis.ZERO, Basis.PLUS])
    a_rand_bit = rng.choice([0, 1])
    
    a_bases.append(a_rand_basis)
    a_bits.append(a_rand_bit)

    send(qc, a_rand_basis, a_rand_bit)

    # Eve: Recieve and send
    if evesdropper:
        e_recieve_basis = rng.choice([Basis.ZERO, Basis.PLUS])
        #e_send_basis = rng.choice([Basis.ZERO, Basis.PLUS])
        e_recieved_bit = recieve(qc, e_recieve_basis)
        send(qc, e_recieve_basis, e_recieved_bit)
    
    b_recieve_basis = rng.choice([Basis.ZERO, Basis.PLUS])
    b_recieved_bit = recieve(qc, b_recieve_basis)
    
    b_bases.append(b_recieve_basis)
    b_bits.append(b_recieved_bit)

print("Evesdropper present?: " + str(evesdropper))
print("Alice's sent bits:   " + str(a_bits))
print("Bob's recieved bits: " + str(b_bits))

for i in range(key_length):
    if a_bases[i] == b_bases[i]:
        a_key.append(a_bits[i])
        b_key.append(b_bits[i])

print("")
print("Alice's Key: " + str(a_key))
print("Bob's key:   " + str(b_key))

result_msg = "Key Valid!"
# Check resulting key is a decent length
if len(a_key) <= check_length * 2:
    result_msg = "Key Invalid: too short"
else:
    # Check for evesdropper and discard check bits
    for i in range(check_length):
        if a_key[i] != b_key[i]:
            result_msg = "Key Invalid: noise or evesdropper detected"

a_key = a_key[check_length:]
b_key = b_key[check_length:]

print(result_msg)
print("")
print("Alice's Final Key: " + str(a_key))
print("Bob's Final key:   " + str(b_key))

