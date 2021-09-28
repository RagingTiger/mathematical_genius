# std libs
import math


# funcs
def pi_approximation(n: int) -> tuple[float, float]:
    """Approximates pi using an n-sided polygon.
    
    Ref: https://arxiv.org/abs/2008.07995
    """
    # convert to radians
    angle = math.radians(180 / n)
    
    # calculate circumscribed approximation
    circum_approx = n * math.tan(angle)
    
    # calculate inscribed approximation
    inscribed_approx = n * math.sin(angle)
    
    # return values
    return inscribed_approx, circum_approx
    