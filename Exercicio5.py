''' 5) Faça um programa que leia as duas notas de um aluno em uma matéria e mostre na tela a sua média na disciplina. '''

NomeDoAluno = str(input('Nome do aluno: ')) # Recebe a informação do nome do aluno
nota1 = float(input('Primeira nota: ')) # Recebe a primeira nota
nota2 = float(input('Segunda nota: ')) # Recebe a segunda nota
media = ( nota1 + nota2 ) / 2    # Retorna a media do Aluno

print() # Espacamento entre linhas
print(f'O aluno {NomeDoAluno} tem a média de: {media:.2f}') # Mostra o Nome e a media do aluno.

