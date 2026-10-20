num = [2, 5, 9, 1]
b = num[:]
num[2] = 3
num.append(7)
num.sort(reverse=True) # num.sort() do menor para maior
num.insert(2, 0)
num.pop(2)
num.remove(2)
for c ,v in enumerate(num):
    print(f'na posicao {c} encontrei o valor {v}')
print(f'Essa lista tem {len(num)} elementos.')
print(b)