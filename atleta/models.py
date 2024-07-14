from datetime import datetime
from sqlalchemy import Float, Integer, String,DateTime
from workout_api.contrib.models import BaseModel
from sqlalchemy.orm import Mapped,mapped_column


class AtletaModel(BaseModel):
    __tablename__ = 'atletas'

    pk_id: Mapped[int]=mapped_column(Integer, primary_key=True)
    nome:  Mapped[str]=mapped_column(String(50), primary_key=False)
    cpf:  Mapped[str]=mapped_column(String(11), primary_key=False)
    idade:  Mapped[int]=mapped_column(Integer, primary_key=False)
    peso:  Mapped[float]=mapped_column(Float, primary_key=False)
    altura:  Mapped[float]=mapped_column(Float, primary_key=False)
    sexo:  Mapped[str]=mapped_column(String(1), primary_key=False)
    created_at: Mapped[datetime]=mapped_column(DateTime, nullable=False)