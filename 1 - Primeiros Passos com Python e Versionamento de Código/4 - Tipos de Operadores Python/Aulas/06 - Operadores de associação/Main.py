def main():
    """
    Função principal que demonstra os Operadores de Associação em Python.
    Estes operadores verificam se um elemento pertence a uma sequência.
    """

    """
    Operador de Associação IN (in)
    Finalidade: Retorna True se um elemento for encontrado dentro de uma sequência.
    """
    print("\n--------- 1. Operador de Associação IN (in) ---------")
    # Exemplo 01:
    # Verificando se um número está em uma lista e se uma letra está em uma palavra.
    numeros_sorteados = [4, 8, 15, 16, 23, 42]
    palavra_chave = "Python"
    
    print(f"Exemplo estático: O número 15 está na lista de sorteados? {15 in numeros_sorteados}")
    print(f"Exemplo estático: O número 7 está na lista de sorteados? {7 in numeros_sorteados}")
    print(f"Exemplo estático: A letra 'P' está na palavra '{palavra_chave}'? {'P' in palavra_chave}")

    # Exemplo 02:
    # Verificando se a fruta escolhida pelo usuário está na lista de disponíveis.
    frutas_disponiveis = ["maçã", "banana", "laranja", "uva"]
    fruta_escolhida = input("Digite o nome de uma fruta para verificar a disponibilidade: ").lower()
    
    esta_disponivel = fruta_escolhida in frutas_disponiveis
    print(f"Exemplo interativo: A fruta '{fruta_escolhida}' está disponível? {esta_disponivel}")

    # Exemplo 03:
    # Validando um comando digitado pelo usuário.
    comandos_validos = ["listar", "adicionar", "remover", "sair"]
    comando_digitado = input("Digite um comando (listar, adicionar, remover, sair): ").lower()

    if comando_digitado in comandos_validos:
        print(f"Comando '{comando_digitado}' reconhecido. Executando ação...")
    elif comando_digitado == "":
        print("Valor inválido! O comando não pode ser vazio.")
    else:
        print(f"Comando '{comando_digitado}' não reconhecido. Tente novamente.")
    
    # Exemplo 04:
    # Percorrendo uma lista de convidados e verificando quem está na lista VIP.
    lista_de_convidados = ["marcos", "ana", "daniel", "carla"]
    lista_vip = ["ana", "carla"]
    print("\nVerificando status dos convidados na festa:")

    for convidado in lista_de_convidados:
        if convidado in lista_vip:
            print(f"  -> {convidado.title()} está na lista VIP! Acesso liberado.")
        else:
            print(f"  -> {convidado.title()} é um convidado comum.")



    """
    Operador de Associação NOT IN (not in)
    Finalidade: Retorna True se um elemento NÃO for encontrado dentro de uma sequência.
    """
    print("\n--------- 2. Operador de Associação NOT IN (not in) ---------")
    # Exemplo 01:
    # Verificando se um usuário não está na lista de banidos.
    usuarios_banidos = ["hacker01", "spammer_x", "bot_malicioso"]
    usuario_a_verificar = "paulo_ricardo"
    
    nao_esta_banido = usuario_a_verificar not in usuarios_banidos
    print(f"Exemplo estático: O usuário '{usuario_a_verificar}' não está na lista de banidos? {nao_esta_banido}")

    # Exemplo 02:
    # Jogo simples onde o jogador não pode escolher uma classe proibida.
    classes_proibidas = ["necromante", "assassino"]
    classe_escolhida = input("Escolha sua classe de personagem (ex: guerreiro, mago): ").lower()

    pode_jogar = classe_escolhida not in classes_proibidas
    print(f"Exemplo interativo: Sua classe é permitida? {pode_jogar}")

    # Exemplo 03:
    # Sistema de cadastro que verifica se um novo nome de usuário já não está em uso.
    usuarios_existentes = ["admin", "root", "paulo"]
    novo_usuario = input("Digite um novo nome de usuário para cadastro: ").lower()

    if novo_usuario not in usuarios_existentes and novo_usuario != "":
        print(f"Parabéns! O nome de usuário '{novo_usuario}' está disponível e foi cadastrado.")
    elif novo_usuario in usuarios_existentes:
        print("Nome de usuário já existe! Por favor, escolha outro.")
    else: # Captura o caso do input ser vazio
        print("Nome de usuário inválido! Não pode ser vazio.")

    # Exemplo 04:
    # Processando uma lista de dados para remover (filtrar) itens indesejados.
    dados_brutos = [10, 20, "ERRO", 30, "FALHA", 40, None, 50]
    marcadores_invalidos = ["ERRO", "FALHA", None]
    dados_limpos = []
    print("\nIniciando limpeza de dados...")

    for dado in dados_brutos:
        if dado not in marcadores_invalidos:
            dados_limpos.append(dado)
            print(f"  -> Dado '{dado}' é válido e foi adicionado.")
        else:
            print(f"  -> Dado '{dado}' é inválido e foi descartado.")
    
    print(f"Exemplo com for: A lista de dados limpos é: {dados_limpos}")


if __name__ == '__main__':
    main()