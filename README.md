# PDF_watermark

**Add user's info watermark in the private report PDF.**

## 介紹
>在私人報告中添加個人訊息浮水印。

## 來試試
我們需要安裝一些酷東西來讓程式碼跑得動。
- [ReportLab](https://www.reportlab.com/)

- 安裝reportlab：`pip install reportlab`

- [pikepdf](https://pikepdf.readthedocs.io/en/latest/)

- 安裝pikepdf：`pip install pikepdf`

在同層資料夾中放入你要上浮水印的PDF，並將target_pdf_path設為其名稱，eth_address設為乙太坊地址。

```python3
add_watermark(target_pdf_path='0206呢喃週報_L1賽道潛在投資機會.pdf',
            eth_address='0x1Fa8dA0B63C639a7b53baE343e5761D56F898bAc')
```

- 跑吧：`python3 watermark.py`
