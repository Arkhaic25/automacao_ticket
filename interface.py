import streamlit as st

def interface():
    # Dicionário com os destinos
    todos_os_destinos = {
        2: 'Sede', 3: 'Confea/Outros CREAs (Ofícios)', 4: 'Águas Lindas de Goiás', 5: 'Anápolis',
        6: 'Aparecida de Goiânia', 7: 'Aragarças', 8: 'Caldas Novas', 9: 'Campos Belos', 10: 'Ceres',
        11: 'Catalão', 12: 'Cristalina', 13: 'Formosa', 14: 'Goianésia', 15: 'Goiás', 16: 'Goiatuba',
        17: 'Ipameri', 18: 'Iporá', 19: 'Itumbiara', 20: 'Jataí', 21: 'Luziânia', 22: 'Minaçu',
        23: 'Mineiros', 24: 'Morrinhos', 25: 'Palmeiras de Goiás', 26: 'Planaltina', 27: 'Porangatu',
        28: 'Quirinópolis', 29: 'Rio Verde', 30: 'Santa Helena de Goiás', 31: 'Uruaçu'
    }
    
    documentos = {
        2: 'Carteira', 3: 'Certidão', 4: 'CAT', 5: 'Processos', 6: 'Auto de infração', 7: 'Outros'
    }

    st.title("Abrir Tickets")

    usuario = st.text_input("Usuário")
    senha = st.text_input("Senha", type="password")
    
    with st.expander("Escolha os Destinos"):
        selecionar_tudo = st.checkbox("Selecionar Tudo")
        
        destinos_selecionados = []
        
        for key, value in todos_os_destinos.items():
            if selecionar_tudo or st.checkbox(value, key=key):
                destinos_selecionados.append(key)
    
    st.subheader("Escolha o Documento")
    documento_nome = st.selectbox("", list(documentos.values()))
    documento_chave = [key for key, val in documentos.items() if val == documento_nome][0]
    
    texto = st.text_input("Digite o texto")
    
    if st.button("Confirmar"):
        resultado = {
            "destinos": destinos_selecionados,
            "documento": documento_chave,
            "texto": texto,
            "usuario": usuario,
            "senha": senha
        }
        st.success("Iniciando automação!")
        return resultado

if __name__ == "__main__":
    dados = interface()
    