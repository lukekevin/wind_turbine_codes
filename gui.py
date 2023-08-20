import flet as ft
from threading import Thread
import gui_test

class main():
    def __init__(self,page:ft.Page) -> None:
        self.page = page
        self.page.title = "Wind Turbine"

        self.NavigationRail = ft.NavigationRail(selected_index=0,
                                                destinations=[

                                                    ft.NavigationRailDestination(icon=ft.icons.HOME_ROUNDED,label="Home",padding=10,),
                                                    ft.NavigationRailDestination(icon=ft.icons.CAMERA_ALT_ROUNDED,label="Stream",padding=10),
                                                    ft.NavigationRailDestination(icon=ft.icons.QUESTION_MARK,label="How it Works",padding=10),
                                                    ft.NavigationRailDestination(icon=ft.icons.PEOPLE_ROUNDED,label="Contributors",padding=10)
                                                ],width=100,group_alignment=0.0,on_change=self.ChangeTabs)
        
        


        self.page.add(
        ft.Row(
            [
                self.NavigationRail,
                ft.VerticalDivider(width=1),
                ft.Column(controls=[
                    ft.Row(controls=[
                        ft.Column(controls=[
                            ft.Text(value="Home",style=ft.TextThemeStyle.DISPLAY_LARGE,text_align=ft.TextAlign.CENTER),
                            ft.Text(value="Description",style=ft.TextThemeStyle.TITLE_LARGE,text_align=ft.TextAlign.CENTER),

                            ft.ElevatedButton(text="Placeholder Button")
                        ])
                        
                    ],alignment=ft.MainAxisAlignment.CENTER)
                ], alignment=ft.MainAxisAlignment.CENTER, expand=True),


            ],
            expand=True,
        )
        )

        
    def ChangeTabs(self,e):
        if self.NavigationRail.selected_index == 0:
            self.page.controls.clear()
            
            self.page.add(
            ft.Row(
            [
                self.NavigationRail,
                ft.VerticalDivider(width=1),
                ft.Column(controls=[
                    ft.Row(controls=[
                        ft.Column(controls=[
                            ft.Text(value="Home",style=ft.TextThemeStyle.DISPLAY_LARGE,text_align=ft.TextAlign.CENTER),
                            ft.Text(value="Description",style=ft.TextThemeStyle.TITLE_LARGE,text_align=ft.TextAlign.CENTER),

                            ft.ElevatedButton(text="Placeholder Button")
                        ])
                        
                    ],alignment=ft.MainAxisAlignment.CENTER)
                ], alignment=ft.MainAxisAlignment.CENTER, expand=True),
            ],
            expand=True,
            )
            )
            
            
            self.page.update()

        elif self.NavigationRail.selected_index == 1:
            self.page.controls.clear()
            
            self.page.add(
            ft.Row(
            [
                self.NavigationRail,
                ft.VerticalDivider(width=1),
                ft.Column(controls=[
                    ft.Row(controls=[
                        ft.Column(controls=[
                            ft.Text(value="Stream",style=ft.TextThemeStyle.DISPLAY_LARGE,text_align=ft.TextAlign.CENTER),
                            ft.Text(value="Description",style=ft.TextThemeStyle.TITLE_LARGE,text_align=ft.TextAlign.CENTER),

                            ft.ElevatedButton(text="Placeholder Button")
                        ])
                        
                    ],alignment=ft.MainAxisAlignment.CENTER)
                ], alignment=ft.MainAxisAlignment.CENTER, expand=True),
            ],
            expand=True,
            )
            )
            
            
            self.page.update()

        elif self.NavigationRail.selected_index == 2:
            self.page.controls.clear()
            
            self.page.add(
            ft.Row(
            [
                self.NavigationRail,
                ft.VerticalDivider(width=1),
                ft.Column(controls=[
                    ft.Row(controls=[
                        ft.Column(controls=[
                            ft.Text(value="How it Works",style=ft.TextThemeStyle.DISPLAY_LARGE,text_align=ft.TextAlign.CENTER),
                            ft.Text(value="Description",style=ft.TextThemeStyle.TITLE_LARGE,text_align=ft.TextAlign.CENTER),

                            ft.ElevatedButton(text="Placeholder Button")
                        ])
                        
                    ],alignment=ft.MainAxisAlignment.CENTER)
                ], alignment=ft.MainAxisAlignment.CENTER, expand=True),
            ],
            expand=True,
            )
            )
            
            
            self.page.update()
        
        elif self.NavigationRail.selected_index == 3:
            self.page.controls.clear()
            
            self.page.add(
            ft.Row(
            [
                self.NavigationRail,
                ft.VerticalDivider(width=1),
                ft.Column(controls=[
                    ft.Row(controls=[
                        ft.Column(controls=[
                            ft.Text(value="Contributors",style=ft.TextThemeStyle.DISPLAY_LARGE,text_align=ft.TextAlign.CENTER),
                            ft.Text(value="Description",style=ft.TextThemeStyle.TITLE_LARGE,text_align=ft.TextAlign.CENTER),

                            ft.ElevatedButton(text="Placeholder Button")
                        ])
                        
                    ],alignment=ft.MainAxisAlignment.CENTER)
                ], alignment=ft.MainAxisAlignment.CENTER, expand=True),
            ],
            expand=True,
            )
            )
            
            
            self.page.update()
        




ft.app(target=main,view=ft.AppView.WEB_BROWSER)







