def main():
    """
    Função principal que demonstra todos os Operadores de Comparação em Python.
    Cada operador resulta em um valor booleano: True ou False.
    """

    """
    Operador de Igualdade (==)
    Finalidade: Verifica se dois valores são iguais.
    Atenção: Não confunda com o sinal de atribuição '=', que serve para dar valor a uma variável.
    """
    print("\n--------- 1. Operador de Igualdade (==) ---------")
    # Exemplo 01:
    n1_static = 20
    n2_static = 20
    resultado_static = (n1_static == n2_static) # Comparando dois números iguais
    print(f"Exemplo estático: A afirmação '{n1_static} é igual a {n2_static}' é: {resultado_static}")

    # Exemplo 02:
    palavra_secreta = "Python"
    palavra_usuario = input("Tente adivinhar a palavra secreta: ")
    resultado_user = (palavra_secreta == palavra_usuario)
    print(f"Resultado: Você acertou a palavra secreta? {resultado_user}")



    """
    Operador de Diferença (!=)
    Finalidade: Verifica se dois valores são diferentes.
    """
    print("\n--------- 2. Operador de Diferença (!=) ---------")
    # Exemplo 01:
    n1_static = 15
    n2_static = 10
    resultado_static = (n1_static != n2_static) # Comparando dois números diferentes
    print(f"Exemplo estático: A afirmação '{n1_static} é diferente de {n2_static}' é: {resultado_static}")

    # Exemplo 02:
    numero_sorteado = 7
    numero_chute = int(input("Chute um número de 1 a 10 (tente não chutar 7): "))
    resultado_user = (numero_sorteado != numero_chute)
    print(f"Resultado: Você chutou um número diferente do sorteado? {resultado_user}")



    """
    Operador Maior que (>)
    Finalidade: Verifica se o valor da esquerda é estritamente maior que o da direita.
    """
    print("\n--------- 3. Operador Maior que (>) ---------")
    # Exemplo 01:
    n1_static = 50
    n2_static = 25
    resultado_static = (n1_static > n2_static)
    print(f"Exemplo estático: A afirmação '{n1_static} é maior que {n2_static}' é: {resultado_static}")

    # Exemplo 02:
    maioridade_penal = 18
    idade_usuario = int(input("Digite sua idade para verificação: "))
    resultado_user = (idade_usuario > maioridade_penal)
    print(f"Resultado: Sua idade é maior que {maioridade_penal} anos? {resultado_user}")



    """
    Operador Menor que (<)
    Finalidade: Verifica se o valor da esquerda é estritamente menor que o da direita.
    """
    print("\n--------- 4. Operador Menor que (<) ---------")
    # Exemplo 01:
    n1_static = 10
    n2_static = 20
    resultado_static = (n1_static < n2_static)
    print(f"Exemplo estático: A afirmação '{n1_static} é menor que {n2_static}' é: {resultado_static}")

    # Exemplo 02:
    temperatura_congelamento = 0
    temperatura_atual = float(input("Digite a temperatura atual em Celsius: "))
    resultado_user = (temperatura_atual < temperatura_congelamento)
    print(f"Resultado: A temperatura está abaixo de zero? {resultado_user}")



    """
    Operador Maior ou Igual a (>=)
    Finalidade: Verifica se o valor da esquerda é maior ou igual ao da direita.
    """
    print("\n--------- 5. Operador Maior ou Igual a (>=) ---------")
    # Exemplo 01:
    n1_static = 7
    n2_static = 7
    resultado_static = (n1_static >= n2_static)
    print(f"Exemplo estático: A afirmação '{n1_static} é maior ou igual a {n2_static}' é: {resultado_static}")

    # Exemplo 02:
    nota_minima_aprovacao = 7.0
    nota_aluno = float(input("Digite a nota do aluno: "))
    resultado_user = (nota_aluno >= nota_minima_aprovacao)
    print(f"Resultado: O aluno foi aprovado? {resultado_user}")



    """
    Operador Menor ou Igual a (<=)
    Finalidade: Verifica se o valor da esquerda é menor ou igual ao da direita.
    """
    print("\n--------- 6. Operador Menor ou Igual a (<=) ---------")
    # Exemplo 01:
    n1_static = 4
    n2_static = 10
    resultado_static = (n1_static <= n2_static)
    print(f"Exemplo estático: A afirmação '{n1_static} é menor ou igual a {n2_static}' é: {resultado_static}")

    # Exemplo 02:
    limite_peso_bagagem = 23
    peso_bagagem = float(input("Digite o peso da sua bagagem em kg: "))
    resultado_user = (peso_bagagem <= limite_peso_bagagem)
    print(f"Resultado: A bagagem está dentro do limite de peso? {resultado_user}")


if __name__ == '__main__':
    main()