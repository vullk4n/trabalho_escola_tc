#!/usr/bin/env python
def print_answers(answers):
    print(f"Respostas obtidas:    {answers}\n",
          f"    Menor valor:      {min(answers)}\n",
          f"    Maior valor:      {max(answers)}\n",
          f"    Média Aritmética: {sum(answers) / len(answers)}\n");
