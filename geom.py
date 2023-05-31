#Лицеванова Милана 1307
#ТВиМС ИДЗ №4
#Задание 1 (g.e-g.f)

import statsmodels.distributions.empirical_distribution as ed
from  scipy.stats import poisson
import numpy as np
import matplotlib.pyplot as plt
from scipy. stats import chi2
import math

intervals = [0, 2, 4, 6, 8]  #интервалы по гистограмме
k = len(intervals) - 1
lam = 1.0     # значение lambda_0
sample = list(map(int, ('1 0 3 0 0 0 1 3 1 1 3 1 1 1 3 0 0 0 1 3 0 0 0 0 4 0 0 1 0 0 0 0 1 0 2 5 0 7 0 0 0 0 0 1 1 0 2 3 0 1').split(' ')))
sample.sort()

ecdf = ed.ECDF(sample)

print("g.e)")

n = [41, 7, 1, 1]  # количество элементов выборки в каждом интервале
print("ni: ", n)

# Функция X^2
def Chi2(lam):
    res = 0
    for i in range(len(n)):
        res += (n[i] - sum(n) * p(i, lam))**2 / (sum(n) * p(i, lam))
    return res

# Вероятность
def p(i, lam):
    return lam**i / ((lam + 1)**(i + 1))

N = sum(n)   # должны равнять n элементов выборки
pArray = [p(i, lam) for i in range(len(n))]       # pi
npArray = [N * pArray[i] for i in range(len(n))]   #npi
func = [((n[i] - npArray[i])**2)/(npArray[i]) for i in range(len(n))]


x = np.arange (-5, 5, 0.001)
plt.plot (x, poisson.cdf (x, mu=lam ), label=str(lam))  
plt.show()  # функция распределения Пуассона

print("p_i ", pArray, " sum: ", sum(pArray))
print("n_i ", n, " sum: ", sum(n))
print("np_i ", npArray, " sum: ", sum(npArray))
print("func_i ", func, " sum: ", sum(func))

df = k - 0 - 1
print("df: ", df)   # степени свободы

alpha1 = 0.2    # значение alpha_1

# Подсчёт критического значения
for xi in range(0, 10000):
    e = 0.001
    x = xi/100
    if ( (1 - alpha1) - e <= chi2.cdf(x, df=df) <= (1 - alpha1) + e):
        print("x_alpha: ", end = "")
        print(x, chi2.cdf(x, df=df))

X2 = Chi2(lam)

print("max_alpha", 1 - chi2.cdf(X2, df=df))


print("X^2: ", X2)

print("g.f)")
print("Минимизация")

min_X2 = 99999
true_lam = 0
for lam_newI in range(1, 10000):
    lam_new = lam_newI / 1000
    X2_new = Chi2(lam_new)
    if (X2_new < min_X2):
        min_X2 = X2_new
        true_lam = lam_new

print("min_X2:", min_X2)
print("lam:", true_lam)

lam = true_lam   # найденное значение lambda

N = sum(n)
pArray = [p(i, lam) for i in range(len(n))]
npArray = [N * pArray[i] for i in range(len(n))]
func = [((n[i] - npArray[i])**2)/(npArray[i]) for i in range(len(n))]

print("p_i ", pArray, " sum: ", sum(pArray))
print("n_i ", n, " sum: ", sum(n))
print("np_i ", npArray, " sum: ", sum(npArray))
print("func_i ", func, " sum: ", sum(func))

df = k - 1 - 1
print("df: ", df)

alpha1 = 0.2   # значение alpha_1

for xi in range(0, 10000):
    e = 0.001
    x = xi/100
    if ( (1 - alpha1) - e <= chi2.cdf(x, df=df) <= (1 - alpha1) + e):
        print("x_alpha: ", end = "")
        print(x, chi2.cdf(x, df=df))

X2 = Chi2(lam)

print("max_alpha", 1 - chi2.cdf(X2, df=df))

print("X^2: ", X2)