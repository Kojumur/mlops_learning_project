import numpy as np
import pandas as pd


def generate_data(
    k: float,
    b: float,
    num: int,
    mu: float = 0,
    sigma: float = 1,
    ):
    """
    Generate data according to the rule: y = kx + b + e, where e is random
    variable with normal distribution N(mu, sigma)

    Args:
        k (float): slope coefficient
        b (float): bias
        num (int): number of data points to generate
        mu (float, optional): mean of random variable e. Defaults to 0.
        sigma (float, optional): standart deviation of random
            variable e. Defaults to 1.
    """
    x = np.random.uniform(-100, 100, num)
    e = np.random.normal(mu, sigma, num)

    y = k * x + b + e
    df = pd.DataFrame({'x': x, 'y': y})
    return df
