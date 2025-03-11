# 7. Considere dois países: A com 80.000 habitantes e taxa de crescimento anual de 3%, e B
#com 200.000 habitantes e taxa de 1,5%. Determine quantos anos serão necessários para que a população do país A ultrapasse a população do país B.
pais1 = 80000
pais2 = 200000 
crescimento1 = 0.03
crescimento2 = 0.015
anos = 0
while pais1 <= pais2:
    pais1 +=pais1 * crescimento1  
    pais2 += pais2 * crescimento2
    anos+=1

print("ultrapassará em", anos, "anos")