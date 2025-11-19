#!/bin/bash
python3 -m venv .venv
source .venv/bin/activate

pip install qiskit
pip install qiskit[visualization]==1.1.0
# Use the following if you are on MacOS/zsh
#!pip install 'qiskit[visualization]'==1.1.0
pip install qiskit_aer
pip install qiskit_ibm_runtime
pip install numpy