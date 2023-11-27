import flet as ft
import pandas as pd

def main(page: ft.Page):
    page.title= "RE-Analyzer"   
    page.padding = 5
    page.drawer = ft.NavigationDrawer(
        controls=[
            ft.Container(height=12),
            ft.NavigationDrawerDestination(
                label="RE-Analyzer",
                icon=ft.icons.HOME,
                selected_icon_content=ft.Icon(ft.icons.HOME_OUTLINED),
            ),
            ft.Divider(thickness=2),
            ft.NavigationDrawerDestination(
                icon_content=ft.Icon(ft.icons.HOUSE_OUTLINED),
                label="Single Family",
                selected_icon=ft.icons.HOUSE,
            ),
            ft.NavigationDrawerDestination(
                icon_content=ft.Icon(ft.icons.HOME_WORK_OUTLINED),
                label="Multi Family",
                selected_icon=ft.icons.HOME_WORK_OUTLINED,
            ),
            ft.NavigationDrawerDestination(
                icon_content=ft.Icon(ft.icons.LANDSCAPE_OUTLINED),
                label="Land",
                selected_icon=ft.icons.LANDSCAPE,
            ),
        ],
    )

    def show_drawer(e):
        page.drawer.open = True
        page.drawer.update()

    page.add(
       ft.IconButton( 
            icon=ft.icons.MENU_OPEN_SHARP,
            icon_color="pink600",
            icon_size=30,
            tooltip="Open menu",
            on_click=show_drawer
        )
    )


ft.app(main)