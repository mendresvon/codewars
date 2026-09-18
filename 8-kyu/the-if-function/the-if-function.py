from collections.abc import Callable
​
def _if(bool, func1: Callable, func2: Callable):
    if bool:
        func1()
    else:
        func2()