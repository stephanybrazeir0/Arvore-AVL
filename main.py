class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerdo = None
        self.direito = None
        self.altura = 0

def novo_no(x):
    novo = No(x)
    return novo

def altura_do_no(no):
    if no is None:
        return -1
    else:
        return no.altura

def fator_de_balanceamento(no):
    if no:
        return altura_do_no(no.esquerdo) - altura_do_no(no.direito)
    else:
        return 0
    
def rotacao_esquerda(r):
        y = r.direito
        f = y.esquerdo

        y.esquerdo = r
        r.direito = f

        r.altura = max(altura_do_no(r.esquerdo), altura_do_no(r.direito)) + 1
        y.altura = max(altura_do_no(y.esquerdo), altura_do_no(y.direito)) + 1

        return y
    
def rotacao_direita(r):
        y = r.esquerdo
        f = y.direito

        y.direito = r
        r.esquerdo = f

        r.altura = max(altura_do_no(r.esquerdo), altura_do_no(r.direito)) + 1
        y.altura = max(altura_do_no(y.esquerdo), altura_do_no(y.direito)) + 1

        return y

def rotacao_direita_esquerda(r):
    r.direito = rotacao_direita(r.direito)
    return rotacao_esquerda(r)

def rotacao_esquerda_direita(r):
    r.esquerdo = rotacao_esquerda(r.esquerdo)
    return rotacao_direita(r) 

def inserir(raiz, x):
    if raiz is None:  # Árvore vazia, cria um novo nó
        return novo_no(x)
    else:
        if x < raiz.valor:
            raiz.esquerdo = inserir(raiz.esquerdo, x)
        elif x > raiz.valor:
            raiz.direito = inserir(raiz.direito, x)
        else:
            print('\n Inserção não realizada!')  

    raiz.altura = max(altura_do_no(raiz.esquerdo), altura_do_no(raiz.direito)) + 1

    raiz = balancear(raiz)

    return raiz

def balancear(raiz):
    fb = fator_de_balanceamento(raiz)

    # Rotação à esquerda
    if fb < -1 and fator_de_balanceamento(raiz.direito) <= 0:
        raiz = rotacao_esquerda(raiz)

    # Rotação à direita
    elif fb > 1 and fator_de_balanceamento(raiz.esquerdo) >= 0:
        raiz = rotacao_direita(raiz)

    # Rotação dupla à esquerda
    elif fb > 1 and fator_de_balanceamento(raiz.esquerdo) < 0:
        raiz = rotacao_esquerda_direita(raiz)

    # Rotação dupla à direita
    elif fb < -1 and fator_de_balanceamento(raiz.direito) > 0:
        raiz = rotacao_direita_esquerda(raiz)

    return raiz

def remover(raiz, chave):
    if raiz is None:
        print('Valor não encontrado!')
        return None
    else:
        if raiz.valor == chave:
            # Remover nós folhas - nós sem filhos
            if raiz.esquerdo is None and raiz.direito is None:
                print('Elemento folha removido:', chave)
                return None
            else:
                # Remover nós que possuem 2 filhos
                if raiz.esquerdo is not None and raiz.direito is not None:
                    aux = raiz.esquerdo
                    while aux.direito is not None:
                        aux = aux.direito
                    raiz.valor, aux.valor = aux.valor, chave
                    print('Elemento trocado:', chave)
                    raiz.esquerdo = remover(raiz.esquerdo, chave)
                    return raiz
                else:
                    # Remover nós que possuem apenas 1 filho
                    if raiz.esquerdo is not None:
                        aux = raiz.esquerdo
                    else:
                        aux = raiz.direito
                    print('Elemento com 1 filho removido:', chave)
                    return aux
        else:
            if chave < raiz.valor:
                raiz.esquerdo = remover(raiz.esquerdo, chave)
            else:
                raiz.direito = remover(raiz.direito, chave)

        # Recalcula a altura de todos os nós entre a raiz e o novo nó inserido
        raiz.altura = max(altura_do_no(raiz.esquerdo), altura_do_no(raiz.direito)) + 1

        # Verifica a necessidade de rebalancear a árvore
        raiz = balancear(raiz)

        return raiz

def imprimir(raiz, nivel):
    if raiz:
        imprimir(raiz.direito, nivel + 1)
        print('\n')
        
        for i in range(nivel):
            print('\t', end='')
        
        print(raiz.valor)
        imprimir(raiz.esquerdo, nivel + 1)


def pesquisa(raiz, pesq):
    if raiz is not None:
        if raiz.valor == pesq:
            print("Nodo encontrado: ", raiz.valor)
        else:
            if pesq > raiz.valor:
                print("Pesquisando a direita.\n")
                pesquisa(raiz.direito, pesq)
            else:
                print("Pesquisando a esquerda.\n")
                pesquisa(raiz.esquerdo, pesq)
    else:
        print("Nodo não encontrado!\n")

if __name__ == "__main__":
    opcao = None
    valor = None
    raiz = None

    while opcao != 0:
        print("0 - Sair")
        print("1 - Inserir")
        print("2 - Remover")
        print("3 - Imprimir")
        print("4 - Procurar\n")
        opcao = int(input("Escolha uma opção: "))
        print('\n')

        if opcao == 0:
            print("Finalizando...")
        elif opcao == 1:
            valor = int(input("Digite o valor a ser inserido: "))
            raiz = inserir(raiz, valor)
        elif opcao == 2:
            valor = int(input("Digite o valor a ser removido: "))
            raiz = remover(raiz, valor)
        elif opcao == 3:
            imprimir(raiz, 1)
        elif opcao == 4:
            valor = int(input("Digite o valor a ser procurado: "))
            pesquisa(raiz, valor)
        else:
            print("Opção inválida!\n")



