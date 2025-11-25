import streamlit as st
from core.prompts import CUSTOM_PROMPT
from core.groq_client import create_groq_client, ask_groq

# --- CONFIGURAÇÃO ---
st.set_page_config(
    page_title="Pyxel | Assistente Python IA",
    page_icon="🐍",
    layout="wide"
)


st.title("🐍 Pyxel AI Coder")
st.caption("Seu assistente inteligente de Programação Python.")

# --- SIDEBAR ---
with st.sidebar:
    st.header("🔑 Configurações Essenciais")
    groq_key = st.text_input("Chave API Groq", type="password", help="Obtenha sua chave em https://console.groq.com/keys")

    st.markdown("---")
    st.header("🌐 Conecte-se com o Desenvolvedor")
    st.markdown("Desenvolvido por **Breno Crespo**")
    st.markdown("[LinkedIn](https://www.linkedin.com/in/brenocrespo/)")
    st.markdown("[GitHub](https://github.com/Breno-Crespo)")

# Histórico de mensagens
if "messages" not in st.session_state:
    st.session_state.messages = []

# Renderizar mensagens anteriores
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Entrada do usuário
prompt = st.chat_input("Qual sua dúvida sobre Python?")

if prompt:
    if not groq_key:
        st.warning("Insira sua API Key primeiro.")
        st.stop()

    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.write(prompt)

    try:
        client = create_groq_client(groq_key)

        messages_api = [{"role": "system", "content": CUSTOM_PROMPT}]
        messages_api.extend(st.session_state.messages)

        with st.chat_message("assistant"):
            with st.spinner("Processando..."):
                response = ask_groq(client, messages_api)
                reply = response.choices[0].message.content

                st.write(reply)
                st.session_state.messages.append({"role": "assistant", "content": reply})

    except Exception as e:
        st.error(f"Erro ao se comunicar com API: {e}")

with st.expander("📚 Sobre o Projeto"):
    st.markdown("""
        <p style="text-align:left; color:gray;">
        Este é um projeto Open Source focado em demonstrar o poder da IA Generativa 
        (via Groq) integrada ao Streamlit. O Pyxel é um assistente especializado em 
        responder dúvidas de programação Python de forma rápida e precisa.
        <br><br>
        *Inspirado no curso Python da Data Science Academy.*
        </p>
        """,
        unsafe_allow_html=True
    )
