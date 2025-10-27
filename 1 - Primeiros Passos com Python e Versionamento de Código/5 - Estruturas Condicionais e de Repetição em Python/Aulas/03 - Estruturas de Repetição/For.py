def main():
    """
    Função principal que demonstra as Estruturas de Repetição FOR em Python.
    Estas estruturas repetem a execução do código de acordo com o "limite" estabelecido.
    """

    # `*---------**---------*EXEMPLOS*---------**---------*´
    # Exemplo 01: Imprimindo na tela uma lista de pessoas (convidados)
    print("\n*---------*LISTA DE CONVIDADOS*---------*")
    convidados = [
        "Paulo",
        "Raissa",
        "Cauã",
        "Alice",
        "Fabrício",
        "Lorena",
        "Giovana",
        "Miguel",
        "Davi",
        "Marina"
    ]
    for nome in convidados:
        print(f"{nome}")
    
    # Exemplo 02: Contando até N
    print("\n*---------*CONTANTO ATÉ N*---------*")
    numero = int(input("Digite até quanto deseja contar: "))
    for numero in range(numero):
        print(f"O número atualmente é: {numero + 1}")
    
    # Exemplo 03: Soletrando uma palavra
    palavra = "Jabuticaba"
    print("\n*---------*SOLETRANDO UMA PALAVRA*---------*")
    print(f"Soletrando a palavra: {palavra}")
    for letra in palavra:
        print(letra)
    
    # Exemplo 04: Tabuada
    print("\n*---------*TABUADA*---------*")
    numero_tabuada = int(input("Qual número da tabuada deseja ver? "))
    for i in range(1, 11):
        resultado = numero_tabuada * i
        print(f"{numero_tabuada} X {i} = {resultado}")
    
    # Exemplo 05: Par ou Ímpar
    print(f"\n*---------*NÚMEROS PARES E ÍMPARES ENTRE N*---------*")
    numero = int(input("Digite um número: "))
    print(f"Calculando os números PARES e ÍMPARES que tem de 0 a {numero}")
    for numero in range(numero):
        if numero % 2 == 0:
            print(f"{numero} é par!")
        else:
            print(f"{numero} é ímpar!")



    # `*---------**---------*EXERCÍCIOS*---------**---------*´
    # Exercício 01: Calcule a a soma de todos os números que estiver entre 0 a N, n = número que o usuário digitar
    numero = int(input("\nDigite um número para calcular a soma de tudo entre 0 e o número que digitar: "))
    for numero in range(numero):
        resultado += numero
    print(f"A soma de tudo do número {numero} é: {resultado}")

    # Exercício 02: Imprima as vogais de uma palavra que o usuário digitar
    palavra = input("Digite uma palavra: ")
    vogais = "AEIOU"
    print(f"Vogais da palavra {palavra}:")
    for letra in palavra:
        if letra.upper() in vogais:
            print(letra)
    
    # Exercício 03: Gerando todos os números ímpares de 1 a 50
    numeros_impares = 50
    print("\nImprimindo os números ímpares entre 1 a 50")
    for numeros_impares in range(1, 51):
        if numeros_impares % 2 > 0:
            print(numeros_impares)



if __name__ == '__main__':
    main()