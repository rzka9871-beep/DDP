import streamlit as st

st.title("My Data Diri")
st.write("Silahkan isi data diri anda")
st.write("Made by Rizka")

with st.form("form_data_diri"):
    nama = st.text_input("Nama")
    alamat = st. text_input("Alamat")
    usia = st.number_input("Usia")
    email = st.text_input("email")
    submit = st.form_submit_button("Submit")
    

if submit: 
    st.success(f"Terimah kasih {nama} telah mengisi form data diri")
    st.write(f"Nama : {nama}")
    st.write(f"Alamat : {alamat}")
    st.write(f"Usia : {usia}")
    st.write(f"Email : {email}")
