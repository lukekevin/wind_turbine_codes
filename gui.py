import flet as ft
from threading import Thread
import gui_test
from multiprocessing import Process, Value


class main():
    def __init__(self,page:ft.Page) -> None:
        self.page = page
        self.page.title = "Wind Turbine"
        self.SharedVariable = Value('i',0)
        self.NavigationRail = ft.NavigationRail(selected_index=0,
                                                destinations=[

                                                    ft.NavigationRailDestination(icon=ft.icons.HOME_ROUNDED,label="Home",padding=10,),
                                                    ft.NavigationRailDestination(icon=ft.icons.QUESTION_ANSWER,label="Information",padding=10),
                                                    ft.NavigationRailDestination(icon=ft.icons.CAMERA_ALT_ROUNDED,label="Making of It",padding=10),
                                                    ft.NavigationRailDestination(icon=ft.icons.QUESTION_MARK,label="How it Works",padding=10),
                                                    ft.NavigationRailDestination(icon=ft.icons.PEOPLE_ROUNDED,label="Contributors",padding=10),

                                                ],width=200,group_alignment=0.0,on_change=self.ChangeTabs,leading=ft.Image(src=f"/img/transparent.png",width=75,height=75))
                            
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
                        ft.Column(controls=self.InfoText),
                        
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
                ft.Container(content=ft.Column(controls=[
                    ft.Row(controls=[
                        ft.Column(controls=[
                            ft.Container(content=
                                         ft.Column(controls=[
                                                ft.Text(value="Offshore Wind Farm",style=ft.TextThemeStyle.DISPLAY_LARGE,text_align=ft.TextAlign.CENTER,size=70),
                                                ft.Text(value='---- Made by "Science-AI Symbiotic Group, SSAN"',style=ft.TextThemeStyle.TITLE_LARGE,text_align=ft.TextAlign.CENTER,size=30),
                            ],alignment=ft.MainAxisAlignment.CENTER),margin=ft.margin.only(left=500)),
                            
                            
                            ft.Text(value='We aim to develop a model of wind turbine systems which will foster conservation mentality in kids ',style=ft.TextThemeStyle.TITLE_LARGE,text_align=ft.TextAlign.CENTER,size=40),
                            ft.Text(value='and will also pave the way for the future nurturing of scientists and engineers.',style=ft.TextThemeStyle.TITLE_LARGE,text_align=ft.TextAlign.CENTER,size=40),

                            ft.Container(content=ft.Column(controls=[
                                ft.Switch(label="Change Theme",label_position=ft.LabelPosition.LEFT,value=True,on_change=self.ChangeThemes,)

                            ],alignment=ft.MainAxisAlignment.CENTER,),margin=ft.margin.only(left=700),),
                            
                            
                        ])
                        
                    ],alignment=ft.MainAxisAlignment.CENTER)
                ], alignment=ft.MainAxisAlignment.CENTER, expand=True),image_src="home.jpg",image_fit=ft.ImageFit.FILL,width=self.page.width,image_opacity=0.4),
                


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
                ft.Container(content=ft.Column(controls=[
                    ft.Row(controls=[
                        ft.Column(controls=[
                            ft.Container(content=
                                         ft.Column(controls=[
                                                ft.Text(value="Offshore Wind Farm",style=ft.TextThemeStyle.DISPLAY_LARGE,text_align=ft.TextAlign.CENTER,size=70),
                                                ft.Text(value='---- Made by "Science-AI Symbiotic Group, SSAN"',style=ft.TextThemeStyle.TITLE_LARGE,text_align=ft.TextAlign.CENTER,size=30),
                            ],alignment=ft.MainAxisAlignment.CENTER),margin=ft.margin.only(left=500)),
                            
                            
                            ft.Text(value='We aim to develop a model of wind turbine systems which will foster conservation mentality in kids ',style=ft.TextThemeStyle.TITLE_LARGE,text_align=ft.TextAlign.CENTER,size=40),
                            ft.Text(value='and will also pave the way for the future nurturing of scientists and engineers.',style=ft.TextThemeStyle.TITLE_LARGE,text_align=ft.TextAlign.CENTER,size=40),

                            ft.Container(content=ft.Column(controls=[
                                ft.Switch(label="Change Theme",label_position=ft.LabelPosition.LEFT,value=True,on_change=self.ChangeThemes,)

                            ],alignment=ft.MainAxisAlignment.CENTER,),margin=ft.margin.only(left=700),),
                            
                            
                        ])
                        
                    ],alignment=ft.MainAxisAlignment.CENTER)
                ], alignment=ft.MainAxisAlignment.CENTER, expand=True),image_src="home.jpg",image_fit=ft.ImageFit.FILL,width=self.page.width,image_opacity=0.4),
                


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
                print("An error was Given")


            print(self.SharedVariable.value)
            self.Text.value = f"Randomly Generated Number in Thread: {self.SharedVariable.value}"
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
                            ft.Text(value="How it Works",style=ft.TextThemeStyle.DISPLAY_LARGE,text_align=ft.TextAlign.CENTER),
                            ft.Text(value="Description",style=ft.TextThemeStyle.TITLE_LARGE,text_align=ft.TextAlign.CENTER),

                        ])
                        
                    ],alignment=ft.MainAxisAlignment.CENTER)
                ], alignment=ft.MainAxisAlignment.CENTER, expand=True),
            ],
            expand=True,
            )
            )
            
            
            self.page.update()
        
        elif self.NavigationRail.selected_index == 4:
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
                            ft.Row(controls=[
                                ft.Card(
                                        content=ft.Container(
                                            content=ft.Column(
                                                        [
                                                            ft.ListTile(
                                                                leading=ft.Icon(ft.icons.PERSON_2),
                                                                title=ft.Text("Student Name"),
                                                                subtitle=ft.Text("Class"),
                                                            ),
                                                            ft.ListTile(
                                                                leading=ft.Icon(ft.icons.PERSON_2),
                                                                title=ft.Text("Student Name"),
                                                                subtitle=ft.Text("Class"),
                                                                
                                                            ),

                                                            
                                                        ]                       
                                                            ),
                                                width=800,
                                                alignment=ft.alignment.center,
                                                padding=10,
                                    
                                                        )
        )
                        

                            ],alignment=ft.alignment.center)
                            
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
                ft.Container(content=ft.Column(controls=[
                    ft.Row(controls=[
                        ft.Column(controls=[
                            
                            
                            
                        ])
                        
                    ],alignment=ft.MainAxisAlignment.CENTER)
                ], alignment=ft.MainAxisAlignment.CENTER, expand=True)),
                


            ],
            expand=True,
        )
            )
            
            
            self.page.update()

        
    def ChangeThemes(self,e):
        self.page.theme_mode = (
            ft.ThemeMode.DARK
            if self.page.theme_mode == ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT
        )

        self.page.update()




if __name__ == "__main__":
    ft.app(target=main,view=ft.AppView.WEB_BROWSER,assets_dir="assets")







