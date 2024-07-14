from pydantic import BaseModel, Field,PositiveFloat
from typing import Annotated

class Atleta:
    nome: Annotated[str, Field(description='Nome do atleta', examples='João', max_length=50)]
    cpf: Annotated[str, Field(description='CPF do atleta', examples='1234544353', max_length=11)]
    idade: Annotated[int, Field(description='idade do atleta', examples=24)]
    peso: Annotated[PositiveFloat, Field(description='Peso do atleta', examples=75.8)]
    altura: Annotated[PositiveFloat, Field(description='Altura do atleta', examples=1.8)]
    sexo: Annotated[PositiveFloat, Field(description='Sexo do atleta', examples='M',max_length=1)]