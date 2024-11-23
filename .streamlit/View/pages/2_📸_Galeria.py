import funcs as f

f.st.set_page_config(page_title= "ForMyLove 💜", 
                     page_icon= ".\.streamlit\Sources\Images\Icon.png")

f.st.logo(".\.streamlit\Sources\Images\sideIcon.png", size="large")
f.st.sidebar.text("Feito para meu Dengo 💗")

col1, col2, col3 = f.st.columns([1.6,2,1.5])

with col1:
    f.st.image("./.streamlit/Sources/Images/t6.png", width=120)

with col2:
    f.st.subheader(":sparkling_heart: Fotinhas :sparkling_heart:  ")
    f.st.audio("./.streamlit/Sources/Audios/Galeria.mp3")
    f.st.subheader("")

with col3:
    f.st.image("./.streamlit/Sources/Images/t5.png", width=100)

with f.st.container(height=700, border=True):
    f.st.write("")

    f.st.write('''Então minha gatinha, resolvi separar essa sessão para só para
**nossas fotinhas** :camera: afinal, tudo isso me faz lembrar a namorada incrível que tenho hihihi
''')
    f.st.divider()
    
    f.mostrarFotos()

