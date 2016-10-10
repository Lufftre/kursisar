#!/bin/python
from html.parser import HTMLParser
import re


class MyHTMLParser(HTMLParser):
    parse = False
    blocks = []
    row = []
    #period = 0
    block = []

    last_tag = ""

    def handle_starttag(self, tag, attrs):
        if self.parse and self.last_tag == "td" and tag == "table" and ('width', '222') in attrs:
            if self.block:
                self.blocks.append(self.block)
            self.block = []
        if self.parse and tag == "tr":
            self.row = []
        self.last_tag = tag

    def handle_endtag(self, tag):
        try:
            if self.parse and tag == "tr" and len(self.row) == 3 and self.row[0] != b'Kurskod':
                self.row = [x.decode('utf-8') for x in self.row]
                
                self.block.append(self.row[:3])
                #self.rows.append(self.row + [self.period, self.block])
        except AttributeError:
            pass

    def handle_data(self, data):
        if re.search(r'Termin 8', data):
            self.parse = True
            #self.period += 1
        elif re.search(r'termin 8', data):
            self.parse = False

        if self.parse:
            data = data.encode('utf-8')
            data = data.strip()
            if data:
                self.row.append(data)
