from datetime import datetime

class Task:
    
    
    def __init__(self, task_name: str, start_date: str, end_date: str, completed: bool, desc: str) -> None:
        """construtor

        Args:
            task_name (str): nome da task
            sub_tasks (list): lista com as subtasks
            start_date (str): data inicial
            end_date (str): data final
            task_categories (list): etiquetas da task
            completed (bool): completada ou não
            desc (str): descrição da tarefa
        """
        self.task_name = task_name
        self.sub_tasks = []
        if start_date is not None:
            data_obj = datetime.strptime(start_date, "%Y-%m-%d")
            self.start_date = str(data_obj.strftime("%m/%d/%Y"))
        else:
            self.start_date = start_date
        if end_date is not None:
            data_obj = datetime.strptime(end_date, "%Y-%m-%d")
            self.end_date = str(data_obj.strftime("%m/%d/%Y"))
        else:
            self.end_date = end_date
        self.task_categories = []
        self.completed = completed
        self.desc = desc
    
    
    def add_sub_task(self, sub_task: str):
        self.sub_tasks.append(sub_task)
    

            
        