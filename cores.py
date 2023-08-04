tabela = {'cores': {'branco': 30,
                    'vermelho': 31,
                    'verde': 32,
                    'amarelo': 33,
                    'azul': 34,
                    'lilas': 35,
                    'ciano': 36,
                    'cinza': 37},
          'estilo': {'normal': 0,
                     'negrito': 1,
                     'sublinhado': 4,
                     'invertido': 7}}

text = input('Texto para ser formatado: ')
tex_color = input(f'Cor do texto {[k for k in tabela["cores"]]}: ')
bottom_color = input(f'Cor do fundo {[k for k in tabela["cores"]]}: ')
style = input(f'Estilo {[k for k in tabela["estilo"]]}: ')

print(f'\033[{tabela["estilo"][style]};{tabela["cores"][tex_color]};{tabela["cores"][bottom_color]+10}m{text}\033[m')
