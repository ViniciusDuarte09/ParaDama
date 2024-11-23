import streamlit as st

def lerTextos():
    with open("./.streamlit/Sources/Texts/textos.txt", "r", encoding="utf-8") as arq:

     for l in arq:

      linha = l.strip()

      if(linha == ""):
           continue

      else:
         with st.container(height=150, border=True):
            st.write("")
            st.write(linha)

def mostrarFotos():
   
   pathFotos = "./.streamlit/Sources/Images/FotosBoiolas"

   for i in range(1, 27):

      foto = pathFotos + f"/f{i}.jpg"

      try:
         st.image(foto)

      except:
         pass

