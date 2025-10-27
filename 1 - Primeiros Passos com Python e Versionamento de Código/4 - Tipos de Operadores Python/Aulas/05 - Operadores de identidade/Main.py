def main():
    """
    Função principal que demonstra os Operadores de Identidade em Python.
    Estes operadores comparam a identidade dos objetos (seu local na memória).
    """

    """
    Operador de Identidade IS (is)
    Finalidade: Verifica se duas variáveis apontam para o mesmo objeto na memória.
    """
    print("\n--------- 1. Operador de Identidade IS (is) ---------")
    # Exemplo 01:
    # Duas listas com o mesmo VALOR, mas são OBJETOS diferentes na memória.
    lista_a = [1, 2, 3]
    lista_b = [1, 2, 3]
    lista_c = lista_a # lista_c agora aponta para o MESMO objeto que lista_a
    
    print(f"Exemplo estático: lista_a == lista_b (compara VALOR): {lista_a == lista_b}")
    print(f"Exemplo estático: lista_a is lista_b (compara OBJETO): {lista_a is lista_b}")
    print(f"Exemplo estático: lista_a is lista_c (compara OBJETO): {lista_a is lista_c}")

    # Exemplo 02:
    # O uso mais comum de 'is' é para verificar se uma variável é 'None'.
    variavel_vazia = None
    nome = input("Digite algo ou deixe em branco: ")
    if nome == "":
        resultado = None
    else:
        resultado = nome
    
    print(f"Exemplo interativo: A variável 'resultado' é o objeto None? {resultado is variavel_vazia}")

    # Exemplo 03:
    # Simulando um "objeto nulo" ou um estado especial.
    CONFIGURACAO_PADRAO = {"tema": "escuro"}
    config_usuario = None # O usuário ainda não definiu sua configuração

    print(f"Configuração atual: {'Padrão' if config_usuario is None else 'Personalizada'}")
    escolha = input("Deseja usar a configuração padrão? (s/n): ").lower()

    if escolha == 's':
        config_final = CONFIGURACAO_PADRAO
        if config_final is CONFIGURACAO_PADRAO:
            print("Aplicando a configuração padrão do sistema.")
    elif escolha == 'n':
        config_final = {"tema": "claro"} # Um novo objeto, diferente do padrão
        if config_final is not CONFIGURACAO_PADRAO:
            print("Aplicando uma nova configuração personalizada.")
    else:
        print("Opção inválida!")
    
    # Exemplo 04:
    # Percorrendo uma lista e identificando um objeto específico.
    objeto_especial = ["item_secreto"]
    lista_de_itens = [1, "texto", objeto_especial, 3.14]
    print(f"\nProcurando pelo objeto especial na lista...")

    for item in lista_de_itens:
        print(f"  -> Verificando o item: {item}")
        if item is objeto_especial:
            print("    ACHEI! Este é o exato objeto que estávamos procurando.")
            break # Para o loop



    """
    Operador de Identidade IS NOT (is not)
    Finalidade: Verifica se duas variáveis apontam para objetos diferentes na memória.
    """
    print("\n--------- 2. Operador de Identidade IS NOT (is not) ---------")
    # Exemplo 01:
    # Usando o mesmo setup do exemplo anterior.
    lista_d = [4, 5, 6]
    lista_e = [4, 5, 6]
    lista_f = lista_d

    print(f"Exemplo estático: lista_d is not lista_e (objetos diferentes): {lista_d is not lista_e}")
    print(f"Exemplo estático: lista_d is not lista_f (mesmo objeto): {lista_d is not lista_f}")
    
    # Exemplo 02:
    # O uso mais comum de 'is not' é para garantir que uma variável TEM um valor.
    valor_recebido = None
    entrada_usuario = input("Digite um valor para o produto (ou deixe em branco): ")
    if entrada_usuario != "":
        valor_recebido = float(entrada_usuario)

    tem_valor_valido = valor_recebido is not None
    print(f"Exemplo interativo: A variável 'valor_recebido' contém um valor válido? {tem_valor_valido}")

    # Exemplo 03:
    # Simulando a busca de um usuário em um "banco de dados" (dicionário).
    db_usuarios = {"paulo": {"nome": "Paulo Ricardo", "nivel": "admin"}}
    
    def buscar_usuario(nome):
        # A função .get() retorna o valor da chave, ou None se a chave não existir.
        return db_usuarios.get(nome, None)

    nome_busca = input("Digite o nome de usuário para buscar: ").lower()
    usuario_encontrado = buscar_usuario(nome_busca)

    if usuario_encontrado is not None:
        print(f"Bem-vindo, {usuario_encontrado['nome']}! Seu nível de acesso é {usuario_encontrado['nivel']}.")
    elif nome_busca == "":
        print("Valor inválido! O nome de usuário não pode estar em branco.")
    else:
        print("Usuário não encontrado em nosso sistema.")

    # Exemplo 04:
    # Filtrando uma lista para remover valores 'None' e criar uma lista limpa.
    dados_brutos = ["Sensor A: 22.5", None, "Sensor B: 21.9", "Erro de leitura", None]
    dados_validos = []
    print("\nProcessando dados brutos...")

    for dado in dados_brutos:
        if dado is not None:
            dados_validos.append(dado)
            print(f"  -> Dado '{dado}' é válido e foi adicionado.")
        else:
            print("  -> Dado 'None' encontrado e descartado.")
    
    print(f"Exemplo com for: Lista de dados válidos: {dados_validos}")


if __name__ == '__main__':
    main()