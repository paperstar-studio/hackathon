import sys
import streamlit as st

st.set_page_config(layout='wide')
st.title("Hackathon 2025")
st.code("Emma Kludze\nFabian Holl\nAbel Moricz")

st.markdown("""### background 
Challenge information will be updated on the website
Additional information about the challenges will be published on the website from Wednesday onward. 
This gives everyone time on Wednesday, Thursday, and Friday to think about the challenge directions, get creative, and prepare. 
The exact and final challenge requirements will only be released shortly before the hackathon so that no team has an unfair advantage and everyone starts on equal terms.""",)

st.divider()

col1, col2, col3 = st.columns([0.45,0.1,0.45])
with col1:
    st.title("challenge1: Product Passport meets ERP")
    st.code("""Build a functional ERP-integrated prototype using Digital Product Passport / Battery Passport data. """, language='plaintext', wrap_lines=True)

    st.markdown("""
    ---
    ### our ideas / research
    DPP (digital product passport):
    https://data.europa.eu/en/news-events/news/eus-digital-product-passport-advancing-transparency-and-sustainability
    """)
with col2:  pass
with col3:
    st.title("challenge2: AI-Powered Construction Photo Compliance Audit")
    st.code("""
    Develop a prototype that uses computer vision to assess geo-referenced construction site photos for completeness, compliance, duplicate use, and potential manipulation, and generate a clear deficiency report.
    """, language='plaintext', wrap_lines=True)


    st.markdown("""
    ---
    ### our ideas / research
    """)


st.code(""" \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n""", language='plaintext')


st.markdown(""" 
### main hackathon website
https://www.sustainista.net/hackathon

may 15th 15:00 - may 17th 12:30


### 3 hackathon challenges in 2024
1. Combating Political Fake News with AI
2. Uncovering New Business Horizons with AI
3. ESG Insight AI Accelerator

source: https://www.sustainista.net/blog-1/2019/3/11/on-letting-go-ft8xd

--- 

 """)

st.image("email.png")


st.write(f"using python version: {sys.version}")