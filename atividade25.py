# Enunciado: Crie um programa que receba a nota de 5 alunos e exiba quantos foram aprovados (nota maior ou igual a 7).

soma = 0
contador = 0

for n in range(5):
    nota2=float(input("digite a sua nota:"))
    if nota2 >= 7:
        contador += 1
print(f"{contador} alunos foram aprovados")