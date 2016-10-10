from flask import Flask
from parse import MyHTMLParser
from urllib.request import urlopen
app = Flask(__name__)
parser = MyHTMLParser()
kurshandboken_url = 'http://kdb-5.liu.se/liu/lith//studiehandboken/Action.Lasso?&-Response=schemablock_all.lasso&-op=eq&kp_budget_year=2017&-op=cn&kp_termin_ber=Vt&-op=eq&kp_programprofil=D&-op=eq&kp_programkod=D'

class Kurs(object):

    def __init__(self, kurskod, kursnamn, hp, period, block):
        self.kurskod = kurskod
        self.kursnamn = kursnamn
        self.hp = hp
        self.period = period
        self.block = block

@app.route("/")
def hello():
    #response = urlopen(kurshandboken_url)
    with open('blockschema.html', 'rb') as myfile:
        html = myfile.read() 
    #html = response.read().decode("utf-8")
    html = html.decode('utf-8')
    parser.feed(html)

    output = "<table>"

    row_nr = 1
    for row in parser.rows:
        output += "<tr><td>{}</td>".format(row_nr)
        row_nr += 1
        for data in row:
            output += "<td>{}</td>".format(data)
        output += "</tr>"

    output += "</table>"

    return output

if __name__ == "__main__":
    app.run()