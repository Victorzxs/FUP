#apenas importei o OS para limpar o console pois não consegui importa o IPython.display.
import os

def voltar_menu():
    print("\n[**Tecle enter para voltar ao Menu Principal**]")
    if input(""):
        return

#função extra criada para permitir fazer comparações mais flexiveis.
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
            if letra in "cç":
                titulo_simplificado += "c"
            else:
                titulo_simplificado += letra
        else:
            if letra in a:
                titulo_simplificado += a[0]
            elif letra in e:
                titulo_simplificado += e[0]
            elif letra in i:
                titulo_simplificado += i[0]
            elif letra in o:
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

    """"
    verifica a entrada do úsuario para não quebrar o código e depois eu converto para inteiro 
    nesse caso nem precisava converter contanto que eu comparasse as opções como strings.
    """
    if opcao.isdigit() and opcao in "123456789":
        return int(opcao)
    else:
        print("\nOpção inválida.")
        voltar_menu()



"""
função que adiciona os filmes ao banco de filmes, ela possui três paramêtros, o 'user' 
serve para direcionar o fluxo do programa caso quem a acesse seja o úsuario e o sistema, o
'dados' somente é utilizado no fluxo do sistema, já que ele utiliza as informações do arquivo e 
elas não precisam de nenhuma verificação, e 'filmes' é o banco em si, a parte que fica na mémoria ram.
A função recebe os dados do úsuario e os verifica para garantir a integridade do sistema, após isso, 
os adiciona no banco de filmes. Caso seja o sistema ele so preenche as variveis e adiciona no banco.
"""
def cria_filme(user,dados,filmes):
    if user:
        print("\n*********** SysFilmes ***********")
        print("******* Cadastrando Filme *******")
        print("*********************************")

        #verifica se o titulo já existe na lista.
        while True:
            titulo = input("Título: ")
            if len(titulo) < 3:
                print("Titulo invalido\n")
                continue
            if not titulo.replace(" ","").isalnum():
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
            titulo = titulo.capitalize()
            break

        """"
        verifica se o ano está dentro do intervalo que eu determinei, o limitante inferior é o ano de lançamento 
        do primeiro filme de acordo com o google, e o superior o ano atual. o é recebido como inteiro para ter 
        mais tolerância a falha e não quebrar o código.
        """
        while True:
            ano = input("Ano: ")
            if ano.isdigit() and int(ano) >= 1896 and int(ano) <= 2026:
                ano = int(ano)
                break
            else:
                print("Ano invalido\n")
        generos_cinematograficos = [
            "Ação",
            "Aventura",
            "Animação",
            "Comédia",
            "Comédia Romântica",
            "Crime",
            "Documentário",
            "Drama",
            "Fantasia",
            "Ficção Científica",
            "Guerra",
            "Mistério",
            "Musical",
            "Romance",
            "Suspense",
            "Terror",
            "Thriller Psicológico",
            "Western",
            "Biografia",
            "Família",
            "Esporte",
            "Histórico",
            "Noir",
            "Super-herói"]
        
        """
        verifica se o gênero digitado pertence a lista de gêneros acima usando a função simplifica_titulo 
        inicialmente a função seria usada apenas para o titulo, mas como eu quis melhorar a entrada dos gêneros 
        eu a utilizei, e devido ao fato de ela já ter sido usada em outras partes do código eu preferi não 
        alterar o nome, para não ter que mudar tudo.
        """
        while True:
            genero = input("Gênero: ")
            genero_valido = False
            for genero_cine in generos_cinematograficos:
                if simplifica_titulo(genero) == simplifica_titulo(genero_cine):
                    genero = genero_cine
                    genero_valido = True
                    break
            if genero_valido:
                break
            else:
                print("gênero invalido!!\n")
    else:
        titulo = dados[0]
        ano = int(dados[1])
        genero = dados[2].strip()

        for filme in filmes:
            if simplifica_titulo(filme["titulo"]) == simplifica_titulo(titulo):
                filme["titulo"] = titulo
                filme["genero"] = genero
                filme["ano"] = ano
                return
        
    filme = {
        "titulo":titulo,
        "ano":ano,
        "genero":genero,
        "estrelas":0.0,
        "num_avaliacoes":0
        }
    
    return filme


# Recebe um filme do banco de filmes e envia para a função mostra_filme
def lista_todos(filmes):
    print("*********** SysFilmes ***********")
    print("******** Listando Filmes ********")
    print("*********************************")
    for filme in filmes:
        mostra_filme(filme)

# imprime na tela as informações sobre cada filme no layout visivel abaixo
def mostra_filme(filme):
    print("\n")
    print(f"| Título: {filme["titulo"]}                       ")
    print(f"| Ano: {filme["ano"]}                             ")
    print(f"| Gênero: {filme["genero"]}                       ")
    print(f"| Estrelas: {filme["estrelas"]}                   ")
    print(f"| Número de avaliações: {filme["num_avaliacoes"]} ")


"""
Recebe um filme do banco de filmes e verifica se o gênero do filme é igual ao digitado pelo úsuario 
e novamente eu usei a função simplifica_titulo para o que ela não foi pensada inicialmente, mas isso
não é relevante.
"""
def lista_genero(genero, filmes):
    print("*********** SysFilmes ***********")
    print("*** Listando Filmes por Gênero **")
    print("*********************************")
    encontrado = False
    for filme in filmes:
        if simplifica_titulo(filme["genero"]) == simplifica_titulo(genero):
            mostra_filme(filme)
            encontrado = True
    
    if not encontrado:
        print("\nNenhum filme desse gênero foi encontrado!")


"""
Recebe um filme e um número minimo de estrelas que um filme deve ter e depois verifica se o número 
de estrelas do filme está dentro do intervalo, minimo, digitado pelo úsuario, e 5, que é o limitante 
padrão do sistema.
"""
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


"""
Recebe um titulo do úsuario e verifica no banco de filmes se aquele titulo está contido, a 
verificação busca é feita usando a função busca_titulo.
"""
def consulta_titulo(filmes):
    print("*********** SysFilmes ***********")
    print("*** Consulta Filmes por Título **")
    print("*********************************")
    titulo = input("Digite o título do filme desejado: ")

    encontrado = False
    for filme in filmes:
        if busca_titulo(titulo, filme, 2):
            mostra_filme(filme)
            encontrado = True

    if not encontrado:
        print("\nFilme não encontrado!")
    

"""
Verifica se um titulo digitado pelo úsuario é igual ou está contido em um titulo vindo 
do banco de filmes, o que permite uma boa flexibilidade para buscas de filmes e uma boa 
rigidez para fazer a avaliação dos filmes.
"""
def busca_titulo(titulo,filme,modo):
    if modo == 1:
        if simplifica_titulo(filme["titulo"]) == simplifica_titulo(titulo): 
            return filme
    elif modo == 2:
        if simplifica_titulo(titulo) in simplifica_titulo(filme["titulo"]): 
            return filme


"""
A função avalia_filme possui semelhança com a cria_filme devido ao fato de ser usado pelo úsuario 
e o sistema, a explicação para os paramêtros da avalia_filme e a mesma da cria_filme. Caso seja o úsuario 
a função recebe o titulo de um filme e verifica se pertence ao banco, caso pertença ela solicita uma avaliação e 
somente a adiciona ao banco caso ela pertença ao intervalo (0,5], e em seguida adiciona ao arquivo de avaliações. 
Caso seja o sistema ela recebe os dados e o adiciona no banco.
"""
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
        if busca_titulo(titulo, filme, 1):
            if user:
                while True:
                    estrelas = float(input(f"\nQuantas estrelas você atribui ao filme {filme["titulo"]}? (1 a 5): "))
                    if estrelas <= 5 and estrelas > 0:
                        break
                    else:
                        print("Número inválido. Tente novamente.")
            else:
                estrelas = float(dados[1].strip())

            filme["num_avaliacoes"] += 1
            filme["estrelas"] = round((filme["estrelas"]*(filme["num_avaliacoes"]-1)+estrelas)/filme["num_avaliacoes"],1)

            if user:
                atualiza_avaliacoes(filme["titulo"], estrelas)
                print("\nAvaliação efetuada com sucesso :)")

            encontrado = True
            break

    if not encontrado:
        print("\nFilme não encontrado!")


"""
A função verifica se um arquivo com o nome digitado pelo úsuario exista, para que não de Erro e caso ele 
exista ela pega o contéudo do arquivo e o fecha. Em seguida ela passa por todas as linhas e adiciona suas 
informações no banco por meio da função cria_filme, exceto a primeira, que é ignorada devido a variavel 
'primeira_linha'.
"""
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
                if cria_filme(False,dados,bd_filmes) is not None:
                    filmes.append(cria_filme(False,dados,bd_filmes))
        print("\nFilmes carregados com sucesso!")
    else:
        print("Arquivo não encontrado!")


"""
Semelhante a primeira ela faz as mesmas coisas só que para as avalições e usa a função avalia_filme 
para colocar as informações no banco.
"""
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
                avalia_filme(filmes,False,dados)
        print("\nAvaliações carregadas com sucesso!")
    else:
        print("Arquivo não encontrado!")


"""
A função copia todas as informações do arquivo com a função 'readlines()' e em seguida percorre cada 
filme do banco e verifica se já foi adicionado, caso tenha sido segue para o proximo, caso não, 
ele o adiciona e continua assim até o ultimo filme.
"""
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


# apenas recebe um titulo e a avaliação e a adiciona no arquivo de avaliações
def  atualiza_avaliacoes(titulo, estrelas):
    with open(f"arquivos/avaliacoes.csv","a",encoding="utf-8") as arquivo_aberto:
        arquivo_aberto.write(f"{titulo},{estrelas}\n")


bd_filmes = []
filmes_carregados = False

while True:
    opcao = mostra_menu(len(bd_filmes))

    os.system('cls' if os.name == 'nt' else 'clear')

    if opcao == 1:
        bd_filmes.append(cria_filme(True, None, bd_filmes))
        atualiza_filmes(bd_filmes)

    elif opcao == 2:
        if not bd_filmes:
            print("\nNenhum filme adicionado!!")
        else:
            avalia_filme(bd_filmes, True, None)

    elif opcao == 3:
        if not bd_filmes:
            print("\nNenhum filme adicionado!!")
        else:
            consulta_titulo(bd_filmes)

    elif opcao == 4:
        if not bd_filmes:
            print("\nNenhum filme adicionado!!")
        else:
            genero = input("\nDigite o gênero desejado: ")

            os.system('cls' if os.name == 'nt' else 'clear')
            lista_genero(genero, bd_filmes)

    elif opcao == 5:
        if not bd_filmes:
            print("\nNenhum filme adicionado!!")
        else:
            while True:
                estrelas = float(input("\nDigite o número de estrelas desejado: "))
                if estrelas <= 5 and estrelas >= 0:
                    break
                else:
                    print("Número inválido. Tente novamente.")

            os.system('cls' if os.name == 'nt' else 'clear')
            lista_estrelas(estrelas, bd_filmes)

    elif opcao == 6:
        if not bd_filmes:
            print("\nNenhum filme adicionado!!")
        else:
            lista_todos(bd_filmes)

    elif opcao == 7:
        carrega_filmes(bd_filmes)
        filmes_carregados = True

    elif opcao == 8:
        if filmes_carregados:
            carrega_avaliacoes(bd_filmes)
        else:
            print("\nOs filmes ainda não foram carregados do arquivo 'filmes.csv'.")

    elif opcao == 9:
        print("\n[**Bye, você saiu do SysFilmes!**]")
        break

    voltar_menu()
    os.system('cls' if os.name == 'nt' else 'clear')