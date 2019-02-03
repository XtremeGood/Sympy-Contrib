#!/usr/bin/env python
# coding: utf-8

# In[5]:


from sympy.abc import x
from sympy.solvers.deutils import ode_order
from sympy.solvers.ode import classify_ode,sub_func_doit,dsolve
from sympy import *
init_printing()

def reduction_of_order(eq):
    
    try: 
        
        return dsolve(eq)

    except NotImplementedError:
        
        atom_x = list(eq.atoms(Symbol))[0]
        atom_f = list(eq.atoms(Function))[0]
        
        if ode_order(eq,atom_f)> 1:
            g = Function('g')(atom_x)
            eq = eq.subs(atom_f.diff(atom_x),g)
            if not(eq.has(atom_f)):
                return dsolve(reduction_of_order(eq).subs(g,atom_f.diff(atom_x)))
            else:
                raise NotImplementedError
        else:
            raise NotImplementedError
            
    else:
        raise NotImplementedError
            


# In[ ]:





# In[ ]:




