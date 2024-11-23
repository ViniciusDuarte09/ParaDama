import funcs as f

f.st.set_page_config(page_title= "ForMyLove 💜", 
                     page_icon= ".\.streamlit\Sources\Images\Icon.png")

f.st.logo(".\.streamlit\Sources\Images\sideIcon.png", size="large")
f.st.sidebar.text("Feito para meu Dengo 💗")


col1, col2, col3 = f.st.columns([1.6, 2.1, 1.4])

with col1:
    f.st.image("./.streamlit/Sources/Images/t1.png", width=100)

with col2:
    f.st.subheader("Seu Presente 🎁")
    f.st.subheader("")

with col3:
    f.st.image("./.streamlit/Sources/Images/t2.png", width=100)
    

f.st.write('''Admito que esse é um projeto que tô a um tempo 
trabalhando mais de verdade espero que você goste de verdade, em
resumo é um site bem simplezinho com algumas coisinhas que preparei pra 
você, depois assiti o videozinho que aqui a abaixo que preparei 💖''')

f.st.link_button(url="https://youtu.be/F-gzR1Dpiy0?si=JPv2ayItc0mp3GGK", label= "Clique Aqui! 💕")

f.st.image("./.streamlit/Sources/Images/mh1.png")

f.st.audio("./.streamlit/Sources/Audios/HomePage.mp3")
