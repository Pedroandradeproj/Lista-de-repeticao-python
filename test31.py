# O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora 
# possui uma loja de conveniências. Faça um programa que implemente uma caixa registradora 
# rudimentar. O programa deverá receber um número desconhecido de valores referentes aos
# preços das mercadorias. Um valor zero deve ser informado pelo operador para indicar o 
# final da compra. O programa deve então mostrar o total da compra e perguntar o valor 
# em dinheiro que o cliente forneceu, para então calcular e mostrar o valor do troco.
# Após esta operação, o programa deverá voltar ao ponto inicial, para registrar a próxima compra
# . A saída deve ser conforme o exemplo abaixo:

print("Lojas Tabajara ")
lista=1
nprod=1
vtotal=0
while lista>0:
    produto=float(input(f"Produto {nprod}: R$ "))
    vtotal+=produto
    nprod+=1
    if produto==0:
        print(f"Total: R$ {vtotal}")
        dinheiro=float(input("Dinheiro: R$ "))
        troco=dinheiro-vtotal
        print(f"Troco: R$ {troco}")
        lista-=1
    