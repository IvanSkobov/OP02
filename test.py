symbol_list =  []
for i in range(5):
    value =input(f"Введите символ или цифру ({i + 1}/5):")
    symbol_list.append(value)
print("Итоговый список:", symbol_list)
for i in range(5):
    total_list_1=input(f"Введите еще символы ({i + 1}/5):")
    symbol_list.extend(total_list_1)
print("Итоговый список:", symbol_list)
symbol_list.sort(reverse=True)
print("Итоговый список:", symbol_list)