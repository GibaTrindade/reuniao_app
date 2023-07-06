from fastapi import APIRouter, File, UploadFile, Depends
from typing import List
from sqlalchemy import orm
from ..services import create_aircraft_photo, get_db, update_aircraft_photo, delete_photo
from ..schemas.index import Aircraft_photos_create, Aircraft_photos
import base64

uploadFiles = APIRouter()

@uploadFiles.post("/convertToBase64", tags=["uploadFiles"])
async def convert_files(files: List[UploadFile]):
    all_files = []
    for file in files:
        contents = file.file.read()
        encoded_string = base64.b64encode(contents)
        all_files.append(encoded_string)
    return {"photos": all_files}

@uploadFiles.post("/aircraft/{aircraft_id}/photos", response_model=List[Aircraft_photos], tags=["uploadFiles"])
async def create_upload_files(aircraft_id: int, photos: List[Aircraft_photos_create], db: orm.Session = Depends(get_db)):
    print("entrou no create_upload_files")
    photo_list=[]
    for photo in photos:
        photo_list.append(create_aircraft_photo(db=db, photos=photo, aircraft_id=aircraft_id))
    return photo_list

@uploadFiles.put("/photo/{photo_id}", response_model=Aircraft_photos, tags=["uploadFiles"])
def update_business_route(photo_id: int, photo: Aircraft_photos_create, db: orm.Session=Depends(get_db)):
    return update_aircraft_photo(db=db, photo_id=photo_id, photo=photo)

@uploadFiles.delete("/photo/{id}", tags=["uploadFiles"])
async def delete_data(id: int, db: orm.Session=Depends(get_db)):
    delete_photo(db=db, photo_id=id)
    return {"Message": "Photo deleted!"}