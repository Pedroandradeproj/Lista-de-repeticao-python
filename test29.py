# O Sr. Manoel Joaquim possui uma grande loja de artigos de R$ 1,99, com cerca de 10 caixas.
# Para agilizar o cálculo de quanto cada cliente deve pagar ele desenvolveu um tabela que 
# contém o número de itens que o cliente comprou e ao lado o valor da conta. Desta forma 
# a atendente do caixa precisa apenas contar quantos itens o cliente está levando e olhar
# na tabela de preços. Você foi contratado para desenvolver o programa que monta esta tabela de preços
# , que conterá os preços de 1 até 50 produtos, conforme o exemplo abaixo


lista=50
valor=0
n=0
print("Lojas Quase Dois - Tabela de preços")
for i in range(lista):
    valor+=1.99
    n+=1
    print(f"{n} - R$ {valor:.2f}")