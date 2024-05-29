def login_usuario(perfil):
    

    
    perfil = perfil.lower()

   
    if perfil == 'admin':
        print('Bem-vindo, Administrador')
    else:
        print('Bem-vindo, Usuário')


perfil = input("Loguin De Usuario: ")

login_usuario(perfil)