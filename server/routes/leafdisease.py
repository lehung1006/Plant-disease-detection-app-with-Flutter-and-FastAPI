from routes.root import router
import base64
from io import BytesIO
from PIL import Image
from database.leafdisease.leafdisease import (
    retrieve_leaf_diseaes,
    retrieve_leafdisease_by_id,
    retrieve_leafdisease_by_label,
)
from model.plant import (
    IMEI,
    ErrorResponseModel,
    ResponseModel,)
from ultils.classify.leafdisease.leafdiseaseclassify import classify
CLASSIFYDIR = "./ultils/classify/images"


@router.get("/leafdisease", response_description="get all leafdisease: name and description")
async def get_leafdisease():
    leafdisease = await retrieve_leaf_diseaes()
    if leafdisease:
        return ResponseModel(leafdisease, "leafdisease data retrieved successfully")
    return ResponseModel(leafdisease, "Empty list returned")


@router.get("/leafdisease/", response_description="get info of leafdisease by id")
async def get_leafdisease_data_by_id(id: str):
    leafdisease = await retrieve_leafdisease_by_id(id)
    if leafdisease:
        return ResponseModel(leafdisease, "leafdisease data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "leafdisease doesn't exist.")


@router.get("/leafdisease/labels/", response_description="get all leafdisease: name and description")
async def get_leafdisease_by_label(label: str):
    leafdisease = await retrieve_leafdisease_by_label(label)
    if leafdisease:
        return ResponseModel(leafdisease, "leafdisease data retrieved successfully")
    return ResponseModel(leafdisease, "Empty list returned")


@router.post("/leafdisease_classify", response_description="get all leafdisease: name and description")
async def leafdisease_classify(im: IMEI):
    img64 = im.dict()
    imgcode = img64['img']
    imgdata = base64.b64decode(imgcode)
    im_file = BytesIO(imgdata)
    img = Image.open(im_file)
    label = classify(img)
    disease = await retrieve_leafdisease_by_label(label)
    if disease:
        return ResponseModel(disease, "leafdisease data retrieved successfully")
    return ResponseModel(disease, "Empty list returned")
