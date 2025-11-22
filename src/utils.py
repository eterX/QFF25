import numpy as np
from qiskit import QuantumCircuit
from qiskit.circuit.library import ZGate

def _oracle(circuit, key):
    """
    Implementa el oráculo que marca el estado 'key'.
    """
    # Invertimos la clave para que coincida con el orden de qubits de Qiskit (q_n-1...q_0)
    reversed_key = key[::-1]
    
    # Aplicamos compuertas X a los qubits que son '0' en la clave
    for i, bit in enumerate(reversed_key):
        if bit == '0':
            circuit.x(i)
    
    # Aplicamos una compuerta Z multi-controlada
    num_qubits = circuit.num_qubits
    circuit.append(ZGate().control(num_qubits - 1), range(num_qubits))
    
    # Revertimos las compuertas X
    for i, bit in enumerate(reversed_key):
        if bit == '0':
            circuit.x(i)


def _diffuser(circuit, n):
    """
    Implementa el difusor de Grover para n qubits.
    """
    # Se implementa como H...H -> X...X -> MCZ -> X...X -> H...H
    circuit.h(range(n))
    circuit.x(range(n))
    
    # Compuerta Z multi-controlada
    circuit.append(ZGate().control(n - 1), range(n))
    
    circuit.x(range(n))
    circuit.h(range(n))

def create_grover_circuit(n_qubits, secret_key):
    """
    Crea un circuito de Grover completo.

    Args:
        n_qubits (int): El número de qubits.
        secret_key (str): La clave secreta a buscar.

    Returns:
        QuantumCircuit: El circuito de Grover completo.
    """
    # Inicialización: Aplicar Hadamard a todos los qubits
    grover_circuit = QuantumCircuit(n_qubits, n_qubits)
    grover_circuit.h(range(n_qubits))
    grover_circuit.barrier()

    # --- Aplicar Grover (Oráculo + Difusor) ---
    # El número óptimo de iteraciones es aprox. (pi/4) * sqrt(2^n)
    iterations = int(np.round(np.pi/4 * np.sqrt(2**n_qubits)))
    print(f"Número de qubits: {n_qubits}, Iteraciones de Grover: {iterations}")

    for _ in range(iterations):
        _oracle(grover_circuit, secret_key)
        grover_circuit.barrier()
        _diffuser(grover_circuit, n_qubits)
        grover_circuit.barrier()

    # --- Medición ---
    grover_circuit.measure(range(n_qubits), range(n_qubits))
    return grover_circuit