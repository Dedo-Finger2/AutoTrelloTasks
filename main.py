from Class.Task import Task
from Class.Trello import Trello
import openpyxl
from time import sleep

def create_tasks_objects():
    # Crie um objeto Task para cada linha
    task_name = row[4].value if not row[13].value else None
    sub_task_name = row[4].value if row[13].value else None
    parent_task_name = row[13].value
    task_start_date = lambda x: row[8].value if x else None
    task_start_date = task_start_date(row[8].value)
    task_end_date = lambda x: row[9].value if x else None
    task_end_date = task_end_date(row[9].value)
    completed = True if row[2].value else False
    desc = lambda x: row[11].value if x else None
    desc = desc(row[11].value)

    task = Task(task_name, task_start_date, task_end_date, completed, desc)

    # Se esta é uma sub-tarefa, adicione-a à lista de sub-tarefas da tarefa correspondente
    if sub_task_name is not None:    
        for t in tasks:
            if t.task_name == parent_task_name:
                t.add_sub_task(sub_task_name)
                break
    else:
        # Adicione a tarefa ao dicionário
        tasks.append(task)

# teste = Task("Nome", [], "2023-02-02", "2023-03-03", [], True)

trello = Trello("antonio.neto12@ba.estudante.senai.br", "marcosDE22", "https://trello.com/b/nmUvjDF5/tcc-geral")
trello.log_in()

tasks = []

workbook = openpyxl.load_workbook('Tarefas/tarefas_tcc.xlsx')
sheet_tarefas = workbook['Worksheet']

for row in sheet_tarefas.iter_rows(min_row=2):
    create_tasks_objects()

trello.create_new_card(tasks)



