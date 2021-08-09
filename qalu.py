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
    
def full_adder(circ,a,b,c_in,t_0,t_1,t_2,c_out,sum_):
    xor_(circ,a,b,t_0)
    xor_(circ,t_0,c_in,sum_)
    and_(circ,a,b,t_1)
    and_(circ,c_in,t_0,t_2)
    or_(circ,t_1,t_2,c_out)
    
def half_subtractor(circ, a, b, carry, diff):
    xor_(circ,a,b,diff)
    circ.ccx(b,diff,carry)
    
def full_subtractor(circ,a,b,c_in,t_0,t_1,t_2,c_out,diff):
    xor_(circ,a,b,t_0)
    xor_(circ,t_0,c_in,diff)
    circ.x(a)
    circ.ccx(a,b,t_1)
    circ.x(a)
    circ.x(t_0)
    circ.ccx(t_0,c_in,t_2)
    or_(circ,t_1,t_2,c_out)
