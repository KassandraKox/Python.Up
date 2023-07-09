# Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
# Напишите функцию, которая при запуске заменяет содержимое переменных оканчивающихся на s
# (кроме переменной из одной буквы s) на None.
# Значения не удаляются, а помещаются в одноимённые переменные без s на конце.
def change_var(var_dict: dict):
    vars_to_change = [c for c in var_dict if len(c) > 1 and c[-1] == 's']
    for c in vars_to_change:
        var_dict[c[:-1]] = var_dict[c]
        var_dict[c] = None

a = 123
b = 'Test'
c = 'teeeest'
s = 567
var_s = 1

all_var = globals()
print(f"{a = }\n{b = }\n{s = }\n{s = }\n{var_s = }\n{all_var = }\n")

change_var(all_var)
print(f"{a = }\n{b = }\n{s = }\n{s = }\n{var_s = }\n{all_var = }\n")
print(f"{b = }\n{var_ = }\n")
