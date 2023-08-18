import flet as ft
from threading import Thread
import gui_test

class main():
    def __init__(self,page:ft.Page) -> None:
        self.page = page
        self.page.title = "Wind Turbine"

        self.NavigationRail = ft.NavigationRail(selected_index=0,
                                                destinations=[
                                                    ft.NavigationRailDestination(icon=ft.icons.HOME_ROUNDED,label="Home"),
                                                    ft.NavigationRailDestination(icon=ft.icons.QUESTION_MARK,label="How it Works"),
                                                    ft.NavigationRailDestination(icon=ft.icons.PEOPLE_ROUNDED,label="Contributors")
                                                ])
        self.page.add(
        ft.Row(
            [
                self.NavigationRail,
                ft.VerticalDivider(width=1),
                ft.Column([ ft.Text("Body!")], alignment=ft.MainAxisAlignment.START, expand=True),
            ],
            expand=True,
        )
        )


ft.app(target=main)




