# Arithmetic Operations
    QALU has arithmetic operators: adders and subtractors. 
***
## half_adder(circ, a, b, carry,sum_)
    **half_adder** adds two qubits (**a**+**b**). It has 5 arguments:
  * **circ** is QuantumCircuit that will be added half_adder.
  * **a** is position of qubit that will be added.
  *  **b** is position of qubit that will be added.
  *  **carry** is position of qubit that has information of carry loaded.
  *  **sum_** is position of qubit that has information of sum.
## full_adder(circ,a,b,c_in,c_out,sum_)
    **full_adder** adds three qubits (**a**+**b**+**c_in**). It has 6 arguments:
  * **circ** is QuantumCircuit that will be added full_adder.
  * **a** is position of qubit that will be added.
  *  **b** is position of qubit that will be added.
  *  **c_in** is position of qubit that has carried. 
  *  **c_ot** is position of qubit that has information of carry loaded.
  *  **sum_** is position of qubit that has information of sum.
## half_subtractor(circ, a, b, bor, diff)
    **half_subtractor** subtracts two qubits (**a**-**b**). It has 5 arguments:
  * **circ** is QuantumCircuit that will be added half_adder.
  * **a** is position of qubit that is minuend.
  *  **b** is position of qubit that is subtrahend.
  *  **bor** is position of qubit that represents borrow
  *  **diff** is position of qubit that has information of difference
## full_subtractor(circ,a,b,b_in,b_out,diff)
    **full_subtractor** subtracts qubits (**a**-**b**-**b_in**). It has 6 arguments:
  * **circ** is QuantumCircuit that will be added full_subtracted.
  * **a** is position of qubit that is minuend.
  *  **b** is position of qubit that is subtrahend.
  *  **b_in** is position of qubit that has borrowed. 
  *  **c_ot** is position of qubit that has information of carry loaded.
  *  **sum_** is position of qubit that has information of sum.
## def multi_qubits_adder(circ,A,B,T,C)
    **multi_qubits_adder** 
