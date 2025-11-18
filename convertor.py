from fastapi import FastAPI, Request
from docling.document_converter import DocumentConverter
import tempfile
import os

app = FastAPI()

@app.post("/convert")
async def convert_docx(request: Request):
    file_content = await request.body()


    with tempfile.NamedTemporaryFile(delete=False, suffix=".docx") as temp_input:
        temp_input.write(file_content)
        input_path = temp_input.name

    converter = DocumentConverter()
    result = converter.convert(input_path)
    markdown_content = result.document.export_to_markdown()

    os.remove(input_path)

    return {"markdown": markdown_content}