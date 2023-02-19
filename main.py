from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from datetime import timedelta, date
import pygsheets

client = pygsheets.authorize(service_account_file="")  # You need a key here google-api
spreadsht = client.open("")  # Name table in Google Drive
today = date.today()

try:
    spreadsht.add_worksheet(today.strftime("%d.%m.%Y"), rows=1, cols=5)
    spreadsht.worksheet("title", today.strftime("%d.%m.%Y")).cell(f"B{1}").value = "0"
    spreadsht.worksheet("title", today.strftime("%d.%m.%Y")).cell(f"E{1}").value = "0"
    for l in range(30):
        l += 1
        spreadsht.add_worksheet((today - timedelta(days=(l))).strftime("%d.%m.%Y"), rows=1, cols=5)
        spreadsht.worksheet("title", (today - timedelta(days=(l))).strftime("%d.%m.%Y")).cell(f"B{1}").value = "0"
        spreadsht.worksheet("title", (today - timedelta(days=(l))).strftime("%d.%m.%Y")).cell(f"E{1}").value = "0"
except:
    pass

worksht = spreadsht.worksheet("title", today.strftime("%d.%m.%Y"))
workshtt = spreadsht.worksheet("title", "Журнал_Система")
workshtl = spreadsht.worksheet("title", "Журнал_Локодром")


class Container(Screen):
    def __init__(self, **kwargs):
        super(Container, self).__init__(**kwargs)
        self.today = today.strftime("%d.%m.%Y")
        self.time.text = str(self.today)
        self.bold = 0
        self.i = 0
        self.a = []
        self.b = []
        self.c = []
        self.d = []
        self.doyou = 1
        self.loop = int(worksht.cell(f"B{1}").value)
        lopux = str(worksht.cell(f"A{1}").value).split(';')
        for row in range(self.loop):
            lol = TextInput(text=lopux[0 + row * 4], size_hint_x=0.13, size_hint_y=None, height="70sp",
                            font_size='14sp')
            self.a.append(lol)
            self.fp.add_widget(self.a[row])
            lol1 = TextInput(text=lopux[1 + row * 4], size_hint_x=0.4, size_hint_y=None, height="70sp",
                             font_size='14sp')
            self.b.append(lol1)
            self.fp.add_widget(self.b[row])
            lol2 = TextInput(text=lopux[2 + row * 4], size_hint_x=0.8, size_hint_y=None, height="70sp",
                             font_size='14sp')
            self.c.append(lol2)
            self.fp.add_widget(self.c[row])
            lol3 = TextInput(text=lopux[3 + row * 4], size_hint_x=0.4, size_hint_y=None, height="70sp",
                             font_size='14sp')
            self.d.append(lol3)
            self.fp.add_widget(self.d[row])

    def plus(self):
        if self.bold == 0:
            self.bold = 1
            self.plus1 = TextInput(text=''
                                   , size_hint_x=0.13, size_hint_y=None, height="70sp")
            self.a.append(self.plus1)
            self.fp.add_widget(self.a[self.loop])
            self.plus2 = TextInput(text=''
                                   , size_hint_x=0.4, size_hint_y=None, height="70sp")
            self.b.append(self.plus2)
            self.fp.add_widget(self.b[self.loop])
            self.plus3 = TextInput(text=''
                                   , size_hint_x=0.8, size_hint_y=None, height="70sp")
            self.c.append(self.plus3)
            self.fp.add_widget(self.c[self.loop])
            self.plus4 = TextInput(text=''
                                   , size_hint_x=0.4, size_hint_y=None, height="70sp")
            self.d.append(self.plus4)
            self.fp.add_widget(self.d[self.loop])
        else:
            pass

    def minus(self):
        if self.bold == 1:
            self.bold = 0
            self.fp.remove_widget(self.a[self.loop])
            self.fp.remove_widget(self.b[self.loop])
            self.fp.remove_widget(self.c[self.loop])
            self.fp.remove_widget(self.d[self.loop])
            self.a.remove(self.plus1)
            self.b.remove(self.plus2)
            self.c.remove(self.plus3)
            self.d.remove(self.plus4)
        else:
            pass

    def left(self):
        try:
            global worksht
            try:
                for row in range(self.looop):
                    self.fp.remove_widget(self.aa[row])
                    self.fp.remove_widget(self.bb[row])
                    self.fp.remove_widget(self.cc[row])
                    self.fp.remove_widget(self.dd[row])
                self.doyou = 1
            except:
                pass
            try:
                self.fp.remove_widget(self.a[self.loop])
                self.fp.remove_widget(self.b[self.loop])
                self.fp.remove_widget(self.c[self.loop])
                self.fp.remove_widget(self.d[self.loop])
                self.a.remove(self.plus1)
                self.b.remove(self.plus2)
                self.c.remove(self.plus3)
                self.d.remove(self.plus4)
            except:
                pass
            spreadsht.worksheet("title", str((date.today() + timedelta(days=(self.i - 1))).strftime("%d.%m.%Y")))
            self.i -= 1
            worksht = spreadsht.worksheet("title", str((date.today() + timedelta(days=self.i)).strftime("%d.%m.%Y")))
            for row in range(int(self.loop)):
                self.fp.remove_widget(self.a[row])
                self.fp.remove_widget(self.b[row])
                self.fp.remove_widget(self.c[row])
                self.fp.remove_widget(self.d[row])
            self.today = today + timedelta(days=self.i)
            self.today = self.today.strftime("%d.%m.%Y")
            self.time.text = str(self.today)
            self.bold = 0
            self.loop = int(worksht.cell(f"B{1}").value)
            self.a = []
            self.b = []
            self.c = []
            self.d = []
            lopux = str(worksht.cell(f"A{1}").value).split(';')
            for row in range(int(self.loop)):
                lol = TextInput(text=lopux[0 + row * 4], size_hint_x=0.13, size_hint_y=None, height="70sp",
                                font_size='14sp')
                self.a.append(lol)
                self.fp.add_widget(self.a[row])
                lol1 = TextInput(text=lopux[1 + row * 4], size_hint_x=0.4, size_hint_y=None, height="70sp",
                                 font_size='14sp')
                self.b.append(lol1)
                self.fp.add_widget(self.b[row])
                lol2 = TextInput(text=lopux[2 + row * 4], size_hint_x=0.8, size_hint_y=None, height="70sp",
                                 font_size='14sp')
                self.c.append(lol2)
                self.fp.add_widget(self.c[row])
                lol3 = TextInput(text=lopux[3 + row * 4], size_hint_x=0.4, size_hint_y=None, height="70sp",
                                 font_size='14sp')
                self.d.append(lol3)
                self.fp.add_widget(self.d[row])
        except:
            return self.i

    def right(self):
        global worksht
        if self.i == 0:
            return self.i
        else:
            try:
                for row in range(self.looop):
                    self.fp.remove_widget(self.aa[row])
                    self.fp.remove_widget(self.bb[row])
                    self.fp.remove_widget(self.cc[row])
                    self.fp.remove_widget(self.dd[row])
                self.doyou = 1
            except:
                pass
            try:
                self.fp.remove_widget(self.a[self.loop])
                self.fp.remove_widget(self.b[self.loop])
                self.fp.remove_widget(self.c[self.loop])
                self.fp.remove_widget(self.d[self.loop])
                self.a.remove(self.plus1)
                self.b.remove(self.plus2)
                self.c.remove(self.plus3)
                self.d.remove(self.plus4)
            except:
                pass
            for row in range(int(self.loop)):
                self.fp.remove_widget(self.a[row])
                self.fp.remove_widget(self.b[row])
                self.fp.remove_widget(self.c[row])
                self.fp.remove_widget(self.d[row])
            self.i += 1
            self.today = today + timedelta(days=self.i)
            self.today = self.today.strftime("%d.%m.%Y")
            self.time.text = str(self.today)
            worksht = spreadsht.worksheet("title", (date.today() + timedelta(days=self.i)).strftime("%d.%m.%Y"))
            self.bold = 0
            self.loop = int(worksht.cell(f"B{1}").value)
            self.a = []
            self.b = []
            self.c = []
            self.d = []
            lopux = str(worksht.cell(f"A{1}").value).split(';')
            for row in range(self.loop):
                lol = TextInput(text=lopux[0 + row * 4], size_hint_x=0.13, size_hint_y=None, height="70sp",
                                font_size='14sp')
                self.a.append(lol)
                self.fp.add_widget(self.a[row])
                lol1 = TextInput(text=lopux[1 + row * 4], size_hint_x=0.4, size_hint_y=None, height="70sp",
                                 font_size='14sp')
                self.b.append(lol1)
                self.fp.add_widget(self.b[row])
                lol2 = TextInput(text=lopux[2 + row * 4], size_hint_x=0.8, size_hint_y=None, height="70sp",
                                 font_size='14sp')
                self.c.append(lol2)
                self.fp.add_widget(self.c[row])
                lol3 = TextInput(text=lopux[3 + row * 4], size_hint_x=0.4, size_hint_y=None, height="70sp",
                                 font_size='14sp')
                self.d.append(lol3)
                self.fp.add_widget(self.d[row])

    def save(self):
        global worksht
        if self.doyou == 1:
            self.loop = int(worksht.cell(f"B{1}").value)
            cols = str()
            for row in range(self.loop):
                tryu = str(str(self.a[row].text) + ";" + str(self.b[row].text) + ";" + str(
                    self.c[row].text) + ";" + str(self.d[row].text) + ";")
                cols += tryu
            worksht.cell(f"A{1}").value = cols
            if self.bold == 1:
                self.bold = 0
                worksht.cell(f"A{1}").value = str(worksht.cell(f"A{1}").value) + str(
                    self.a[self.loop].text) + ";" + str(self.b[self.loop].text) + ";" \
                                              + str(self.c[self.loop].text) + ";" + str(self.d[self.loop].text) + ";"
                worksht.cell(f"B{1}").value = self.loop + 1
                self.loop += 1
            else:
                pass

    def search_do(self):
        if self.search.text == "":
            return self.search.text
        self.tab = 0
        try:
            for row in range(self.looop):
                self.fp.remove_widget(self.aa[row])
                self.fp.remove_widget(self.bb[row])
                self.fp.remove_widget(self.cc[row])
                self.fp.remove_widget(self.dd[row])
        except:
            pass
        if self.bold == 1:
            self.bold = 0
            self.fp.remove_widget(self.a[self.loop])
            self.fp.remove_widget(self.b[self.loop])
            self.fp.remove_widget(self.c[self.loop])
            self.fp.remove_widget(self.d[self.loop])
            self.a.remove(self.plus1)
            self.b.remove(self.plus2)
            self.c.remove(self.plus3)
            self.d.remove(self.plus4)
        try:
            self.aa = []
            self.bb = []
            self.cc = []
            self.dd = []
            self.looop = 0
            while self.tab != 30:
                workshs = spreadsht.worksheet("title", (date.today() - timedelta(days=self.tab)).strftime("%d.%m.%Y"))
                self.tab += 1
                try:
                    for row in range(int(worksht.cell(f"B{1}").value)):
                        self.fp.remove_widget(self.a[row])
                        self.fp.remove_widget(self.b[row])
                        self.fp.remove_widget(self.c[row])
                        self.fp.remove_widget(self.d[row])
                except:
                    pass
                self.loop = int(workshs.cell(f"B{1}").value)
                self.a = []
                self.b = []
                self.c = []
                self.d = []
                lopux = str(workshs.cell(f"A{1}").value).split(';')
                for row in range(int(self.loop)):
                    lol = TextInput(text=lopux[0 + row * 4], size_hint_x=0.13, size_hint_y=None, height="70sp",
                                    font_size='14sp')
                    self.a.append(lol)
                    lol1 = TextInput(text=lopux[1 + row * 4], size_hint_x=0.4, size_hint_y=None, height="70sp",
                                     font_size='14sp')
                    self.b.append(lol1)
                    lol2 = TextInput(text=lopux[2 + row * 4], size_hint_x=0.8, size_hint_y=None, height="70sp",
                                     font_size='14sp')
                    self.c.append(lol2)
                    lol3 = TextInput(text=lopux[3 + row * 4], size_hint_x=0.4, size_hint_y=None, height="70sp",
                                     font_size='14sp')
                    self.d.append(lol3)
                for row in range(int(workshs.cell(f"B{1}").value)):
                    if self.search.text == str(self.b[row].text):
                        for loop in range(1):
                            lol = TextInput(text=self.a[row].text, size_hint_x=0.13, size_hint_y=None, height="70sp",
                                            font_size='14sp')
                            self.aa.append(lol)
                            self.fp.add_widget(self.aa[self.looop])
                            lol1 = TextInput(text=self.b[row].text, size_hint_x=0.4, size_hint_y=None, height="70sp",
                                             font_size='14sp')
                            self.bb.append(lol1)
                            self.fp.add_widget(self.bb[self.looop])
                            lol2 = TextInput(text=self.c[row].text, size_hint_x=0.8, size_hint_y=None, height="70sp",
                                             font_size='14sp')
                            self.cc.append(lol2)
                            self.fp.add_widget(self.cc[self.looop])
                            lol3 = TextInput(text=self.d[row].text, size_hint_x=0.4, size_hint_y=None, height="70sp",
                                             font_size='14sp')
                            self.dd.append(lol3)
                            self.fp.add_widget(self.dd[self.looop])
                            self.looop += 1
                        self.bold = 2
                        self.doyou = 0
                    else:
                        pass
        except:
            pass

    def clean_do(self):
        try:
            for row in range(self.looop):
                self.fp.remove_widget(self.aa[row])
                self.fp.remove_widget(self.bb[row])
                self.fp.remove_widget(self.cc[row])
                self.fp.remove_widget(self.dd[row])
            for row in range(self.loop):
                self.fp.remove_widget(self.a[row])
                self.fp.remove_widget(self.b[row])
                self.fp.remove_widget(self.c[row])
                self.fp.remove_widget(self.d[row])
            workshs = spreadsht.worksheet("title", self.time.text)
            self.a = []
            self.b = []
            self.c = []
            self.d = []
            self.loop = int(workshs.cell(f"B{1}").value)
            lopux = str(workshs.cell(f"A{1}").value).split(';')
            for row in range(self.loop):
                lol = TextInput(text=lopux[0 + row * 4], size_hint_x=0.13, size_hint_y=None, height="70sp",
                                font_size='14sp')
                self.a.append(lol)
                self.fp.add_widget(self.a[row])
                lol1 = TextInput(text=lopux[1 + row * 4], size_hint_x=0.4, size_hint_y=None, height="70sp",
                                 font_size='14sp')
                self.b.append(lol1)
                self.fp.add_widget(self.b[row])
                lol2 = TextInput(text=lopux[2 + row * 4], size_hint_x=0.8, size_hint_y=None, height="70sp",
                                 font_size='14sp')
                self.c.append(lol2)
                self.fp.add_widget(self.c[row])
                lol3 = TextInput(text=lopux[3 + row * 4], size_hint_x=0.4, size_hint_y=None, height="70sp",
                                 font_size='14sp')
                self.d.append(lol3)
                self.fp.add_widget(self.d[row])
            self.bold = 0
            self.doyou = 1
            self.search.text = ""
        except:
            self.search.text = ""


class Container_locodrom(Screen):
    def __init__(self, **kwargs):
        super(Container_locodrom, self).__init__(**kwargs)
        self.today = today.strftime("%d.%m.%Y")
        self.time.text = str(self.today)
        self.bold1 = 0
        self.e = []
        self.f = []
        self.g = []
        self.h = []
        self.k = 0
        self.doyou = 1
        self.loop1 = int(worksht.cell(f"E{1}").value)
        lopux = str(worksht.cell(f"D{1}").value).split(';')
        for row in range(self.loop1):
            lol = TextInput(text=lopux[0 + row * 4], size_hint_x=0.13, size_hint_y=None, height="70sp",
                            font_size='14sp')
            self.e.append(lol)
            self.fl.add_widget(self.e[row])
            lol1 = TextInput(text=lopux[1 + row * 4], size_hint_x=0.4, size_hint_y=None, height="70sp",
                             font_size='14sp')
            self.f.append(lol1)
            self.fl.add_widget(self.f[row])
            lol2 = TextInput(text=lopux[2 + row * 4], size_hint_x=0.8, size_hint_y=None, height="70sp",
                             font_size='14sp')
            self.g.append(lol2)
            self.fl.add_widget(self.g[row])
            lol3 = TextInput(text=lopux[3 + row * 4], size_hint_x=0.4, size_hint_y=None, height="70sp",
                             font_size='14sp')
            self.h.append(lol3)
            self.fl.add_widget(self.h[row])

    def plus(self):
        if self.bold1 == 0:
            self.bold1 = 1
            self.plus11 = TextInput(text='', size_hint_x=0.13, size_hint_y=None, height="70sp")
            self.e.append(self.plus11)
            self.fl.add_widget(self.e[self.loop1])
            self.plus22 = TextInput(text='', size_hint_x=0.4, size_hint_y=None, height="70sp")
            self.f.append(self.plus22)
            self.fl.add_widget(self.f[self.loop1])
            self.plus33 = TextInput(text='', size_hint_x=0.8, size_hint_y=None, height="70sp")
            self.g.append(self.plus33)
            self.fl.add_widget(self.g[self.loop1])
            self.plus44 = TextInput(text='', size_hint_x=0.4, size_hint_y=None, height="70sp")
            self.h.append(self.plus44)
            self.fl.add_widget(self.h[self.loop1])
        else:
            pass

    def minus(self):
        if self.bold1 == 1:
            self.bold1 = 0
            self.fl.remove_widget(self.e[self.loop1])
            self.fl.remove_widget(self.f[self.loop1])
            self.fl.remove_widget(self.g[self.loop1])
            self.fl.remove_widget(self.h[self.loop1])
            self.e.remove(self.plus11)
            self.f.remove(self.plus22)
            self.g.remove(self.plus33)
            self.h.remove(self.plus44)
        else:
            pass

    def left(self):
        global worksht
        try:
            spreadsht.worksheet("title", str((date.today() + timedelta(days=(self.k - 1))).strftime("%d.%m.%Y")))
            self.k -= 1
            worksht = spreadsht.worksheet("title", str((date.today() + timedelta(days=self.k)).strftime("%d.%m.%Y")))
            try:
                for row in range(self.looop):
                    self.fl.remove_widget(self.aa[row])
                    self.fl.remove_widget(self.bb[row])
                    self.fl.remove_widget(self.cc[row])
                    self.fl.remove_widget(self.dd[row])
                self.doyou = 1
            except:
                pass
            try:
                for row in range(self.loop1):
                    self.fl.remove_widget(self.e[row])
                    self.fl.remove_widget(self.f[row])
                    self.fl.remove_widget(self.g[row])
                    self.fl.remove_widget(self.h[row])
            except:
                pass
            try:
                self.fl.remove_widget(self.e[self.loop1])
                self.fl.remove_widget(self.f[self.loop1])
                self.fl.remove_widget(self.g[self.loop1])
                self.fl.remove_widget(self.h[self.loop1])
                self.e.remove(self.plus11)
                self.f.remove(self.plus22)
                self.g.remove(self.plus33)
                self.h.remove(self.plus44)
            except:
                pass
            self.today = today + timedelta(days=self.k)
            self.today = self.today.strftime("%d.%m.%Y")
            self.time.text = str(self.today)
            self.bold1 = 0
            self.loop1 = int(worksht.cell(f"E{1}").value)
            self.e = []
            self.f = []
            self.g = []
            self.h = []
            lopux = str(worksht.cell(f"D{1}").value).split(';')
            for row in range(self.loop1):
                lol = TextInput(text=lopux[0 + row * 4], size_hint_x=0.13, size_hint_y=None, height="70sp",
                                font_size='14sp')
                self.e.append(lol)
                self.fl.add_widget(self.e[row])
                lol1 = TextInput(text=lopux[1 + row * 4], size_hint_x=0.4, size_hint_y=None, height="70sp",
                                 font_size='14sp')
                self.f.append(lol1)
                self.fl.add_widget(self.f[row])
                lol2 = TextInput(text=lopux[2 + row * 4], size_hint_x=0.8, size_hint_y=None, height="70sp",
                                 font_size='14sp')
                self.g.append(lol2)
                self.fl.add_widget(self.g[row])
                lol3 = TextInput(text=lopux[3 + row * 4], size_hint_x=0.4, size_hint_y=None, height="70sp",
                                 font_size='14sp')
                self.h.append(lol3)
                self.fl.add_widget(self.h[row])
        except:
            return self.k

    def right(self):
        global worksht
        if self.k == 0:
            return self.k
        else:
            try:
                for row in range(self.looop):
                    self.fl.remove_widget(self.aa[row])
                    self.fl.remove_widget(self.bb[row])
                    self.fl.remove_widget(self.cc[row])
                    self.fl.remove_widget(self.dd[row])
                self.doyou = 1
            except:
                pass
            try:
                for row in range(self.loop1):
                    self.fl.remove_widget(self.e[row])
                    self.fl.remove_widget(self.f[row])
                    self.fl.remove_widget(self.g[row])
                    self.fl.remove_widget(self.h[row])
            except:
                pass
            try:
                self.fl.remove_widget(self.e[self.loop1])
                self.fl.remove_widget(self.f[self.loop1])
                self.fl.remove_widget(self.g[self.loop1])
                self.fl.remove_widget(self.h[self.loop1])
                self.e.remove(self.plus11)
                self.f.remove(self.plus22)
                self.g.remove(self.plus33)
                self.h.remove(self.plus44)
            except:
                pass
            self.k += 1
            self.today = today + timedelta(days=self.k)
            self.today = self.today.strftime("%d.%m.%Y")
            self.time.text = str(self.today)
            worksht = spreadsht.worksheet("title", (date.today() + timedelta(days=self.k)).strftime("%d.%m.%Y"))
            self.bold1 = 0
            self.loop1 = int(worksht.cell(f"E{1}").value)
            self.e = []
            self.f = []
            self.g = []
            self.h = []
            lopux = str(worksht.cell(f"D{1}").value).split(';')
            for row in range(self.loop1):
                lol = TextInput(text=lopux[0 + row * 4], size_hint_x=0.13, size_hint_y=None, height="70sp",
                                font_size='14sp')
                self.e.append(lol)
                self.fl.add_widget(self.e[row])
                lol1 = TextInput(text=lopux[1 + row * 4], size_hint_x=0.4, size_hint_y=None, height="70sp",
                                 font_size='14sp')
                self.f.append(lol1)
                self.fl.add_widget(self.f[row])
                lol2 = TextInput(text=lopux[2 + row * 4], size_hint_x=0.8, size_hint_y=None, height="70sp",
                                 font_size='14sp')
                self.g.append(lol2)
                self.fl.add_widget(self.g[row])
                lol3 = TextInput(text=lopux[3 + row * 4], size_hint_x=0.4, size_hint_y=None, height="70sp",
                                 font_size='14sp')
                self.h.append(lol3)
                self.fl.add_widget(self.h[row])

    def save(self):
        global worksht
        if self.doyou == 1:
            self.loop1 = int(worksht.cell(f"E{1}").value)
            cols = str()
            for row in range(self.loop1):
                tryu = str(str(self.e[row].text) + ";" + str(self.f[row].text) + ";" + str(
                    self.g[row].text) + ";" + str(self.h[row].text) + ";")
                cols += tryu
            worksht.cell(f"D{1}").value = cols
            if self.bold1 == 1:
                self.bold1 = 0
                worksht.cell(f"D{1}").value = str(worksht.cell(f"D{1}").value) + str(
                    self.e[self.loop1].text) + ";" + str(self.f[self.loop1].text) + ";" \
                                              + str(self.g[self.loop1].text) + ";" + str(self.h[self.loop1].text) + ";"
                worksht.cell(f"E{1}").value = self.loop1 + 1
                self.loop1 += 1
            else:
                pass

    def search_do(self):
        if self.search.text == "":
            return self.search.text
        try:
            self.tab = 0
            try:
                for row in range(self.looop):
                    self.fl.remove_widget(self.aa[row])
                    self.fl.remove_widget(self.bb[row])
                    self.fl.remove_widget(self.cc[row])
                    self.fl.remove_widget(self.dd[row])
            except:
                pass
            try:
                if self.bold1 == 1:
                    self.bold1 = 0
                    self.fl.remove_widget(self.e[self.loop1])
                    self.fl.remove_widget(self.f[self.loop1])
                    self.fl.remove_widget(self.g[self.loop1])
                    self.fl.remove_widget(self.h[self.loop1])
                    self.e.remove(self.plus11)
                    self.f.remove(self.plus22)
                    self.g.remove(self.plus33)
                    self.h.remove(self.plus44)
            except:
                pass
            try:
                self.aa = []
                self.bb = []
                self.cc = []
                self.dd = []
                self.looop = 0
                while self.tab != 30:
                    workshs = spreadsht.worksheet("title", (date.today() - timedelta(days=self.tab)).strftime(
                        "%d.%m.%Y"))
                    self.tab += 1
                    try:
                        for row in range(int(worksht.cell(f"E{1}").value)):
                            self.fl.remove_widget(self.e[row])
                            self.fl.remove_widget(self.f[row])
                            self.fl.remove_widget(self.g[row])
                            self.fl.remove_widget(self.h[row])
                    except:
                        pass
                    self.loop1 = int(workshs.cell(f"E{1}").value)
                    self.e = []
                    self.f = []
                    self.g = []
                    self.h = []
                    lopux = str(workshs.cell(f"D{1}").value).split(';')
                    for row in range(int(self.loop1)):
                        lol = TextInput(text=lopux[0 + row * 4], size_hint_x=0.13, size_hint_y=None,
                                        height="70sp",
                                        font_size='14sp')
                        self.e.append(lol)
                        lol1 = TextInput(text=lopux[1 + row * 4], size_hint_x=0.4, size_hint_y=None,
                                         height="70sp",
                                         font_size='14sp')
                        self.f.append(lol1)
                        lol2 = TextInput(text=lopux[2 + row * 4], size_hint_x=0.8, size_hint_y=None,
                                         height="70sp",
                                         font_size='14sp')
                        self.g.append(lol2)
                        lol3 = TextInput(text=lopux[3 + row * 4], size_hint_x=0.4, size_hint_y=None,
                                         height="70sp",
                                         font_size='14sp')
                        self.h.append(lol3)
                    for row in range(int(workshs.cell(f"E{1}").value)):
                        if self.search.text == str(self.f[row].text):
                            for loop in range(1):
                                lol = TextInput(text=self.e[row].text, size_hint_x=0.13, size_hint_y=None,
                                                height="70sp",
                                                font_size='14sp')
                                self.aa.append(lol)
                                self.fl.add_widget(self.aa[self.looop])
                                lol1 = TextInput(text=self.f[row].text, size_hint_x=0.4, size_hint_y=None,
                                                 height="70sp",
                                                 font_size='14sp')
                                self.bb.append(lol1)
                                self.fl.add_widget(self.bb[self.looop])
                                lol2 = TextInput(text=self.g[row].text, size_hint_x=0.8, size_hint_y=None,
                                                 height="70sp",
                                                 font_size='14sp')
                                self.cc.append(lol2)
                                self.fl.add_widget(self.cc[self.looop])
                                lol3 = TextInput(text=self.h[row].text, size_hint_x=0.4, size_hint_y=None,
                                                 height="70sp",
                                                 font_size='14sp')
                                self.dd.append(lol3)
                                self.fl.add_widget(self.dd[self.looop])
                                self.looop += 1
                            self.bold = 2
                            self.doyou = 0
                        else:
                            pass
            except:
                pass
        except:
            pass

    def clean_do(self):
        try:
            for row in range(self.looop):
                self.fl.remove_widget(self.aa[row])
                self.fl.remove_widget(self.bb[row])
                self.fl.remove_widget(self.cc[row])
                self.fl.remove_widget(self.dd[row])
            for row in range(self.loop1):
                self.fl.remove_widget(self.e[row])
                self.fl.remove_widget(self.f[row])
                self.fl.remove_widget(self.g[row])
                self.fl.remove_widget(self.h[row])
            self.e = []
            self.f = []
            self.g = []
            self.h = []
            workshs = spreadsht.worksheet("title", self.time.text)
            self.loop1 = int(workshs.cell(f"E{1}").value)
            lopux = str(workshs.cell(f"D{1}").value).split(';')
            for row in range(self.loop1):
                lol = TextInput(text=lopux[0 + row * 4], size_hint_x=0.13, size_hint_y=None, height="70sp",
                                font_size='14sp')
                self.e.append(lol)
                self.fl.add_widget(self.e[row])
                lol1 = TextInput(text=lopux[1 + row * 4], size_hint_x=0.4, size_hint_y=None, height="70sp",
                                 font_size='14sp')
                self.f.append(lol1)
                self.fl.add_widget(self.f[row])
                lol2 = TextInput(text=lopux[2 + row * 4], size_hint_x=0.8, size_hint_y=None, height="70sp",
                                 font_size='14sp')
                self.g.append(lol2)
                self.fl.add_widget(self.g[row])
                lol3 = TextInput(text=lopux[3 + row * 4], size_hint_x=0.4, size_hint_y=None, height="70sp",
                                 font_size='14sp')
                self.h.append(lol3)
                self.fl.add_widget(self.h[row])
            self.bold1 = 0
            self.doyou = 1
            self.search.text = ""
        except:
            self.search.text = ""


class Other(Screen):
    pass


class Journal_Sistem(Screen):
    def __init__(self, **kwargs):
        super(Journal_Sistem, self).__init__(**kwargs)
        self.today = today.strftime("%d.%m.%Y")
        self.l = 1
        self.number.text = str(self.l) + " страница"
        self.minus = int(workshtt.cell(f"E{1}").value)
        self.a = []
        self.b = []
        self.c = []
        self.d = []
        try:
            if workshtt.cell(f"D{1}").value < date.today().strftime("%d.%m.%Y"):
                workshtt.cell(f"D{1}").value = (date.today() + timedelta(days=9)).strftime("%d.%m.%Y")
                workshtt.cell(f"E{1}").value = str(int(workshtt.cell(f"E{1}").value) + 1)
                self.minus = int(workshtt.cell(f"E{1}").value)
                workshtt.cell(f"A{str(self.minus)}").value = ";;;;" * 10
                lopux = str(workshtt.cell(f"A{str(self.minus)}").value).split(';')
                for row in range(10):
                    lol = TextInput(text=lopux[0 + row * 4], size_hint_x=0.25, height="30sp",
                                    font_size='13sp')
                    self.a.append(lol)
                    self.js.add_widget(self.a[row])
                    lol1 = TextInput(text=lopux[1 + row * 4], size_hint_x=0.3, height="30sp",
                                     font_size='13sp')
                    self.b.append(lol1)
                    self.js.add_widget(self.b[row])
                    lol2 = TextInput(text=lopux[2 + row * 4], size_hint_x=0.25, height="30sp",
                                     font_size='13sp')
                    self.c.append(lol2)
                    self.js.add_widget(self.c[row])
                    lol3 = TextInput(text=lopux[3 + row * 4], size_hint_x=0.25, height="30sp",
                                     font_size='13sp')
                    self.d.append(lol3)
                    self.js.add_widget(self.d[row])
                cols = str()
                for row in range(10):
                    self.a[row].text = (date.today() + timedelta(days=9) - timedelta(days=row)).strftime("%d.%m.%Y")
                    tryu = str(str(self.a[row].text) + ";" + str(self.b[row].text) + ";" + str(
                        self.c[row].text) + ";" + str(self.d[row].text) + ";")
                    cols += tryu
                workshtt.cell(f"A{str(self.minus)}").value = cols
        except:
            pass
        try:
            lopux = str(workshtt.cell(f"A{str(self.minus)}").value).split(';')
            for row in range(10):
                lol = TextInput(text=lopux[0 + row * 4], size_hint_x=0.25, height="30sp",
                                font_size='13sp')
                self.a.append(lol)
                self.js.add_widget(self.a[row])
                lol1 = TextInput(text=lopux[1 + row * 4], size_hint_x=0.3, height="30sp",
                                 font_size='13sp')
                self.b.append(lol1)
                self.js.add_widget(self.b[row])
                lol2 = TextInput(text=lopux[2 + row * 4], size_hint_x=0.25, height="30sp",
                                 font_size='13sp')
                self.c.append(lol2)
                self.js.add_widget(self.c[row])
                lol3 = TextInput(text=lopux[3 + row * 4], size_hint_x=0.25, height="30sp",
                                 font_size='13sp')
                self.d.append(lol3)
                self.js.add_widget(self.d[row])
        except:
            pass

    def left(self):
        global workshtt
        self.l -= 1
        if self.l == 0:
            self.l += 1
            return self.l
        for row in range(int(10)):
            self.js.remove_widget(self.a[row])
            self.js.remove_widget(self.b[row])
            self.js.remove_widget(self.c[row])
            self.js.remove_widget(self.d[row])
        self.a = []
        self.b = []
        self.c = []
        self.d = []
        self.number.text = str(self.l) + " страница"
        self.minus += 1
        lopux = str(workshtt.cell(f"A{str(self.minus)}").value).split(';')
        for row in range(10):
            lol = TextInput(text=lopux[0 + row * 4], size_hint_x=0.25, height="30sp",
                            font_size='13sp', scroll_y=0)
            self.a.append(lol)
            self.js.add_widget(self.a[row])
            lol1 = TextInput(text=lopux[1 + row * 4], size_hint_x=0.3, height="30sp",
                             font_size='13sp', scroll_y=0)
            self.b.append(lol1)
            self.js.add_widget(self.b[row])
            lol2 = TextInput(text=lopux[2 + row * 4], size_hint_x=0.25, height="30sp",
                             font_size='13sp', scroll_y=0)
            self.c.append(lol2)
            self.js.add_widget(self.c[row])
            lol3 = TextInput(text=lopux[3 + row * 4], size_hint_x=0.25, height="30sp",
                             font_size='13sp', scroll_y=0)
            self.d.append(lol3)
            self.js.add_widget(self.d[row])

    def right(self):
        global workshtt
        try:
            self.minus -= 1
            if self.minus == 0:
                self.minus += 1
                return self.minus
            for row in range(int(10)):
                self.js.remove_widget(self.a[row])
                self.js.remove_widget(self.b[row])
                self.js.remove_widget(self.c[row])
                self.js.remove_widget(self.d[row])
            self.a = []
            self.b = []
            self.c = []
            self.d = []
            lopux = str(workshtt.cell(f"A{str(self.minus)}").value).split(';')
            self.l += 1
            self.number.text = str(self.l) + " страница"
            for row in range(10):
                lol = TextInput(text=lopux[0 + row * 4], size_hint_x=0.25, height="30sp",
                                font_size='13sp', scroll_y=0)
                self.a.append(lol)
                self.js.add_widget(self.a[row])
                lol1 = TextInput(text=lopux[1 + row * 4], size_hint_x=0.3, height="30sp",
                                 font_size='13sp', scroll_y=0)
                self.b.append(lol1)
                self.js.add_widget(self.b[row])
                lol2 = TextInput(text=lopux[2 + row * 4], size_hint_x=0.25, height="30sp",
                                 font_size='13sp', scroll_y=0)
                self.c.append(lol2)
                self.js.add_widget(self.c[row])
                lol3 = TextInput(text=lopux[3 + row * 4], size_hint_x=0.25, height="30sp",
                                 font_size='13sp', scroll_y=0)
                self.d.append(lol3)
                self.js.add_widget(self.d[row])
        except:
            pass

    def save(self):
        col = str()
        for row in range(10):
            tryy = str(str(self.a[row].text) + ";" + str(self.b[row].text) + ";" + str(
                self.c[row].text) + ";" + str(self.d[row].text) + ";")
            col += tryy
        workshtt.cell(f"A{self.minus}").value = col


class Journal_Locodrom(Screen):
    def __init__(self, **kwargs):
        super(Journal_Locodrom, self).__init__(**kwargs)
        self.today = today.strftime("%d.%m.%Y")
        self.l = 1
        self.number_l.text = str(self.l) + " страница"
        self.minus = int(workshtl.cell(f"E{1}").value)
        self.aa = []
        self.bb = []
        self.cc = []
        self.dd = []
        try:
            if workshtl.cell(f"D{1}").value < date.today().strftime("%d.%m.%Y"):
                workshtl.cell(f"D{1}").value = (date.today() + timedelta(days=9)).strftime("%d.%m.%Y")
                workshtl.cell(f"E{1}").value = str(int(workshtl.cell(f"E{1}").value) + 1)
                self.minus = int(workshtl.cell(f"E{1}").value)
                workshtl.cell(f"A{str(self.minus)}").value = ";;;;" * 10
                lopux = str(workshtl.cell(f"A{str(self.minus)}").value).split(';')
                for row in range(10):
                    lol = TextInput(text=lopux[0 + row * 4], size_hint_x=0.25, height="30sp",
                                    font_size='13sp')
                    self.aa.append(lol)
                    self.jl.add_widget(self.aa[row])
                    lol1 = TextInput(text=lopux[1 + row * 4], size_hint_x=0.25, height="30sp",
                                     font_size='13sp')
                    self.bb.append(lol1)
                    self.jl.add_widget(self.bb[row])
                    lol2 = TextInput(text=lopux[2 + row * 4], size_hint_x=0.3, height="30sp",
                                     font_size='13sp')
                    self.cc.append(lol2)
                    self.jl.add_widget(self.cc[row])
                    lol3 = TextInput(text=lopux[3 + row * 4], size_hint_x=0.25, height="30sp",
                                     font_size='13sp')
                    self.dd.append(lol3)
                    self.jl.add_widget(self.dd[row])
                cols = str()
                for row in range(10):
                    self.aa[row].text = (date.today() + timedelta(days=9) - timedelta(days=row)).strftime("%d.%m.%Y")
                    tryu = str(str(self.aa[row].text) + ";" + str(self.bb[row].text) + ";" + str(
                        self.cc[row].text) + ";" + str(self.dd[row].text) + ";")
                    cols += tryu
                workshtl.cell(f"A{str(self.minus)}").value = cols
        except:
            pass
        try:
            lopux = str(workshtl.cell(f"A{str(self.minus)}").value).split(';')
            for row in range(10):
                lol = TextInput(text=lopux[0 + row * 4], size_hint_x=0.25, height="30sp",
                                font_size='13sp')
                self.aa.append(lol)
                self.jl.add_widget(self.aa[row])
                lol1 = TextInput(text=lopux[1 + row * 4], size_hint_x=0.25, height="30sp",
                                 font_size='13sp')
                self.bb.append(lol1)
                self.jl.add_widget(self.bb[row])
                lol2 = TextInput(text=lopux[2 + row * 4], size_hint_x=0.3, height="30sp",
                                 font_size='13sp')
                self.cc.append(lol2)
                self.jl.add_widget(self.cc[row])
                lol3 = TextInput(text=lopux[3 + row * 4], size_hint_x=0.25, height="30sp",
                                 font_size='13sp')
                self.dd.append(lol3)
                self.jl.add_widget(self.dd[row])
        except:
            pass

    def left(self):
        global workshtl
        if self.l == 1:
            return self.l
        for row in range(int(10)):
            self.jl.remove_widget(self.aa[row])
            self.jl.remove_widget(self.bb[row])
            self.jl.remove_widget(self.cc[row])
            self.jl.remove_widget(self.dd[row])
        self.aa = []
        self.bb = []
        self.cc = []
        self.dd = []
        self.l -= 1
        self.number_l.text = str(self.l) + " страница"
        self.minus += 1
        lopux = str(workshtl.cell(f"A{str(self.minus)}").value).split(';')
        for row in range(10):
            lol = TextInput(text=lopux[0 + row * 4], size_hint_x=0.25, height="30sp",
                            font_size='13sp')
            self.aa.append(lol)
            self.jl.add_widget(self.aa[row])
            lol1 = TextInput(text=lopux[1 + row * 4], size_hint_x=0.25, height="30sp",
                             font_size='13sp')
            self.bb.append(lol1)
            self.jl.add_widget(self.bb[row])
            lol2 = TextInput(text=lopux[2 + row * 4], size_hint_x=0.3, height="30sp",
                             font_size='13sp')
            self.cc.append(lol2)
            self.jl.add_widget(self.cc[row])
            lol3 = TextInput(text=lopux[3 + row * 4], size_hint_x=0.25, height="30sp",
                             font_size='13sp')
            self.dd.append(lol3)
            self.jl.add_widget(self.dd[row])

    def right(self):
        global workshtl
        try:
            self.minus -= 1
            if self.minus == 0:
                self.minus += 1
                return self.minus
            lopux = str(workshtl.cell(f"A{str(self.minus)}").value).split(';')
            for row in range(int(10)):
                self.jl.remove_widget(self.aa[row])
                self.jl.remove_widget(self.bb[row])
                self.jl.remove_widget(self.cc[row])
                self.jl.remove_widget(self.dd[row])
            self.aa = []
            self.bb = []
            self.cc = []
            self.dd = []
            self.l += 1
            self.number_l.text = str(self.l) + " страница"
            for row in range(10):
                lol = TextInput(text=lopux[0 + row * 4], size_hint_x=0.25, height="30sp",
                                font_size='13sp')
                self.aa.append(lol)
                self.jl.add_widget(self.aa[row])
                lol1 = TextInput(text=lopux[1 + row * 4], size_hint_x=0.25, height="30sp",
                                 font_size='13sp')
                self.bb.append(lol1)
                self.jl.add_widget(self.bb[row])
                lol2 = TextInput(text=lopux[2 + row * 4], size_hint_x=0.3, height="30sp",
                                 font_size='13sp')
                self.cc.append(lol2)
                self.jl.add_widget(self.cc[row])
                lol3 = TextInput(text=lopux[3 + row * 4], size_hint_x=0.25, height="30sp",
                                 font_size='13sp')
                self.dd.append(lol3)
                self.jl.add_widget(self.dd[row])
        except:
            pass

    def save(self):
        col = str()
        for row in range(10):
            tryy = str(str(self.aa[row].text) + ";" + str(self.bb[row].text) + ";" + str(
                self.cc[row].text) + ";" + str(self.dd[row].text) + ";")
            col += tryy
        workshtl.cell(f"A{self.minus}").value = col


class Journal_Sistem_S(Screen):
    def __init__(self, **kwargs):
        super(Journal_Sistem_S, self).__init__(**kwargs)
        self.today = today.strftime("%d.%m.%Y")
        self.l = 1
        self.bold = 0
        self.doyou = 1
        self.number.text = str(self.l) + " страница"
        self.minus = int(workshtt.cell(f"H{1}").value)
        self.plus = int(workshtt.cell(f"I{self.minus}").value)
        self.a = []
        self.b = []
        self.c = []
        try:
            lopux = str(workshtt.cell(f"G{str(self.minus)}").value).split(';')
            for row in range(int(self.plus)):
                lol = TextInput(text=lopux[0 + row * 3], size_hint_y=None, height="45sp",
                                font_size='13sp')
                self.a.append(lol)
                self.jss.add_widget(self.a[row])
                lol1 = TextInput(text=lopux[1 + row * 3], size_hint_y=None, height="45sp",
                                 font_size='13sp')
                self.b.append(lol1)
                self.jss.add_widget(self.b[row])
                lol2 = TextInput(text=lopux[2 + row * 3], size_hint_y=None, height="45sp",
                                 font_size='13sp')
                self.c.append(lol2)
                self.jss.add_widget(self.c[row])
        except:
            pass

    def left(self):
        global workshtt
        self.l -= 1
        if self.l == 0:
            self.l += 1
            return self.l
        try:
            if self.bold == 1:
                self.bold = 0
                self.jss.remove_widget(self.a[int(self.plus)])
                self.jss.remove_widget(self.b[int(self.plus)])
                self.jss.remove_widget(self.c[int(self.plus)])
                self.a.remove(self.plus1)
                self.b.remove(self.plus2)
                self.c.remove(self.plus3)
        except:
            pass
        for row in range(int(10)):
            self.jss.remove_widget(self.a[row])
            self.jss.remove_widget(self.b[row])
            self.jss.remove_widget(self.c[row])
        self.a = []
        self.b = []
        self.c = []
        self.bold = 2
        self.minus += 1
        self.number.text = str(self.l) + " страница"
        self.plus = int(workshtt.cell(f"I{str(self.minus)}").value)
        if self.plus < 10:
            self.bold = 0
        try:
            lopux = str(workshtt.cell(f"G{str(self.minus)}").value).split(';')
            for row in range(int(self.plus)):
                lol = TextInput(text=lopux[0 + row * 3], size_hint_y=None, height="45sp",
                                font_size='13sp')
                self.a.append(lol)
                self.jss.add_widget(self.a[row])
                lol1 = TextInput(text=lopux[1 + row * 3], size_hint_y=None, height="45sp",
                                 font_size='13sp')
                self.b.append(lol1)
                self.jss.add_widget(self.b[row])
                lol2 = TextInput(text=lopux[2 + row * 3], size_hint_y=None, height="45sp",
                                 font_size='13sp')
                self.c.append(lol2)
                self.jss.add_widget(self.c[row])
        except:
            pass

    def right(self):
        global workshtt
        self.minus -= 1
        if self.minus == 0:
            self.minus += 1
            return self.minus
        try:
            if self.bold == 1:
                self.bold = 0
                self.jss.remove_widget(self.a[int(self.plus)])
                self.jss.remove_widget(self.b[int(self.plus)])
                self.jss.remove_widget(self.c[int(self.plus)])
                self.a.remove(self.plus1)
                self.b.remove(self.plus2)
                self.c.remove(self.plus3)
        except:
            pass
        for row in range(int(self.plus)):
            self.jss.remove_widget(self.a[row])
            self.jss.remove_widget(self.b[row])
            self.jss.remove_widget(self.c[row])
        self.plus = int(workshtt.cell(f"I{str(self.minus)}").value)
        self.bold = 2
        if self.plus < 10:
            self.bold = 0
        self.a = []
        self.b = []
        self.c = []
        self.l += 1
        self.number.text = str(self.l) + " страница"
        lopux = str(workshtt.cell(f"G{str(self.minus)}").value).split(';')
        for row in range(int(self.plus)):
            lol = TextInput(text=lopux[0 + row * 3], size_hint_y=None, height="45sp",
                            font_size='13sp')
            self.a.append(lol)
            self.jss.add_widget(self.a[row])
            lol1 = TextInput(text=lopux[1 + row * 3], size_hint_y=None, height="45sp",
                             font_size='13sp')
            self.b.append(lol1)
            self.jss.add_widget(self.b[row])
            lol2 = TextInput(text=lopux[2 + row * 3], size_hint_y=None, height="45sp",
                             font_size='13sp')
            self.c.append(lol2)
            self.jss.add_widget(self.c[row])

    def save(self):
        if self.bold == 1 and self.plus != 9 and self.plus != 10:
            workshtt.cell(f"I{self.minus}").value = str(int(workshtt.cell(f"I{self.minus}").value) + 1)
            self.bold = 0
            self.plus = int(workshtt.cell(f"I{self.minus}").value)
        cols = str()
        for row in range(int(self.plus)):
            tryu = str(str(self.a[row].text) + ";" + str(self.b[row].text) + ";" + str(
                self.c[row].text) + ";")
            cols += tryu
        workshtt.cell(f"G{str(self.minus)}").value = cols
        if self.plus == 9 and self.bold == 1:
            self.bold = 2
            workshtt.cell(f"I{self.minus}").value = str(int(workshtt.cell(f"I{self.minus}").value) + 1)
            self.plus = int(workshtt.cell(f"I{self.minus}").value)
            cols = str()
            for row in range(int(self.plus)):
                tryu = str(str(self.a[row].text) + ";" + str(self.b[row].text) + ";" + str(
                    self.c[row].text) + ";")
                cols += tryu
            workshtt.cell(f"G{str(self.minus)}").value = cols
            workshtt.cell(f"H{1}").value = str(int(workshtt.cell(f"H{1}").value) + 1)
            self.minus = int(workshtt.cell(f"H{1}").value)
            workshtt.cell(f"I{str(self.minus)}").value = str(0)
            self.l += 1
            self.number.text = str(self.l) + " страница"
            self.minus -= 1

    def plus_minus(self):
        try:
            if workshtt.cell(f"I{self.minus}").value == 10:
                return self.minus
            else:
                pass
            if self.bold == 0:
                self.bold = 1
                self.plus1 = TextInput(text="", size_hint_y=None, height="45sp",
                                       font_size='13sp')
                self.a.append(self.plus1)
                self.jss.add_widget(self.a[int(self.plus)])
                self.plus2 = TextInput(text="", size_hint_y=None, height="45sp",
                                       font_size='13sp')
                self.b.append(self.plus2)
                self.jss.add_widget(self.b[int(self.plus)])
                self.plus3 = TextInput(text="", size_hint_y=None, height="45sp",
                                       font_size='13sp')
                self.c.append(self.plus3)
                self.jss.add_widget(self.c[int(self.plus)])
            elif self.bold == 1:
                self.bold = 0
                self.jss.remove_widget(self.a[int(self.plus)])
                self.jss.remove_widget(self.b[int(self.plus)])
                self.jss.remove_widget(self.c[int(self.plus)])
                self.a.remove(self.plus1)
                self.b.remove(self.plus2)
                self.c.remove(self.plus3)
        except:
            pass

    def search_do(self):
        if self.search.text == "":
            return self.search.text
        try:
            try:
                if self.bold == 1:
                    self.bold = 0
                    self.jss.remove_widget(self.a[self.plus])
                    self.jss.remove_widget(self.b[self.plus])
                    self.jss.remove_widget(self.c[self.plus])
                    self.a.remove(self.plus1)
                    self.b.remove(self.plus2)
                    self.c.remove(self.plus3)
            except:
                pass
            try:
                for row in range(self.looop):
                    self.jss.remove_widget(self.aa[row])
                    self.jss.remove_widget(self.bb[row])
                    self.jss.remove_widget(self.cc[row])
            except:
                pass
            self.aa = []
            self.bb = []
            self.cc = []
            self.looop = 0
            self.pas = len(self.search.text)
            for row in range(int(workshtt.cell(f"I{str(self.minus)}").value)):
                self.jss.remove_widget(self.a[row])
                self.jss.remove_widget(self.b[row])
                self.jss.remove_widget(self.c[row])
                b = str()
                try:
                    for pok in range(self.pas):
                        b += str(self.b[row].text[pok])
                except:
                    pass
                if str(self.search.text) == str(b):
                    for loop in range(1):
                        lol = TextInput(text=self.a[row].text, size_hint_y=None, height="45sp",
                                        font_size='13sp')
                        self.aa.append(lol)
                        self.jss.add_widget(self.aa[self.looop])
                        lol1 = TextInput(text=self.b[row].text, size_hint_y=None, height="45sp",
                                         font_size='13sp')
                        self.bb.append(lol1)
                        self.jss.add_widget(self.bb[self.looop])
                        lol2 = TextInput(text=self.c[row].text, size_hint_y=None, height="45sp",
                                         font_size='13sp')
                        self.cc.append(lol2)
                        self.jss.add_widget(self.cc[self.looop])
                        self.looop += 1
                    self.bold = 2
                    self.doyou = 0
        except:
            pass

    def clean_do(self):
        try:
            for row in range(self.looop):
                self.jss.remove_widget(self.aa[row])
                self.jss.remove_widget(self.bb[row])
                self.jss.remove_widget(self.cc[row])
            for row in range(self.plus):
                self.jss.remove_widget(self.a[row])
                self.jss.remove_widget(self.b[row])
                self.jss.remove_widget(self.c[row])
            self.a = []
            self.b = []
            self.c = []
            lopux = str(workshtt.cell(f"G{str(self.minus)}").value).split(';')
            for row in range(int(self.plus)):
                lol = TextInput(text=lopux[0 + row * 3], size_hint_y=None, height="45sp",
                                font_size='13sp')
                self.a.append(lol)
                self.jss.add_widget(self.a[row])
                lol1 = TextInput(text=lopux[1 + row * 3], size_hint_y=None, height="45sp",
                                 font_size='13sp')
                self.b.append(lol1)
                self.jss.add_widget(self.b[row])
                lol2 = TextInput(text=lopux[2 + row * 3], size_hint_y=None, height="45sp",
                                 font_size='13sp')
                self.c.append(lol2)
                self.jss.add_widget(self.c[row])
            self.bold = 0
            self.doyou = 1
            self.search.text = ""
        except:
            self.search.text = ""


class Journal_Locodrom_L(Screen):
    def __init__(self, **kwargs):
        super(Journal_Locodrom_L, self).__init__(**kwargs)
        self.today = today.strftime("%d.%m.%Y")
        self.l = 1
        self.bold = 0
        self.number.text = str(self.l) + " страница"
        self.minus = int(workshtl.cell(f"H{1}").value)
        self.plus = int(workshtl.cell(f"I{self.minus}").value)
        self.a = []
        self.b = []
        self.c = []
        try:
            lopux = str(workshtl.cell(f"G{str(self.minus)}").value).split(';')
            for row in range(int(self.plus)):
                lol = TextInput(text=lopux[0 + row * 3], size_hint_y=None, height="45sp",
                                font_size='13sp')
                self.a.append(lol)
                self.jss.add_widget(self.a[row])
                lol1 = TextInput(text=lopux[1 + row * 3], size_hint_y=None, height="45sp",
                                 font_size='13sp')
                self.b.append(lol1)
                self.jss.add_widget(self.b[row])
                lol2 = TextInput(text=lopux[2 + row * 3], size_hint_y=None, height="45sp",
                                 font_size='13sp')
                self.c.append(lol2)
                self.jss.add_widget(self.c[row])
        except:
            pass

    def left(self):
        global workshtl
        self.l -= 1
        if self.l == 0:
            self.l += 1
            return self.l
        try:
            if self.bold == 1:
                self.bold = 0
                self.jss.remove_widget(self.a[int(self.plus)])
                self.jss.remove_widget(self.b[int(self.plus)])
                self.jss.remove_widget(self.c[int(self.plus)])
                self.a.remove(self.plus1)
                self.b.remove(self.plus2)
                self.c.remove(self.plus3)
        except:
            pass
        for row in range(int(10)):
            self.jss.remove_widget(self.a[row])
            self.jss.remove_widget(self.b[row])
            self.jss.remove_widget(self.c[row])
        self.a = []
        self.b = []
        self.c = []
        self.bold = 2
        self.minus += 1
        self.number.text = str(self.l) + " страница"
        self.plus = int(workshtl.cell(f"I{str(self.minus)}").value)
        if self.plus < 10:
            self.bold = 0
        try:
            lopux = str(workshtl.cell(f"G{str(self.minus)}").value).split(';')
            for row in range(int(self.plus)):
                lol = TextInput(text=lopux[0 + row * 3], size_hint_y=None, height="45sp",
                                font_size='13sp')
                self.a.append(lol)
                self.jss.add_widget(self.a[row])
                lol1 = TextInput(text=lopux[1 + row * 3], size_hint_y=None, height="45sp",
                                 font_size='13sp')
                self.b.append(lol1)
                self.jss.add_widget(self.b[row])
                lol2 = TextInput(text=lopux[2 + row * 3], size_hint_y=None, height="45sp",
                                 font_size='13sp')
                self.c.append(lol2)
                self.jss.add_widget(self.c[row])
        except:
            pass

    def right(self):
        global workshtl
        self.minus -= 1
        if self.minus == 0:
            self.minus += 1
            return self.minus
        try:
            if self.bold == 1:
                self.bold = 0
                self.jss.remove_widget(self.a[int(self.plus)])
                self.jss.remove_widget(self.b[int(self.plus)])
                self.jss.remove_widget(self.c[int(self.plus)])
                self.a.remove(self.plus1)
                self.b.remove(self.plus2)
                self.c.remove(self.plus3)
        except:
            pass
        for row in range(int(self.plus)):
            self.jss.remove_widget(self.a[row])
            self.jss.remove_widget(self.b[row])
            self.jss.remove_widget(self.c[row])
        self.plus = int(workshtl.cell(f"I{str(self.minus)}").value)
        self.bold = 2
        if self.plus < 10:
            self.bold = 0
        self.a = []
        self.b = []
        self.c = []
        self.l += 1
        self.number.text = str(self.l) + " страница"
        lopux = str(workshtl.cell(f"G{str(self.minus)}").value).split(';')
        for row in range(int(self.plus)):
            lol = TextInput(text=lopux[0 + row * 3], size_hint_y=None, height="45sp",
                            font_size='13sp')
            self.a.append(lol)
            self.jss.add_widget(self.a[row])
            lol1 = TextInput(text=lopux[1 + row * 3], size_hint_y=None, height="45sp",
                             font_size='13sp')
            self.b.append(lol1)
            self.jss.add_widget(self.b[row])
            lol2 = TextInput(text=lopux[2 + row * 3], size_hint_y=None, height="45sp",
                             font_size='13sp')
            self.c.append(lol2)
            self.jss.add_widget(self.c[row])

    def save(self):
        if self.bold == 1 and self.plus != 9 and self.plus != 10:
            workshtl.cell(f"I{self.minus}").value = str(int(workshtl.cell(f"I{self.minus}").value) + 1)
            self.bold = 0
            self.plus = int(workshtl.cell(f"I{self.minus}").value)
        cols = str()
        for row in range(int(self.plus)):
            tryu = str(str(self.a[row].text) + ";" + str(self.b[row].text) + ";" + str(
                self.c[row].text) + ";")
            cols += tryu
        workshtl.cell(f"G{str(self.minus)}").value = cols
        if self.plus == 9 and self.bold == 1:
            self.bold = 2
            workshtl.cell(f"I{self.minus}").value = str(int(workshtl.cell(f"I{self.minus}").value) + 1)
            self.plus = int(workshtl.cell(f"I{self.minus}").value)
            cols = str()
            for row in range(int(self.plus)):
                tryu = str(str(self.a[row].text) + ";" + str(self.b[row].text) + ";" + str(
                    self.c[row].text) + ";")
                cols += tryu
            workshtl.cell(f"G{str(self.minus)}").value = cols
            workshtl.cell(f"H{1}").value = str(int(workshtl.cell(f"H{1}").value) + 1)
            self.minus = int(workshtl.cell(f"H{1}").value)
            workshtl.cell(f"I{str(self.minus)}").value = str(0)
            self.l += 1
            self.number.text = str(self.l) + " страница"
            self.minus -= 1

    def plus_minus(self):
        try:
            if workshtl.cell(f"I{self.minus}").value == 10:
                return self.minus
            else:
                pass
            if self.bold == 0:
                self.bold = 1
                self.plus1 = TextInput(text="", size_hint_y=None, height="45sp",
                                       font_size='13sp')
                self.a.append(self.plus1)
                self.jss.add_widget(self.a[int(self.plus)])
                self.plus2 = TextInput(text="", size_hint_y=None, height="45sp",
                                       font_size='13sp')
                self.b.append(self.plus2)
                self.jss.add_widget(self.b[int(self.plus)])
                self.plus3 = TextInput(text="", size_hint_y=None, height="45sp",
                                       font_size='13sp')
                self.c.append(self.plus3)
                self.jss.add_widget(self.c[int(self.plus)])
            elif self.bold == 1:
                self.bold = 0
                self.jss.remove_widget(self.a[int(self.plus)])
                self.jss.remove_widget(self.b[int(self.plus)])
                self.jss.remove_widget(self.c[int(self.plus)])
                self.a.remove(self.plus1)
                self.b.remove(self.plus2)
                self.c.remove(self.plus3)
        except:
            pass

    def search_do(self):
        if self.search.text == "":
            return self.search.text
        try:
            try:
                if self.bold == 1:
                    self.bold = 0
                    self.jss.remove_widget(self.a[self.plus])
                    self.jss.remove_widget(self.b[self.plus])
                    self.jss.remove_widget(self.c[self.plus])
                    self.a.remove(self.plus1)
                    self.b.remove(self.plus2)
                    self.c.remove(self.plus3)
            except:
                pass
            try:
                for row in range(self.looop):
                    self.jss.remove_widget(self.aa[row])
                    self.jss.remove_widget(self.bb[row])
                    self.jss.remove_widget(self.cc[row])
            except:
                pass
            self.aa = []
            self.bb = []
            self.cc = []
            self.looop = 0
            self.pas = len(self.search.text)
            for row in range(int(workshtt.cell(f"I{str(self.minus)}").value)):
                self.jss.remove_widget(self.a[row])
                self.jss.remove_widget(self.b[row])
                self.jss.remove_widget(self.c[row])
                b = str()
                try:
                    for pok in range(self.pas):
                        b += str(self.b[row].text[pok])
                except:
                    pass
                if str(self.search.text) == str(b):
                    for loop in range(1):
                        lol = TextInput(text=self.a[row].text, size_hint_y=None, height="45sp",
                                        font_size='13sp')
                        self.aa.append(lol)
                        self.jss.add_widget(self.aa[self.looop])
                        lol1 = TextInput(text=self.b[row].text, size_hint_y=None, height="45sp",
                                         font_size='13sp')
                        self.bb.append(lol1)
                        self.jss.add_widget(self.bb[self.looop])
                        lol2 = TextInput(text=self.c[row].text, size_hint_y=None, height="45sp",
                                         font_size='13sp')
                        self.cc.append(lol2)
                        self.jss.add_widget(self.cc[self.looop])
                        self.looop += 1
                    self.bold = 2
                    self.doyou = 0
                else:
                    pass
        except:
            pass

    def clean_do(self):
        try:
            for row in range(self.looop):
                self.jss.remove_widget(self.aa[row])
                self.jss.remove_widget(self.bb[row])
                self.jss.remove_widget(self.cc[row])
            for row in range(self.plus):
                self.jss.remove_widget(self.a[row])
                self.jss.remove_widget(self.b[row])
                self.jss.remove_widget(self.c[row])
            self.a = []
            self.b = []
            self.c = []
            lopux = str(workshtt.cell(f"G{str(self.minus)}").value).split(';')
            for row in range(int(self.plus)):
                lol = TextInput(text=lopux[0 + row * 3], size_hint_y=None, height="45sp",
                                font_size='13sp')
                self.a.append(lol)
                self.jss.add_widget(self.a[row])
                lol1 = TextInput(text=lopux[1 + row * 3], size_hint_y=None, height="45sp",
                                 font_size='13sp')
                self.b.append(lol1)
                self.jss.add_widget(self.b[row])
                lol2 = TextInput(text=lopux[2 + row * 3], size_hint_y=None, height="45sp",
                                 font_size='13sp')
                self.c.append(lol2)
                self.jss.add_widget(self.c[row])
            self.bold = 0
            self.doyou = 1
            self.search.text = ""
        except:
            self.search.text = ""


class Closed(Screen):
    def __init__(self, **kwargs):
        super(Closed, self).__init__(**kwargs)
        self.ranges = int(workshtt.cell(f"K{1}").value)
        self.a = []
        self.b = []
        self.c = []
        self.d = []
        self.pluss = 0
        self.top = 0
        try:
            lopux = str(workshtt.cell(f"J{1}").value).split(';')
            for row in range(self.ranges):
                self.lol3 = Label(text=f"{self.top}", size_hint_y=None, height="45sp",
                                  font_size='13sp')
                self.d.append(self.lol3)
                self.jssc.add_widget(self.d[row])
                lol = TextInput(text=lopux[0 + row * 3], size_hint_y=None, height="45sp",
                                font_size='13sp')
                self.a.append(lol)
                self.jssc.add_widget(self.a[row])
                lol1 = TextInput(text=lopux[1 + row * 3], size_hint_y=None, height="45sp",
                                 font_size='13sp')
                self.b.append(lol1)
                self.jssc.add_widget(self.b[row])
                lol2 = TextInput(text=lopux[2 + row * 3], size_hint_y=None, height="45sp",
                                 font_size='13sp')
                self.c.append(lol2)
                self.jssc.add_widget(self.c[row])
                self.top += 1
        except:
            pass

    def plus(self):
        if self.pluss == 0:
            self.pluss = 1
            self.plus4 = Label(text=f"{self.ranges}", size_hint_y=None, height="45sp",
                               font_size='13sp')
            self.d.append(self.plus4)
            self.jssc.add_widget(self.d[self.ranges])
            self.plus1 = TextInput(text="", size_hint_y=None, height="45sp",
                                   font_size='13sp')
            self.a.append(self.plus1)
            self.jssc.add_widget(self.a[self.ranges])
            self.plus2 = TextInput(text="", size_hint_y=None, height="45sp",
                                   font_size='13sp')
            self.b.append(self.plus2)
            self.jssc.add_widget(self.b[self.ranges])
            self.plus3 = TextInput(text="", size_hint_y=None, height="45sp",
                                   font_size='13sp')
            self.c.append(self.plus3)
            self.jssc.add_widget(self.c[self.ranges])

    def save(self):
        if self.pluss == 1:
            self.pluss = 0
            cols = str()
            for row in range(int(self.ranges)):
                tryu = str(str(self.a[row].text) + ";" + str(self.b[row].text) + ";" + str(
                    self.c[row].text) + ";")
                cols += tryu
            cols += str(str(self.a[self.ranges].text) + ";" + str(self.b[self.ranges].text) + ";" + str(
                self.c[self.ranges].text) + ";")
            workshtt.cell(f"J{1}").value = cols
            self.ranges += 1
            workshtt.cell(f"K{1}").value = self.ranges
        else:
            cols = str()
            for row in range(int(self.ranges)):
                tryu = str(str(self.a[row].text) + ";" + str(self.b[row].text) + ";" + str(
                    self.c[row].text) + ";")
                cols += tryu
            workshtt.cell(f"J{1}").value = cols

    def del_p(self):
        try:
            for row in range(int(self.ranges)):
                if int(self.d[row].text) == int(self.search.text):
                    self.jssc.remove_widget(self.a[row])
                    self.jssc.remove_widget(self.b[row])
                    self.jssc.remove_widget(self.c[row])
                    self.jssc.remove_widget(self.d[row])
                else:
                    pass
            try:
                for row in range(self.ranges):
                    if int(self.d[row].text) == int(self.search.text):
                        self.a.remove(self.a[row])
                        self.b.remove(self.b[row])
                        self.c.remove(self.c[row])
                        self.d.remove(self.d[row])
                        self.ranges -= 1
                        workshtt.cell(f"K{1}").value = self.ranges
            except:
                pass
            try:
                if int(self.d[self.ranges].text) == int(self.search.text):
                    self.jssc.remove_widget(self.a[self.ranges])
                    self.jssc.remove_widget(self.b[self.ranges])
                    self.jssc.remove_widget(self.c[self.ranges])
                    self.jssc.remove_widget(self.d[self.ranges])
                    self.a.remove(self.plus1)
                    self.b.remove(self.plus2)
                    self.c.remove(self.plus3)
                    self.d.remove(self.plus4)
                    self.pluss = 0
            except:
                pass
            cols = str()
            for row in range(int(self.ranges)):
                tryu = str(str(self.a[row].text) + ";" + str(self.b[row].text) + ";" + str(
                    self.c[row].text) + ";")
                cols += tryu
            workshtt.cell(f"J{1}").value = cols
            self.search.text = ""
        except:
            pass


class MyApp(App):
    def build(self):
        sm = ScreenManager(transition=NoTransition())
        sm.add_widget(Container(name='menu'))
        sm.add_widget(Container_locodrom(name='menu_1'))
        sm.add_widget(Other(name='menu_other'))
        sm.add_widget(Journal_Sistem(name='journal_sis'))
        sm.add_widget(Journal_Locodrom(name='journal_lok'))
        sm.add_widget(Journal_Sistem_S(name='journal_sis_s'))
        sm.add_widget(Journal_Locodrom_L(name='journal_lok_l'))
        sm.add_widget(Closed(name='close'))
        return sm


if __name__ == '__main__':
    MyApp().run()
