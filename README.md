[![Status][statuss-shield]][statuss-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

<!-- PROJECT LOGO -->
<div align="center">
  <a href="https://github.com/hmfarias/SmartCheff-IA">
    <img src="https://github.com/hmfarias/SmartCheff-IA/blob/main/LOGO.png" alt="Logo" width="270" height="270">
  </a>
  <h2 align="center">PROYECTO SmartCheff-IA</h2>

  <p align="center">
    Generador de Recetas de Cocina Potenciado por IA
    <br />
    <a href="https://github.com/hmfarias/SmartCheff-IA"><strong>Explora los documentos »</strong></a>
    <br />
    <br />
    <a href="https://github.com/hmfarias/SmartCheff-IA">Ver repositorio</a>
    ·
    <a href="https://github.com/hmfarias/SmartCheff-IA/issues">Reportar un error</a>
    ·
    <a href="https://github.com/hmfarias/SmartCheff-IA/issues">Solicitar función</a>
  </p>


  
</div>

<!-- TABLE OF CONTENTS -->

### Tabla de contenidos

  <ol>
    <li>
      <a href="#introduccion">Introducción</a>
      <ul>
        <li><a href="#construido-con">Construido con</a></li>
        <li><a href="#descripción-general">Desripción General</a></li>
          <ul><a href="#uso-de-librerías">Uso de Librerías</a></ul>
      </ul>
    </li>
    <li>
      <a href="#comenzando">Comenzando</a>
      <ul>
        <li><a href="#prerequisitos">Prerequisitos</a></li>
        <li><a href="#instalación">Instalación</a></li>
      </ul>
    </li>
    <li><a href="#contribuyendo">Contribuyendo</a></li>
    <li><a href="#licencia">Licencia</a></li>
    <li><a href="#contacto">Contacto</a></li>
  </ol>

<!-- ABOUT THE PROJECT -->

## Introduccion

SmartCheff-IA, es un sistema de inteligencia artificial innovador que permite crear recetas de cocina personalizadas a partir de una lista de ingredientes. Solo necesitas ingresar los ingredientes disponibles, y la IA se encargará de sugerir platos creativos que puedes preparar. Además, genera una imagen del plato final, brindándote una visualización clara de lo que puedes esperar al seguir la receta. Ideal para quienes buscan inspiración en la cocina o quieren aprovechar al máximo los ingredientes que tienen a mano

<img src="https://github.com/hmfarias/SmartCheff-IA/blob/main/imageWeb.png" alt="Logo" width="700" height="auto">
    
<p align="right">(<a href="#tabla-de-contenidos">volver</a>)</p>

### Construido con

![Static Badge](https://img.shields.io/badge/Python-green?style=for-the-badge) como lenguaje de programación que cuenta con una amplia gama de librerías y frameworks que facilitan la interacción con APIs y el procesamiento de datos. Librerías como openai están bien documentadas y simplifican enormemente la implementación de solicitudes API.

![Static Badge](https://img.shields.io/badge/APIOpenAI-blue?style=for-the-badge) como API proveedora de modelos de inteligencia artificial desarrollado por OpenAI. Cada modelo de OpenAI, puede considerarse como una funcionalidad o capacidad específica. Estos modelos son entrenados para realizar diversas tareas relacionadas con el procesamiento del lenguaje natural. Pueden llevar a cabo funciones como generación de texto, imágenes, traducción de idiomas, respuestas a preguntas, redacción de contenido, etc., todo basado en el contexto proporcionado durante su entrenamiento.

<p align="right">(<a href="#tabla-de-contenidos">volver</a>)</p>

### Descripción general

SmartCheff-IA es un sistema de IA que ayude a los usuarios a crear recetas personalizadas a partir de los ingredientes que tienen en su cocina. Este problema es relevante porque muchas personas se sienten abrumadas por la falta de ideas para cocinar y terminan comprando ingredientes adicionales, lo que puede generar desperdicio de alimentos.


<img src="https://github.com/hmfarias/SmartCheff-IA/blob/main/imgReceta.png" alt="Logo" width="900" height="auto">


#### Uso de Librerías

- **openAI:** Para interactuar con las API de GPT-3 y DALL-E.
- **Streamlit:** Para el front-end
- **dotenv** Para controlar todos los pares de key-values de un archivo que sea etiquetado como archivo de entorno o . env y configurarlos como variables del entorno. (En este caso la API-KEY OpenAI)
- **fpdf** Para generar el archivo PDF con la receta
- **PILLOW** Para la edición de la imágen de la receta
- **requests** Para hacer la petición HTTP de la imágen de la receta generada
- **BytesIO**  Para manejar las imágenes como datos binarios en memoria.

<p align="right">(<a href="#tabla-de-contenidos">volver</a>)</p>

<!-- GETTING STARTED -->

## Comenzando

Esta guía describe paso a paso cómo utilizar el sitio web de SmartCheff-IA.

### Prerequisitos

Antes de comenzar la instalación, es necesario:

- Python 3.8 o superior
- Cuenta de OpenAI con acceso a las API de GPT-3 y DALL-E
- Pip (gestor de paquetes de Python)
- API Key de API openAI

### Instalación 

1. ##### Clonar el proyecto del repositorio

- Cree una carpeta en un directorio local y desde la `terminal` dentro de la carpeta creada, inicialice git:

```
git init
```

- Clonar todo el proyecto:

```
git clone https://github.com/hmfarias/SmartCheff-IA.git
```

- Ejecuta Visual Studio Code

- Crea un entorno virtual:
```
  Paleta de comandos: "Crear Entorno o Create Environment"
  Selecciona Venv
```

- Instala las dependencias:
```
pip install streamlit
pip install openai
pip install python-dotenv
pip install fpdf
pip install pillow
pip install requests

```
- Agrega la API-KEY de OpneAI, en el archivo .env

- Ejecuta con el comando "streamlite run app.py"
  
<p align="right">(<a href="#tabla-de-contenidos">volver</a>)</p>
    
<!-- CONTRIBUTING -->

## Contribuyendo

Las contribuciones son lo que hace que la comunidad de código abierto sea un lugar increíble para aprender, inspirar y crear. Cualquier contribución que haga es **muy apreciada**.

Si tiene una sugerencia para mejorar este proyecto, por favor haga un "fork" al repositorio y cree un "pull request". También puede simplemente abrir un "issue" con la etiqueta "mejora".
¡No olvide darle una estrella al proyecto! ¡Gracias de nuevo!

1. Fork al Proyecto
2. Cree una nueva rama para su característica (`git checkout -b feature/newFeature`)
3. Commit para los cambios (`git commit -m 'Add some newFeature'`)
4. Push a la nueva rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

<p align="right">(<a href="#tabla-de-contenidos">volver</a>)</p>

<!-- LICENSE -->

## Licencia

Distribuido bajo la licencia MIT. Consulte `LICENSE.txt` para obtener más información.

<p align="right">(<a href="#tabla-de-contenidos">volver</a>)</p>

<!-- CONTACT -->

## Contacto

Marcelo Farias - [+54 9 3512601888] - hmfarias7@gmail.com

Link del Proyecto: [https://https://github.com/hmfarias/SmartCheff-IA](https://https://github.com/hmfarias/SmartCheff-IA)

<p align="right">(<a href="#tabla-de-contenidos">volver</a>)</p>

<!-- ACKNOWLEDGMENTS -->

<!-- MARKDOWN LINKS & IMAGES -->

<!-- [statuss-shield]: https://img.shields.io/badge/STATUS-Developing-green -->

[statuss-shield]: https://img.shields.io/badge/STATUSS-finished-green
[statuss-url]: https://https://github.com/hmfarias/SmartCheff-IA#readme
[forks-shield]: https://img.shields.io/github/forks/hmfarias/SmartCheff-IA
[forks-url]: https://github.com/hmfarias/SmartCheff-IA/network/members
[stars-shield]: https://img.shields.io/github/stars/hmfarias/SmartCheff-IA
[stars-url]: https://github.com/hmfarias/SmartCheff-IA/stargazers
[issues-shield]: https://img.shields.io/github/issues/hmfarias/SmartCheff-IA
[issues-url]: https://github.com/hmfarias/SmartCheff-IA/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg
[license-url]: https://github.com/hmfarias/SmartCheff-IA/blob/master/LICENSE.txt
[product-screenshot]: https://github.com/hmfarias/SmartCheff-IA/blob/main/assets/images/screenShot.webp
[product-screenshot-navbar]: https://github.com/hmfarias/SmartCheff-IA/blob/main/assets/images/navbar.webp
[others-url]: https://github.com/hmfarias/SmartCheff-IA





