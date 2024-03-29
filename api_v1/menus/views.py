from fastapi import APIRouter, BackgroundTasks, Depends, status

from .dependencies import menu_by_id, menu_by_id_not_from_cache
from .responses import (
    delete_menu_by_id_responses,
    get_all_menus_responses,
    get_menu_by_id_responses,
    patch_menu_by_id_responses,
    post_menu_responses,
)
from .schemas import FullBase, Menu, MenuCreate, MenuUpdatePartial
from .service_repository import MenuService

router = APIRouter(tags=["Menus"])


@router.get(
    "/all/",
    response_model=list[FullBase],
    status_code=status.HTTP_200_OK,
    summary="Возвращает список всех меню с подменю и блюдами",
    responses=get_all_menus_responses,
)
async def get_all_base(
    background_tasks: BackgroundTasks,
    repo: MenuService = Depends(),
) -> list[Menu]:
    return await repo.get_all_base(background_tasks=background_tasks)


@router.get(
    "/",
    response_model=list[Menu],
    status_code=status.HTTP_200_OK,
    summary="Возвращает список всех меню",
    responses=get_all_menus_responses,
)
async def get_menus(
    background_tasks: BackgroundTasks,
    repo: MenuService = Depends(),
) -> list[Menu]:
    return await repo.get_all_menus(background_tasks=background_tasks)


@router.post(
    "/",
    response_model=Menu,
    status_code=status.HTTP_201_CREATED,
    summary="Создание нового меню",
    responses=post_menu_responses,
)
async def create_menu(
    background_tasks: BackgroundTasks,
    menu_in: MenuCreate,
    repo: MenuService = Depends(),
) -> Menu:
    return await repo.create_menu(
        background_tasks=background_tasks,
        menu_in=menu_in,
    )


@router.get(
    "/{menu_id}",
    response_model=Menu,
    status_code=status.HTTP_200_OK,
    summary="Возвращает меню по его id",
    responses=get_menu_by_id_responses,
)
async def get_menu_by_id(
    menu: Menu = Depends(menu_by_id_not_from_cache),
) -> Menu:
    return menu


@router.patch(
    "/{menu_id}",
    response_model=MenuUpdatePartial,
    status_code=status.HTTP_200_OK,
    summary="Обновление меню по его id",
    responses=patch_menu_by_id_responses,
)
async def update_menu_partial(
    background_tasks: BackgroundTasks,
    menu_update: MenuUpdatePartial,
    menu: Menu = Depends(menu_by_id_not_from_cache),
    repo: MenuService = Depends(),
) -> Menu:
    return await repo.update_menu(
        background_tasks=background_tasks,
        menu=menu,
        menu_update=menu_update,
    )


@router.delete(
    "/{menu_id}",
    status_code=status.HTTP_200_OK,
    summary="Удаление меню по его id",
    responses=delete_menu_by_id_responses,
)
async def delete_menu(
    background_tasks: BackgroundTasks,
    menu: Menu = Depends(menu_by_id),
    repo: MenuService = Depends(),
) -> None:
    return await repo.delete_menu(
        background_tasks=background_tasks,
        menu=menu,
    )
