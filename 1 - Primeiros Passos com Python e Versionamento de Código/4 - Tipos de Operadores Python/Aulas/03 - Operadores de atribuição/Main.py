def main():
    """
    Função principal que demonstra os Operadores de Atribuição em Python.
    Estes operadores são usados para modificar o valor de uma variável.
    """

    """
    Operador de Atribuição Simples (=)
    Finalidade: Associa um valor a uma variável. É a base de todas as outras atribuições.
    """
    print("\n--------- 1. Operador de Atribuição Simples (=) ---------")
    # Exemplo 01:
    saldo_bancario = 1500.00
    print(f"Exemplo estático: O saldo inicial é de R$ {saldo_bancario}")

    # Exemplo 02:
    nome_usuario = input("Digite seu nome de usuário: ")
    print(f"Exemplo interativo: O nome '{nome_usuario}' foi atribuído à variável.")

    # Exemplo 03:
    # A variável 'status' recebe um valor com base na validação da idade.
    idade = int(input("Digite sua idade para definir o status: "))
    status = "" # Inicializa a variável
    if idade >= 18:
        status = "Maior de idade"
        print(f"Exemplo com if/else: Seu status é '{status}'")
    elif idade >= 0 and idade < 18:
        status = "Menor de idade"
        print(f"Exemplo com if/else: Seu status é '{status}'")
    else:
        # O else captura qualquer valor que não se encaixe nas condições válidas (ex: números negativos).
        print("Valor inválido! Por favor, digite uma idade válida.")

    # Exemplo 04:
    # A variável 'ultimo_numero' é re-atribuída a cada iteração do loop.
    ultimo_numero = 0
    for i in range(1, 6): # Loop de 1 a 5
        ultimo_numero = i
        print(f"  -> No loop, ultimo_numero agora é {ultimo_numero}")
    print(f"Exemplo com for: Após o loop, o valor final de ultimo_numero é {ultimo_numero}")



    """
    Operador de Atribuição com Adição (+=)
    Finalidade: Adiciona um valor à variável e atualiza a própria variável com o resultado.
    """
    print("\n--------- 2. Operador de Atribuição com Adição (+=) ---------")
    # Exemplo 01:
    pontos = 100
    print(f"Exemplo estático: Pontos iniciais = {pontos}")
    pontos += 50 # Equivalente a: pontos = pontos + 50
    print(f"  -> Pontos após adicionar 50: {pontos}")

    # Exemplo 02:
    saldo = float(input("Digite seu saldo atual: R$ "))
    deposito = float(input("Digite o valor a ser depositado: R$ "))
    if deposito > 0:
        saldo += deposito
        print(f"Exemplo interativo: Seu novo saldo é R$ {saldo:.2f}")
    else:
        print("Valor de depósito inválido! Apenas valores positivos são aceitos.")

    # Exemplo 03:
    score = 1000
    print(f"Seu score inicial é {score}.")
    resposta = input("Você completou a missão bônus? (s/n): ").lower() # .lower() torna a resposta minúscula
    if resposta == 's':
        score += 500
        print("Parabéns! Você ganhou 500 pontos bônus!")
    elif resposta == 'n':
        print("Missão bônus não completada.")
    else:
        print("Resposta inválida! Por favor, digite 's' para sim ou 'n' para não.")
    print(f"Exemplo com if/else: Seu score final é {score}")

    # Exemplo 04:
    # Usando += como um 'acumulador' para somar números.
    soma_total = 0
    for numero in range(1, 6): # Soma os números de 1 a 5
        soma_total += numero
        print(f"  -> somando {numero}, total agora é {soma_total}")
    print(f"Exemplo com for: A soma dos números de 1 a 5 é {soma_total}")



    """
    Operador de Atribuição com Subtração (-=)
    Finalidade: Subtrai um valor da variável e a atualiza com o resultado.
    """
    print("\n--------- 3. Operador de Atribuição com Subtração (-=) ---------")
    # Exemplo 01:
    nivel_energia = 100
    print(f"Exemplo estático: Energia inicial = {nivel_energia}%")
    nivel_energia -= 20 # Equivalente a: nivel_energia = nivel_energia - 20
    print(f"  -> Energia após usar habilidade: {nivel_energia}%")

    # Exemplo 02:
    limite_cartao = float(input("Digite o limite do seu cartão: R$ "))
    compra = float(input("Digite o valor da compra: R$ "))
    if compra > 0 and compra <= limite_cartao:
        limite_cartao -= compra
        print(f"Exemplo interativo: Seu limite restante é R$ {limite_cartao:.2f}")
    elif compra > limite_cartao:
        print("Compra negada! O valor excede seu limite.")
    else:
        print("Valor de compra inválido! Deve ser um número positivo.")

    # Exemplo 03:
    estoque = 50
    print(f"Temos {estoque} unidades no estoque.")
    qtd_retirada = int(input("Quantas unidades deseja retirar? "))
    if qtd_retirada > 0 and qtd_retirada <= estoque:
        estoque -= qtd_retirada
        print(f"Retirada bem-sucedida!")
    elif qtd_retirada > estoque:
        print("Valor inválido! A quantidade de retirada excede o estoque.")
    else:
        print("Valor inválido! A quantidade deve ser um número positivo.")
    print(f"Exemplo com if/else: Estoque atual: {estoque} unidades.")

    # Exemplo 04:
    # Usando -= para fazer uma contagem regressiva.
    contador = 10
    print("Iniciando contagem regressiva...")
    while contador > 0:
        print(f"  -> {contador}...")
        contador -= 1
    print(f"Exemplo com while: Fogo!")



    """
    Operador de Atribuição com Multiplicação (*=)
    Finalidade: Multiplica a variável por um valor e a atualiza.
    """
    print("\n--------- 4. Operador de Atribuição com Multiplicação (*=) ---------")
    # Exemplo 01:
    valor_investido = 1000
    print(f"Exemplo estático: Valor investido inicial = R$ {valor_investido}")
    valor_investido *= 1.1 # Equivalente a: valor_investido = valor_investido * 1.1 (rendimento de 10%)
    print(f"  -> Valor após rendimento: R$ {valor_investido:.2f}")

    # Exemplo 02:
    salario_base = float(input("Digite seu salário base: R$ "))
    multiplicador_bonus = float(input("Digite o multiplicador de bônus (ex: 1.5 para 50% de bônus): "))
    if multiplicador_bonus >= 1.0:
        salario_base *= multiplicador_bonus
        print(f"Exemplo interativo: Seu salário com bônus é R$ {salario_base:.2f}")
    else:
        print("Multiplicador inválido! Deve ser 1.0 ou maior.")

    # Exemplo 03:
    dano = 50
    print(f"Dano base do ataque: {dano}")
    acerto_critico = input("Foi um acerto crítico? (s/n): ").lower()
    if acerto_critico == 's':
        dano *= 2 # Dano em dobro
        print("Dano dobrado!")
    elif acerto_critico == 'n':
        print("Dano normal.")
    else:
        print("Resposta inválida! O dano normal será aplicado.")
    print(f"Exemplo com if/else: Dano final causado: {dano}")

    # Exemplo 04:
    # Calculando o fatorial de um número.
    fatorial = 1
    numero_fatorial = 5
    for i in range(1, numero_fatorial + 1):
        fatorial *= i
        print(f"  -> Multiplicando por {i}, fatorial agora é {fatorial}")
    print(f"Exemplo com for: O fatorial de {numero_fatorial} é {fatorial}")



    """
    Operador de Atribuição com Divisão (/=)
    Finalidade: Divide a variável por um valor e a atualiza. O resultado é sempre um float.
    """
    print("\n--------- 5. Operador de Atribuição com Divisão (/=) ---------")
    # Exemplo 01:
    distancia_restante = 100.0
    print(f"Exemplo estático: Distância inicial = {distancia_restante} km")
    distancia_restante /= 2 # Equivalente a: distancia_restante = distancia_restante / 2
    print(f"  -> Metade da distância percorrida. Restam: {distancia_restante} km")

    # Exemplo 02:
    conta_total = float(input("Digite o valor total da conta: R$ "))
    num_pessoas = int(input("Dividir entre quantas pessoas? "))
    if num_pessoas > 1:
        conta_total /= num_pessoas
        print(f"Exemplo interativo: Cada pessoa deve pagar R$ {conta_total:.2f}")
    elif num_pessoas == 1:
        print(f"A conta não precisa ser dividida. O total é R$ {conta_total:.2f}")
    else:
        print("Número de pessoas inválido! Deve ser 1 ou mais.")

    # Exemplo 03:
    preco_produto = 200.0
    print(f"Preço original do produto: R$ {preco_produto:.2f}")
    aplicar_desconto_metade = input("Aplicar super desconto de 50%? (s/n): ").lower()
    if aplicar_desconto_metade == 's':
        preco_produto /= 2
        print("Desconto aplicado!")
    elif aplicar_desconto_metade == 'n':
        print("Nenhum desconto aplicado.")
    else:
        print("Resposta inválida! Nenhum desconto foi aplicado.")
    print(f"Exemplo com if/else: Preço final: R$ {preco_produto:.2f}")

    # Exemplo 04:
    # Simula a meia-vida de um material radioativo
    material = 128.0
    print(f"Material inicial: {material}g")
    ciclos = 0
    while material >= 1:
        material /= 2
        ciclos += 1
        print(f"  -> Após {ciclos} ciclo(s), restam {material}g")
    print(f"Exemplo com while: O material levou {ciclos} ciclos para ficar abaixo de 1g.")


if __name__ == '__main__':
    main()