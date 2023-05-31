#Лицеванова Милана 1307
#ТВиМС ИДЗ №4
#Задание 1 (a-c)

import math
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import kurtosis, skew
import statsmodels.distributions.empirical_distribution as ed

a = 0.0
b = 2.41

sample = list(map(int, ('1 0 3 0 0 0 1 3 1 1 3 1 1 1 3 0 0 0 1 3 0 0 0 0 4 0 0 1 0 0 0 0 1 0 2 5 0 7 0 0 0 0 0 1 1 0 2 3 0 1').split(' ')))
sample.sort()

print("a)")

variationalSeries = sorted(sample)
print("Вариационный ряд: ", variationalSeries)          #Вариационный ряд
n = len(sample)

ecdf = ed.ECDF(sample)

plt.minorticks_on()
plt.xlim([-0.10, 8.0])
plt.ylim([-0.01, 1.01])
plt.grid(which='major')
# включаем дополнительную сетку
plt.grid(which='minor', linestyle=':')
plt.step(ecdf.x, ecdf.y, color="blue")
plt.ylabel('$F_n(y)$', fontsize=20)
plt.xlabel('$y$', fontsize=20)

plt.plot([-5, 0], [0, 0], color="blue")
plt.plot([7, 10], [1, 1], color="blue")

plt.show()   # Эмпирическая функция распределения

bin_ranges = [0, 2, 4, 6, 8]     # интервалы по гистограмме

plt.hist(variationalSeries, bins = bin_ranges, edgecolor='black', density=True)

plt.show()  # Гистограмма частот

print("b)")

print("Величина выборки:", n)
E = sum(sample) / n
print("Выборочное мат. ожидание (выборочное среднее):", E)
D = sum((xi - E)*(xi - E) for xi in sample) / n
print("Выборочная дисперсия:", D)
medain = np.median(sample)
print("Медиана: " + str(medain))
print("Ассиметрия: " + str(skew(sample)))
print("Эксцесса: " + str(kurtosis(sample)))
print("Pr(X in [a; b]):", ecdf(b) , "-", ecdf(a), "=", ecdf(b) - ecdf(a))

print("c)")

print("Метод максимального правдоподобия")

print("Оценка lambda равна выборочному среднему: ", E)

print("Метод моментов")

print("Оценка lambda равна выборочному среднему: ", E)

print("d)")

xa = 1.28   # значение x_alpha

def c():
    return (2*E + (xa**2)/n + math.sqrt((4*E + (xa**2)/n) * xa/n))/2

def cmin():
    return (2*E + (xa**2)/n - math.sqrt((4*E + (xa**2)/n) * xa/n))/2

print("Доверительный интервал: (", cmin(), ", ", c(), ")")



