def calculadora(valor1, valor2, operacao):
    """
    Realiza uma das cinco operações matemáticas básicas (soma, subtração,
    multiplicação, divisão, potenciação) entre dois valores.

    Args:
        valor1 (any): O primeiro valor da operação. Pode ser int, float ou uma string
                      que possa ser convertida para float.
        valor2 (any): O segundo valor da operação. Pode ser int, float ou uma string
                      que possa ser convertida para float.
        operacao (str): O símbolo da operação a ser realizada.
                        Valores aceitos: '+', '-', '*', '/', '^'.

    Returns:
        float or None: O resultado da operação matemática se as entradas forem
                       válidas, ou None caso contrário.
    """
    # 1. Valida se os valores de entrada podem ser convertidos para números (float)
    try:
        num1 = float(valor1)
        num2 = float(valor2)
    except (ValueError, TypeError):
        # Se a conversão falhar, os valores são inválidos.
        return None

    # 2. Define as operações válidas
    operacoes_validas = ['+', '-', '*', '/', '^']

    # 3. Valida se a operação solicitada existe na lista de operações válidas
    if operacao not in operacoes_validas:
        return None

    # 4. Realiza o cálculo correspondente à operação
    resultado = 0
    if operacao == '+':
        resultado = num1 + num2
    elif operacao == '-':
        resultado = num1 - num2
    elif operacao == '*':
        resultado = num1 * num2
    elif operacao == '^':
        # Em Python, o operador de potenciação é **
        resultado = num1 ** num2
    elif operacao == '/':
        # Caso especial: verifica a divisão por zero
        if num2 == 0:
            print("Erro: Divisão por zero não é permitida.")
            return None
        resultado = num1 / num2

    return resultado

# --- Bloco de Execução Principal ---
# Este código só será executado quando o script for rodado diretamente
if __name__ == "__main__":
    print("--- Calculadora Simples em Python ---")

    # Obter entrada do usuário
    val1 = input("Digite o primeiro valor: ")
    op = input("Digite a operação (+, -, *, /, ^): ")
    val2 = input("Digite o segundo valor: ")

    # Chamar a função da calculadora com os dados do usuário
    resultado_final = calculadora(val1, val2, op)

    # Exibir o resultado ou a mensagem de erro
    if resultado_final is not None:
        # Usamos f-string para formatar a saída de forma clara
        print(f"\nO resultado de {val1} {op} {val2} é: {resultado_final}")
    else:
        print("\nOperação falhou. Por favor, verifique se os valores são numéricos e a operação é válida.")
        