import funcs as f

f.st.set_page_config(page_title= "ForMyLove 💜", 
                     page_icon= "./.streamlit/Sources/Images/Icon.png")

f.st.logo("./.streamlit/Sources/Images/sideIcon.png", size="large")
f.st.sidebar.text("Feito para meu Dengo 💗")

col1, col2, col3 = f.st.columns([1.6, 2.1, 1.4])

with col1:
    f.st.image("./.streamlit/Sources/Images/t4.png", width=100)

with col2:
    f.st.subheader("Textinhos Boiolas ✍")
    f.st.audio("./.streamlit/Sources/Audios/Textos.mp3")

with col3:
    f.st.image("./.streamlit/Sources/Images/t3.png", width=100)

f.st.write('''Então minha vida, aqui tão uns textinhos que escrevi para você durante um tempinho, afinal
é o minímo que posso fazer hihihi, enfim, espero que consiga sentir o minímo que tentei 
desmostar do quão incrível você é! <3''')
f.st.subheader("")

f.lerTextos()
