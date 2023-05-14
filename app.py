import datetime
import os
import locale

def criar_pagina_perolas(perolas):
    # Verifica se o arquivo já existe
    arquivo_existente = os.path.isfile('index.html')

    # Abre o arquivo HTML no modo de adição se já existir, caso contrário, cria um novo arquivo
    with open('index.html', 'a' if arquivo_existente else 'w') as arquivo:
        # Verifica se o arquivo é novo e escreve o cabeçalho do HTML
        if not arquivo_existente:
            arquivo.write('<html>\n')
            arquivo.write('<head>\n')
            arquivo.write('<title>Página de Pérolas</title>\n')
            arquivo.write('<style>\n')

            # Define o tema escuro
            arquivo.write('body {\n')
            arquivo.write('    background-color: #1f1f1f;\n')
            arquivo.write('    color: #fff;\n')
            arquivo.write('    text-align: center;\n')
            arquivo.write('}\n')

            arquivo.write('h1 {\n')
            arquivo.write('    color: #fff;\n')
            arquivo.write('}\n')

            arquivo.write('p {\n')
            arquivo.write('    border-bottom: 1px solid #fff;\n')
            arquivo.write('    padding-bottom: 10px;\n')
            arquivo.write('    text-align: center;\n')
            arquivo.write('}\n')

            arquivo.write('.perola {\n')
            arquivo.write('    font-weight: bold;\n')
            arquivo.write('    font-style: italic;\n')
            arquivo.write('}\n')

            arquivo.write('.autor, .data {\n')
            arquivo.write('    font-size: 12px;\n')
            arquivo.write('    font-style: italic;\n')
            arquivo.write('}\n')

            arquivo.write('</style>\n')
            arquivo.write('</head>\n')
            arquivo.write('<body>\n')
            arquivo.write('<h1>Pérolas</h1>\n')

        # Escreve cada pérola no arquivo
        for perola in perolas:
            arquivo.write('<p>\n')
            arquivo.write('<span class="perola">{}</span>\n'.format(perola['frase']))
            arquivo.write('<br>\n')
            arquivo.write('<span class="autor">Autor: {}</span>\n'.format(perola['autor']))
            arquivo.write('<br>\n')
            arquivo.write('<span class="data">Data: {}</span>\n'.format(perola['data']))
            arquivo.write('</p>\n')

        # Fecha as tags HTML se o arquivo é novo
        if not arquivo_existente:
            arquivo.write('</body>\n')
            arquivo.write('</html>\n')

# Configura o local para PT-BR
locale.setlocale(locale.LC_TIME, 'pt_BR.utf8')

# Exemplo de uso
perolas = []

# Solicita as pérolas ao usuário
# Solicita as pérolas ao usuário
# Solicita as pérolas ao usuário
while True:
    frase = input("Digite a frase: ")
    autor = input("Digite o autor: ")
    data = datetime.date.today().strftime("%d de %B de %Y")
    acao = input("Finalizar (F) ou Inserir outra (I): ")

    perolas.append({
        'frase': frase,
        'autor': autor,
        'data': data
    })

    if acao.lower() == 'f':
        break
    elif acao.lower() == 'i':
        continue

# Chama a função para criar a página de pérolas
criar_pagina_perolas(perolas)
