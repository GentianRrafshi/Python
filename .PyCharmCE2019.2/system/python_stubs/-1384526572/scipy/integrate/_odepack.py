# encoding: utf-8
# module scipy.integrate._odepack
# from C:\Program Files (x86)\Python37-32\lib\site-packages\scipy\integrate\_odepack.cp37-win32.pyd
# by generator 1.147
# no doc
# no imports

# Variables with simple values

__version__ = ' 1.9 '

# functions

def odeint(fun, y0, t, args=(), Dfun=None, col_deriv=0, ml, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    [y,{infodict,}istate] = odeint(fun, y0, t, args=(), Dfun=None, col_deriv=0, ml=, mu=, full_output=0, rtol=, atol=, tcrit=, h0=0.0, hmax=0.0, hmin=0.0, ixpr=0.0, mxstep=0.0, mxhnil=0, mxordn=0, mxords=0)
      yprime = fun(y,t,...)
    """
    pass

# classes

class error(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x0FE4E810>'

__spec__ = None # (!) real value is "ModuleSpec(name='scipy.integrate._odepack', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x0FE4E810>, origin='C:\\\\Program Files (x86)\\\\Python37-32\\\\lib\\\\site-packages\\\\scipy\\\\integrate\\\\_odepack.cp37-win32.pyd')"

