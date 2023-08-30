import flet as ft
from threading import Thread
import gui_test
from time import sleep
from multiprocessing import Process, Value


class main():
    def __init__(self,page:ft.Page) -> None:
        global data
        data = "Default Value"
        self.page = page
        self.page.title = "Wind Turbine"
        self.SharedVariable = Value('i',0)
        self.NavigationRail = ft.NavigationRail(selected_index=0,
                                                destinations=[

                                                    ft.NavigationRailDestination(icon=ft.icons.HOME_ROUNDED,label="Home",padding=10,),
                                                    ft.NavigationRailDestination(icon=ft.icons.CAMERA_ALT_ROUNDED,label="Information",padding=10),
                                                    ft.NavigationRailDestination(icon=ft.icons.QUESTION_MARK,label="How it Works",padding=10),
                                                    ft.NavigationRailDestination(icon=ft.icons.PEOPLE_ROUNDED,label="Contributors",padding=10)
                                                ],width=100,group_alignment=0.0,on_change=self.ChangeTabs)
                            
        self.Text = ft.Text(value="Description",style=ft.TextThemeStyle.TITLE_LARGE,text_align=ft.TextAlign.CENTER,)
        self.InfoText = [ft.Text(value="Information",style=ft.TextThemeStyle.DISPLAY_LARGE,text_align=ft.TextAlign.CENTER),
                            self.Text,
                            ft.ElevatedButton(text="Placeholder Button")]
        self.streamView = ft.Row(
            [
                self.NavigationRail,
                ft.VerticalDivider(width=1),
                ft.Column(controls=[
                    ft.Row(controls=[
                        ft.Column(controls=self.InfoText)
                        
                    ],alignment=ft.MainAxisAlignment.CENTER)
                ], alignment=ft.MainAxisAlignment.CENTER, expand=True),
            ],
            expand=True,
            )
            

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
            self.streamView,
            )
            
            print("Started Thread")
            try:
                self.BackgroundThread = Process(target=gui_test.main,args=(self.SharedVariable,))
                self.BackgroundThread.start()
                self.BackgroundThread.join()
                self.BackgroundThread = None
            except:
                print("Thread Cannot be Started again.")


            print(self.SharedVariable.value)
            self.Text.value = f"Randomly Generated Number in Thread: {self.SharedVariable.value}"
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
                            ft.ElevatedButton(text="Placeholder Button")
                        ])
                        
                    ],alignment=ft.MainAxisAlignment.CENTER)
                ], alignment=ft.MainAxisAlignment.CENTER, expand=True),
            ],
            expand=True,
            )
            )
            
            
            self.page.update()
        



if __name__ == "__main__":
    ft.app(target=main,view=ft.AppView.WEB_BROWSER)







