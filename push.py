import git

def realizar_commit_push():
    # Inicializa o repositório Git existente
    repo = git.Repo()

    # Adiciona todos os arquivos alterados à área de preparação (staging area)
    repo.index.add("*")

    # Realiza o commit
    repo.index.commit("Atualiza página_perolas.html")

    # Realiza o push para o repositório remoto
    origin = repo.remote(name='origin')
    origin.push()

    # Informa que o commit e o push foram realizados com sucesso
    print("Commit e Push realizados com sucesso!")

# Chama a função para realizar o commit e o push
realizar_commit_push()
