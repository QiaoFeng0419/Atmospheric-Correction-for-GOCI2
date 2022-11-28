import numpy as np


def rho_709_to_rho745(rho_709):
    """
    Reference: Estimating Water Reflectance at Near-Infrared Wavelengths for Turbid Water Atmospheric Correction: A Preliminary Study for GOCI-II
    """
    coef = np.array([0.00079, 0.2614, 0.1614, 52.333])
    p = np.polynomial.polynomial.Polynomial(coef=coef)
    rho_745 = p(rho_709)
    return rho_745


def rho_745_to_rho865(rho_745):
    """
    Reference: Estimating Water Reflectance at Near-Infrared Wavelengths for Turbid Water Atmospheric Correction: A Preliminary Study for GOCI-II
    """
    coef = np.array([0, 0.4885, 2.4233])
    p = np.polynomial.polynomial.Polynomial(coef=coef)
    rho_865 = p(rho_745)
    return rho_865
