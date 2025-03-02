from pydantic import BaseModel 


class Extracted_text(BaseModel):
    language : str
    text : list
    model : str

class Convert_audio(BaseModel):
    file: str
    type: str
    date: str
    model: str
    