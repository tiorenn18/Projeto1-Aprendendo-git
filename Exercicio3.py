''' 3) Crie um programa que leia o nome e o salário de um funcionário, mostrando no final uma mensagem.
Ex:
    Nome do Funcionário: Maria do Carmo
    Salário: 1850,45
    O funcionário Maria do Carmo tem um salário de R$1850,45 em Junho. '''

nome = str(input('Qual seu nome? ')) # recebe a informaçao do nome do usuario.
salario = float(input('Valor do seu salario: ')) # recebe a informação do salario do usuario.
print() # dar espacamento 
print(f'O funcionário {nome} teve um salário de R$ {salario:.2f} No mes de Agosto. ') # mostra as informçaoes recebidas 