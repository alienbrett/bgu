import numpy as np
import typing

def calculate_implied_correlation(
        sigmas:       np.ndarray,
        observed_vol: float,
        weights:      typing.Optional[np.ndarray],
    ) -> float:

    sigmas = sigmas.reshape(-1,1)
    var = sigmas**2
    n = len(sigmas)
    
    if weights is None:
        weights = np.ones(n)/n
    weights = weights.reshape(-1,1)

    # Hypothetical covariance matrix, for 100% correlation
    cov_mat = sigmas @ sigmas.T

    m0 = weights.T @ (cov_mat - np.eye(n)*var) @ weights
    k = np.sum(weights**2 * var)

    corr = (observed_vol**2 - k)/m0

    return corr.reshape(-1)
