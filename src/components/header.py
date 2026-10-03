import streamlit as st

def header_home():

    logo_url = 'https://cdn-icons-png.flaticon.com/512/11146/11146111.png'
    
    st.markdown(f"""
        <div style = 'display : flex; flex-direction : column; justify-content : center; align-items : center; margin-bottom:10px; margin-top:10px'>
            <img src = {logo_url} height = 90px; />
            <h1 style = 'text-align : center; color : #E0E3FF'>SMART<br><span style="margin-left:15px;">CLASS</span></h1>
        </div>
    """, unsafe_allow_html=True)

def header_dashboard():

    logo_url = 'https://cdn-icons-png.flaticon.com/512/11146/11146111.png'
    
    st.markdown(f"""
        <div style = 'display : flex; justify-content : center; align-items : center; gap : 10px'>
            <img src = {logo_url} height = 70px; />
            <h2 style = 'text-align : left; color : #5865F2; margin-top : 10px'>SMART<br>CLASS</h2>
        </div>
    """, unsafe_allow_html=True)

