login = ['joao', 'jose', 'chico']

def addlista(lista):

    while True:
        addlogin = input('Informe seu login: ')

        if addlogin == 'sair':
            break

        elif addlogin in lista:
            print('Login ja existente')

        else:
            lista.append(addlogin)
            print(lista)

addlista(login)

print(login)