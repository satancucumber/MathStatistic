#Лицеванова Милана 1307
#ТВиМС ИДЗ №4
#Задание 2 (a-c)

import math
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import kurtosis, skew
import statsmodels.distributions.empirical_distribution as ed

d = 3.2
c = 6.4

sample = list(map(float, ('5.67 0.73 2.31 3.42 0.96 1.51 5.37 10.83 2.76 0.96 3.49 10.38 2.47 4.19 10.63 5.62 1.77 1.75 9.26 3.50 0.32 2.09 1.73 1.04 4.62 1.39 5.09 1.10 8.60 2.83 3.91 4.03 4.95 1.68 1.79 1.27 3.15 1.25 1.55 4.64 1.23 22.51 13.88 7.38 0.54 0.87 8.48 0.46 4.55 2.19').split(' ')))
sample.sort()

print("a)")

variationalSeries = sorted(sample)
print("Вариационный ряд: ", variationalSeries)

n = len(sample)
print("Величина выборки:", n)

k = 15   # количество интервалов
h = 1.6  #шаг

intervals = [0, 1.6, 3.2, 4.8, 6.4, 8.0, 9.6, 11.2, 12.8, 14.4, 16.0, 17.6, 19.2, 20.8, 22.4, 24.0]  #интервалы

xi = [0]*k
for i in range(0, k):
    xi[i] = intervals[i] + h/2
ni = [0]*k
wi = [0]*k
j = 0
for i in range(0, k):
    while j < 50 and (intervals[i] <= sample[j] < intervals[i+1]):
        ni[i] += 1
        j += 1
    if ni[i] != 0:
        wi[i] = ni[i]/n

print("Сумма ni: ", sum(ni))   #должна равняться n

xi.pop()
wi.pop()

plt.grid(which='major')
plt.grid(which='minor', linestyle=':')
plt.ylabel('$F_{frequency}$', fontsize=20)
plt.xlabel('$X_i$', fontsize=20)
plt.plot(xi, wi)
plt.scatter(xi, wi)
plt.show()         #Полигон частот


bin_ranges = [0, 1.6, 3.2, 4.8, 6.4, 8.0, 9.6, 11.2, 12.8, 14.4, 16.0, 17.6, 19.2, 20.8, 22.4, 24.0]
plt.hist(variationalSeries, bins = bin_ranges, edgecolor='black', density=True)

plt.show()  #Гистограмма частот


ecdf = ed.ECDF(sample)
plt.minorticks_on()
plt.xlim([-0.01, 22.55])
plt.ylim([-0.01, 1.01])
plt.grid(which='major')
# включаем дополнительную сетку
plt.grid(which='minor', linestyle=':')
plt.step(ecdf.x, ecdf.y, color="blue")
plt.ylabel('$F_n(y)$', fontsize=20)
plt.xlabel('$y$', fontsize=20)

plt.plot([-5, 0.32], [0, 0], color="blue")
plt.plot([22.51, 25], [1, 1], color="blue")

plt.show()    # Эмперическая функция распределения

print("b)")

E = sum(sample) / n
print("Выборочное мат. ожидание:", E)
D = sum((xi - E)*(xi - E) for xi in sample) / n
print("Выборочная дисперсия:", D)
medain = np.median(sample)
print("Медиана: " + str(medain))
print("Ассиметрия: " + str(skew(sample)))
print("Эксцесса: " + str(kurtosis(sample)))
print("Pr(X in [a; b]):",  ecdf(c) , "-", ecdf(d), "=", ecdf(c) - ecdf(d))

print("c)")

print("Метод максимального правдоподобия")

print("Оценка lambda равна 1 деленному на выборочное среднее: ", 1/E)

print("Метод моментов")

print("Оценка lambda равна 1 деленному на выборочное среднее: ", 1/E)

print("d)")

xa = 2.17   # значение x_alpha

def c():
    return xa/(E*math.sqrt(n)) + 1/E

def cmin():
    return -xa/(E*math.sqrt(n)) + 1/E

print("Доверительный интервал: (", cmin(), ", ", c(), ")")