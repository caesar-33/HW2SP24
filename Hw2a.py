import math


def simpsons_rule(f, a, b, n=1000):
    """Simpson's rule for numerical integration."""
    h = (b - a) / n
    s = f(a) + f(b)

    for i in range(1, n, 2):
        s += 4 * f(a + i * h)
    for i in range(2, n - 1, 2):
        s += 2 * f(a + i * h)

    return s * h / 3


def gaussian_pdf(x, mu, sigma):
    """Gaussian probability density function."""
    return 1 / (math.sqrt(2 * math.pi) * sigma) * math.exp(-0.5 * ((x - mu) / sigma) ** 2)


def Probability(PDF, args, c, GT=True):
    """Calculate the probability of x being greater or less than c."""
    mu, sigma = args
    if GT:
        # For x > c, integrate from c to mu + 5σ
        lower_bound = c
        upper_bound = mu + 5 * sigma
    else:
        # For x < c, integrate from mu - 5σ to c
        lower_bound = mu - 5 * sigma
        upper_bound = c

    # Define a wrapped PDF function to integrate
    def wrapped_pdf(x):
        return PDF(x, mu, sigma)

    # Use Simpson's 1/3 rule for integration
    probability = simpsons_rule(wrapped_pdf, lower_bound, upper_bound)
    return probability


def main():
    # Example calculations
    print(f"P(x<105|N(100,12.5))={Probability(gaussian_pdf, (100, 12.5), 105, GT=False):.2f}")
    print(f"P(x>μ+2σ|N(100, 3))={Probability(gaussian_pdf, (100, 3), 100 + 2 * 3, GT=True):.2f}")


if __name__ == "__main__":
    main()
