import streamlit as st #para la interface gráfica
from openai import OpenAI #para usar la API de Chat GPT
from dotenv import load_dotenv, find_dotenv #para poder trabajar con el archivo .env
from fpdf import FPDF #para trabajar con pdfs
from PIL import Image #para poder importar imágenes
import requests
from io import BytesIO #para manejar operaciones de input y ouput de archivos


#CARGO VARIABLES DE ENTORNO (API key de OpenAI en este caso)
load_dotenv(find_dotenv(), override=True)

#CREO UN CLIENTE OPENAI
cliente = OpenAI()

#CREO LA FUNCION PARA GENERAR LA RECETA
def generar_receta(ingredientes):
    contexto = '''
        Eres un chef profesional de primera clase mundial
        '''
    
    prompt_usuario = f'''
        Crea una receta detallada basada en los siguientes ingredientes: {','.join(ingredientes)}.
        Formatea la receta de la siguiente manera:
        
        Título de la Receta:
        [Aquí coloca el titulo de la receta sin asteriscos ni caracteres especiales]

        Ingredientes de la Receta con tamaño y porción:

        Lista de Instrucciones para la receta:

    '''
    respuesta = cliente.chat.completions.create(
        model='gpt-4o',
        messages=[
            {'role': 'system', 'content': contexto},
            {'role': 'user', 'content': prompt_usuario}
        ],
        max_tokens=1020,
        temperature=0.9
    )
    return respuesta.choices[0].message.content

#CREO LA FUNCION PARA OBTENER EL NOMBRE DE LA RECETA
def obtener_nombre_receta(texto):
    lineas = texto.splitlines() #divido el texto en lineas
    return lineas[1] #tomo la segunda linea, ya que ahi viene el titulo de la receta que le estoy pidiendo en prompt_usuario

#CREO LA FUNCION PARA GENERAR LA IMÁGEN DE LA RECETA CREADA
def generar_imagen(titulo_receta):
    prompt_imagen = f'''
    Crea una imágen fotorealista del plato final titulado "{titulo_receta}".
    La comida debe estar bellamente presentada en un plato de cerámica con un enfoque cercano en las texturas y colores de los ingredientes.
    La ambientación debe ser sobre una mesa de madera con iluminación natural para resaltar las características apetitosas de la comida. La imágen debe capturar los colores ricos y vibrantes asi como los detalles intrincados, haciéndola parecer recien preparada y lista para comer. 
    '''

    respuesta=cliente.images.generate(
        model='dall-e-3',
        prompt=prompt_imagen,
        style='vivid',
        size='1024x1024',
        quality='standard',
        n = 1 
    )

    return respuesta.data[0].url

#CREO LA FUNCION PARA PODER GUARDAR LA RECETA EN UN PDF
def save_to_pdf(titulo_receta, receta, imagen_url):
    pdf = FPDF() #creo una instancia de la clase pdf
    pdf.add_page() #agrego una página al pdf creado
    pdf.set_font(family="Arial", size=12)
    
    #TITULO
    pdf.set_font(family="Arial", style='B', size=16) #configuro formato para el título 
    pdf.cell(w=0, h=10, txt=titulo_receta, ln=True, align='C')

    #IMAGEN
    respuesta = requests.get(imagen_url)
    img = Image.open(BytesIO(respuesta.content)).convert("RGB")
    img_path = f"{titulo_receta.replace(' ', '-')}.jpg"
    img.save(img_path, format="JPEG")
    pdf.ln(10) #hago un salto de línea de tamaño 10
    img_width = 170
    pdf.image(img_path, x=(pdf.w - img_width)/2, w=img_width, type='JPEG') # pongo la imagen en el pdf
    pdf.ln(10) #hago un salto de línea de tamaño 10

    #RECETA
    pdf.set_font(family= "Arial", size=12) #le configuro el tipo y tamaño de letra nuevamente
    for linea in receta.split('\n'):
        pdf.multi_cell(w = 0, h = 10, txt = linea)

    pdf_archivo = f"{titulo_receta.replace(' ', '-')}.pdf"
    pdf.output(pdf_archivo)

    return pdf_archivo

#AHORA LA INTERFACE CON STREAMLIT-------------------------------------------------------------

st.title("SmartCheff - IA  :sunglasses:")
st.subheader("_Crea tus recetas inteligentes con lo que tengas a mano ..._",divider="red")
st.write("Ingresa los ingredietes para la receta:") 
ingredientes = st.text_input("Ingresa los ingredientes (separados por comas)") # el prompt

#CREO EL BOTON PARA GENERAR LA RECETA
if st.button("Generar Receta", type="primary"):
    lista_ingredientes = [ing.strip() for ing in ingredientes.split(",")]

    #GENERO LA RECETA
    receta = generar_receta(lista_ingredientes)
    st.session_state.receta = receta
    # st.write("1 RECETA:")
    # st.write(receta)

    #TRAIGO EL TÍTULO DE LA RECETA
    titulo_receta = obtener_nombre_receta(receta)
    # st.write("2 ESTE TITULO GENERA:")
    # st.write(titulo_receta)

    st.session_state.titulo_receta = titulo_receta

    #GENERO LA IMAGEN DE LA RECETA
    imagen_receta = generar_imagen(titulo_receta)
    st.session_state.imagen_receta = imagen_receta


#SI SE GENERA LA RECETA ENTONCES LA MUESTRO CON SU TITULO Y SU IMÁGEN
if 'receta' in st.session_state:
    st.write(f"{st.session_state.titulo_receta}")
    st.write(st.session_state.receta)
    st.image(st.session_state.imagen_receta, caption=st.session_state.titulo_receta)

    #CREO EL BOTON PARA GENERAR EL PDF CON LA RECETA
    if st.button("Generar PDF"):
        archivo_pdf = save_to_pdf(st.session_state.titulo_receta,
                                  st.session_state.receta,
                                  st.session_state.imagen_receta)
        with open(archivo_pdf, "rb") as f:
            st.download_button(label="Descargar PDF",
                               data=f, file_name=archivo_pdf,
                               mime="application/pdf")


