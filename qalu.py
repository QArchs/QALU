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
