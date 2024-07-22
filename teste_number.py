import locale

def format_number(value):
    # Sua função para formatar números, ajuste conforme necessário
    return value

amount_list = []
for i in range(0, len(df['Amount'].values)):
    number = df['Amount'].values[i]
    print(number)
    if type(number) == type(None): continue
    number = number.replace('.', '').replace(',', '.')
    amount_list.append(float(number))

amount_total = sum(amount_list)
print(amount_total)

# Formatação para exibir todas as casas decimais presentes
amount_total_as_string = "{:,.2f}".format(amount_total).replace('.', ',').replace(',', 'x').replace('x', '.')

print(amount_total_as_string)

amount_total_as_string = format_number(amount_total_as_string)
text_result = ['Total Amount:', amount_total_as_string]