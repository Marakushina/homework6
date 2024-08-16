immutable_var= (1,2,True,"spring")
print(immutable_var)
#immutable_var[0]=200
#print(immutable_var)
#На выходе выдает: TypeError: 'tuple' object does not support item assignment
# Объяснение: Кортеж — это неизменяемый тип данных, который используется для хранения упорядоченной последовательности элементов.
immutable_var= ([1,2],True,"spring")  #возможность изменения при использовании квадратных скобок
print(immutable_var)
immutable_var[0][0]=6
print(immutable_var)
mutable_list=["reptile","amphibian","bird","fish"]
print(mutable_list)
mutable_list.append(False)
print(mutable_list)
mutable_list[2]="dable"
print(mutable_list)
mutable_list.extend("12345")
print(mutable_list)
mutable_list.extend(['global',44])
print(mutable_list)
mutable_list.remove('fish')
print(mutable_list)
mutable_list.pop()
print(mutable_list)