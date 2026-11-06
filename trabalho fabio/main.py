
# VARIAVEIS GLOBAIS

dados = []
MAX = 0

estrutura_criada = ""

# PILHA
ponteiro = -1

# FILA E FILA CIRCULAR
spos = 0
rpos = 0
quantidade = 0


# INICIALIZAR ESTRUTURA

def inicializa(tipo):
    global dados, MAX, ponteiro
    global spos, rpos, quantidade, estrutura_criada

    MAX = int(input("Informe o tamanho da estrutura: "))

    if MAX <= 0:
        print("Tamanho invalido!")
        return

    dados = [None] * MAX

    ponteiro = -1
    spos = 0
    rpos = 0
    quantidade = 0

    estrutura_criada = tipo

    print("\nEstrutura criada com sucesso!")


# PILHA

def push_pilha(valor):
    global dados, ponteiro

    if ponteiro == MAX - 1:
        print("\nPilha Cheia!!!")
        return

    ponteiro = ponteiro + 1
    dados[ponteiro] = valor

    print("Valor armazenado!")


def pop_pilha():
    global dados, ponteiro

    if ponteiro < 0:
        print("\nPilha Vazia!!!")
        return

    valor = dados[ponteiro]
    dados[ponteiro] = None
    ponteiro = ponteiro - 1

    print("Valor extraido:", valor)


def show_pilha():
    if ponteiro < 0:
        print("\nPilha Vazia!!!")
        return

    print("\nConteudo da pilha:")

    for i in range(ponteiro, -1, -1):
        print(dados[i])


# FILA

def push_fila(valor):
    global dados, spos, rpos, quantidade

    if quantidade == MAX:
        print("\nFila Cheia!!!")
        return

    # Reorganiza a fila se chegar ao final do vetor
    if spos == MAX:

        for i in range(quantidade):
            dados[i] = dados[rpos + i]

        for i in range(quantidade, MAX):
            dados[i] = None

        rpos = 0
        spos = quantidade

    dados[spos] = valor
    spos = spos + 1
    quantidade = quantidade + 1

    print("Valor armazenado!")


def pop_fila():
    global dados, rpos, spos, quantidade

    if quantidade == 0:
        print("\nFila Vazia!!!")
        return

    valor = dados[rpos]
    dados[rpos] = None

    rpos = rpos + 1
    quantidade = quantidade - 1

    if quantidade == 0:
        rpos = 0
        spos = 0

    print("Valor extraido:", valor)


def show_fila():
    if quantidade == 0:
        print("\nFila Vazia!!!")
        return

    print("\nConteudo da fila:")

    for i in range(rpos, spos):
        print(dados[i])


# FILA CIRCULAR

def push_circular(valor):
    global dados, spos, quantidade

    if quantidade == MAX:
        print("\nFila Circular Cheia!!!")
        return

    dados[spos] = valor

    spos = (spos + 1) % MAX
    quantidade = quantidade + 1

    print("Valor armazenado!")


def pop_circular():
    global dados, rpos, quantidade

    if quantidade == 0:
        print("\nFila Circular Vazia!!!")
        return

    valor = dados[rpos]
    dados[rpos] = None

    rpos = (rpos + 1) % MAX
    quantidade = quantidade - 1

    print("Valor extraido:", valor)


def show_circular():
    if quantidade == 0:
        print("\nFila Circular Vazia!!!")
        return

    print("\nConteudo da fila circular:")

    for i in range(quantidade):
        posicao = (rpos + i) % MAX
        print(dados[posicao])



# MENU DAS ESTRUTURAS


def menu_estrutura(tipo):

    opcao = 0

    while opcao != 5:

        print("\n===== MENU", tipo.upper(), "=====")
        print("1 - Criar estrutura")
        print("2 - Armazenar valor")
        print("3 - Extrair valor")
        print("4 - Imprimir conteudo")
        print("5 - Voltar ao menu anterior")

        opcao = int(input("Escolha: "))

        if opcao == 1:
            inicializa(tipo)

        elif opcao == 2:

            if estrutura_criada != tipo:
                print("Crie esta estrutura primeiro!")
                continue

            valor = int(input("Digite o valor: "))

            if tipo == "Pilha":
                push_pilha(valor)

            elif tipo == "Fila":
                push_fila(valor)

            elif tipo == "Fila Circular":
                push_circular(valor)

        elif opcao == 3:

            if estrutura_criada != tipo:
                print("Crie esta estrutura primeiro!")
                continue

            if tipo == "Pilha":
                pop_pilha()

            elif tipo == "Fila":
                pop_fila()

            elif tipo == "Fila Circular":
                pop_circular()

        elif opcao == 4:

            if estrutura_criada != tipo:
                print("Crie esta estrutura primeiro!")
                continue

            if tipo == "Pilha":
                show_pilha()

            elif tipo == "Fila":
                show_fila()

            elif tipo == "Fila Circular":
                show_circular()

        elif opcao == 5:
            print("Voltando ao menu principal...")

        else:
            print("Opcao invalida!")



# ALGORITMOS DE ORDENACAO


def ordenacao_bolha(A):
    n = len(A)

    for i in range(n):
        for j in range(0, n - 1):
            if A[j] > A[j + 1]:
                temp = A[j]
                A[j] = A[j + 1]
                A[j + 1] = temp


def ordenacao_selecao(A):
    n = len(A)

    for i in range(n):
        minimo = i

        for j in range(i + 1, n):
            if A[minimo] > A[j]:
                minimo = j

        A[i], A[minimo] = A[minimo], A[i]


def ordenacao_insercao(A):
    n = len(A)

    for j in range(1, n):
        chave = A[j]
        i = j - 1

        while i >= 0 and A[i] > chave:
            A[i + 1] = A[i]
            i = i - 1

        A[i + 1] = chave



# ORGANIZAR DADOS PARA ORDENACAO


def obter_dados():
    global dados

    if estrutura_criada == "Pilha":
        return dados[:ponteiro + 1]

    elif estrutura_criada == "Fila":
        return dados[rpos:spos]

    elif estrutura_criada == "Fila Circular":

        lista = []

        for i in range(quantidade):
            posicao = (rpos + i) % MAX
            lista.append(dados[posicao])

        return lista


def salvar_ordenacao(lista):
    global dados, rpos, spos, ponteiro

    if estrutura_criada == "Pilha":

        for i in range(len(lista)):
            dados[i] = lista[i]

    elif estrutura_criada == "Fila":

        dados = [None] * MAX

        for i in range(len(lista)):
            dados[i] = lista[i]

        rpos = 0
        spos = len(lista)

    elif estrutura_criada == "Fila Circular":

        dados = [None] * MAX

        for i in range(len(lista)):
            dados[i] = lista[i]

        rpos = 0
        spos = len(lista) % MAX



# MENU DE ORDENACAO


def menu_ordenacao():

    if estrutura_criada == "":
        print("\nCrie primeiro uma Pilha, Fila ou Fila Circular!")
        return

    opcao = 0

    while opcao != 4:

        print("\n===== MENU ORDENAR =====")
        print("1 - Bubble Sort")
        print("2 - Selection Sort")
        print("3 - Insertion Sort")
        print("4 - Voltar ao menu anterior")

        opcao = int(input("Escolha: "))

        if opcao == 4:
            break

        if opcao < 1 or opcao > 4:
            print("Opcao invalida!")
            continue

        lista = obter_dados()

        if len(lista) == 0:
            print("Nao existem valores para ordenar!")
            continue

        print("\nAntes da ordenacao:", lista)

        if opcao == 1:
            ordenacao_bolha(lista)

        elif opcao == 2:
            ordenacao_selecao(lista)

        elif opcao == 3:
            ordenacao_insercao(lista)

        salvar_ordenacao(lista)

        print("Depois da ordenacao:", lista)



# MENU PRINCIPAL


opcao = 0

while opcao != 5:

    print("\n========== MENU PRINCIPAL ==========")
    print("1 - PILHA")
    print("2 - FILA")
    print("3 - FILA CIRCULAR")
    print("4 - ORDENAR")
    print("5 - SAIR")

    opcao = int(input("Escolha uma opcao: "))

    if opcao == 1:
        menu_estrutura("Pilha")

    elif opcao == 2:
        menu_estrutura("Fila")

    elif opcao == 3:
        menu_estrutura("Fila Circular")

    elif opcao == 4:
        menu_ordenacao()

    elif opcao == 5:
        print("\nPrograma encerrado!")

    else:
        print("\nOpcao invalida!")
