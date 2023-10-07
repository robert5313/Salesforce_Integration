from core.config import settings
from fastapi import FastAPI, File, Response, Body, UploadFile
from helpers.process_xml import process_xml_data
from google2 import upload
app = FastAPI(
    title=settings.app_name,
    description=settings.app_description,
    version=settings.app_version,
)
import os

@app.get("/")
def health_status():
    return {"message": "Healthy"}

@app.post(path="/salesforce/webhooks/new_contact")
def process_new_contact(payload: bytes = Body()):
    data = process_xml_data(payload=payload)
    print(data)
    upload("tester.txt")
    return Response(status_code=200, content="Data recieved")


@app.post("/file-upload")
async def upload_file(file: UploadFile = File(...)):
    print(f"Filename: {file.filename}")
    contents = await file.read()
        # save the file
    DATA_DIR = "data/"
    with open(f"{DATA_DIR}{file.filename}", "wb") as f:
        f.write(contents)

    file_path = f"./{DATA_DIR}{file.filename}"
    upload(file_path)

    if os.path.exists(file_path):
        os.remove(file_path)
    else:
        print("The file does not exist")
    

    return Response(status_code=200, content="file recieved")
