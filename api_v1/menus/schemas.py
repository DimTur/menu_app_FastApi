import uuid
from typing import Annotated

from annotated_types import MaxLen, MinLen
from pydantic import BaseModel, ConfigDict

from api_v1.submenus.schemas import FullBaseSubmenu


class MenuBase(BaseModel):
    title: Annotated[str, MinLen(3), MaxLen(32)]
    description: Annotated[str, MinLen(0), MaxLen(300)]


class MenuCreate(MenuBase):
    pass


class MenuUpdate(MenuCreate):
    pass


class MenuUpdatePartial(MenuCreate):
    pass


class Menu(MenuBase):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    submenus_count: int = 0
    dishes_count: int = 0


class FullBase(Menu):
    submenus: list[FullBaseSubmenu]
