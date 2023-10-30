from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class Trello:
    
    
    def __init__(self, email: str, password: str, link: str) -> None:
        self.email = email
        self.password = password
        self.link = link
        self.driver = webdriver.Edge()
    
    
    
    def log_in(self) -> None:
        # Acessando o site do trello
        self.acesss_website()
        # Clicando no link de log-in
        link_login = self.find_element_by_xpath("//button[@data-testid='request-access-login-button']")
        link_login.click()
        
        # Encontrar o campo de e-mail e o botão de continuação
        email_field = self.find_element_by_xpath("//input[@id='user']")
        continue_button = self.find_element_by_xpath("//input[@id='login']")

        # Preencher o campo de e-mail
        email_field.send_keys(self.email)
        continue_button.click()
        
        # Encontrar o campo de senha e o botão de login final
        password_field = self.find_element_by_xpath("//input[@name='password']")
        login_final_button = self.find_element_by_xpath("//button[@id='login-submit']")

        # Preencher o campo de senha
        password_field.send_keys(self.password)

        # Clicar no botão de login final
        login_final_button.click()
    
    
    def acesss_website(self) -> None:
        self.driver.get(self.link)
    
    
    def find_element_by_xpath(self, xpath: str):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, xpath))
        )

        return element
    

    def create_new_card(self, tasks: list):        
        for task in tasks:
            try:
                existing_task = self.find_element_by_xpath(f"//span[contains(text(), '{task.task_name}')]")
                print(existing_task.text)
                continue
            except Exception as e:
            
                # Encontrar botão de criação de novo card
                create_new_card_button = self.find_element_by_xpath("//h2[text()='To do']/following::a[@data-testid='list-add-card-button']")
                # Clicar no botão de criação de novo card
                create_new_card_button.click()
                sleep(0.2)
                card_title_textarea = self.find_element_by_xpath("//textarea[@data-testid='list-card-composer-textarea']")
                card_title_textarea.send_keys(task.task_name)
                sleep(0.2)
                card_title_textarea.send_keys(Keys.ENTER)
                sleep(0.5)
                
                if len(task.sub_tasks) > 0:
                    # Localize o card com base no título
                    new_card = self.find_element_by_xpath(f"//span[contains(text(), '{task.task_name}')]/ancestor::a")
                    # Clicar no card
                    new_card.click()
                    
                    create_checklist_button = self.find_element_by_xpath("//a[@title='Checklist']")
                    # Clicar no botão de criar novo checklist
                    create_checklist_button.click()

                    sleep(0.5)  # ...

                    # Localizar o campo de inserção de nome do checklist
                    checklist_name_field = self.find_element_by_xpath("//input[@id='id-checklist']")
                    # Colar nome do checklist
                    checklist_name_field.send_keys("Subtarefas")
                    sleep(0.5)
                    # Localize o botão para adicionar o checklist e clique nele
                    add_checklist_button = self.find_element_by_xpath("//input[@value='Add']")
                    add_checklist_button.click()
                    
                    for subtarefa in task.sub_tasks:
                        # Localizar campo de inserção do nome da subtarefa
                        subtask_field = self.find_element_by_xpath("//textarea[@placeholder='Add an item']")
                        # Colar o nome da subtarefa
                        subtask_field.send_keys(subtarefa)
                        sleep(0.5)
                        # Apertar ENTER
                        subtask_field.send_keys(Keys.ENTER)
                        sleep(0.5)
                    
                if task.start_date is not None or task.end_date is not None:
                    date_button = self.find_element_by_xpath("//button[@data-testid='card-back-due-date-button']")
                    date_button.click()
                
                # Se tiver data de inicio
                if task.start_date is not None:
                    start_date_checkbox = self.find_element_by_xpath("//span[@class='CpyGgjAzUkQDno']")
                    start_date_checkbox.click()
                    start_date_input = self.find_element_by_xpath("//input[@data-testid='start-date-field']")
                    start_date_input.clear()
                    start_date_input.send_keys(task.start_date)
                # Se tiver data de fim
                if task.end_date is not None:
                    end_date_input = self.find_element_by_xpath("//input[@data-testid='due-date-field']")
                    end_date_input.clear()
                    end_date_input.send_keys(task.end_date)
                    save_date_button = self.find_element_by_xpath("//button[@data-testid='save-date-button']")
                    save_date_button.click()
                    
                # Localizar botão de fecharo card aberto
                close_card = self.find_element_by_xpath("//a[@class='icon-md icon-close dialog-close-button js-close-window']")
                # Clicar no botão de fechar o card
                close_card.click()
                
                
                

        