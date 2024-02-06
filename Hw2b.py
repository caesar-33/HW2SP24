import math


def Secant(fcn, x0, x1, maxiter=10, xtol=1e-5):
    """
    Secant method for finding a root of fcn(x) in the neighborhood of x0 and x1.

    Parameters:
    - fcn: The function for which we want to find the root.
    - x0, x1: Two initial guesses close to the root.
    - maxiter: Maximum number of iterations.
    - xtol: Tolerance for convergence (the method exits if the difference between successive iterations is less than xtol).

    Returns:
    - The estimated root of the function.
    """
    for _ in range(maxiter):
        fx0 = fcn(x0)
        fx1 = fcn(x1)
        if abs(fx1 - fx0) < 1e-10:  # Prevent division by zero
            break
        xnew = x1 - (fx1 * (x1 - x0) / (fx1 - fx0))
        if abs(xnew - x1) < xtol:
            return xnew
        x0, x1 = x1, xnew
    return x1


def main():
    # First function: x - 3*cos(x) = 0
    f1 = lambda x: x - 3 * math.cos(x)
    root1 = Secant(f1, 1, 2, 5, 1e-4)
    print(f"Root of x - 3*cos(x) = 0: {root1}")

    # Second function: cos(2x)*x^3 = 0
    f2 = lambda x: math.cos(2 * x) * x ** 3
    root2 = Secant(f2, 1, 2, 15, 1e-8)
    print(f"Root of cos(2x)*x^3 = 0: {root2}")

    # Third function: cos(2x)^3 = 0
    f3 = lambda x: math.cos(2 * x) ** 3
    root3 = Secant(f3, 1, 2, 3, 1e-8)
    print(f"Root of cos(2x)^3 = 0: {root3}")


if __name__ == "__main__":
    main()
