from pydantic import BaseModel
from datetime import date


class TodoCreate(BaseModel):
    title: str
    detail: str | None
    duedate: date

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "title": "ชื่อรายการ",
                    "detail": "รายละเอียดข้อมูล",
                    "duedate":"วันครบกำหนดรายการ(yyyy-mm-dd)"
                }
            ]
        }
    }

class TodoUpdate(BaseModel):
    title: str
    detail: str | None
    duedate: date

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "title": "ชื่อรายการ",
                    "detail": "รายละเอียดข้อมูล",
                    "duedate":"วันครบกำหนดรายการ(yyyy-mm-dd)"
                }
            ]
        }
    }