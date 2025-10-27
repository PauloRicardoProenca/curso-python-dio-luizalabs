def main():
    """
    Função principal que demonstra as Estruturas Condicionais em Python.
    Estas estruturas controlam o fluxo de execução do programa.
    """

    """
    1. Estrutura Condicional Padrão (if, elif, else)
    Finalidade: Criar múltiplos caminhos de execução, dos quais apenas um será seguido.
    """
    print("\n--------- 1. Estrutura Condicional Padrão (if, elif, else) ---------")
    # Exemplo 01:
    # Classificando uma nota escolar.
    nota = 8.5
    if nota >= 9.0:
        conceito = "A"
    elif nota >= 7.0:
        conceito = "B"
    elif nota >= 5.0:
        conceito = "C"
    else:
        conceito = "D"
    print(f"Exemplo estático: A nota {nota} corresponde ao conceito '{conceito}'.")

    # Exemplo 02:
    # Dando uma sugestão com base no clima.
    clima = input("Como está o clima hoje (sol, chuva, nublado)? ").lower()
    if clima == "sol":
        sugestao = "Que tal ir à praia?"
    elif clima == "chuva":
        sugestao = "Perfeito para um filme e pipoca!"
    elif clima == "nublado":
        sugestao = "Uma caminhada no parque seria agradável."
    else:
        sugestao = "Não reconheci esse clima, mas aproveite seu dia!"
    print(f"Exemplo interativo: {sugestao}")

    # Exemplo 03:
    # Um menu de opções simples com validação de entrada.
    print("\n[ 1 ] Ver Saldo")
    print("[ 2 ] Fazer Depósito")
    print("[ 3 ] Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("Seu saldo é R$ 1.500,00.")
    elif opcao == "2":
        print("Área de depósito.")
    elif opcao == "3":
        print("Saindo do sistema...")
    else:
        print("Opção inválida! Por favor, digite 1, 2 ou 3.")

    # Exemplo 04:
    # O clássico "FizzBuzz": um loop com múltiplas condições.
    print("\nExemplo com for (FizzBuzz de 1 a 15):")
    for numero in range(1, 16):
        # A ordem aqui é crucial: a condição mais específica (divisível por ambos) vem primeiro.
        if numero % 3 == 0 and numero % 5 == 0:
            print(f"  -> {numero}: FizzBuzz")
        elif numero % 3 == 0:
            print(f"  -> {numero}: Fizz")
        elif numero % 5 == 0:
            print(f"  -> {numero}: Buzz")
        else:
            print(f"  -> {numero}")

    """
    2. Estruturas Condicionais Aninhadas (Nested)
    Finalidade: Criar uma verificação dentro de outra, para lógicas mais detalhadas.
    """
    print("\n--------- 2. Estruturas Condicionais Aninhadas ---------")
    # Exemplo 01:
    # Para entrar em uma área restrita, precisa ser maior de idade E ter o passe VIP.
    idade = 25
    passe = "vip"
    if idade >= 18:
        print("Exemplo estático (verificação de idade): OK, maior de idade.")
        if passe == "vip":
            print("Exemplo estático (verificação de passe): OK, passe VIP. Acesso concedido!")
        else:
            print("Exemplo estático (verificação de passe): Acesso negado, passe não é VIP.")
    else:
        print("Exemplo estático (verificação de idade): Acesso negado, menor de idade.")

    # Exemplo 02:
    # Compra de um produto com verificação de estoque.
    produto = "café"
    estoque = {"café": 10, "açúcar": 0}
    
    if produto in estoque:
        print(f"Exemplo interativo: O produto '{produto}' existe.")
        # Condição aninhada: só verifica a quantidade se o produto existir.
        if estoque[produto] > 0:
            print("  -> E temos em estoque! Compra pode ser realizada.")
        else:
            print("  -> Mas está fora de estoque no momento.")
    else:
        print(f"Exemplo interativo: O produto '{produto}' não existe em nosso catálogo.")

    # Exemplo 03:
    # Lógica de um jogo para usar uma habilidade.
    classe_personagem = input("Qual a sua classe (guerreiro, mago)? ").lower()
    if classe_personagem == "mago":
        mana = int(input("Qual sua mana atual? "))
        if mana >= 50:
            print("Você tem mana suficiente e pode lançar a Bola de Fogo!")
        else:
            print("Mana insuficiente para lançar a magia.")
    elif classe_personagem == "guerreiro":
        vigor = int(input("Qual seu vigor atual? "))
        if vigor >= 30:
            print("Você tem vigor suficiente e pode usar o Ataque Giratório!")
        else:
            print("Vigor insuficiente para usar a habilidade.")
    else:
        print("Classe inválida! Escolha entre guerreiro ou mago.")
        
    # Exemplo 04:
    # Processando uma lista de usuários e aplicando regras diferentes.
    usuarios = [
        {"nome": "Ana", "ativo": True, "admin": True},
        {"nome": "Beto", "ativo": True, "admin": False},
        {"nome": "Carlos", "ativo": False, "admin": True},
    ]
    print("\nAnalisando permissões de usuários:")
    for usuario in usuarios:
        print(f"  Verificando {usuario['nome']}:")
        if usuario["ativo"]:
            if usuario["admin"]:
                print("    -> Usuário ATIVO e ADMIN. Acesso total.")
            else:
                print("    -> Usuário ATIVO mas não é admin. Acesso limitado.")
        else:
            print("    -> Usuário INATIVO. Acesso bloqueado.")

    """
    3. Operador Condicional Ternário
    Finalidade: Uma forma concisa de escrever uma instrução if/else simples em uma única linha.
    Sintaxe: valor_se_verdadeiro if condicao else valor_se_falso
    """
    print("\n--------- 3. Operador Condicional Ternário ---------")
    # Exemplo 01:
    # Definindo o status de maioridade de forma concisa.
    idade_ternario = 22
    status = "Maior de idade" if idade_ternario >= 18 else "Menor de idade"
    print(f"Exemplo estático: Com {idade_ternario} anos, o status é '{status}'.")

    # Exemplo 02:
    # Verificando se um número é par ou ímpar.
    numero = int(input("Digite um número inteiro: "))
    resultado = "Par" if numero % 2 == 0 else "Ímpar"
    print(f"Exemplo interativo: O número {numero} é {resultado}.")

    # Exemplo 03:
    # Atribuindo um desconto com base no tipo de cliente.
    tipo_cliente = input("Você é cliente 'vip' ou 'comum'? ").lower()
    
    # A validação de entrada é feita com um if/else normal
    if tipo_cliente in ["vip", "comum"]:
        # O operador ternário é usado apenas para a atribuição simples
        taxa_desconto = 0.15 if tipo_cliente == "vip" else 0.05
        print(f"Sua taxa de desconto é de {taxa_desconto * 100}%.")
    else:
        print("Tipo de cliente inválido!")
        
    # Exemplo 04:
    # Usando o operador ternário dentro de uma list comprehension (um recurso avançado e elegante).
    # Vamos criar uma lista de rótulos para números de 1 a 10.
    rotulos = ["Par" if n % 2 == 0 else "Ímpar" for n in range(1, 11)]
    print(f"\nExemplo com for (list comprehension): Rótulos de 1 a 10: {rotulos}")


if __name__ == '__main__':
    main()