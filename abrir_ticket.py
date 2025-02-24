from executar_streamlit import executar_streamlit
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import interface
from time import sleep

# Inicia o Streamlit
executar_streamlit()

# Pega os dados da interface (incluindo login e senha)
dados = interface.interface()

if dados:
    usuario = dados['usuario']
    senha = dados['senha']
    destinos = dados['destinos']
    documento = dados['documento']
    texto = dados['texto']

    # abrir navegador
    navegador = webdriver.Chrome()

    # site tickets
    navegador.get('http://www.crea-go.org.br/osticket/upload/login.php')

    # maximizar tela
    navegador.maximize_window()

    # login com os dados da interface
    usuario_element = navegador.find_element('id', 'username')
    usuario_element.send_keys(usuario)

    senha_element = navegador.find_element('id', 'passwd')
    senha_element.send_keys(senha)

    entrar = navegador.find_element(
        'xpath', '//*[@id="clientLogin"]/div/div[1]/p/input')
    entrar.click()

    # loop para processar cada destino selecionado
    for destino in destinos:
        # clicar em "abrir ticket" a cada iteração
        abrir = navegador.find_element('xpath', '//*[@id="nav"]/li[2]/a')
        abrir.click()

        # selecionar o tópico
        topico_malotes = navegador.find_element(
            'xpath', '//*[@id="topicId"]/option[17]')
        topico_malotes.click()

        # escolher o destino / espera dinâmica
        sleep(1)
        destino_element = navegador.find_element(
            'xpath', f'/html/body/div[1]/div[3]/form/table/tbody[3]/tr[2]/td/label/select/option[{destino}]')

        espera = WebDriverWait(navegador, 10)
        espera.until(EC.element_to_be_clickable(destino_element))

        destino_element.click()

        # documento enviado
        documento_element = navegador.find_element(
            'xpath', f'/html/body/div[1]/div[3]/form/table/tbody[3]/tr[4]/td/label/select/option[{documento}]')
        documento_element.click()

        # detalhes
        detalhes = navegador.find_element(
            'xpath', '/html/body/div[1]/div[3]/form/table/tbody[3]/tr[6]/td/div[1]/div')
        detalhes.send_keys(texto)

        # publicar / scroll para achar publicar / clique
        publicar = navegador.find_element(
            'xpath', '/html/body/div[1]/div[3]/form/p/input[1]')
        navegador.execute_script(
            'arguments[0].scrollIntoView({block: "center"})', publicar)

        # clicar no publicar
        publicar.click()

        # dar um refresh na página após o clique
        #navegador.refresh()

    # Fechar o navegador
    navegador.quit()
