import tkinter as tk
from tkinter import ttk
from inventory_tab.form import Form


class View(tk.Tk):

    def __init__(self):
        super().__init__()

        # self.controller = controller

        self._window_settings()
        self._app_notebook()
        self._create_form()

    def main(self):
        self.mainloop()

    def _window_settings(self):
        self.title("tkinventory")
        self.geometry('426x562')
        # self.resizable(0, 0)

    def _app_notebook(self):
        self.tab_menu = ttk.Notebook(self)
        self.tab_menu.pack(expand=True, fill='both')
        self._inventory_tab()

    def _inventory_tab(self):
        self.inventory_frame = ttk.Frame(self.tab_menu)
        self.inventory_frame.pack(fill='both', expand=True)
        self.tab_menu.add(self.inventory_frame, text='Inventory')

    def _create_form(self):
        Form(self.inventory_frame).main()


if __name__ == '__main__':
    View().mainloop()