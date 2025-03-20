#5) As maçãs custam R$ 1,30 cada se forem compradas menos de uma dúzia, e R$ 1,00 se forem compradas pelo menos 12. Escreva um programa que leia o número de maçãs compradas, calcule e escreva o custo total da compra.
print("Informe a quantidade de maçãs compradas")
quantidade1=int(input())
print("O valor da compra foi")
valortotal1=int(quantidade1*1.30)
valortotal2=int(quantidade1*1.00)
if(quantidade1<=11):
    print(valortotal1)
else:
    print(valortotal2)
