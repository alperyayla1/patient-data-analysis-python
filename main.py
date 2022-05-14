import csv
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

class Test:
    def __init__(self,var1,var2):
        self._dosya=None
        self._data1=var1
        self._data2=var2
    def oku(self,fileName):
        self._dosya=fileName
        pass
    def veri_grafik(self):
        if(self._dosya==None):
            print("Dosya okunamadı lütfen dosyayı örnek.csv formatında giriniz.")
            return 0
        else:
            filename = open(self._dosya, 'r')
            file = csv.DictReader(filename)
            X = []
            Y = []
            for col in file:
                X.append(float(col[self._data1]))
                Y.append(float(col[self._data2]))
            Y.sort()
            fig1 = plt.figure()
            fig2 = plt.figure()
            fig3 = plt.figure()
            ax1 = fig1.add_subplot(111)
            ax2 = fig2.add_subplot(111)
            ax3 = fig3.add_subplot(111)
            ax1.set_title(self._data1 + " and "+ self._data2 + " graph")
            ax2.set_title(self._data1 + " and " + self._data2 + " graph")
            ax3.set_title(self._data1 + " and " + self._data2 + " graph")
            ax1.set_xlabel(self._data1)
            ax1.set_ylabel(self._data2)
            ax2.set_xlabel(self._data1)
            ax2.set_ylabel(self._data2)
            ax3.set_xlabel(self._data1)
            ax3.set_ylabel(self._data2)
            ax1.grid()
            ax2.grid()
            ax3.grid()
            fig1.tight_layout()
            fig2.tight_layout()
            fig3.tight_layout()
            ax1.hist(X, Y)
            ax2.scatter(X,Y,s=10)
            m, b = np.polyfit(X, Y, 1)
            s = pd.Series(X)
            plt.plot(X, ((m * s) + b))
            print(f"Slope is:{m}")
            ax3.scatter(X,Y,s=10)
            fig1.savefig(self._data1+self._data2+"kutu.png")
            plt.show()
        pass

arg = Test("BMI","Insulin")
arg.oku("diabetes.csv")
arg.veri_grafik()


