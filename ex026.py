frase = input('Digite uma frase: ').strip()

print(f'\nAparece a letra "A" {frase.count("A")} vezes'
      f'\nAparece pela primeira vez a letra "A" na posição {frase.find("A")}'
      f'\nAparece pela ultima vez a letra "A" na posição {frase.find("A",-1)}')
