def and_(circ,a,b,out):
    if not type(a)==int:
        raise TypeError("a must be an integer")
    if not type(b)==int:
        raise TypeError("b must be an integer")
    if not type(out)==int:
        raise TypeError("out must be an integer")
    if not len(tuple({a,b,out}))==len((a,b,out)):
        raise ValueError("Qubits mustn't be coincided")
    circ.ccx(a,b,out)

def or_(circ,a,b,out):
    if not type(a)==int:
        raise TypeError("a must be an integer")
    if not type(b)==int:
        raise TypeError("b must be an integer")
    if not type(out)==int:
        raise TypeError("out must be an integer")
    if not len(tuple({a,b,out}))==len((a,b,out)):
        raise ValueError("Qubits mustn't be coincided")
    circ.cx(a,out)
    circ.cx(b,out)
    circ.ccx(a,b,out)
    
def xor_(circ,a,b,out):
    if not type(a)==int:
        raise TypeError("a must be an integer")
    if not type(b)==int:
        raise TypeError("b must be an integer")
    if not type(out)==int:
        raise TypeError("out must be an integer") 
    if not len(tuple({a,b,out}))==len((a,b,out)):
        raise ValueError("Qubits mustn't be coincided")
    circ.cx(a,out)
    circ.cx(b,out)
    
def nand_(circ,a,b,out):
    if not type(a)==int:
        raise TypeError("a must be an integer")
    if not type(b)==int:
        raise TypeError("b must be an integer")
    if not type(out)==int:
        raise TypeError("out must be an integer")
    if not len(tuple({a,b,out}))==len((a,b,out)):
        raise ValueError("Qubits mustn't be coincided")
    circ.ccx(a,b,out)
    circ.x(out)
    
def nor_(circ,a,b,out):
    if not type(a)==int:
        raise TypeError("a must be an integer")
    if not type(b)==int:
        raise TypeError("b must be an integer")
    if not type(out)==int:
        raise TypeError("out must be an integer")
    if not len(tuple({a,b,out}))==len((a,b,out)):
        raise ValueError("Qubits mustn't be coincided")
    circ.cx(a,out)
    circ.cx(b,out)
    circ.ccx(a,b,out)
    circ.x(out)

def xnor_(circ,a,b,out):
    if not type(a)==int:
        raise TypeError("a must be an integer")
    if not type(b)==int:
        raise TypeError("b must be an integer")
    if not type(out)==int:
        raise TypeError("out must be an integer")
    if not len(tuple({a,b,out}))==len((a,b,out)):
        raise ValueError("Qubits mustn't be coincided")
    circ.cx(a,out)
    circ.cx(b,out)
    circ.x(out)

def half_adder(circ, a, b, carry,sum_):
    xor_(circ,a,b,sum_)
    and_(circ,a,b,carry)
    
def full_adder(circ,a,b,c_in,c_out,sum_):
    circ.cx(a,sum_)
    circ.cx(b,sum_)
    circ.cx(c_in,sum_)
    circ.ccx(a,b,c_out)
    circ.ccx(b,c_in,c_out)
    circ.ccx(c_in,a,c_out)
    
def half_subtractor(circ, a, b, carry, diff):
    xor_(circ,a,b,diff)
    circ.ccx(b,diff,carry)
    
def full_subtractor(circ,a,b,b_in,b_out,diff):
    circ.cx(a,diff)
    circ.cx(b,diff)
    circ.cx(b_in,diff)
    circ.x(a)
    circ.ccx(b_in,a,b_out)
    circ.ccx(b_in,b,b_out)
    circ.ccx(a,b,b_out)
    circ.x(a)
  
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
    for i in range(len(A)-1,1,-1):
        circ.ccx(T[i-2],A[i-1],T[i-1])
        circ.ccx(T[i-2],B[i-1],T[i-1])
        circ.ccx(B[i-1],A[i-1],T[i-1])
    circ.ccx(A[0],B[0],T[0])

def __fs(circ,a,b,b_in,b_out,diff):
    circ.cx(a,diff)
    circ.cx(b,diff)
    circ.cx(b_in,diff)
    circ.x(a)
    circ.ccx(b_in,a,b_out)
    circ.ccx(b_in,b,b_out)
    circ.ccx(a,b,b_out)

    
def multi_qubits_subtractor(circ,A,B,T,C):
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

    half_subtractor(circ,A[0],B[0],T[0],C[0])
    for i in range(1,len(A)-1):
        __fs(circ,A[i],B[i],T[i-1],T[i],C[i])
    __fs(circ,A[-1],B[-1],T[-1],C[-1],C[-2])
    for i in range(len(A)-2,0,-1):
        circ.ccx(A[i],B[i],T[i])
        circ.ccx(B[i],T[i-1],T[i])
        circ.ccx(A[i],T[i-1],T[i])
    circ.ccx(C[0],B[0],T[0])
    circ.x(A[1:])

class utils():
    @staticmethod
    def analyse(sv,p,q,t):
        if p=="-":
            probs=[]
            
            for i in range(len(sv)):
                if not sv[i]==0:
                    probs.append([i,abs(sv[i])**2])
            l=len(probs)
            for i in range(l):
                s=bin(probs[i][0])[2:]
                probs[i].append("0"*(3*q+t+1-len(s))+s)
                
            for i in range(l):
                s=probs[i][2]
                probs[i].append(s[:q+1]+"-"+s[q+1:t+q+1]+"-"+s[t+q+1:t+2*q+1]+"-"+s[2*q+t+1:3*q+t+1])
            for i in range(l):
                s=probs[i][3].split("-")
                c,b,a=int(s[0][1:],2),int(s[2][1:],2),int(s[3][1:],2)
                c,b,a=int(s[0],2),int(s[2],2),int(s[3],2)
                a=int(s[3],2)
                b=int(s[2],2)
                if s[0][0]=="0":
                    c=int(s[0],2)
                else:
                    c=-2**(q)+int(s[0][1:],2)
                probs[i].append((str(c)+"="+str(a)+"-"+str(b)).replace("--","+"))            
            return probs
        
        elif p=="+":
            probs=[]
            for i in range(len(sv)):
                if not sv[i]==0:
                    probs.append([i,abs(sv[i])**2])
            for i in range(len(probs)):
                probs[i][0]=bin(probs[i][0])[2:]
                probs[i][0]="0"*(3*q+1+t-len((probs[i][0])))+probs[i][0]
            
            for i in range(len(probs)):
                probs[i].append(probs[i][0][:q+1]+"-"+probs[i][0][q+1:t+q+1]+"-"+probs[i][0][q+t+1:2*q+t+1]+"-"+probs[i][0][2*q+t+1:3*q+t+1])
            for i in range(len(probs)):
                m=""
                t=probs[i][2].split("-")
                m+=str(int(t[0],2))+"="+str(int(t[2],2))+"+"+str(int(t[3],2))
                probs[i].append(m)
            return probs
        elif p=="×":
            probs=[]
            for i in range(len(sv)):
                if not sv[i]==0:
                    probs.append([i,abs(sv[i])**2])
            for i in range(len(probs)):
                probs[i][0]=bin(probs[i][0])[2:]
                probs[i][0]="0"*(3*q+1+t-len((probs[i][0])))+probs[i][0]
            
            for i in range(len(probs)):
                probs[i].append(probs[i][0][:q+1]+"-"+probs[i][0][q+1:t+q+1]+"-"+probs[i][0][q+t+1:2*q+t+1]+"-"+probs[i][0][2*q+t+1:3*q+t+1])
            for i in range(len(probs)):
                m=""
                t=probs[i][2].split("-")
                m+=str(int(t[0],2))+"="+str(int(t[2],2))+"×"+str(int(t[3],2))
                probs[i].append(m)
            return probs
