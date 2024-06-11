# Repetir el punto anterior pero con la expresión que determina que una letra NO es vocal.


for i in range(4):
    for j in range(6):
        if i==0 or j==0:
            print('*', end='')
        else:
            print(' ', end='')
    print()


print()
print('*'*10)

print('hola', end='')
print('aca es el ed')