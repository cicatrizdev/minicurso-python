usuario = senha = ''
while (usuario == senha):
    usuario = input('Informe um nome de usuario: ')
    senha = input('Informe a senha: ')
    if (usuario == senha):
        print ('A senha nao pode ser igual ao nome do usuario')
