# -*- coding:utf-8 -*-
# Python 3.6.9

from typing import List,Union,Tuple
from reportlab.lib import units
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import  TTFont
from pikepdf import Pdf,Page,Rectangle
import os

pdfmetrics.registerFont(TTFont('myfont-regu', r'./font/TaipeiSansTCBeta-Regular.ttf'))

'''
用於生成ETH地址縮寫的浮水印pdf文件

eth_address_path: 浮水印路徑+名稱
eth_address_content: 浮水印內容
width: 畫布寬度,單位(mm)
height: 畫布高度,單位(mm)
font: 對應注冊的字體代號
fontsize: 字號大小
angle: 旋轉角度
text_stroke_color_rgb: 文字輪廓rgb色
text_fill_color_rgb: 文字填充rgb色
text_fill_alpha: 文字透明度
'''

def create_wartmark(eth_address_path:str,
                    eth_address_content:str,
                    width: Union[int, float],
                    height: Union[int, float],
                    font: str,
                    fontsize: int,
                    angle: Union[int, float] = 45,
                    text_stroke_color_rgb: Tuple[int, int, int] = (0, 0, 0),
                    text_fill_color_rgb: Tuple[int, int, int] = (0, 0, 0),
                    text_fill_alpha: Union[int, float] = 1) -> None:

    #創建PDF文件，指定文件名及尺寸，以像素為單位
    c = canvas.Canvas(f'{eth_address_path}_watermark.pdf',pagesize=(width*units.mm,height*units.mm))

    #畫布平移保證文字完整性
    c.translate(0.2*width*units.mm,0.1*height*units.mm)

    #設置旋轉角度
    c.rotate(angle)

    #設置字體大小
    c.setFont(font,fontsize)

    #設置字體輪廓彩色
    c.setStrokeColorRGB(*text_stroke_color_rgb)

    #設置填充色
    c.setFillColorRGB(*text_fill_color_rgb)

    #設置字體透明度
    c.setFillAlpha(text_fill_alpha)

    #後繪制字體內容
    c.drawString(0,0,eth_address_content)

    #保存文件
    c.save()
   

'''
向目標pdf文件批量添加水印

target_pdf_path: 目標pdf文件路徑+文件名
eth_address: ETH地址
'''

def add_watermark(target_pdf_path:str , eth_address:str) -> None:

    #ETH address 處理
    eth_address_path = eth_address[:5] + eth_address[-3:]
    eth_address_content = eth_address[:5] + "..." + eth_address[-3:]

    #製作此ETH地址的浮水印
    create_wartmark(eth_address_path=eth_address_path,
                    eth_address_content=eth_address_content,
                    width=35,
                    height=35,
                    font='myfont-regu',
                    fontsize=18,
                    text_fill_alpha=0.05)

    #選擇需要添加水印的pdf文件
    target_pdf = Pdf.open(target_pdf_path)

    #讀取水印pdf文件並提取水印
    watermark_pdf = Pdf.open(f'{eth_address_path}_watermark.pdf')
    watermark_page = watermark_pdf.pages[0]
    
    #浮水印行列數
    nrow = 10
    ncol = 10

    #遍歷目標pdf文件中的所有頁，批量添加水印
    for idx,target_page in enumerate(target_pdf.pages):
        for x in range(ncol):
            for y in range(nrow):
                #向目標頁指定範圍添加水印
                target_page.add_overlay(watermark_page,
                                        Rectangle(target_page.trimbox[2] * x / ncol,
                                        target_page.trimbox[3] * y / nrow,
                                        target_page.trimbox[2] * (x + 1) / ncol,
                                        target_page.trimbox[3] * (y + 1) / nrow
                                        ))
    #保存PDF文件，同時對pdf文件進行重命名，加上ETH地址
    target_pdf.save(target_pdf_path[:-4] + '_' + eth_address_path + '.pdf')
    
    #浮水印用完即刪
    try:
        os.remove(f'{eth_address_path}_watermark.pdf')
    except OSError as e:
        print(e)


add_watermark(target_pdf_path='0206呢喃週報_L1賽道潛在投資機會.pdf',
            eth_address='0x1Fa8dA0B63C639a7b53baE343e5761D56F898bAc')