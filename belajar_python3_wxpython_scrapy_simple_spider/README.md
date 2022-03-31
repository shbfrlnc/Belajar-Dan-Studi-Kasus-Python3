# Belajar Python3 wxPython Scrapy Simple Spider

## Cara Mencoba Kode Ini

### Untuk Menjalankannya

Pertama, pastikan Python 3.9 sudah terinstall di OS Anda.

Download folder ini.

Kemudian buka foldernya dengan perintah:

```
cd belajar_python3_wxpython_scrapy_simple_spider
```

Kemudian jalankan:

```
python -m venv ./venv
./venv/Scripts/activate
```

Lalu install requirements.txt:

```
pip install -r requirements.txt 
```

Selanjutnya, Anda bisa langsung coba:

```
python src/wxscrapy.py
```

### Untuk Membuild Jadi Executable

Jalankan:

```
pyinstaller src/wxscrapy.py
```

### Catatan Untuk Kode Ini

Hanya telah diuji di Windows 10.

## Pendahuluan

Tujuan dibuatnya source code ini adalah untuk mempelajari cara mem-passing data dari scrapy ke wxPython, dalam hal ini ke rich text control nya.

Python 3 adalah salah satu bahasa pemrograman yang bisa digunakan untuk banyak hal.

Hanya saja, fokus kita kali ini adalah untuk digunakan sebagai kode aplikasi dekstop, terutama Windows 10.

Kenapa di sini ada wxPython dan Scrapy?

Alasannya sederhana, saya ingin memastikan bahwa kedua modul tersebut bisa dibuild menjadi executable dengan menggunakan Pyinstaller.

Jika berhasil tanpa masalah, maka Python 3 punya potensi untuk digunakan dalam aplikasi web scraping.

## Penjelasan

Di sini, saya meng-generate GUI, dalam hal ini form-nya dengan wxFormBuilder.

Dengan aplikasi tersebut, saya meng-generate file "src/wxscrapy_form.py".

```
# file: wxscrapy_form.py
# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.richtext

###########################################################################
## Class WXSPFrame
###########################################################################

class WXSPFrame ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer1 = wx.BoxSizer( wx.VERTICAL )

        self.m_button1 = wx.Button( self, wx.ID_ANY, u"Scrape", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
        bSizer1.Add( self.m_button1, 0, wx.ALL|wx.EXPAND, 5 )

        self.m_richText1 = wx.richtext.RichTextCtrl( self, wx.ID_ANY, u"Ini adalah aplikasi untuk mencoba wxPython dan Scrapy", wx.DefaultPosition, wx.DefaultSize, 0|wx.VSCROLL|wx.HSCROLL|wx.NO_BORDER|wx.WANTS_CHARS )
        bSizer1.Add( self.m_richText1, 1, wx.EXPAND |wx.ALL, 5 )


        self.SetSizer( bSizer1 )
        self.Layout()

        self.Centre( wx.BOTH )

    def __del__( self ):
        pass
```

Nantinya, script tersebut digunakan di  "src/wxscrapy.py".

```
# file: wxscrapy.py

# begin: import modules
from glob import glob
import wx
import wxscrapy_form as wxsf
import scrapy
from scrapy.crawler import CrawlerProcess
# end: import modules

# global var untuk mengaitkan rich text control di form dengan data dari scrapy
response_rich_text_control = None

# simple spider dengan scrapy
class MySimpleSpider(scrapy.Spider):
    name = "mysimplespider"
    start_urls = ['https://shbfrlnc.github.io/'] # start url ke website saya

    def parse(self, response): # ketika di-parse
        print(response.url) # print response url di console/terminal
        if response_rich_text_control:
            # inilah maksud utama saya, mengisi value rich text control dengan data dari scrapy
            response_rich_text_control.SetValue(response.url)

# di sini, saya extend MyFrame dari frame yang di-generate via wxFormBuilder
class MyFrame(wxsf.WXSPFrame):
    def __init__(self): # constructor
        wxsf.WXSPFrame.__init__ (self,None)
        self.Bind(wx.EVT_BUTTON, self.OnButtonClick) # supaya button click bisa terdeteksi
        global response_rich_text_control # di-global kan
        response_rich_text_control = self.m_richText1 # rich text control diisi dari form ke global variabel tadi

    def __del__( self ):
        pass

    def OnButtonClick(self, e):
        print("CLICKED!")

        # ini adalah cara agar scrapy bisa di-run via kode Python 3
        process = CrawlerProcess({
            "USER_AGENT": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 Safari/537.36"
        })
        process.crawl(MySimpleSpider)
        process.start()

# begin: cara menampilkan form
app = wx.App()
frame = MyFrame()
frame.Show()
app.MainLoop()
# end: cara menampilkan form
```

Agar bisa memahami kedua script di atas, silakan baca komentarnya baik-baik, lalu coba di komputer Anda.

## Info Tambahan

Traktir Saya:

https://sociabuzz.com/lsfkrshb/tribe

Channel YouTube Saya:

https://www.youtube.com/c/shbfrlnc
