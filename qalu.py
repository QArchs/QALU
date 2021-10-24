def and_(circ,a,b,out):
    circ.ccx(a,b,out)

def or_(circ,a,b,out):
    circ.cx(a,out)
    circ.cx(b,out)
    circ.ccx(a,b,out)
    
def xor_(circ,a,b,out):
    circ.cx(a,out)
    circ.cx(b,out)
    
def nand_(circ,a,b,out):
    circ.ccx(a,b,out)
    circ.x(out)
    
def nor_(circ,a,b,out):
    circ.cx(a,out)
    circ.cx(b,out)
    circ.ccx(a,b,out)
    circ.x(out)

def xnor_(circ,a,b,out):
    circ.cx(a,out)
    circ.cx(b,out)

def half_adder(circ, a, b, carry,sum_):
    xor_(circ,a,b,sum_)
    and_(circ,a,b,carry)
    
def full_adder(circ,a,b,c_in,c_out,sum_):
    qc.cx(a,sum_)
    qc.cx(b,sum_)
    qc.cx(c_in,sum_)
    qc.ccx(a,b,c_out)
    qc.ccx(b,c_in,c_out)
    qc.ccx(c_in,a,c_out)
    
def half_subtractor(circ, a, b, carry, diff):
    xor_(circ,a,b,diff)
    circ.ccx(b,diff,carry)
    
def full_subtractor(circ,a,b,b_in,b_out,diff):
    qc.cx(a,diff)
    qc.cx(b,diff)
    qc.cx(b_in,diff)
    qc.x(a)
    qc.ccx(b_in,a,b_out)
    qc.ccx(b_in,b,b_out)
    qc.ccx(a,b,b_out)
    qc.x(a)
  
def multi_qubits_adder(circ,A,B,T,C):
    if not (type(A)==tuple or type(A)==list):
        raise TypeError("A must be a tuple or list")
    if not (type(B)==tuple or type(B)==list):
        raise TypeError("B must be a tuple or list")
    if not (type(T)==tuple or type(T)==list):
        raise TypeError("T must be a tuple or list")
    if not (type(C)==tuple or type(C)==list):
        raise TypeError("C must be a tuple or list")
    if not len(A)==len(B):
        raise ValueError("# of qubits of A and B must be equal")
    if not len(A)+1==len(C):
        raise ValueError("C must has one more qubit than A and B")
    if not len(A)-1==len(T):
        raise ValueError("T must has one more less qubit than A and B")
    A=tuple(A)
    B=tuple(B)
    T=tuple(T)
    C=tuple(C)
    if len(set(A+B+T+C))<len(A+B+T+C):
        raise ValueError("Qubits must not coindice")
        
    half_adder(circ,A[0],B[0],T[0],C[0])
    for i in range(1,len(A)-1):
        full_adder(circ,A[i],B[i],T[i-1],T[i],C[i])
    full_adder(circ,A[-1],B[-1],T[-1],C[-1],C[-2])
