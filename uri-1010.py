linha1 = input()
linha2 = input()

l1 = linha1.split()
l2 = linha2.split()

for i in range(len(l1)):
    l1[i],l2[i] = float(l1[i]),float(l2[i])

cod1,cod2 = l1[0],l2[0]
number1,number2 = l1[1],l2[1]
val1,val2 = l1[2],l2[2]

valor = val1*number1+val2*number2

print(f"VALOR A PAGAR: R$ {valor:.2f}")
