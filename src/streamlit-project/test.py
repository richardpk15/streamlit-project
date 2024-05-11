import streamlit as st

def main():
    # Definir o fundo como preto
    st.markdown(
        """
        <style>
        body {
            background-color: #000000;
            color: #ffffff;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.title("Exemplo com Fundo Preto")
    st.write("Este é um exemplo de Streamlit com fundo preto.")

if __name__ == "__main__":
    main()