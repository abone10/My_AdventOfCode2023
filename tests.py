lista = [2,5,6,6,4,4]
print('lista: ', lista)

lista2 = []
lista2.append(lista)

lista3 = []
lista3.extend(lista)

print('lista2: ', lista2)
print('lista3: ', lista3)
lista.clear()
print('lista2: ', lista2)
print('lista3: ', lista3)