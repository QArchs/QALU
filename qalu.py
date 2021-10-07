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
    
