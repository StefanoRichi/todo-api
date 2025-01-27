from sqlalchemy import Column, Integer , String ,Text ,Boolean ,DateTime , Date
from app.db.database import Base

class Todo(Base):
    __tablename__ = "todo"
    __table_args__ = {"comment": "ข้อมูลรายการ todo"}
    id  = Column(Integer, primary_key=True,nullable=False,unique=True ,index=True , comment="รหัสของรายการ")
    title = Column(String , comment="ชื่อรายการ")
    detail = Column(Text , nullable=True ,  comment="รายละเอียดรายการ")
    is_done =  Column(Boolean , default=False , comment="สถานะของรายการ")
    is_done_timestamp =  Column(DateTime , nullable=True, comment="วันเวลาของสถานะของรายการ")
    due_date =  Column(Date , comment="วันครบกำหนดรายการ")
