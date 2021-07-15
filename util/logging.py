from typing import Callable
def log(f: Callable) -> Callable:

    def wrapped(*args, **kwargs):
        print(f"START {args} {kwargs}")
        result = f(*args, **kwargs)
        print(f"FINISH {args} {kwargs} {result}")
        return result

    return wrapped
