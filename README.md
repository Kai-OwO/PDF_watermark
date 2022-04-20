# PDF_watermark

**Add user's info watermark in the private report PDF.**

## 介紹
>在私人報告中添加個人訊息浮水印防止外洩，以呢喃貓公開報告為範例。


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

以此範例，你會得到一個名為"0206呢喃週報_L1賽道潛在投資機會_0x1FabAc.pdf"的檔案，打開看看。

&nbsp;

## 工商時間

如果你覺得這報告很讚，你可以在下面的連結找到我們，歡迎一起來玩~~~

>呢喃貓Discord🟣 https://discord.gg/murmurcats

>Line社群 🟢 https://line.me/ti/g2/5sHR7ar4ZoqtkwYvbnAsofskWeQJ1xutvWLPcg

>呢喃貓官網 🐱 https://murmurcats.club/

>呢喃貓Opensea 🎨 https://opensea.io/collection/murmurcats

### 參考引用

股哥大神<br>
[漢字鑄造](ttps://sites.google.com/view/jtfoundry/)<br>
[Python3，2段代码，给pdf文件添加水印，原来watermark还可以这么玩](https://blog.csdn.net/wuyoudeyuer/article/details/122858139)。<br>
