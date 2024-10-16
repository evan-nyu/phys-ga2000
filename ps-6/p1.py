#steve brunton online SVD lectures
from astropy.io import fits
import matplotlib.pyplot as plt
import numpy as np
import time

hdu_list = fits.open('specgrid.fits')
logwave = hdu_list['LOGWAVE'].data
flux = hdu_list['FLUX'].data[:10]
wavelength = (10**logwave)/10

def N_Integrate(x, y):
    '''Numerically integrate y dx'''
    boxes = np.zeros(len(x))
    for i in range(len(x)-1):
        boxes[i] = (x[i+1]-x[i])*y[i]
    return boxes.sum()

def normalize(x, y):
    '''Normalize integral of y dx'''
    c = N_Integrate(x, y)
    return 1/c*y

# Normalize all fluxes
flux_normd = np.zeros_like(flux)
for i in range(len(flux)):
    flux_normd[i] = normalize(wavelength, flux[i])

# Plot Normalized fluxes
plt.plot(wavelength, flux_normd[0])
plt.plot(wavelength, flux_normd[1])
plt.plot(wavelength, flux_normd[2])
plt.plot(wavelength, flux_normd[3])
plt.xlabel('wavelength(nm)')
plt.ylabel('Normalized Flux')
plt.legend(['0','1','2','3'])
plt.show()

f_mean = np.sum(flux_normd)/(np.size(flux_normd))

flux_normd_meand = flux_normd - f_mean

plt.plot(wavelength, flux_normd_meand[0])
plt.plot(wavelength, flux_normd_meand[1])
plt.plot(wavelength, flux_normd_meand[2])
plt.plot(wavelength, flux_normd_meand[3])
plt.xlabel('wavelength(nm)')
plt.ylabel('Normalized & Meaned Flux')
plt.legend(['0','1','2','3'])
plt.show()

initialT = time.time()

C = np.dot(np.transpose(flux_normd_meand), flux_normd_meand)

eigenvalues, eigenvectors = np.linalg.eig(C)

eigenvectors = np.transpose(eigenvectors)

print("EigenTime", time.time()-initialT)

plt.plot(wavelength, eigenvectors[0])
plt.plot(wavelength, eigenvectors[1])
plt.plot(wavelength, eigenvectors[2])
plt.plot(wavelength, eigenvectors[3])
plt.plot(wavelength, eigenvectors[4])
plt.xlabel('wavelength')
plt.ylabel('eigenvectors')
plt.legend(['0','1','2','3','4'])

plt.show()

initialT = time.time()

(u, w, vt) = np.linalg.svd(flux_normd_meand)

evecs = np.transpose(vt)

print("SVDTime", time.time()-initialT)

plt.plot(wavelength, evecs[0])
plt.plot(wavelength, evecs[1])
plt.plot(wavelength, evecs[2])
plt.plot(wavelength, evecs[3])
plt.plot(wavelength, evecs[4])
plt.xlabel('wavelength')
plt.ylabel('eigenvectors')
plt.legend(['0','1','2','3','4'])
plt.show()

print("R Condition Number", np.max(np.absolute(w)) / np.min(np.absolute(w)))
print("C Condition Number", np.max(np.absolute(eigenvalues)) / np.min(np.absolute(eigenvalues)))

large_evecs = eigenvectors[:5]

cs = np.dot(large_evecs, np.transpose(flux_normd_meand)) 

pcad_data = np.transpose(np.dot(np.transpose(large_evecs), cs))

plt.plot(wavelength, pcad_data[0])
plt.xlabel('wavelength (nm)')
plt.ylabel('Approximate Spectra')
plt.show()

plt.scatter(cs[0], cs[1])
plt.xlabel('c_0')
plt.ylabel('c_1')
plt.show()

plt.scatter(cs[0], cs[2])
plt.xlabel('c_0')
plt.ylabel('c_2')
plt.show()

def squared_residuals(Nc):
    large_evecs = eigenvectors[:Nc]

    cs= np.dot(large_evecs, np.transpose(flux_normd_meand))
    pcad_data = np.transpose(np.dot(np.transpose(large_evecs), cs))

    return (pcad_data - flux_normd_meand)**2

plt.plot(wavelength, squared_residuals(1)[0])
plt.plot(wavelength, squared_residuals(2)[0])
plt.plot(wavelength, squared_residuals(4)[0])
plt.plot(wavelength, squared_residuals(8)[0])
plt.plot(wavelength, squared_residuals(16)[0])
plt.plot(wavelength, squared_residuals(20)[0])
plt.legend(['1','2','4','8','16','20'])
plt.xlabel("wavelength (nm)")
plt.ylabel("Squard residuals")

plt.show()

print("RMS Residual of for Nc = 20", np.sqrt(np.mean(squared_residuals(20))))
