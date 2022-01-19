import numpy as np
def simplex(A, b, c, x, basic_vars = None, minimize: bool = True) -> np.array :
    """
    Implementation of the simplex method for linear programming
    problems

    Args:
    -----------------------------------
    A:  Matrix of size constraints x variables with the coefficients of 
        the variables in the constraints (equalities)
        (3x1 + 2x2) -> (3, 2)
    b:  Vector  of constraints size with the the independent variable of the constraints
    c:  Vector of size variables with the cost associataed to the variables in the objective funciton.
    x:  Initial feasible solution
    basic_vars: List with the basic variables in the current solution

    Returns:
    ------------------------------------
    result: String with the result status (unbounded, unfeasible, optimal)
    x:   Array of size variables which contains the optimal solution if result is optimal
    """

    # Convert to numpy arrys
    A_ = np.array(A)
    b_ = np.array(b)
    c_ = np.array(c)
    x_ = np.array(x)

    # Infers te basic variables if they are not given (does not work with 0)
    if not basic_vars:
        basic_vars = [i for i, v in enumerate(x_) if v == 0 ]

    B = np.matrix(A_[:, basic_vars])
    if B.shape[0] != B.shape[1]:
        return

    cb = c_[basic_vars]
    sensibilities = np.linalg.solve(B.T, cb)
    
    N = np.delete(A_, basic_vars, axis=1)
    cn = np.delete(c, basic_vars)

    sensibilities = cn - np.linalg.matmul(N.T, sensibilities)
    
    Nj = np.argmin(sensibilities)
    if sensibilities[Nj] >= 0:
        return "optimal", x
    
    direction_basic = np.linalg.solve(B, A_[:, Nj])
    step_size = min(-x_[basic_vars]/direction_basic)
    direction = direction_basic.tolist()
    # todo: create the direction vector (union of the direction basic and the non basic)
    x = x + step_size * direction