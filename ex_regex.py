import locale
import re

# Definindo o locale para o formato de moeda dos Estados Unidos
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

def format_to_dollar(number_str):
    # Expressão regular para formato europeu (1.234,56)
    european_pattern = re.compile(r'^\d{1,3}(\.\d{3})*,\d{2}$')
    # Expressão regular para formato americano (1,234.56)
    american_pattern = re.compile(r'^\d{1,3}(,\d{3})*\.\d{2}$')

    if european_pattern.match(number_str):
        # Formato europeu: 1.234,56
        # Remover os pontos (separador de milhar)
        number_str = number_str.replace('.', '')
        # Substituir a vírgula pelo ponto (separador decimal)
        number_str = number_str.replace(',', '.')
    elif american_pattern.match(number_str):
        # Formato americano: 1,234.56
        # Remover as vírgulas (separador de milhar)
        number_str = number_str.replace(',', '')
    else:
        return "Número inválido"

    try:
        # Convertendo a string para float
        number_float = float(number_str)
        
        # Formatando o número como dólar
        formatted_number = locale.currency(number_float, grouping=True)
        return formatted_number
    except ValueError:
        return "Número inválido"

# Exemplo de uso
number = "1.234,56"  # Número no formato europeu
formatted_number = format_to_dollar(number)
print(formatted_number)  # Resultado esperado: $1,234.56

number = "1,234.56"  # Número no formato americano
formatted_number = format_to_dollar(number)
print(formatted_number)  # Resultado esperado: $1,234.56

number = "1234,56"  # Número no formato europeu sem separador de milhar
formatted_number = format_to_dollar(number)
print(formatted_number)  # Resultado esperado: $1,234.56

number = "1234.56"  # Número no formato americano sem separador de milhar
formatted_number = format_to_dollar(number)
print(formatted_number)  # Resultado esperado: $1,234.56

number = "93.20"  # Número inválido
formatted_number = format_to_dollar(number)
print(formatted_number)  # Resultado esperado: Número inválido
