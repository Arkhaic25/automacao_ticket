import subprocess
import psutil

def executar_streamlit():
    # Verifica se já existe um processo do Streamlit rodando
    for process in psutil.process_iter(attrs=['pid', 'name', 'cmdline']):
        try:
            cmdline = process.info['cmdline']
            if cmdline and 'streamlit' in cmdline and 'run' in cmdline:
                print("Streamlit já está rodando. Não será iniciado novamente.")
                return  # Sai da função se já estiver rodando
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue
    
    # Se não encontrou nenhum processo do Streamlit, inicia um novo
    subprocess.Popen(["streamlit", "run", "abrir_ticket.py"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

