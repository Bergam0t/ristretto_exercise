import flet as ft
from flet import IconButton, Page, Row, TextField, icons, theme
import pandas as pd

def main(page: Page):

    sheet_name = "exercises"
    sheet_id = "1_ijtit-PPcbh67s1t_vQ4h-qzE6kwm-txOhE9Wj29PU"
    url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"

    exercise_list_df = pd.read_csv(url)
    
    # global num_exercises
    num_exercises = 6

    # global duration_exercise 
    duration_exercise = 6

    def slider_changed_num_exercises(e):
        nonlocal num_exercises
        num_exercises = int(e.control.value)
        print(num_exercises)
        page.update()

    def slider_changed_duration(e):
        nonlocal duration_exercise
        duration_exercise = int(e.control.value)
        print(duration_exercise)
        page.update()


    range_slider_num_exercises = ft.Slider(
        min=1,
        max=15,
        value=6,
        divisions=14,
        inactive_color=ft.colors.GREEN_300,
        active_color=ft.colors.GREEN_700,
        overlay_color=ft.colors.GREEN_100,
        label="{value}",
        on_change=slider_changed_num_exercises
    )

    range_slider_duration = ft.Slider(
        min=3,
        max=30,
        value=6,
        divisions=30-3,
        inactive_color=ft.colors.GREEN_300,
        active_color=ft.colors.GREEN_700,
        overlay_color=ft.colors.GREEN_100,
        label="{value}",
        on_change=slider_changed_duration
    )


    page.add(
        ft.Column(
            # horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Text(
                    "Select the number of exercises",
                    size=20,
                    weight=ft.FontWeight.BOLD,
                ),
                ft.Container(height=30),
                range_slider_num_exercises,
                ft.Text(
                    "Select the duration",
                    size=20,
                    weight=ft.FontWeight.BOLD,
                ),
                ft.Container(height=30),
                range_slider_duration,
            ],

        )
    )


    def update_exercise_list(e):
        nonlocal datatable
        selected_exercises = exercise_list_df.sample(num_exercises)

        new_datatable = ft.DataTable(columns=[
            ft.DataColumn(ft.Text("Exercise")),
            ft.DataColumn(ft.Text("What")), 
            ft.DataColumn(ft.Text("Duration"))]
            )

        # # https://stackoverflow.com/questions/75167564/populate-flet-datatable-with-pandas-dataframe
        for row in range(len(selected_exercises)):
            new_datatable.rows.append(
                        ft.DataRow(
                        cells=[
                            ft.DataCell(ft.Text(f"{row+1}")),
                            ft.DataCell(ft.Text(selected_exercises["Name"].values[row])), 
                            ft.DataCell(ft.Text("60s"))
                        ]
                        ) 
                    )   

        old_table_index = page.controls.index(datatable)  
        # Replace the old DataTable with the new one
        page.controls[old_table_index] = new_datatable
        # Update the reference to the current DataTable
        
        datatable = new_datatable
        page.update()

    page.add(
        Row(
            [
                IconButton(icons.ADD, on_click=update_exercise_list),
                IconButton(icons.REFRESH, on_click=update_exercise_list)
            ],
            alignment="left",
            vertical_alignment="top"
        )
    )


    generated = False

    datatable = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Column 1")),
            ft.DataColumn(ft.Text("Column 2")),
        ],
        rows=[
            ft.DataRow(cells=[ft.DataCell(ft.Text("Row 1 Col 1")), ft.DataCell(ft.Text("Row 1 Col 2"))]),
            ft.DataRow(cells=[ft.DataCell(ft.Text("Row 2 Col 1")), ft.DataCell(ft.Text("Row 2 Col 2"))]),
        ],
    )

    page.add(datatable)

    datatable.visible = False
    
    # def get_initial_exercise_list(e):
        
    #     selected_exercises = exercise_list_df.sample(6)
        
    #     datatable = ft.DataTable(columns=[ft.DataColumn(ft.Text("Exercise")), ft.DataColumn(ft.Text("Duration"))])

    #     for row in range(len(selected_exercises)):
    #         datatable.rows.append(
    #                     ft.DataRow(
    #                     cells=[
    #                         ft.DataCell(ft.Text(selected_exercises["Name"].values[row])), 
    #                         ft.DataCell(ft.Text("60s"))
    #                     ]
    #                     ) 
    #         )

    #         page.add(datatable)
    #         page.update()
    #         global generated
    #         generated = True
        
    

    page.title = "Flet counter example"
    page.vertical_alignment = "top"
    page.theme = theme.Theme(color_scheme_seed="green")
    page.update()

    
    


    # t = ft.Text(value="Hello, world!", color="green")

    # txt_number = TextField(value="0", text_align="right", width=100)

    # def minus_click(e):
    #     txt_number.value = str(int(txt_number.value) - 1)
    #     page.update()

    # def plus_click(e):
    #     txt_number.value = str(int(txt_number.value) + 1)
    #     page.update()

    # page.add(
    #     Row(
    #         [
    #             IconButton(icons.REMOVE, on_click=minus_click),
    #             txt_number,
    #             IconButton(icons.ADD, on_click=plus_click),
    #         ],
    #         alignment="center",
    #     )
    # )

    # page.controls.append(t)
    page.update()

ft.app(target=main)