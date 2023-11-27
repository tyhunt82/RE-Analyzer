import flet as ft
import pandas as pd
import numpy as np


def main(page: ft.Page):
    t = ft.Text(value="Hello, world!", color="green")
    page.controls.append(t)
    page.update()


ft.app(target=main)