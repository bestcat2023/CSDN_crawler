from newspaper import Article
import html2text as ht
import pdfkit
from markdown import markdown

print("This is a crawler that can craw articles form csdn blog.")

url = input("\nurl")

print("crawling...")

article = Article(url)
article.download()

# 获取html内容
html = article.html

# 实例化html2text对象
runner = ht.HTML2Text()
# 转化html为markdown
res = runner.handle(html)
# print(res)

# 将markdown内容保存到res.md
with open ('res.md',mode='w',encoding='utf-8') as f:
    f.write(res)

print("crawled successfully")
# print("converting to pdf")
'''
input_filename = 'res.md'
output_filename = 'res.pdf'

with open(input_filename, encoding='utf-8') as f:
    #with open(self.wkhtmltopdf) as f:
    text = f.read()

html = markdown(text, output_format='html')  # MarkDown转HTML
pdfkit.from_string(html, output_filename, options={'encoding': 'utf-8'})  # HTML转PDF

wkhtmltopdf = r'D:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'  # 指定wkhtmltopdf
configuration = pdfkit.configuration(wkhtmltopdf=wkhtmltopdf)
pdfkit.from_string(html, output_filename, configuration=configuration, options={'encoding': 'utf-8'})  # HTML转PDF
'''