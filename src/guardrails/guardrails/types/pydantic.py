from typing import Any, Union

from pydantic import BaseModel

ModelOrListOfModels = Union[type[BaseModel], type[list[type[BaseModel]]]]

ModelOrListOrDict = Union[
    type[BaseModel], type[list[type[BaseModel]]], type[dict[str, type[BaseModel]]]
]

ModelOrModelUnion = Union[type[BaseModel], Union[type[BaseModel], Any]]
