from ..utils.base_multiprocess import Multiprocess

def func(line, params):
    
mul = Multiprocess(
    lines=lines, 
    processes_number=10, 
    function=func, 
    params=params
)