from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager #garante que as versoes sao compativies selenium x chrome
from selenium.webdriver.common.by import By #comando pronto "por algo"
import time

# Configuração do WebDriver
servico = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=servico)

def testar_registro():
    try: #tente ate que algo aconteça
        # URL Direta para o formulário de registro
        url_registro = "https://jpetstore.mate.academy/actions/Account.action?newAccountForm="
        driver.get(url_registro)
        print("--- Iniciando Validação de Requisitos ---")

        # --- PS-REQ-006: Teste de Campos Vazios ---
        # Tentamos salvar sem preencher nada
        driver.find_element(By.NAME, "newAccount").click()
        print("PS-REQ-006: Verifique se o sistema impediu o envio com campos vazios.")
        time.sleep(2) #nao recomendado em testes prontos, 

        # --- PS-REQ-004 e 005: Teste de Senhas ---
        driver.get(url_registro) # Resetar formulário
        driver.find_element(By.NAME, "password").send_keys("12345") # Sem símbolo especial
        driver.find_element(By.NAME, "repeatedPassword").send_keys("54321") # Diferente da primeira
        driver.find_element(By.NAME, "newAccount").click()
        print("PS-REQ-004/005: Verifique se houve erro de complexidade e divergência de senhas.")
        time.sleep(2)

        # --- PS-REQ-001 e 003: Teste de Unicidade (ID e Email) ---
        driver.get(url_registro)
        # Usando dados que provavelmente já existem (padrão do sistema)
        driver.find_element(By.NAME, "username").send_keys("j2ee") 
        driver.find_element(By.NAME, "account.email").send_keys("yourname@domain.com")
        
        # Preencher o restante para conseguir clicar em salvar
        driver.find_element(By.NAME, "password").send_keys("Senha@123")
        driver.find_element(By.NAME, "repeatedPassword").send_keys("Senha@123")
        driver.find_element(By.NAME, "account.firstName").send_keys("Nicolas")
        driver.find_element(By.NAME, "account.lastName").send_keys("Silva")
        
        driver.find_element(By.NAME, "newAccount").click()
        print("PS-REQ-001/003: Validando se o sistema aceita IDs ou Emails duplicados.")

    except Exception as e:
        print(f"Erro na execução: {e}")
    finally:
        print("\nAnalise o navegador antes de fechar.")
        time.sleep(8)
        driver.quit()

if __name__ == "__main__":
    testar_registro()
