import random
import time
from math import *
from numpy import *

#--------------------------FUNÇÕES PARA OS TESTES--------------------------------
def matriz_Wa():
    """ a) n = m = 64, Wi,i = 2, i = 1, n, Wi,j = 1, se |i − j| = 1 e Wi,j = 0, se |i − j| > 1. Use b(i) = 1, i = 1, n"""
    matriz_Wa = []
    for i in range(64):
        linha = []
        for j in range(64):
            if i - j == 0:
                linha.append(2)
            elif i - j == 1 or i - j == -1:
                linha.append(1)
            else: #|i - j| > 1
                linha.append(0)
        matriz_Wa.append(linha)
    return matriz_Wa

def matriz_Wb():
    """b) n = 20, m = 17, Wi,j = 1/(i + j − 1), se |i − j| ≤ 4 e Wi,j = 0, se |i − j| > 4. Use b(i) = i, i = 1, n"""
    matriz_Wb = []
    for i in range(1,21):
        linha = []
        for j in range(1,18):
            if -4 <= i - j <= 4:
                den = i+j-1
                linha.append((1/den))
                
            else: #|i - j| > 4
                linha.append(0)

        matriz_Wb.append(linha)
    return matriz_Wb

def matriz_Aa():
    """A(i, 1) = 1, A(i, 2) = i, A(i, 3) = 2i − 1, i = 1, n.
"""
    matriz_Aa = []
    for i in range(1,65):
        linha = []
        for j in range(1,4):
            if j == 1:
                linha.append(1)
            elif j == 2:
                linha.append(i)
            else: #j == 3
                linha.append(2*i-1)
        matriz_Aa.append(linha)
        
    return matriz_Aa

def matriz_Ab():
    """A(i, 1) = 1, A(i, 2) = i, A(i, 3) = 2i − 1, i = 1, n."""
    matriz_Ab = []
    for i in range(1,21):
        linha = []
        for j in range(1,4):
            if j == 1:
                linha.append(1)
            elif j == 2:
                linha.append(i)
            else: #j == 3
                linha.append(2*i-1)
        matriz_Ab.append(linha)

    return matriz_Ab

#----------------------CLASSIFICADORES------------------------------------------------
def classif_W0(ndig_treino,p):
    A=open('train_dig0.txt').read()
    A=[item.split() for item in A.split('\n')[:]]
    for i in range(len(A)):
        A[i]=[float(t) for t in A[i]]
        A[i]=A[i][0:ndig_treino]
        for j in range(len(A[i])):
            A[i][j]=A[i][j]/255

    W_random=[[float(random.randint(0,255)) for j in range(p)] for i in range(len(A))]
    Wd,H=NMF(A,W_random,len(A[0]))
    
    return Wd

def classif_W1(ndig_treino,p):
    A=open('train_dig1.txt').read()
    A=[item.split() for item in A.split('\n')[:]]
    for i in range(len(A)):
        A[i]=[float(t) for t in A[i]]
        A[i]=A[i][0:ndig_treino]
        for j in range(len(A[i])):
            A[i][j]=A[i][j]/255

    W_random=[[float(random.randint(0,255)) for j in range(p)] for i in range(len(A))]
    Wd,H=NMF(A,W_random,len(A[0]))

    return Wd

def classif_W2(ndig_treino,p):
    A=open('train_dig2.txt').read()
    A=[item.split() for item in A.split('\n')[:]]
    for i in range(len(A)):
        A[i]=[float(t) for t in A[i]]
        A[i]=A[i][0:ndig_treino]
        for j in range(len(A[i])):
            A[i][j]=A[i][j]/255
            
    W_random=[[float(random.randint(0,255)) for j in range(p)] for i in range(len(A))]
    Wd,H=NMF(A,W_random,len(A[0]))

    return Wd

def classif_W3(ndig_treino,p):
    A=open('train_dig3.txt').read()
    A=[item.split() for item in A.split('\n')[:]]
    for i in range(len(A)):
        A[i]=[float(t) for t in A[i]]
        A[i]=A[i][0:ndig_treino]
        for j in range(len(A[i])):
            A[i][j]=A[i][j]/255
            
    W_random=[[float(random.randint(0,255)) for j in range(p)] for i in range(len(A))]
    Wd,H=NMF(A,W_random,len(A[0]))

    return Wd

def classif_W4(ndig_treino,p):
    A=open('train_dig4.txt').read()
    A=[item.split() for item in A.split('\n')[:]]
    for i in range(len(A)):
        A[i]=[float(t) for t in A[i]]
        A[i]=A[i][0:ndig_treino]
        for j in range(len(A[i])):
            A[i][j]=A[i][j]/255
  
    W_random=[[float(random.randint(0,255)) for j in range(p)] for i in range(len(A))]
    Wd,H=NMF(A,W_random,len(A[0]))

    return Wd

def classif_W5(ndig_treino,p):
    A=open('train_dig5.txt').read()
    A=[item.split() for item in A.split('\n')[:]]
    for i in range(len(A)):
        A[i]=[float(t) for t in A[i]]
        A[i]=A[i][0:ndig_treino]
        for j in range(len(A[i])):
            A[i][j]=A[i][j]/255
            
    W_random=[[float(random.randint(0,255)) for j in range(p)] for i in range(len(A))]
    Wd,H=NMF(A,W_random,len(A[0]))

    return Wd

def classif_W6(ndig_treino,p):
    A=open('train_dig6.txt').read()
    A=[item.split() for item in A.split('\n')[:]]
    for i in range(len(A)):
        A[i]=[float(t) for t in A[i]]
        A[i]=A[i][0:ndig_treino]
        for j in range(len(A[i])):
            A[i][j]=A[i][j]/255
            
    W_random=[[float(random.randint(0,255)) for j in range(p)] for i in range(len(A))]
    Wd,H=NMF(A,W_random,len(A[0]))

    return Wd

def classif_W7(ndig_treino,p):
    A=open('train_dig7.txt').read()
    A=[item.split() for item in A.split('\n')[:]]
    for i in range(len(A)):
        A[i]=[float(t) for t in A[i]]
        A[i]=A[i][0:ndig_treino]
        for j in range(len(A[i])):
            A[i][j]=A[i][j]/255

    W_random=[[float(random.randint(0,255)) for j in range(p)] for i in range(len(A))]
    Wd,H=NMF(A,W_random,len(A[0]))

    return Wd

def classif_W8(ndig_treino,p):
    A=open('train_dig8.txt').read()
    A=[item.split() for item in A.split('\n')[:]]
    for i in range(len(A)):
        A[i]=[float(t) for t in A[i]]
        A[i]=A[i][0:ndig_treino]
        for j in range(len(A[i])):
            A[i][j]=A[i][j]/255

    W_random=[[float(random.randint(0,255)) for j in range(p)] for i in range(len(A))]
    Wd,H=NMF(A,W_random,len(A[0]))

    return Wd

def classif_W9(ndig_treino,p):
    A=open('train_dig9.txt').read()
    A=[item.split() for item in A.split('\n')[:]]
    for i in range(len(A)):
        A[i]=[float(t) for t in A[i]]
        A[i]=A[i][0:ndig_treino]
        for j in range(len(A[i])):
            A[i][j]=A[i][j]/255

    W_random=[[float(random.randint(0,255)) for j in range(p)] for i in range(len(A))]
    Wd,H=NMF(A,W_random,len(A[0]))

    return Wd

#-------------------------------------------------------------------------------------   
def compara(vet):
    """Retorna a porcentagem de acertos na classificação"""
    V=open('test_index.txt').read()
    V=[item.split() for item in V.split('\n')[:]]
    for i in range(len(V)):
        V[i]=[float(t) for t in V[i]]
        V[i]=V[i][0:10000]
        V[i]=V[i][0]
        
    acertos=0    
    for v in range(len(V)):
        if V[v]==vet[v]:
            acertos+=1
    
    porcento=acertos/100
    
    return porcento


def classificadora(e0,e1,e2,e3,e4,e5,e6,e7,e8,e9):
    """Dado os vetores ej de tamanho n_teste em q cada ej possui a norma euclidiana respectiva a uma imagem j de A
    classifica-se a j-ésima imagem de A para o menor ej"""
    classification=[]
    C=[e0,e1,e2,e3,e4,e5,e6,e7,e8,e9]
    Ct=[list(i) for i in zip(*C)]

    print('lenCt',len(Ct),'lenCt[0]',len(Ct[0]))
    num=[0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]
    for j in range(len(Ct)):
        ind=Ct[j].index(min(Ct[j]))
        classfication.append(num[ind])
        
    print('len-classification',len(classification))
    return classification


def norma_euclidiana(M):
    """Calcula a norma euclidiana para cada coluna da matriz e retorna um vetor com os erros"""
    Mt=[list(i) for i in zip(*M)]
    v=[]
    for i in range(len(Mt)):
        soma=0
        for j in range(len(Mt[0])):
            soma+=Mt[i][j]**2
        e=sqrt(soma)
        v.append(e)
        
    return v

def normal(M):
    """Normaliza matriz"""
    Mt=[list(i) for i in zip(*M)]
    for i in range(len(Mt)):
        soma=0
        for j in range(len(Mt[0])):
            soma += Mt[i][j]**2
        r=sqrt(soma)
        if r!=0.0:
            for k in range(len(Mt[0])):
                Mt[i][k]=Mt[i][k]/r

    M_normal=[list(i) for i in zip(*Mt)]
        
    return M_normal

def Frobenius(E):
    """calcula o erro de A-WH"""
    soma=0
    for i in range(len(E)):
        for j in range(len(E[0])):
            soma += E[i][j]**2

    E=sqrt(soma)
    
    return E

def NMF(A,W,m):
    """Non-negative factorization; usa o MMQ alternado para fatoração não negativa"""
    W=normal(W)

    #var's aux p/ o while
    itmax,F,e=0,100000.0,1.0
    while e>0.00001:
        Ht=QR_factorization(W,A,m)
        H=[list(i) for i in zip(*Ht)]
        
        #Alterna o MMQ
        At=[list(i) for i in zip(*A)]
        W=QR_factorization(Ht,At,len(At[0]))

        E=subtract(A,dot(W,H))
        E=E.tolist()
        E=Frobenius(E)
        
        e=F-E
        F=E
        if itmax==100:
            break
        itmax+=1

    return W,H        

def rot_givens(W,n,m,p,i,j,k,c,s):
    """Se wj,k!=0 aplique Q(i, j, θ)"""
    for col in range(k,p+m):
        aux=c*W[i][col]-s*W[j][col]
        W[j][col]=s*W[i][col]+c*W[j][col]
        W[i][col]=aux
    
    return W

def QR_factorization(W,A,m):
    
    """Dado o sist. WH=A, resolve m sist. lineares"""
    if m>1:
        #concatenagem de W|A p/ aplicar as rot simultaneamente em W e A
        n,p= len(W), len(W[0])
        for t in range(n):
            W[t]=W[t]+A[t]

        #define seno e cosseno
        for k in range(0,p):
            for j in range(n-1,k,-1):
                i=j-1
                if W[j][k]!=0 and abs(W[i][k])>abs(W[j][k]):
                    t=-(W[j][k]/W[i][k])
                    c=1/sqrt(1+t**2)
                    s=c*t
                    W=rot_givens(W,n,m,p,i,j,k,c,s)
                if W[j][k]!=0 and abs(W[i][k])<abs(W[j][k]):
                    t=-(W[i][k]/W[j][k])
                    s=1/sqrt(1+t**2)
                    c=s*t
                    W=rot_givens(W,n,m,p,i,j,k,c,s)

        #[A] redefinida com as rot givens
        A=[]
        for u in range(len(W)):
            A.append(W[u][p:])
            W[u]=W[u][:p]

        #Solução dos m sist. lineares
        At=[list(i) for i in zip(*A)]
        Ht=[]
        for u in range(len(At)):
            b=At[u]
            X=[b[p-1]/W[p-1][p-1]]
            for i in range(p-2,-1,-1):
                for k in range(len(W[0])-1,i,-1):
                    a=W[i][k:p]
                soma=dot(a,X)
                x=(b[i]-soma)/W[i][i]
                X=[x]+X

            #hi,j = max{0, hi,j}
            for ij in range(len(X)):
                if X[ij]<0.0:
                    X[ij]=0.0
            
            Ht.append(X)
        
        return Ht
        
    else:
        """Dado o sistema Wx=b, resolve Rx=Qt*b, em que m=1 """
    
        #concatenação W|b p/ aplicar as rot em W e b simultaneamente
        b=A
        n, p= len(W), len(W[0])
        Wt=[list(i) for i in zip(*W)]
        Wt.append(b)
        W=[list(i) for i in zip(*Wt)]

    
        #define seno e cosseno
        for k in range(0,p):
            for j in range(n-1,k,-1):
                i=j-1
                if W[j][k]!=0 and abs(W[i][k])>abs(W[j][k]):
                    t=-(W[j][k]/W[i][k])
                    c=1/sqrt(1+t**2)
                    s=c*t
                    W=rot_givens(W,n,1,p,i,j,k,c,s)
                if W[j][k]!=0 and abs(W[i][k])<abs(W[j][k]):
                    t=-(W[i][k]/W[j][k])
                    s=1/sqrt(1+t**2)
                    c=s*t
                    W=rot_givens(W,n,1,p,i,j,k,c,s)
                

        #separa b de W
        Wt=[list(i) for i in zip(*W)]
        b=Wt[-1]
        Wt=Wt[:len(Wt)-1]
        W=[list(i) for i in zip(*Wt)]


        #Solução do sist. linear
        X=[b[p-1]/W[p-1][p-1]]
        for i in range(p-2,-1,-1):
            for k in range(len(W[0])-1,i,-1):
                a=W[i][k:p]
            soma=dot(a,X)
            x=(b[i]-soma)/W[i][i]
            X=[x]+X

        return X
            

#----------------------------------------------------------------------------

def main():
    print('Olá. Seja bem-vindo ao Machine learning')
    tarefa=input('Digite a tarefa(tarefa 1, tarefa 2, ML): ')
    if tarefa=='tarefa 1':
        print('#####Teste; Rot-givens, itens a e b#####')
        print('')
        
        b=[1 for i in range(64)]
        W=matriz_Wa()
        x=QR_factorization(W,b,1)
        print('Vetor resultante, ítem a')
        for r in range(len(x)):
            x[r]=round(x[r],3)
            
        x=matrix(x)
        print(x)
        print(' ')
        
        b=[float(1+i) for i in range(20)]
        W=matriz_Wb()
        x=QR_factorization(W,b,1)
        print('Vetor resultante, ítem b')
        for r in range(len(x)):
            x[r]=round(x[r],3)
        x=matrix(x)
        print(x)
        print(' ')
        
        print('#####Teste; Vários sistemas simultâneos, itens a e b#####')
        W,A=matriz_Wa(),matriz_Aa()
        m=len(A[0])
        print('---Vetores h1, h2 e h3; ítem a--- ')
        Ht=QR_factorization(W,A,m)  
        H=matrix(Ht).T
        print(H)
        print(' ')

        print('---Vetores h1, h2, e h3; ítem b--- ')
        W,A=matriz_Wb(),matriz_Ab()
        m=len(A[0])
        Ht=QR_factorization(W,A,m)
        H=matrix(Ht).T
        print(H)
        
    if tarefa=='tarefa 2':
        A=[[0.3,0.6,0.0],[0.5,0.0,1.0],[0.4,0.8,0.0]]
        W_random=[[float(random.randint(0,255)) for j in range(2)] for i in range(len(A))]
        W,H=NMF(A,W_random,3)
        WH=dot(W,H)
        print('')
        print('Aproximação exata')
        print(WH)

    if tarefa=='ML':
        ndig_treino=int(input('Insira o número de dígitos(100,1000,4000) p/ os classificadores do ML: '))
        p=int(input('Insira o valor de p(5,10,15):'))
        n_test=int(input('Insira o números de imagens a serem classificadas(10000): '))
        
        #matriz de dígitos testes
        A=open('test_images.txt').read()
        A=[item.split() for item in A.split('\n')[:]]
        for i in range(len(A)):
            A[i]=[float(t) for t in A[i]]
            A[i]=A[i][0:n_test]
            for j in range(len(A[i])):
                A[i][j]=A[i][j]/255        

        m=len(A[0])
        begin=time.time()
        #fase de treinamento

        #Dígito 0
        W0=classif_W0(ndig_treino,p)
        W,H=NMF(A,W0,m)
        WH=dot(W,H) 
        E=subtract(A,WH)
        e0=norma_euclidiana(E)

        end0=time.time()
        print('1º classificação: W0',round(end0-begin,0))
        
        #D1
        W1=classif_W1(ndig_treino,p)
        W,H=NMF(A,W1,m)
        WH=dot(W,H)
        end=time.time() 
        E=subtract(A,WH)
        e1=norma_euclidiana(E)  
        #D2
        W2=classif_W2(ndig_treino,p)
        W,H=NMF(A,W2,m)
        W0H=dot(W,H)
        E=subtract(A,WH)
        e2=norma_euclidiana(E)
        #D3
        W3=classif_W3(ndig_treino,p)
        W,H=NMF(A,W3,m)
        W0H=dot(W,H)
        E=subtract(A,WH)
        e3=norma_euclidiana(E)
        #D4
        W4=classif_W4(ndig_treino,p)
        W,H=NMF(A,W4,m)
        W0H=dot(W,H)
        E=subtract(A,WH)
        e4=norma_euclidiana(E)  
        #D5
        W5=classif_W5(ndig_treino,p)
        W,H=NMF(A,W5,m)
        W0H=dot(W,H)
        E=subtract(A,WH)
        e5=norma_euclidiana(E) 
        #D6
        W6=classif_W6(ndig_treino,p)
        W,H=NMF(A,W6,m)
        W0H=dot(W,H)
        E=subtract(A,WH)
        e6=norma_euclidiana(E) 
        #D7  
        W7=classif_W7(ndig_treino,p)
        W,H=NMF(A,W7,m)
        W0H=dot(W,H)   
        E=subtract(A,WH)
        e7=norma_euclidiana(E)
        #D8
        W8=classif_W8(ndig_treino,p)
        W,H=NMF(A,W8,m)
        W0H=dot(W,H)
        E=subtract(A,WH)
        e8=norma_euclidiana(E)   
        #D9
        W9=classif_W9(ndig_treino,p)
        W,H=NMF(A,W9,m)
        W0H=dot(W,H)
        E=subtract(A,WH)
        e9=norma_euclidiana(E)

        end=time.time()
        
        #fase de classificações
        ML=classificadora(e0,e1,e2,e3,e4,e5,e6,e7,e8,e9)
        P=compara(ML)
        print(P,'% de acerto')
        print('Tempo de execução',round(end-begin,0),'s')
        
main()    
