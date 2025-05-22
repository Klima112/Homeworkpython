import numpy as np
import matplotlib.pyplot as plt
from scipy.special import spherical_jn, spherical_yn
import xml.etree.ElementTree as ET
import requests

class RCS:
    def __init__(self, D=0.1, f_min=1e9, f_max=10e9):
        self.r = D/2
        self.f = np.linspace(f_min, f_max, 500)
        self.rcs = None
    
    def _hn(self, n, x):
        return spherical_jn(n, x) + 1j*spherical_yn(n, x)
    
    def calculate(self):
        k = 2*np.pi*self.f/3e8
        self.rcs = [(3e8/f)**2/np.pi * abs(sum(
            (-1)**n * (n+0.5) * (
                (k[i]*self.r*spherical_jn(n-1, k[i]*self.r) - n*spherical_jn(n, k[i]*self.r)) / 
                (k[i]*self.r*self._hn(n-1, k[i]*self.r) - n*self._hn(n, k[i]*self.r)) - 
                spherical_jn(n, k[i]*self.r)/self._hn(n, k[i]*self.r)
            ) for n in range(1, 21)
        ))**2 for i, f in enumerate(self.f)]
        return self.rcs
    
    def save_to_txt(self, filename="task4.txt"):
        with open(filename, 'w') as file:
            file.write("Frequency(Hz)\tRCS(m²)\n")
            for freq, rcs in zip(self.f, self.rcs):
                file.write(f"{freq}\t{rcs}\n")
    
    def plot(self):
        plt.figure(figsize=(10, 5))
        plt.plot(self.f/1e9, self.rcs, 'm-')
        plt.xlabel('Frequency (GHz)')
        plt.ylabel('RCS (m²)')
        plt.title('Radar Cross Section')
        plt.grid(True)
        plt.show()

def load_params(url, variant=9):
        response = requests.get(url)
        root = ET.fromstring(response.content)
        var = root.find(f"./variant[@number='{variant}']")
        return float(var.find('D').text), float(var.find('fmin').text), float(var.find('fmax').text)
   

if __name__ == "__main__":
    D, f_min, f_max = load_params("https://jenyay.net/uploads/Student/Modelling/task_rcs_02.xml")
    rcs = RCS(D, f_min, f_max)
    rcs.calculate()
    rcs.save_to_txt()  
    rcs.plot()
    