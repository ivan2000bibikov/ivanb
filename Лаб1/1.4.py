Okl = float(input())
Prem = float(input())
Prem = Okl * Prem
ProfVznos = Okl * 0.01
PensNalog = Okl * 0.06
MROT = 12130
PodNalog = (Okl * MROT * PensNalog) * 0.13
SumRes = Okl - PensNalog + Prem
print(SumRes)
input()

