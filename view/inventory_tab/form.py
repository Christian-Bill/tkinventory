import tkinter as tk
from tkinter import ttk


class Form:

    ENTRY_NAMES = ['Name', 'Quantity', 'Landing Costs', 'Selling Price']
    BUTTON_NAMES = ['Insert', 'Delete', 'Refresh', 'Modify', 'Update']
    ENTRIES = []

    def __init__(self, inventory_frame):

        self.inventory_frame = inventory_frame
        
    def main(self):
        self._form_labelframe()
        self._create_form_entries()
        self._create_buttons()

    def _form_labelframe(self):
        self.product_details = ttk.LabelFrame(self.inventory_frame, text="Product Details")
        self.product_details.pack(side='left', padx=10, pady=10, fill='y')        

    def _create_form_entries(self):
        for index in range(len(self.ENTRY_NAMES)):
            self._entry_names(index)
            self._entry_inputs()

    def _entry_names(self, index):
        entry_name = ttk.Label(self.product_details, text=f"{self.ENTRY_NAMES[index]}: ")
        entry_name.pack(side='top', anchor='w', padx=5)

    def _entry_inputs(self):
        entry_input = ttk.Entry(self.product_details)
        entry_input.pack(side='top', pady=5, padx=5)
        self.ENTRIES.append(entry_input)

    def _create_buttons(self):
        self._half_btn_frame()
        self._full_btn_frame()

    def _half_btn_frame(self):
        self.h_btn_frame = ttk.Frame(self.product_details)
        self.h_btn_frame.pack(side='top')
        self._half_buttons()

    def _half_buttons(self):
        stick = ['W', 'E']
        for i in range(len(stick)):
            btn = ttk.Button(self.h_btn_frame, text=f'{self.BUTTON_NAMES[i]}', width=9)
            btn.grid(column=i, row=0, sticky=stick[i], pady=3, padx=3)

    def _full_btn_frame(self):
        self.f_btn_frame = ttk.Frame(self.product_details)
        self.f_btn_frame.pack(side='top')
        self._full_buttons()

    def _full_buttons(self):
        for i, items in enumerate(self.BUTTON_NAMES[2:]):
            btn = ttk.Button(self.f_btn_frame, text=f'{items}', width=20)
            btn.pack(pady=3, padx=5)