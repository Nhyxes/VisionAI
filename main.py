from fastapi import FastAPI, UploadFile, File
from PIL import Image
import io

app = FastAPI()

@app.get("/")
def root():
    return {"status": "VisionAI API  successfully"}

@app.post("/predict")
async def predict_image(file: UploadFile = File(...)):
    # Lire le contenu du fichier envoyé
    content = await file.read()

    # Ouvrir l'image avec Pillow
    image = Image.open(io.BytesIO(content))

    #recuperer largeur/hauteur
    width, height = image.size

    return {
        "filename": file.filename,
        "width": width,
        "height": height,
        "content_type": file.content_type
    }

