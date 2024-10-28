import gradio as gr
import requests
import os
import datetime
from dotenv import load_dotenv

from functions import generate_stacked_bar_chart as gsbc
from functions import generate_bar_chart as gbc
from functions import generate_pie_chart as gpc
from functions import generate_document as gd
load_dotenv()

url = f"{os.getenv('URL_API')}/evaluation/"

def generate_docx(idTeacher:str,idCourse:str):
    def generate_docx(idTeacher: str, idCourse: str):
        """
        Generates a DOCX report for a given teacher and course.
        This function fetches data from a remote server using the provided teacher and course IDs,
        processes the data to generate various charts and a document, and returns the filename of
        the generated document.
        Args:
            idTeacher (str): The ID of the teacher.
            idCourse (str): The ID of the course.
        Returns:
            str: The filename of the generated DOCX document if the request is successful.
                 Otherwise, prints an error message with the response status code.
        """
    params = {
        'idTeacher': idTeacher,
        'idCourse': idCourse
    }

    headers = {
        'accept': 'application/json'
    }
    
    response = requests.get(url, headers=headers, params=params)

    # Verificar el código de estado de la respuesta
    if response.status_code == 200:
        print("--------------------")
        gr.Info("Generando documento")
        data = response.json()
        print(data['ratingsAspects'])
        gsbc.generate_stacked_bar_chart(data['ratingsAspects'])
        gbc.generate_bar_chart(data['teacherEvaluations'])
        gpc.generate_pie_chart(data['emotions'])
        
        data_document = {
            "%NAME%": data.get('idTeacher', 'Unknown'),
            "%IDCOURSE%": data.get('idCourse', 'Unknown'),
            "%DATE%": str(datetime.datetime.now().strftime("%d/%m/%Y")),
            "%STRENGTHS%": '\n'.join(data['SWOT']['strengths']),
            "%WEAKNESSES%": '\n'.join(data['SWOT']['weaknesses']),
            "%OPPORTUNITIES%": '\n'.join(data['SWOT']['opportunities']),
            "%THREATS%": '\n'.join(data['SWOT']['threats']),
            "%SUMMARY%": data.get('summaryComment', 'Unknown')
        }
        print(data_document)
        gd.generate_document(data_document)
        return "resultado.docx"
    else:
        print(f"Error: {response.status_code}")
    pass

with gr.Interface(
    fn=generate_docx,
    inputs=[gr.Textbox(label="Docente ID"), gr.Textbox(label="Curso ID")],
    outputs=gr.File(label="Download Report"),
    live=False
) as demo:
    demo.launch(share=True)

