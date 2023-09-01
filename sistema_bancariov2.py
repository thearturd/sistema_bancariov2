saldo = 0
limite = 500
extrato = ""
numero_saques = 0
usuarios = []
contas = []
LIMITE_SAQUES = 3
AGENCIA = "0001"

menu = '''
####################

 Selecione uma opção:
 [1] Depositar
 [2] Sacar
 [3] Extrato
 [4] Novo Usuário
 [5] Nova Conta
 [0] Sair

####################
'''
def depositar(saldo, deposito, extrato, /):
    if deposito > 0:
        saldo += deposito
        extrato += f"Depósito:\tR$ {deposito:.2f}\n"
        print(f"\nDeposito de {deposito} feito com sucesso.\nSeu saldo atual é de R$ {saldo:.2f}")
    else:
        print("Valor inválido.")

    return saldo, extrato

def sacar(*, saldo, saque, extrato, limite, numero_saques, LIMITE_SAQUES):
    if numero_saques < LIMITE_SAQUES:
            if saque > 0 and saldo >= saque <= limite:
                numero_saques += 1
                saldo -= saque
                extrato += f"Saque:    R$ {saque:.2f}\n"
                print(f"Saque de R$ {saque} realizado com sucesso.")
            elif saque > 0 and saldo < saque:
                print("Saldo insuficiente.")
            elif saque > limite:
                print(f"Saque invalido, o limite é R$ {limite:.2f} por vez")
            else:
                print("Valor inválido.")
    else:
           print("Limite diário atingido.")
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, /, *, extrato):
    if saldo == 0 and numero_saques == 0 :
            print("Não foram realizadas movimentações.")
    else:
            print(f"""EXTRATO:
{extrato}
____________________
Saldo: R$ {saldo:.2f}""")

def novo_usuario(usuarios):
    cpf = input("Informe o CPF usando somente números: ")
    usuario = filtro_usuario(cpf, usuarios)

    if usuario:
        print("Já existe um usuário com esse CPF!")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, N° - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print(f"Usuário {nome} criado com sucesso!")

def filtro_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def nova_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtro_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("Usuário não encontrado, verifique se existe mesmo o usuário.")


try:
  while True:

    opcao = int(input(menu))

    if opcao == 1:
        deposito = float(input("Digite o valor a Depositar:"))

        saldo, extrato = depositar(saldo, deposito, extrato)

    elif opcao == 2:
        saque = float(input("Digite um deposito de Saque:"))

        saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                saque=saque,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                LIMITE_SAQUES=LIMITE_SAQUES,
            )

    elif opcao == 3:
        exibir_extrato(saldo, extrato=extrato)
            
    elif opcao == 4:
        novo_usuario(usuarios)

    elif opcao == 5:
        numero_conta = len(contas) + 1
        conta = nova_conta(AGENCIA, numero_conta, usuarios)

        if conta:
            contas.append(conta)
    
    elif opcao == 0:
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")

except:
    print("Opção Inválida! Digite o número correspondente a opção.")

        