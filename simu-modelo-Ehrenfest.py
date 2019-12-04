# ==========================================================#
#  Simulacao Computacional do modelo de Ehrenfest:          #
#  rota irreversivel para o equilibrio                      #
# ==========================================================#



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
import numpy as np
import random as rd
import matplotlib.pyplot as plt


# funcao que devolve a quantidade de vezes
# que o numero x aparece no vetor vec
def ocorrencias(vec, x):
    return float(sum(vec==x))

# inicializacao: ne bolas na esquerda de um total de N
def inicializacao(N, ne):        
    bolas0 = np.zeros( ne, dtype=int)
    bolas1 = np.ones(  N-ne, dtype=int)
    urna_inicial = np.concatenate( (bolas0,bolas1), axis=None)
    #np.random.shuffle(full)    
    return urna_inicial

# funcao para transferencia de 1 bola
def transferenciaDeUmabola(vetor_urna):
    numeroBolas = len(vetor_urna)    
    sorteada    = rd.randint(0,numeroBolas-1)
    
    if vetor_urna[sorteada]==1: vetor_urna[sorteada]=0        
    else: vetor_urna[sorteada]=1
                
    return vetor_urna




# parametros
N  = 100; 
ne = N; 
tf = 5*N


# inicializacao
bolaNaUrna = inicializacao(N,ne)

print("t:",0 ,"ne:", ocorrencias(bolaNaUrna, 0), "nd:", ocorrencias(bolaNaUrna, 1) )

# vetores para guardar resultados
vec_ne = [ ocorrencias(bolaNaUrna, 0) ]
vec_nd = [ ocorrencias(bolaNaUrna, 1) ]
vec_eq = [ N/2 ]

print(vec_eq)

# transferencia de bolas durante tf+1 instantes
for t in range(1,tf):
    bolaNaUrna = transferenciaDeUmabola(bolaNaUrna)
    vec_ne.append( ocorrencias(bolaNaUrna, 0) )
    vec_nd.append( ocorrencias(bolaNaUrna, 1) )
    vec_eq.append(N/2)
    
    
    
plt.plot(vec_ne,'s',label='$n_{esquerda}$')
plt.plot(vec_nd,'o',label='$n_{direita}$')
plt.ylabel('$n_{bolas}$',fontsize=16)
plt.xlabel('tempo (u.a.t.)',fontsize=16)
plt.title('Urnas de Ehrenfest: Rota Irreversivel para o Equilibrio')
plt.axhline(y=float(N)/2, color='k', linestyle='--',label='$n_{equilibrio}$')
plt.legend()    


# salvar
np.savetxt( "ne.txt" , vec_ne)
np.savetxt( "nd.txt" , vec_nd)
np.savetxt( "eq.txt" , vec_eq)
