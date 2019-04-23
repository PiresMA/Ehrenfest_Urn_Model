# ==========================================================#
#  Simulacao Computacional do modelo de Ehrenfest:          #
#  rota irreversivel para o equilibrio                      #
# ==========================================================#

#

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

output: 3 arquivos txt

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
            cont += 1 # cont=cont+1
    return cont


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
N = 1000; ne = N; tf = 5000

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

