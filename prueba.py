import random

elegir_mon = int(input('1.Pesos 2.Soles: '))
i = 0
if elegir_mon == 1:
    for i in range(0,10):    
        print(f'{random.uniform(99,9999):.2f} pesos')
else:
    for i in range(0,10):    
        print(f'{(random.uniform(99,9999)*0.04193):.2f} soles')
