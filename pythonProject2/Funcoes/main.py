from Funcoes.F01 import F001

if __name__ == '__main__':
    nome = input("Entre com seu nome: ")
    f1 = F001(nome)
    print(f"O seu nome é: {f1.saudacao()}")
