import streamlit as st

def style_background_home():
    st.markdown("""
       <style>
            .stApp{
                background: #5865F2 !important;
            }
            .stApp div[data-testid = "stColumn"]{
                background: #E0E3FF !important;
                padding : 2rem !important;
                border-radius : 4rem !important;
            }
       
       </style>
    """, unsafe_allow_html=True)

def style_background_dashboard():
    st.markdown("""
       <style>
            .stApp{
                background: #E0E3FF !important;
            }
          
       
       </style>
    """, unsafe_allow_html=True)

def style_base_layout():
    st.markdown("""
        <style>

        @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&family=Outfit:wght@100..900&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Bungee&family=Climate+Crisis:YEAR@1979&family=Outfit:wght@100..900&display=swap');

        #MainMenu, header, footer, [data-testid="stHeader"], [data-testid="stFooter"], [data-testid="stToolbar"], [data-testid="stDecoration"], [data-testid="stHeaderNav"] {
             visibility : hidden !important;
             display : none !important;
             height : 0px !important;
             min-height : 0px !important;
             padding : 0px !important;
             margin : 0px !important;
        }

        html, body {
            height: 100%;
            margin: 0;
            padding: 0;
        }

        .stApp {
            min-height: 100vh;
        }

        .block-container, [data-testid="stMainBlockContainer"] {
            padding-top: 1rem !important;
            padding-bottom: 1rem !important;
            padding-left: 1rem !important;
            padding-right: 1rem !important;
            # max-width: 100% !important;
        }

        h1{
            font-family: 'Bungee', sans-serif !important;
            font-size: 3.5rem !important;
            line-height:0.9 !important;
            margin-bottom:0rem !important;
        }

        h2{
            font-family: 'Bungee', sans-serif !important;
            font-size: 2rem !important;
            line-height:0.9 !important;
            margin-bottom:0rem !important;
        }

        h3, h4, p {
            font-family: 'Outfit', sans-serif;   
            
            
        }

        button{
            border-radius: 1.5rem !important;
            background-color: #5865F2 !important;
            color: white !important;
            padding: 10px 20px !important;
            border: none !important;
            
        }

        button[kind="secondary"]{
            border-radius: 1.5rem !important;
            background-color: #EB459E !important;
            color: white !important;
            padding: 10px 20px !important;
            border: none !important;
            
        }

        button[kind="tertiary"]{
            border-radius: 1.5rem !important;
            background-color: black !important;
            color: white !important;
            padding: 10px 20px !important;
            border: none !important;
            
        }

        button:hover{
            transform :scale(1.05)
        }

        </style>
    """,unsafe_allow_html=True)