# Calculadora-ajudante
feito em Python para usar em PC facos ou testes divertidos participe




def calculadora():
    print("Bem-vindo à Calculadora Simples!")
    print("Selecione a operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")

    # Solicita ao usuário que escolha uma operação
    escolha = input("Digite o número da operação desejada (1/2/3/4): ")

    # Verifica se a escolha é válida
    if escolha in ['1', '2', '3', '4']:
        try:
            # Solicita os números ao usuário
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            # Realiza a operação escolhida
            if escolha == '1':
                print(f"Resultado: {num1} + {num2} = {num1 + num2}")
            elif escolha == '2':
                print(f"Resultado: {num1} - {num2} = {num1 - num2}")
            elif escolha == '3':
                print(f"Resultado: {num1} * {num2} = {num1 * num2}")
            elif escolha == '4':
                if num2 != 0:
                    print(f"Resultado: {num1} / {num2} = {num1 / num2}")
                else:
                    print("Erro: Divisão por zero não é permitida.")
        except ValueError:
            print("Erro: Por favor, insira números válidos.")
    else:
        print("Opção inválida. Por favor, tente novamente.")

# Executa a calculadora
calculadora()
