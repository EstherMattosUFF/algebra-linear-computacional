"""
Aula 2 - Conjuntos e Funções em Python
--------------------------------------
Este script mostra como representar e manipular conjuntos e funções
em Python, conectando conceitos matemáticos à prática de programação.
"""

# ==========================================================
# 1. Definição de Conjuntos
# ==========================================================
def definir_conjuntos():
    """
    Cria dois conjuntos numéricos a partir de intervalos.
    - s = conjunto de inteiros não-negativos no intervalo [-10, 10]
    - a = conjunto de inteiros no intervalo [5, 15)

    Retorna:
        (set, set): dois conjuntos s e a
    """
    z = range(-10, 11)
    s = {x for x in z if x >= 0}  # Usamos set comprehension
    w = range(5, 15)
    a = {x for x in w}
    return s, a


# ==========================================================
# 2. Operações com Conjuntos
# ==========================================================
def operacoes_conjuntos(s, a):
    """
    Aplica operações matemáticas com conjuntos:
    - União (∪)
    - Diferença (\)
    - Interseção (∩)

    Args:
        s (set): conjunto de inteiros
        a (set): conjunto de inteiros

    Retorna:
        dict: dicionário com os resultados das operações
    """
    return {
        "uniao": s.union(a),           # União
        "diferenca": s.difference(a),  # Diferença
        "intersecao": s.intersection(a)  # Interseção
    }


# ==========================================================
# 3. Produto Cartesiano
# ==========================================================
def produto_cartesiano(s, a):
    """
    Calcula o produto cartesiano entre dois conjuntos:
    A × B = {(x, y) | x ∈ A, y ∈ B}

    Args:
        s (set): conjunto de inteiros
        a (set): conjunto de inteiros

    Retorna:
        set: conjunto de tuplas representando o produto cartesiano
    """
    return {(x, y) for x in s for y in a}


# ==========================================================
# 4. Função de Heaviside (Função Degrau)
# ==========================================================
def heaviside(x):
    """
    Implementa a Função de Heaviside (degrau):
        H(x) = 0    se x < 0
        H(x) = 0.5  se x = 0
        H(x) = 1    se x > 0

    Args:
        x (float): valor de entrada

    Retorna:
        float: valor da função degrau em x
    """
    if x < 0:
        return 0
    elif x == 0:
        return 0.5
    else:
        return 1


# ==========================================================
# 5. Composição de Funções
# ==========================================================
def f(x):
    """Exemplo de função f: f(x) = x²"""
    return x ** 2

def h(y):
    """Exemplo de função h: h(y) = y + 1"""
    return y + 1

def g(x):
    """
    Função composta g = h ∘ f:
    g(x) = h(f(x)) = (x²) + 1
    """
    return h(f(x))


# ==========================================================
# Execução e Testes
# ==========================================================
if __name__ == "__main__":
    # 1. Definição de conjuntos
    s, a = definir_conjuntos()
    print("Conjunto s:", s)
    print("Conjunto a:", a)

    # 2. Operações com conjuntos
    resultados = operacoes_conjuntos(s, a)
    print("\nUnião:", resultados["uniao"])
    print("Diferença:", resultados["diferenca"])
    print("Interseção:", resultados["intersecao"])

    # 3. Produto cartesiano
    print("\nProduto cartesiano (exemplo):", list(produto_cartesiano({1, 2}, {3, 4})))

    # 4. Função de Heaviside
    print("\nHeaviside(-10) =", heaviside(-10))
    print("Heaviside(0) =", heaviside(0))
    print("Heaviside(10) =", heaviside(10))

    # 5. Composição de funções
    print("\nFunção composta g(x) = h(f(x))")
    for x in range(-2, 3):
        print(f"g({x}) = {g(x)}")



# Função - Teoria vs Prática - Problema computacional
# Especificações de entrada e saída que um procedimento será exigido a satisfazer. 
# Exemplo: Fatoração de inteiros
# Entrada: um número inteiro n maior que 1
# Saída um para de inteiros maiores que 1 tal que x * y = n

def fatoracao_inteiros(x):
    if x < 0:
        return "X deve ser um valor positivo"
    n = 100
    y = n / x
    return x, y
print(fatoracao_inteiros(10))
