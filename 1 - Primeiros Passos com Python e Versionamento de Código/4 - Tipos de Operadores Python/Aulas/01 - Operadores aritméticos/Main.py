def main():
    """
    Função principal que demonstra todos os Operadores Aritméticos em Python.
    Cada operação é referente a uma expressão matemática.
    """

    """
    Operador de Adição (+)
    Finalidade: Realiza a soma de dois números.
    """
    print("\n--------- 1. Operador de Adição (+) ---------")
    # Exemplo 01:
    n1_static = 10
    n2_static = 50
    resultado_static = n1_static + n2_static
    print(f"Exemplo estático: {n1_static} + {n2_static} = {resultado_static}")

    # Exemplo 02:
    n1_user = int(input("Digite um número inteiro: "))
    n2_user = int(input("Digite outro número inteiro para somar: "))
    resultado_user = n1_user + n2_user
    print(f"Resultado: {n1_user} + {n2_user} = {resultado_user}")



    """
    Operador de Subtração (-)
    Finalidade: Encontra a diferença entre dois números.
    """
    print("\n--------- 2. Operador de Subtração (-) ---------")
    # Exemplo 01:
    n1_static = 100
    n2_static = 35
    resultado_static = n1_static - n2_static
    print(f"Exemplo estático: {n1_static} - {n2_static} = {resultado_static}")

    # Exemplo 02:
    n1_user = int(input("Digite o primeiro número (minuendo): "))
    n2_user = int(input("Digite o segundo número (subtraendo): "))
    resultado_user = n1_user - n2_user
    print(f"Resultado: {n1_user} - {n2_user} = {resultado_user}")



    """
    Operador de Multiplicação (*)
    Finalidade: Calcula o produto de dois números.
    """
    print("\n--------- 3. Operador de Multiplicação (*) ---------")
    # Exemplo 01:
    n1_static = 7
    n2_static = 8
    resultado_static = n1_static * n2_static
    print(f"Exemplo estático: {n1_static} * {n2_static} = {resultado_static}")

    # Exemplo 02:
    n1_user = int(input("Digite o primeiro fator: "))
    n2_user = int(input("Digite o segundo fator: "))
    resultado_user = n1_user * n2_user
    print(f"Resultado: {n1_user} * {n2_user} = {resultado_user}")



    """
    Operador de Divisão (/)
    Finalidade: Realiza a divisão. Retorna um número de ponto flutuante (float).
    """
    print("\n--------- 4. Operador de Divisão (/) ---------")
    # Exemplo 01:
    n1_static = 10
    n2_static = 3
    resultado_static = n1_static / n2_static
    print(f"Exemplo estático: {n1_static} / {n2_static} = {resultado_static} (Note que é um float!)")

    # Exemplo 02:
    n1_user = float(input("Digite o dividendo: "))
    n2_user = float(input("Digite o divisor: "))
    resultado_user = n1_user / n2_user
    print(f"Resultado: {n1_user} / {n2_user} = {resultado_user}")



    """
    Operador de Divisão de Inteiro (//)
    Finalidade: Realiza a divisão e retorna apenas a parte inteira do resultado.
    """
    print("\n--------- 5. Operador de Divisão de Inteiro (//) ---------")
    # Exemplo 01:
    n1_static = 10
    n2_static = 3
    resultado_static = n1_static // n2_static
    print(f"Exemplo estático: {n1_static} // {n2_static} = {resultado_static} (A parte '0.333' foi descartada)")

    # Exemplo 02:
    n1_user = int(input("Digite o dividendo: "))
    n2_user = int(input("Digite o divisor: "))
    resultado_user = n1_user // n2_user
    print(f"Resultado: {n1_user} // {n2_user} = {resultado_user}")



    """ 
    Operador de Módulo ou Resto (%)
    Finalidade: Retorna o resto de uma divisão. Muito útil para verificar se um número é par ou ímpar.
    """
    print("\n--------- 6. Operador de Módulo (%) ---------")
    # Exemplo 01: 10 dividido por 3 é 3, com resto 1.
    n1_static = 10
    n2_static = 3
    resultado_static = n1_static % n2_static
    print(f"Exemplo estático: O resto de {n1_static} / {n2_static} é {resultado_static}")

    # Exemplo 02:
    print("\nExemplo interativo de Módulo:")
    n1_user = int(input("Digite o dividendo: "))
    n2_user = int(input("Digite o divisor: "))
    resultado_user = n1_user % n2_user
    print(f"Resultado: O resto de {n1_user} / {n2_user} é {resultado_user}")



    """
    Operador de Exponenciação (**)
    Finalidade: Eleva um número a uma potência, igual ao 2^2.
    """
    print("\n--------- 7. Operador de Exponenciação (**) ---------")
    # Exemplo 01: 5 ao cubo (5 * 5 * 5)
    n1_static = 5
    n2_static = 3
    resultado_static = n1_static ** n2_static
    print(f"Exemplo estático: {n1_static} elevado a {n2_static} é {resultado_static}")

    # Exemplo 02:
    base = int(input("Digite o número base: "))
    expoente = int(input("Digite o expoente: "))
    resultado_user = base ** expoente
    print(f"Resultado: {base} ** {expoente} = {resultado_user}")

if __name__ == '__main__':
    main()