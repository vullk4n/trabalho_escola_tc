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

print('\nQuais foram os meses que mais tiveram furtos em 2020?')
print ("\noutubro", "janeiro","fevereiro" ,"dezembro" ,"junho")
outubro =[1]
janeiro =[2]
fevereiro =[3]
dezembro =[4]
junho=[5]
SE=(outubro,janeiro,fevereiro,dezembro,junho)

if len(outubro) ==1:
      print("\n Foi outubro")
else:
      print(" \n N foi outubro")

print ('\nQuais regiões do estado do Ceará tiveram mais casos'
    'de crimes letais internacionais-CVLI, em 2020?')
print ('\nregiãoM' , 'fortaleza', 'interiorS')
regiãoM =[1]
fortaleza =[2]
interiorS =[3]
SE=('regiãoM','fortaleza', 'interiorS')

if len(fortaleza) ==2:
     print(" n é fortaleza")
else:
     print("\n é fortaleza")

print("\nQuais foram os 5 AIS-Área Integrada de Segurança,"
    "que mais tiveram crimes sexuais cometidos na capital no total durante 2020?")
AIS2 =[79]
AIS3 =[67]
AIS6 =[97]
AIS7 =[48]
AIS9 =[67]
SE=['AIS2', 'AIS3', 'AIS6', 'AIS7', 'AIS9']

if len(AIS7) ==48:
     print("\nAIS7 não é 48")
else:
     print("\nAIS7 é 48")

