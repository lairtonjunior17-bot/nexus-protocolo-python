# Arquivo encontrado na mesa do estagiário anterior.
# Comentário dele: "calcula o consumo anual do cliente. NUNCA FUNCIONOU."
#
# Sua tarefa: corrigir este script sem reescrevê-lo do zero.

nome = input("Nome do cliente: ")
consumo_mensal = input("Consumo mensal (kWh): ")
tarifa = float(input("Tarifa (R$ por kWh): "))

consumo_anual = consumo_mensal * 12
gasto_anual = consumo_anual * tarifa

print("Cliente: " + nome)
print("Consumo anual: " + consumo_anual + " kWh")
print(f"Gasto anual: R$ {gasto_anua:.2f}")
