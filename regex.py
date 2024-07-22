import locale
import re
from decimal import Decimal

# Definindo o locale para o formato de moeda dos Estados Unidos
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

def format_to_european_currency(number_str):
    # Expressão regular para identificar um número no formato europeu com ponto como separador decimal
    european_pattern_with_dot = re.compile(r'^\d{1,3}(\.\d{3})*\.\d+$')

    if european_pattern_with_dot.match(number_str):
        # Remover os pontos (separador de milhar, se existirem)
        number_str = number_str.replace('.', '')
        # Substituir o último ponto pelo separador decimal europeu
        integer_part, decimal_part = re.match(r'(\d+)(\d{2})$', number_str).groups()
        number_str = f'{integer_part},{decimal_part}'
    else:
        return "Número inválido"

    try:
        # Convertendo a string para Decimal para manter a precisão
        number_decimal = Decimal(number_str.replace(',', '.'))

        # Formatando o número como moeda europeia
        formatted_number = locale.currency(number_decimal, grouping=True)
        return formatted_number
    except ValueError:
        return "Número inválido"

# Exemplo de uso
number = "62.9100"  # Número no formato europeu com ponto como separador decimal
formatted_number = format_to_european_currency(number)
print(formatted_number)  # Resultado esperado: 62.910,00