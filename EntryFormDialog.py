'''
EntryFormDialog
Created on Oct 14, 2018

@author: david
'''

import tkinter as tk
from tkinter import ttk


class insertionForm(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        # Create instance
        self.frm = tk.Tk()
           
        # Add a title
        self.frm.title("Add a Movie")
        self.aForm()
        self.frm.mainloop() 
       
    def aForm(self):
        lbfr = ttk.LabelFrame(self.frm, text=' Input Form ')
        lbfr.grid(column=0, row=0, padx=10, pady=10, sticky='W')
        self.lbl0 = tk.Label(lbfr, text="ID: ").grid(column=0, row=0)
        self.e0 = tk.Entry(lbfr, width=4)
        self.e0.grid(column=1, row=0, padx=5, pady=4, sticky='W')
        self.lbl1 = tk.Label(lbfr, text="Title: ").grid(column=0, row=1)
        self.e1 = tk.Entry(lbfr,width=50)
        self.e1.grid(column=1, row=1, padx=5, pady=4, sticky='W')
        self.lbl2 = tk.Label(lbfr, text="Genre: ").grid(column=0, row=2)
        self.e2 = tk.Entry(lbfr,width=12)
        self.e2.grid(column=1, row=2, padx=5, pady=4, sticky='W')
        self.lbl3 = tk.Label(lbfr, text="Run Time: ").grid(column=0, row=3)
        self.e3 = tk.Entry(lbfr,width=4)
        self.e3.grid(column=1, row=3, padx=5, pady=4, sticky='W')
        self.lbl4 = tk.Label(lbfr, text="Year: ").grid(column=0, row=4)
        self.e4 = tk.Entry(lbfr,width=4)
        self.e4.grid(column=1, row=4, padx=5, pady=4, sticky='W')
        self.lbl5 = tk.Label(lbfr, text="Rating: ").grid(column=0, row=5)
        self.e5 = tk.Entry(lbfr,width=5)
        self.e5.grid(column=1, row=5, padx=5, pady=4, sticky='W')
        self.lbl6 = tk.Label(lbfr, text="Online ID: ").grid(column=0, row=6)
        self.e6 = tk.Entry(lbfr,width=12)
        self.e6.grid(column=1, row=6, padx=5, pady=4, sticky='W')
        
        self.btn = ttk.Button(lbfr, text="Add", command=lambda: self.on_click()).grid(column=1, row=7, padx=8, pady =4)
        
    def on_click(self):
        print("Form closed")
        self.frm.destroy()
        
     
if __name__ == '__main__':
    ef = insertionForm()    