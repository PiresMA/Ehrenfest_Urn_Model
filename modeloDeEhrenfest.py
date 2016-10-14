# ==========================================================#
# Simulacao Computacional do modelo de Ehrenfest
# ==========================================================#

# rota irreversivel para o equilibrio
"""
# Regras
** Temos duas caixas com um total de N bolas numeradas de 1 a N.
** Inicialmente algumas destas bolas estao na caixa 1 e o restante na caixa 2.
** Em cada experimento selecionamos uma bola ao acaso e a trocamos de caixa.
** Repita o procedimento sequencialmente

algoritmo:
Input:

* A cada iteracao:
    Selecionamos ao acaso um numero entre 1 e N
    Trocamos de caixa a bola selecionada

output:

"""

# importar biblioteca geradora de numeros aleatorios
import random
import numpy

# funcao que devolve a quantidade de vezes
# que o numero x aparece no vetor vec
def ocorrencias(vec, x):
    n = len(vec)
    cont = 0
    for k in range(n):
        if vec[k] == x:
            cont += 1
    return cont


# ###### caso simples I ########
"""
print("caso simples I")
N = 4
bolaNaUrna = [1, 1, 0, 0]  # 4 bolas
print(bolaNaUrna)
print("ne:", ocorrencias(bolaNaUrna, 0), "nd:", ocorrencias(bolaNaUrna, 1) )

# transferencia de 1 bola
sorteada = random.randint(0, N - 1)  # sortear uma bola
print("sorteada", sorteada)
print("antes da transferencia", bolaNaUrna[sorteada] )
if bolaNaUrna[sorteada] == 1:  # se a bola sorteada estah a direita
    bolaNaUrna[sorteada] = 0  # transferimos para a esquerda
else:  # a bola sorteada estah a esquerda
    bolaNaUrna[sorteada] = 1  # transferimos para a direita
print("depois da transferencia", bolaNaUrna[sorteada] )
print(bolaNaUrna)
print("ne:", ocorrencias(bolaNaUrna, 0), "nd:", ocorrencias(bolaNaUrna, 1) )

"""

"""

####### caso simples II ########
print("caso simples II")
# inicializacao: todas as bolas na direita
N = 10
posicoes = range(N)
bolaNaUrna = numpy.ones_like(posicoes)
# direto: bolaNaUrna = numpy.ones_like( range(N) )
# visualizar passo a passo
print("ne:", ocorrencias(bolaNaUrna, 0), "nd:", ocorrencias(bolaNaUrna, 1) )

# transferencia de 1 bola
sorteada = random.randint(0,N-1)
if bolaNaUrna[sorteada]==1:
    bolaNaUrna[sorteada]=0
else:
    bolaNaUrna[sorteada]=1
print("ne:", ocorrencias(bolaNaUrna, 0), "nd:", ocorrencias(bolaNaUrna, 1) )
"""

####### caso simples III ########
print("caso simples III")

# inicializacao: ne bolas na direita de um total de N
def inicializacao(N, ne):
    posicoes = range(N)
    for k in range(0,ne):
        posicoes[k] = 0
    for k in range(ne,N):
        posicoes[k] = 1
    urna_inicial=posicoes
    return urna_inicial


# funcao para transferencia de 1 bola
def transferenciaDeUmabola(vetor_urna):
    numeroBolas = len(vetor_urna)
    sorteada = random.randint(0,numeroBolas-1)
    if vetor_urna[sorteada]==1:
        vetor_urna[sorteada]=0
    else:
        vetor_urna[sorteada]=1
    return vetor_urna


# parametros
N = 100; ne = N; tf = 500

# vetores para guardar resultados
vec_ne = []
vec_nd = []
vec_eq = []

# inicializacao
bolaNaUrna = inicializacao(N,ne)
print("t:",0 ,"ne:", ocorrencias(bolaNaUrna, 0), "nd:", ocorrencias(bolaNaUrna, 1) )
vec_ne.append( ocorrencias(bolaNaUrna, 0) )
vec_nd.append( ocorrencias(bolaNaUrna, 1) )
vec_eq.append(N/2)

# transferencia de bolas durante tf+1 instantes
for t in range(1,tf):
    bolaNaUrna = transferenciaDeUmabola(bolaNaUrna)
    vec_ne.append( ocorrencias(bolaNaUrna, 0) )
    vec_nd.append( ocorrencias(bolaNaUrna, 1) )
    vec_eq.append(N/2)



# salvar
numpy.savetxt( "ne.txt" , vec_ne)
numpy.savetxt( "nd.txt" , vec_nd)
numpy.savetxt( "eq.txt" , vec_eq)
