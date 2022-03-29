from glob import glob
import wx
import wxscrapy_form as wxsf
import scrapy
from scrapy.crawler import CrawlerProcess

response_rich_text_control = None

class MySimpleSpider(scrapy.Spider):
    name = "mysimplespider"
    start_urls = ['https://shbfrlnc.github.io/']

    def parse(self, response):
        print(response.url)
        global response_rich_text_control
        if response_rich_text_control is not None:
            response_rich_text_control.SetValue(response.url)

class MyFrame(wxsf.WXSPFrame):
    def __init__(self):
        wxsf.WXSPFrame.__init__ (self,None)
        self.Bind(wx.EVT_BUTTON, self.OnButtonClick)
        global response_rich_text_control
        response_rich_text_control = self.m_richText1

    def __del__( self ):
        pass

    def OnButtonClick(self, e):
        print("CLICKED!")
        process = CrawlerProcess({
            "USER_AGENT": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 Safari/537.36"
        })
        process.crawl(MySimpleSpider)
        process.start()

app = wx.App()
frame = MyFrame()
frame.Show()
app.MainLoop()