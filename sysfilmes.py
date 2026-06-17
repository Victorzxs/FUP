#from IPython.display import clear_output
import os


def voltar_menu():
    print("\n[**Tecle enter para voltar ao Menu Principal**]")
    if input(""):
        return

def simplifica_titulo(titulo):
    consoantes = "bcdfghjklmnpqrstvwxyz"
    a = "aáàâãä"
    e = "eéèêë"
    i = "iíìîï"
    o = "oóòôõö"
    u = "uúùûü"

    titulo = titulo.lower()
    titulo.replace(" ","")
    titulo_simplificado = ""
    for letra in titulo:
        if letra in consoantes:
            titulo_simplificado += letra
        else:
            if letra in a:
                titulo_simplificado += a[0]
            elif letra in e:
                titulo_simplificado += e[0]
            elif letra in e:
                titulo_simplificado += i[0]
            elif letra in e:
                titulo_simplificado += o[0]
            else:
                titulo_simplificado += u[0]

    return titulo_simplificado

# fazendo o menu

def mostra_menu(total):
    print("*********** SysFilmes ***********")
    print(f"******* Existem: {total} filmes *******")
    print("*********************************")
    print("1. Cadastrar Filme")
    print("2. Avaliar Filme")
    print("3. Consultar Filme por Título")
    print("4. Listar Filmes por Gênero")
    print("5. Listar Filmes por Estrelas")
    print("6. Listar Todos os Filmes")
    print("7. Carregar Filmes de Arquivo")
    print("8. Carregar Avaliações de Arquivo")
    print("9. Sair do Sistema")

    opcao = input("\nDigite a opção desejada: ")

    if opcao.isdigit() and opcao in "123456789":
        return int(opcao)
    else:
        print("\nOpção inválida. Tecle enter para repetir!")



# fazendo a cadastra filmes

def cria_filme(user,dados,filmes):
    if user:
        print("\n*********** SysFilmes ***********")
        print("******* Cadastrando Filme *******")
        print("*********************************")
        while True:
            titulo = input("Título: ")
            if len(titulo) < 1:
                print("Titulo invalido\n")
                continue
            existe = False
            for filme in filmes:
                if simplifica_titulo(titulo) == filme["titulo"]:
                    print("O titulo já existe\n")
                    existe = True
                    break
            if existe:
                continue
            break
        while True:
            ano = input("Ano: ")
            if ano.isdigit() and int(ano) >= 1896 and int(ano) <= 2026:
                ano = int(ano)
                break
            else:
                print("Ano invalido\n")

        genero = input("Gênero: ")
    else:
        titulo = dados[0]
        ano = int(dados[1])
        genero = dados[2].strip()
        
    filme = {
        "titulo":titulo,
        "ano":ano,
        "genero":genero,
        "estrelas":0.0,
        "num_avaliacoes":0
        }
    
    return filme


# fazendo a função lista todos

def lista_todos(filmes):
    print("*********** SysFilmes ***********")
    print("******** Listando Filmes ********")
    print("*********************************")
    for filme in filmes:
        mostra_filme(filme)
    


def mostra_filme(filme):
    print("\n")
    print(f"| Título: {filme["titulo"]}                       ")
    print(f"| Ano: {filme["ano"]}                             ")
    print(f"| Gênero: {filme["genero"]}                       ")
    print(f"| Estrelas: {filme["estrelas"]}                   ")
    print(f"| Número de avaliações: {filme["num_avaliacoes"]} ")


# fazendo a função lista por gênero

def lista_genero(genero, filmes):
    print("*********** SysFilmes ***********")
    print("*** Listando Filmes por Gênero **")
    print("*********************************")
    encontrado = False
    for filme in filmes:
        if filme["genero"] == genero:
            mostra_filme(filme)
            encontrado = True
    
    if not encontrado:
        print("\nNenhum filme desse gênero foi encontrado!")


#fazendo a função lista por estrelas

def lista_estrelas(num, filmes):
    print("*********** SysFilmes ***********")
    print("** Listando Filmes por Estrelas *")
    print("*********************************")
    encontrado = False
    for filme in filmes:
        if filme["estrelas"] >= num:
            mostra_filme(filme)
            encontrado = True

    if not encontrado:
        print("\nNenhum filme nesse critério foi encontrado!")


# fazendo consultar filmes por titulo

def consulta_titulo(filmes):
    print("*********** SysFilmes ***********")
    print("*** Consulta Filmes por Título **")
    print("*********************************")
    titulo = input("Digite o título do filme desejado: ")

    encontrado = False
    for filme in filmes:
        if busca_titulo(titulo, filme):
            mostra_filme(filme)
            encontrado = True

    if not encontrado:
        print("\nFilme não encontrado!")
    

def busca_titulo(titulo,filme):
    if simplifica_titulo(filme["titulo"]) == simplifica_titulo(titulo): 
        return filme
    else: 
        return

# avalia filmes

def avalia_filme(filmes, user, dados):
    if user:
        print("*********** SysFilmes ***********")
        print("******* Avaliação de Filme ******")
        print("*********************************")
        titulo = input("Digite o título do filme desejado: ")
    else:
        titulo = dados[0]

    encontrado = False
    for filme in filmes:
        if busca_titulo(titulo, filme):
            if user:
                while True:
                    estrelas = float(input("\nQuantas estrelas você atribui a esse filme? (1 a 5): "))
                    if estrelas <= 5 and estrelas >= 0:
                        break
                    else:
                        print("Número inválido. Tente novamente.")
            else:
                estrelas = float(dados[1].strip())
            filme["num_avaliacoes"] += 1
            filme["estrelas"] = round((filme["estrelas"]*(filme["num_avaliacoes"]-1)+estrelas)/filme["num_avaliacoes"],1)
            encontrado = True

    if not encontrado:
        print("\nFilme não encontrado!")

#carrega filmes do arquivo

def carrega_filmes(filmes):
    print("*********** SysFilmes ***********")
    print("** Carregando Filmes do Arquivo *")
    print("*********************************")
    arquivo = input("Digite o nome do arquvo: ")
    if os.path.exists(f"arquivos/{arquivo}"):
        with open(f"arquivos/{arquivo}","r",encoding="utf-8") as arquivo_aberto:
            conteudo = arquivo_aberto.readlines()
        primeira_linha = True
        for linha in conteudo:
            if primeira_linha:
                primeira_linha = False
                continue
            else:
                dados = linha.split(",")
                bd_filmes.append(cria_filme(False,dados,bd_filmes))
        print("\nFilmes carregados com sucesso!")
    else:
        print("Arquivo não encontrado!")

#carrega avaliações de filmes

def carrega_avaliacoes(filmes):
    print("************ SysFilmes ***********")
    print(" Carregando avaliações do Arquivo ")
    print("**********************************")
    arquivo = input("Digite o nome do arquvo: ")
    if os.path.exists(f"arquivos/{arquivo}"):
        with open(f"arquivos/{arquivo}","r",encoding="utf-8") as arquivo_aberto:
            conteudo = arquivo_aberto.readlines()
        primeira_linha = True
        for linha in conteudo:
            if primeira_linha:
                primeira_linha = False
                continue
            else:
                dados = linha.split(",")
                print(dados)
                avalia_filme(bd_filmes,False,dados)
        print("\nAvaliações carregadas com sucesso!")
    else:
        print("Arquivo não encontrado!")


# atualizar filmes

def atualiza_filmes(filmes):
    with open(f"arquivos/filmes.csv","r",encoding="utf-8") as arquivo_aberto:
        conteudo = arquivo_aberto.readlines()
    for filme in filmes:
        existe = False
        for linha in conteudo:
            dados = linha.split(",")
            if filme["titulo"] == dados[0]:
                existe = True
                break
        if not existe:
            with open(f"arquivos/filmes.csv","a",encoding="utf-8") as arquivo_aberto:
                arquivo_aberto.write(f"{filme["titulo"]},{filme["ano"]},{filme["genero"]}\n")

# atualiza avaliações

def  atualiza_avaliacoes(filmes):
    conteudo_lista = []
    with open(f"arquivos/avaliacoes.csv","r+",encoding="utf-8") as arquivo_aberto:
        conteudo = arquivo_aberto.readlines()
    for linha in conteudo:
        dados = linha.split(",")
        avalia_filme(bd_filmes,False,dados)


# programa princial

bd_filmes = []

while True:
    opcao = mostra_menu(len(bd_filmes))

    os.system('cls' if os.name == 'nt' else 'clear')

    if opcao == 1:
        bd_filmes.append(cria_filme(True, None, bd_filmes))
        atualiza_filmes(bd_filmes)

    elif opcao == 2:
        avalia_filme(bd_filmes, True, None)

    elif opcao == 3:
        consulta_titulo(bd_filmes)

    elif opcao == 4:
        genero = input("\nDigite o gênero desejado: ")

        os.system('cls' if os.name == 'nt' else 'clear')
        lista_genero(genero, bd_filmes)

    elif opcao == 5:
        while True:
            estrelas = float(input("\nDigite o número de estrelas desejado: "))
            if estrelas <= 5 and estrelas >= 0:
                break
            else:
                print("Número inválido. Tente novamente.")

        os.system('cls' if os.name == 'nt' else 'clear')
        lista_estrelas(estrelas, bd_filmes)

    elif opcao == 6:
        lista_todos(bd_filmes)

    elif opcao == 7:
        carrega_filmes(bd_filmes)

    elif opcao == 8:
        carrega_avaliacoes(bd_filmes)

    elif opcao == 9:
        print("\n[**Bye, você saiu do SysFilmes!**]")
        break

    voltar_menu()
    os.system('cls' if os.name == 'nt' else 'clear')