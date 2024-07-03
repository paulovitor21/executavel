import locale

# Definindo o locale para o formato de moeda dos Estados Unidos
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

def format_to_dollar(number_str):
    # Verifica se o número está no formato europeu (1.234,56)
    if ',' in number_str and '.' in number_str:
        if number_str.find('.') < number_str.find(','):
            # Formato europeu: 1.234,56
            # Remover os pontos (separador de milhar)
            number_str = number_str.replace('.', '')
            # Substituir a vírgula pelo ponto (separador decimal)
            number_str = number_str.replace(',', '.')
        else:
            # Formato americano: 1,234.56
            # Remover as vírgulas (separador de milhar)
            number_str = number_str.replace(',', '')
    
    # Caso contrário, verifica se é apenas um formato europeu simples: 1234,56
    elif ',' in number_str:
        # Substituir a vírgula pelo ponto (separador decimal)
        number_str = number_str.replace(',', '.')
    
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
