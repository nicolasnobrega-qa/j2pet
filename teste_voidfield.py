from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager #garante que as versoes sao compativies selenium x chrome
from selenium.webdriver.common.by import By #comando pronto "por algo"
import time

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

    except Exception as e:
        print(f"Erro na execução: {e}")
    finally:
        print("\nAnalise o navegador antes de fechar.")
        time.sleep(8)
        driver.quit()

if __name__ == "__main__":
    testar_registro()

