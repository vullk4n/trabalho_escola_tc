#!/usr/bin/env python

def print_answers(answers):
    print(f"Respostas obtidas:    {answers}\n",
          f"    Menor valor:      {min(answers)}\n",
          f"    Maior valor:      {max(answers)}\n",
          f"    Média Aritmética: {sum(answers) / len(answers)}\n");


print("Equipe Segurança: ",
      "Você se sente segura quando sai e quando está em casa?");
answers = [1, 2, 6, 8, 1, 2, 8, 2, 8, 1];
print_answers(answers);

print("Que nota de 0 a 10 daria para a segurança do Estado?");
answers = [4,5,6,2,3,2,4,5,3,4];
print_answers(answers);

print("Que nota de 0 a 10 daria para a segurança do bairro?");
answers = [8,5,6,3,2,3,4,4,6,1]

print_answers(answers);

answers.sort()
print("Respostas Ordenadas:\n", f"{answers}\n");

print("Distribuiçao de frequencia:\n")

for rating in answers:
    print(f"{rating} -> {answers.count(rating)}");

print("\nFim da Análise de dados\n");

print("Quais foram os meses que mais tiveram furtos em 2020?\n"
    "\noutubro", "janeiro","fevereiro" ,"dezembro" ,"junho");

answers = {
        "jan": 2,
        "feb": 3,
        "jun": 5,
        "oct": 1,
        "dec": 4,
};

if answers["oct"] == 1:
    print(" \n é outubro");
else:
    print("n é outubro");

print ('\nQuais regiões do estado do Ceará tiveram mais casos'
        'de crimes letais internacionais-CVLI, em 2020?\n'
        '\nregiãoM' , 'fortaleza', 'interiorS')

answers = {
        "regiãoM" :1,
        "fortaleza" :2,
        "interiorS" :3
};

if answers["fortaleza"] == 2:
     print("\n é fortaleza\n")
else:
     print("\n n é fortaleza")

print("\nQuais foram os 5 AIS-Área Integrada de Segurança,"
    "que mais tiveram crimes sexuais cometidos na capital no total durante 2020?")

answers = {
        "AIS2" :79,
        "AIS3" :67,
        "AIS6" :97,
        "AIS7" :48,
        "AIS9" :67
};
if answers["AIS7"] == 48:
     print("\nAIS7 é 48")
else:
     print("\nAIS7 n é 48")

