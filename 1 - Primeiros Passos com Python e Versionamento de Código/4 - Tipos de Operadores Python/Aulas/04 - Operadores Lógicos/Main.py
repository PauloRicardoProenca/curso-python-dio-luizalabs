def main():
    """
    Função principal que demonstra os Operadores Lógicos em Python.
    Estes operadores são usados para combinar expressões booleanas.
    """

    """
    Operador Lógico AND (and)
    Finalidade: Combina duas condições e retorna True apenas se AMBAS forem verdadeiras.
    """
    print("\n--------- 1. Operador Lógico AND (and) ---------")
    # Exemplo 01:
    tem_idade_suficiente = True
    tem_ingresso = True
    pode_entrar = tem_idade_suficiente and tem_ingresso
    print(f"Exemplo estático: Idade OK? {tem_idade_suficiente}. Ingresso OK? {tem_ingresso}. Pode entrar? {pode_entrar}")

    # Exemplo 02:
    idade = int(input("Digite sua idade: "))
    possui_cnh = input("Você possui CNH? (s/n): ").lower()
    pode_dirigir = (idade >= 18) and (possui_cnh == 's')
    print(f"Exemplo interativo: Pode dirigir legalmente? {pode_dirigir}")

    # Exemplo 03:
    # Verificação de login e senha com validação de entrada
    usuario_correto = "paulo"
    senha_correta = "1234"
    usuario_digitado = input("Digite o nome de usuário: ")
    senha_digitada = input("Digite a senha: ")

    # Verifica se os campos não estão vazios antes de checar as credenciais
    if usuario_digitado != "" and senha_digitada != "":
        if usuario_digitado == usuario_correto and senha_digitada == senha_correta:
            print("Login bem-sucedido!")
        else:
            print("Usuário ou senha incorretos.")
    else:
        print("Valor inválido! Usuário e senha não podem estar em branco.")

    # Exemplo 04:
    # Encontrando números em um intervalo que são divisíveis por 2 E por 3
    print("Números de 1 a 30 que são divisíveis por 2 E por 3:")
    for numero in range(1, 31):
        if numero % 2 == 0 and numero % 3 == 0:
            print(f"  -> {numero} é divisível por ambos.")



    """
    Operador Lógico OR (or)
    Finalidade: Combina duas condições e retorna True se PELO MENOS UMA delas for verdadeira.
    """
    print("\n--------- 2. Operador Lógico OR (or) ---------")
    # Exemplo 01:
    e_fim_de_semana = False
    e_feriado = True
    pode_descansar = e_fim_de_semana or e_feriado
    print(f"Exemplo estático: É fim de semana? {e_fim_de_semana}. É feriado? {e_feriado}. Pode descansar? {pode_descansar}")

    # Exemplo 02:
    forma_pagamento = input("Pagamento em dinheiro ou pix? (d/p): ").lower()
    tem_desconto = (forma_pagamento == 'd') or (forma_pagamento == 'p')
    print(f"Exemplo interativo: Cliente tem desconto? {tem_desconto}")

    # Exemplo 03:
    # Acesso a uma área restrita se for VIP OU tiver convite especial
    tipo_membro = input("Qual seu tipo de membro (vip/comum): ").lower()
    tem_convite = input("Você tem um convite especial? (s/n): ").lower()

    if tipo_membro == 'vip' or tem_convite == 's':
        print("Acesso concedido!")
    elif tipo_membro not in ['vip', 'comum'] or tem_convite not in ['s', 'n']:
        # Validação se as entradas foram digitadas corretamente
        print("Valor inválido! Responda com as opções dadas.")
    else:
        print("Acesso negado.")

    # Exemplo 04:
    # Loop que para quando o jogador fica sem vidas OU o tempo acaba
    vidas = 3
    tempo = 10
    print(f"Jogo iniciado com {vidas} vidas e {tempo} segundos.")
    while vidas > 0 and tempo > 0: # O jogo continua enquanto tiver vida E tempo
        print(f"  -> Vidas: {vidas}, Tempo: {tempo}")
        vidas -= 1
        tempo -= 3
    # A condição de derrota é o inverso da condição de continuar:
    if vidas <= 0 or tempo <= 0:
        print("Exemplo com while: Fim de Jogo!")



    """
    Operador Lógico NOT (not)
    Finalidade: Inverte um valor booleano. Transforma True em False e False em True.
    """
    print("\n--------- 3. Operador Lógico NOT (not) ---------")
    # Exemplo 01:
    servidor_online = False
    servidor_indisponivel = not servidor_online
    print(f"Exemplo estático: Servidor online? {servidor_online}. O servidor está indisponível? {servidor_indisponivel}")

    # Exemplo 02:
    # Muito usado para verificar se uma string está vazia
    nome = input("Digite seu nome (não deixe em branco): ")
    if not nome: # not "" é True
        print("Exemplo interativo: Erro! O nome não pode ser vazio.")
    else:
        print(f"Olá, {nome}!")

    # Exemplo 03:
    # Verificando permissão de exclusão, apenas se o usuário NÃO for um 'visitante'
    perfil_usuario = input("Digite seu perfil (admin/editor/visitante): ").lower()
    
    # A condição é que o perfil não pode ser 'visitante'
    if not (perfil_usuario == 'visitante') and perfil_usuario in ['admin', 'editor']:
        print("Permissão para excluir concedida.")
    elif perfil_usuario == 'visitante':
        print("Permissão para excluir negada.")
    else:
        print("Perfil inválido! Por favor, digite um perfil válido.")

    # Exemplo 04:
    # Um loop que continua enquanto uma condição de parada NÃO for atingida
    encontrou_item = False
    tentativas = 0
    print("Procurando o item secreto...")
    while not encontrou_item:
        tentativas += 1
        print(f"  -> Tentativa {tentativas}...")
        if tentativas == 5: # Simula encontrar o item na 5ª tentativa
            encontrou_item = True
            print("Exemplo com while: Item encontrado!")


if __name__ == '__main__':
    main()