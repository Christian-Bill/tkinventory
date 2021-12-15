import tkinter as tk
from tkinter import ttk

class StorageList:

    PAD = 10
    
    def __init__(self, inventory_frame):
        
        self.inventory_frame = inventory_frame

    def main(self):
        self._storage_labelframe()
        self._search_section()

    def _storage_labelframe(self):
        self.storage_list = ttk.LabelFrame(self.inventory_frame, text="Storage List")
        self.storage_list.pack(side='left', padx=self.PAD, pady=self.PAD, fill='both', expand=True)    

    def _search_section(self):
        self.search_frame = ttk.LabelFrame(self.storage_list, text='Search Item')
        self.search_frame.pack(side='top', fill='x', padx=self.PAD, pady=self.PAD)
        self._search_widgets()

    def _search_widgets(self):
        self._search_input()
        self._search_btn()

    def _search_input(self):
        entry_input = ttk.Entry(self.search_frame)
        entry_input.pack(side='left', pady=self.PAD, padx=self.PAD, fill='x', expand=True)

    def _search_btn(self):
        searchbtn = ttk.Button(self.search_frame, text='Search')
        searchbtn.pack(side='left', pady=self.PAD, padx=self.PAD)