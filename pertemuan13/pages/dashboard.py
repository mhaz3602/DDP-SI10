import streamlit as st 

st.title("ini Halaman dashboard")
st.session_state['Nabung']

jumlah = 0
for session in st.session_state['Nabung']:
    jumlah += session['Nominal']
    
st.write("Total nominal menabun sebesar", jumlah)