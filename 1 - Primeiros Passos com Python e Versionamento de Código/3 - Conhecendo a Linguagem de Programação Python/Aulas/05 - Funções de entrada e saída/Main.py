def main():
    nome = input("Digite o seu nome: ")
    idade = int(input("Digite a sua idade: "))
    salario = float(input("Digite o seu salario: "))

    print(f"Olá {nome}! Você tem {idade} e seu salário atual é de: R${salario:.2f}")
    print(f"\nOlá {nome}! Você tem {idade} e seu salário atual é de: R${salario:.2f}", end="...\n")
    print(nome, idade, salario, sep = " - ")

if __name__ == '__main__':
    main()