import mysql.connector

st.title("Incluir CLiente")

# criação do formulário para preencher

with st.form(key="include_cliente"):
    input_name = st.text_input(label="Insira o seu nome")
    input_age = st.number_input(label="Insira sua idade", format="%d", step=1)
    input_occupation = st.selectbox("Selecione sua profissão", ["Desenvolvedor", "Músico", "Designer", "Professor"])
    input_button_submit = st.form_submit_button("Enviar")
    
# mostrando os dados preenchidos
    
if input_button_submit:
    st.write(f'Nome: {input_name}')
    st.write(f'Idade: {input_age}')
    st.write(f'Profissão: {input_occupation}')