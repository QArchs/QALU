# Arithmetic Operations
    QALU has arithmetic operators: adders and subtractors. 
***
## half_adder(circ, a, b, carry,sum_)
    **half_adder** adds two qubits (**a**+**b**). It has 5 arguments:
  * **circ** is QuantumCircuit that will be added on half_adder.
  * **a** is position of qubit that will be added.
  *  **b** is position of qubit that will be added.
  *  **carry** is position of qubit that has information of carry loaded.
  *  **sum_** is position of qubit that has information of sum.
## full_adder(circ,a, b, c_in, c_out, sum_)
    **full_adder** adds three qubits (**a**+**b**+**c_in**). It has 6 arguments:
  * **circ** is QuantumCircuit that will be added on full_adder.
  * **a** is position of qubit that will be added.
  *  **b** is position of qubit that will be added.
  *  **c_in** is position of qubit that has carried. 
  *  **c_ot** is position of qubit that has information of carry loaded.
  *  **sum_** is position of qubit that has information of sum.
## half_subtractor(circ, a, b, bor, diff)
    **half_subtractor** subtracts two qubits (**a**-**b**). It has 5 arguments:
  * **circ** is QuantumCircuit that will be added on half_adder.
  * **a** is position of qubit that is minuend.
  *  **b** is position of qubit that is subtrahend.
  *  **bor** is position of qubit that represents borrow
  *  **diff** is position of qubit that has information of difference
## full_subtractor(circ, a, b, b_in, b_out, diff)
    **full_subtractor** subtracts qubits (**a**-**b**-**b_in**). It has 6 arguments:
  * **circ** is QuantumCircuit that will be added on full_subtracted.
  * **a** is position of qubit that is minuend.
  *  **b** is position of qubit that is subtrahend.
  *  **b_in** is position of qubit that has borrowed. 
  *  **c_ot** is position of qubit that has information of carry loaded.
  *  **sum_** is position of qubit that has information of sum.
***
## multi_qubits_adder(circ, A, B, T, C)
    **multi_qubits_adder** performs addition(**A+B=C**) on several qubits. It has 5 arguments:
   * **circ** is QuantumCircuit that will be added on multi_qubits_adder
   * **A** is tuple of qubits that will added
    * **B** is tuple of qubits that will added. It must have the same lenght with A
    * **T** is tuple of qubits that used in some temporary calculations. # of elements of it must be one less than # of elements in A or B.  Qubits of T must be in the state of |ψ⟩=|0⟩ .Otherwise multi_qubits_adder() cannot operate properly. At the and of process T's are in the state of |0⟩. This means you can use T qubits for other processes. 
    * **C** is tuple of qubits that has information of sum. It must have one more qubit than A or B. 
## multi_qubits_subtractor(circ, A, B, T, C)
    **multi_qubits_subtractor** performs suntraction (**A-B=C**) on several qubits. It has 5 arguments:
   * **circ** is QuantumCircuit that will be added on multi_qubits_adder
   * **A** is tuple of qubits. A is minuend
   * **B** is tuple of qubits that will added. B is subtrahend. It must have the same lenght with A
   * **T** is tuple of qubits that used in some temporary calculations. # of elements of it must be one less than # of elements in A or B.  Qubits of T must be in the state of |ψ⟩=|0⟩ .Otherwise multi_qubits_subtractor() cannot operate properly. At the and of process T's are in the state of |0⟩. This means you can use T qubits for other processes. 
    * **C** is tuple of qubits that has information of difference. It must have one more qubit than A or B. 
    
