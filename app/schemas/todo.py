from pydantic import BaseModel
from datetime import date


class TodoCreate(BaseModel):
    title: str
    detail: str | None
    due_date: date

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "title": "ชื่อรายการ",
                    "detail": "รายละเอียดข้อมูล",
                    "due_date":"วันครบกำหนดรายการ(yyyy-mm-dd)"
                }
            ]
        }
    }

class TodoUpdate(BaseModel):
    title: str
    detail: str | None
    due_date: date
    is_done: bool

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "title": "ชื่อรายการ",
                    "detail": "รายละเอียดข้อมูล",
                    "due_date":"วันครบกำหนดรายการ(yyyy-mm-dd)",
                    "is_done": "สถานะของรายการ (true/false)"
                }
            ]
        }
    }