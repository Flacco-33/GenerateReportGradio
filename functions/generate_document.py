import os
import shutil
import zipfile


def generate_document(data):
    """
    Generates a Word document based on a template and provided data.
    This function performs the following steps:
    1. Copies a template directory to a temporary location.
    2. Reads the content of an XML document from the template.
    3. Replaces placeholders in the XML content with values from the provided data dictionary.
    4. Writes the modified XML content to the temporary directory.
    5. Copies image files to the appropriate location in the temporary directory.
    6. Creates a ZIP archive (Word document) from the temporary directory.
    7. Cleans up temporary files and directories.
    Args:
        data (dict): A dictionary where keys are placeholders in the template and values are the corresponding replacements.
    Raises:
        FileNotFoundError: If any of the template files or directories are not found.
        IOError: If there is an error reading or writing files.
    """
    shutil.copytree("utils/document/templete", "temp/document_tmp")
    with open("utils/document/document.xml",'r', encoding='utf-8') as file:
        content = file.read()
        for key, value in data.items():
            content = content.replace(key, value)
            
    with open("temp/document_tmp/word/document.xml", 'w', encoding='utf-8') as file:
        file.write(content)
    shutil.copy("temp/image2.png", "temp/document_tmp/word/media/image2.png")
    shutil.copy("temp/image3.png", "temp/document_tmp/word/media/image3.png")
    shutil.copy("temp/image4.png", "temp/document_tmp/word/media/image4.png")
        
    with zipfile.ZipFile("resultado.docx", 'w') as zipf:
        for root, dirs, files in os.walk("temp/document_tmp"):
            for file in files:
                zipf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), "temp/document_tmp"))
                
    shutil.rmtree("temp/document_tmp")
    os.remove("temp/image2.png")
    os.remove("temp/image3.png")
    os.remove("temp/image4.png")
    