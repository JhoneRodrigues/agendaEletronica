import os

# retirei a chamada os.system('cls') e adicionei uma função 'clear' para o linux também
def clear():
    if os.name == 'nt':
        return os.system('cls')
    return os.system('clear')


print("Agenda eletronica\n")
contatos = []
dados = []
resp = 's'

#Lendo e armazenando os dados de cada contato
while resp == 's':
    dados.append(str(input("Insira o nome: ")))
    dados.append(int(input("Insira o telefone: ")))
    dados.append(str(input("Empresa que trabalha: ")))
    contatos.append(dados[:])
    dados.clear()
    resp = input("Deseja adicionar outro contato (s/n)? ").lower()
    while resp != 's' and resp != 'n':
        resp = input("Resposta invalida, responda apenas com 's' ou 'n': ").lower()
    clear()

#Demonstrando e pedindo ao usuario a opcao a seguir
menu_opcoes = {
    1: "Adicionar contato",
    2: "Excluir contato",
    3: "Listar todos os contatos",
    4: "Alterar contato",
    5: "Listar dados de um determinado contato",
    6: "Sair"
}

# dicionário que recebe as entradas, melhor manutenção futura
print('Menu de opções: ')
for key, value in menu_opcoes.items():
    print(f' >> ({key}) {value}')

while True:
    try:
        resp2 = int(input("Deseja realizar qual opção: "))
        while resp2 not in menu_opcoes.keys():
            resp2 = int(input("Essa opção não está no menu.\nDigite novamente: "))
        break
    except ValueError:
        print("Você não digitou um valor numérico, digite novamente.")
        continue
while resp2 in [1,2,3,4,5]:
    #OPCAO 1 - Criando um novo contato    
    while resp2 == 1:
        print("\nAdicionando um novo contato\n")
        dados.append(str(input("Insira o nome: ")))
        dados.append(int(input("Insira o telefone: ")))
        dados.append(str(input("Empresa que trabalha: ")))
        contatos.append(dados[:])
        dados.clear()
        while True:
            try:
                resp2 = int(input("Qual sua próxima opção? "))
                while resp2 not in [1,2,3,4,5,6]:
                    resp2 = int(input("Opção fora do intervalo de 1 a 6\nDigite novamente: "))
                break
            except ValueError:
                print("Você não digitou um valor numérico, digite novamente.")
                continue
    #OPCAO 2 - Excluindo um contato
    while resp2 == 2:
        print ("\nExluindo um contato\n")
        posi = int (input("Qual a posição do contato que deseja remover? "))
        while posi < 1 or posi > len(contatos):
            posi = int (input("Posição invalida, tente novamente: "))
        del contatos[posi-1]
        while True:
            try:
                resp2 = int(input("Qual sua próxima opção? "))
                while resp2 not in [1,2,3,4,5,6]:
                    resp2 = int(input("Opção fora do intervalo de 1 a 6\nDigite novamente: "))
                break
            except ValueError:
                print("Você não digitou um valor numérico, digite novamente.")
                continue
    #OPCAO 3 - Listar todos os Contatos
    while resp2 == 3:
        print ("\nListando Todos os Contatos\n")
        print("Nome:\t\tTelefone:\t\tEmpresa:")
        for e,i in enumerate (contatos):
            print(i[0],"\t\t",i[1],"\t\t\t",i[2])
        while True:
            try:
                resp2 = int(input("Qual sua próxima opção? "))
                while resp2 not in [1,2,3,4,5,6]:
                    resp2 = int(input("Opção fora do intervalo de 1 a 6\nDigite novamente: "))
                break
            except ValueError:
                print("Você não digitou um valor numérico, digite novamente.")
                continue
    #OPCAO 4 - Alterar Contato
    while resp2 == 4:
        print ("\nAlterando um contato\n")
        posi = int (input("Qual a posição do contato que deseja alterar? "))
        while posi < 1 or posi > len(contatos):
            posi = int (input("Posição invalida, tente novamente: "))    
        for e,i in enumerate (contatos):
            if e == posi-1:
                i[0] = str(input("Insira o nome: "))
                i[1] = int(input("Insira o telefone: "))
                i[2] = str(input("Empresa que trabalha: "))
        while True:
            try:
                resp2 = int(input("Qual sua próxima opção? "))
                while resp2 not in [1,2,3,4,5,6]:
                    resp2 = int(input("Opção fora do intervalo de 1 a 6\nDigite novamente: "))
                break
            except ValueError:
                print("Você não digitou um valor numérico, digite novamente.")
                continue
    #OPCAO 5 - Listar os dados de um determinado contato
    while resp2 == 5:
        print ("\nListando os dados de um contato\n")
        posi = int (input("Qual a posição do contato que deseja listar? "))
        while posi < 1 or posi > len(contatos):
            posi = int (input("Posição invalida, tente novamente: ")) 
        for e,i in enumerate (contatos):
            if e == posi-1:
                print("Nome:\t\tTelefone:\t\tEmpresa:")
                print(i[0],"\t\t",i[1],"\t\t\t",i[2])
        while True:
            try:
                resp2 = int(input("Qual sua próxima opção? "))
                while resp2 not in [1,2,3,4,5,6]:
                    resp2 = int(input("Opção fora do intervalo de 1 a 6\nDigite novamente: "))
                break
            except ValueError:
                print("Você não digitou um valor numérico, digite novamente.")
                continue
#OPCAO 6 - Sair (Fim do programa)
if resp2 == 6:
    clear()
    print("Sua Lista foi finaliza.")