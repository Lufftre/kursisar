from tkinter import *
from parse import MyHTMLParser
from urllib.request import urlopen
from tkinter.ttk import * 
import sys
import itertools

kurshandboken_url = 'http://kdb-5.liu.se/liu/lith//studiehandboken/Action.Lasso?&-Response=schemablock_all.lasso&-op=eq&kp_budget_year=2017&-op=cn&kp_termin_ber=Vt&-op=eq&kp_programprofil=D&-op=eq&kp_programkod=D'

class App(Frame):
    parser = MyHTMLParser()
    blockdata = []

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.CreateUI()
        self.LoadData()
        self.LoadTable(self.parser.blocks)
        self.grid(sticky = (N,S,W,E))
        parent.grid_rowconfigure(0, weight = 1)
        parent.grid_columnconfigure(0, weight = 1)

    def CreateUI(self):
        blockschema = Treeview(self)
        blockschema['columns'] = ('kursnamn', 'hp', 'kurskod2', 'kursnamn2', 'hp2')
        blockschema.heading('#0', text='Kurskod')
        blockschema.column('#0', anchor='w', width=90)
        blockschema.heading('kursnamn', text='Kursnamn')
        blockschema.column('kursnamn', anchor='w', width=300)
        blockschema.heading('hp', text='HP')
        blockschema.column('hp', anchor='center', width=100)

        blockschema.heading('kurskod2', text='Kurskod')
        blockschema.column('kurskod2', anchor='w', width=90)
        blockschema.heading('kursnamn2', text='Kursnamn')
        blockschema.column('kursnamn2', anchor='w', width=300)
        blockschema.heading('hp2', text='HP')
        blockschema.column('hp2', anchor='center', width=100)

        blockschema.grid(sticky = (N,S,W,E))
        self.treeview = blockschema
        self.grid_rowconfigure(0, weight = 1)
        self.grid_columnconfigure(0, weight = 1)

    def LoadTable(self, blocks):
        for block in range(4):
            block1 = blocks[block]
            block2 = blocks[block + 4]



            block_merged = list(itertools.zip_longest(block1, block2))

            for i in range(len(block_merged)):
                row = [x if x != None else [] for x in block_merged[i]]
                row = row[0] + row[1]


                self.treeview.insert('', 'end', text=row[0], values=row[1:])
            self.treeview.insert('', 'end')

    def LoadData(self):
        #response = urlopen(kurshandboken_url)
        with open('blockschema.html', 'rb') as myfile:
            html = myfile.read() 
        #html = response.read().decode("utf-8")
        html = html.decode('utf-8')
        self.parser.feed(html)
        



def main():
    root = Tk()
    App(root)
    root.mainloop()

if __name__ == '__main__':
    main()



