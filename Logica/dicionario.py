gerenciador_tarefas = {
    "Andrey": {
        "tarefa": "Lavar Louça",
        "status": "Concluído"
    },
    "Leonardo": {
        "tarefa": "Varrer a casa",
        "status": "Em andamento"
    }
}


gerenciador_tarefas["Rosane"] = {
    "tarefa": "Passar roupa",
    "status": "Pendente"
}
for nome, tarefa in gerenciador_tarefas.items():
    print(f"{nome}: {tarefa['tarefa']} - {tarefa['status']}")

del gerenciador_tarefas["Leonardo"]
