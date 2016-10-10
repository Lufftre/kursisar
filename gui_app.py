from tkinter import *
from parse import MyHTMLParser
from urllib.request import urlopen
from tkinter.ttk import * 

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
        blockschema['columns'] = ('kursnamn', 'hp')
        blockschema.heading('#0', text='Kurskod')
        blockschema.column('#0', anchor='w', width=90)
        blockschema.heading('kursnamn', text='Kursnamn')
        blockschema.column('kursnamn', anchor='w', width=300)
        blockschema.heading('hp', text='HP')
        blockschema.column('hp', anchor='center', width=100)
        blockschema.grid(sticky = (N,S,W,E))
        self.treeview = blockschema
        self.grid_rowconfigure(0, weight = 1)
        self.grid_columnconfigure(0, weight = 1)

    def LoadTable(self, blocks):
        for block in blocks:
            for course in block:
                self.treeview.insert('', 'end', text=course[0], values=course[1:])
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