import pandas as pd
import numpy as np
if __name__ == '__main__':
    GOCI2_F0 = []
    f0 = np.loadtxt('f0.txt', skiprows=15)
    rsr_table = pd.read_csv('GOCI-II_SRF_Measured.csv')
    wavelength_headers = ['wavelength', 'wavelength.1', 'wavelength.2', 'wavelength.3', 'wavelength.4', 'wavelength.5',
                          'wavelength.6', 'wavelength.7', 'wavelength.8', 'wavelength.9', 'wavelength.10', 'wavelength.11']
    rsr_headers = ['B1 (380 nm)', 'B2 (412 nm)', 'B3 (443 nm)', 'B4 (490 nm)', 'B5 (510 nm)', 'B6 (555 nm)',
                   'B7 (620 nm)', 'B8 (660 nm)', 'B9 (680 nm)', 'B10 (709 nm)', 'B11 (745 nm)', 'B12 (865 nm)']
    for wavelength_header, rsr_header in zip(wavelength_headers, rsr_headers):
        wavelength = rsr_table[wavelength_header]
        rsr = rsr_table[rsr_header]
        idx_min = np.argwhere(f0[:, 0] == wavelength.min())
        idx_max = np.argwhere(f0[:, 0] == wavelength.max())
        numerator = f0[idx_min[0, 0]:idx_max[0, 0]+1, -1]*rsr
        denominator = rsr
        GOCI2_F0.append(numerator.sum()/denominator.sum())
    print(GOCI2_F0)
