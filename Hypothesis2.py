#Лицеванова Милана 1307
#ТВиМС ИДЗ №4
#Задание 2 (e-f)

import math
import statsmodels.distributions.empirical_distribution as ed
from scipy. stats import chi2

sample = list(map(float, ('5.67 0.73 2.31 3.42 0.96 1.51 5.37 10.83 2.76 0.96 3.49 10.38 2.47 4.19 10.63 5.62 1.77 1.75 9.26 3.50 0.32 2.09 1.73 1.04 4.62 1.39 5.09 1.10 8.60 2.83 3.91 4.03 4.95 1.68 1.79 1.27 3.15 1.25 1.55 4.64 1.23 22.51 13.88 7.38 0.54 0.87 8.48 0.46 4.55 2.19').split(' ')))

sample.sort()

print("e)")

intervals = [0, 1.6, 3.2, 4.8, 6.4, 24.0]
k = 5
ni = [0]*k
j = 0
for i in range(0, k):
    while j < 50 and (intervals[i] <= sample[j] < intervals[i+1]):
        ni[i] += 1
        j += 1
print(ni)
k = len(intervals) - 1
lam = 0.14

ecdf = ed.ECDF(sample)

def ni():
    n = 50
    ni = [0]*k
    wi = [0]*k
    j = 0
    for i in range(0, k):
        while j < 50 and (intervals[i] <= sample[j] < intervals[i+1]):
            ni[i] += 1
            j += 1
        if ni[i] != 0:
            wi[i] = ni[i]/n
    wi.pop()
    return ni
n = ni()
print("ni: ", n)

# Функция X^2
def Chi2(lam):
    res = 0
    for i in range(len(n)):
        res += (n[i] - sum(n) * p(i, lam))**2 / (sum(n) * p(i, lam))
    return res

# Вероятность
def p(i, lam):
    r = intervals[i + 1]
    l = intervals[i]
    if l <= 0:
        return 1 - lam * math.exp(-lam * r)
    return - lam * math.exp(-lam*r) + lam * math.exp(-lam*l)

N = sum(n)
pArray = [p(i, lam) for i in range(len(n))]
npArray = [N * pArray[i] for i in range(len(n))]
func = [((n[i] - npArray[i])**2)/(npArray[i]) for i in range(len(n))]

print("p_i ", pArray, " sum: ", sum(pArray))
print("n_i ", n, " sum: ", sum(n))
print("np_i ", npArray, " sum: ", sum(npArray))
print("func_i ", func, " sum: ", sum(func))

df = k - 0 - 1
print("df: ", df)

alpha2 = 0.01   # значение alpha_2

for xi in range(0, 10000):
    e = 0.0001
    x = xi/100
    if ( (1 - alpha2) - e <= chi2.cdf(x, df=df) <= (1 - alpha2) + e):
        print("x_alpha: ", end = "")
        print(x, chi2.cdf(x, df=df))

X2 = Chi2(lam)
print("max_alpha", 1 - chi2.cdf(X2, df=df))
print("X^2: ", X2)

print("f)")
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

lam = true_lam

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

alpha2 = 0.01   # значение alpha_2


for xi in range(0, 10000):
    e = 0.0001
    x = xi/100
    if ( (1 - alpha2) - e <= chi2.cdf(x, df=df) <= (1 - alpha2) + e):
        print("x_alpha: ", end = "")
        print(x, chi2.cdf(x, df=df))

X2 = Chi2(lam)
print("max_alpha", 1 - chi2.cdf(X2, df=df))
print("X^2: ", X2)