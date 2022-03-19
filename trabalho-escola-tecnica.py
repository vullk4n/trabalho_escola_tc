#!/usr/bin/env python

print("Equipe Segurança")

print("\nVocê se sente segura quando sai e quando esta em casa?")
SE=[1,2,6,8,1,2,8,2,8,1]
print("\nResposta obtidas: ",SE)
print("\nMenor valor:", min(SE) )
print("Maior valor:" , max(SE) )
print("media valores:", sum(SE)/len(SE) )

print("\nQue nota de 0 a 10 daria para a segurança do estado?")
SE=[4,5,6,2,3,2,4,5,3,4]
print("\nResposta obtidas: ",SE)
print("\nMenor valor:", min(SE) )
print("Maior valor:" , max(SE) )
print("media valores:", sum(SE)/len(SE) )

print("\nQue nota de 0 a 10 daria para a segurança do bairro?")
SE=[8,5,6,3,2,3,4,4,6,1]
print("\nResposta obtidas: ",SE)
print("\nMenor valor:", min(SE) )
print("Maior valor:" , max(SE) )
print("media valores:", sum(SE)/len(SE) )
(SE)
print("\nRespostas Ordenadas")
SE.sort ()
print(SE)
print("\nDistribuiçao de frequencia:")
for nota in range (0,10+1):
    print( nota, " -> ",SE.count(nota) )
print("Fim da Analise de dados")


