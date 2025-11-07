while True:
    nome = input('Digite Seu Nome: ').strip()
    if len(nome) == 0:
        print('Erro: O nome não pode ficar vazio.\n')
        continue
    if any(char.isdigit() for char in nome):
        print('Erro: O nome não pode conter numeros.\n')
        continue
    print('Nome valisdo')
    break
while True:
    email = input('Digite Seu Email')
    if "@" not in email or "." not in email:
        print('Erro: Email Invalido.\n')
        continue
    print('Email Valido!\n')
    break
while True:
    senha = input("Crie uma senha (mínimo 6 caracteres): ").strip()

    if len(senha) < 6:                          
        
        print("Erro: a senha deve ter pelo menos 6 caracteres.\n")
        continue

    if " " in senha:                            
        print("Erro: a senha não pode conter espaços.\n")
        continue

    print("✅ Senha cadastrada com sucesso!\n")
    break



print("🎉 Cadastro concluído com sucesso!")