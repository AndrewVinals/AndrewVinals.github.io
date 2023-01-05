import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
import time
driver = webdriver.Chrome(executable_path='C:/Users/ajvin/Downloads/chromedriver_win32/chromedriver.exe')
driver.get('https://open.nytimes.com/')
results = []
other_results = []
time.sleep(5)
content = driver.page_source
soup = BeautifulSoup(content)

for a in soup.findAll(attrs='u-contentSansBold u-lineHeightTightest u-xs-fontSize24 u-paddingBottom2 u-paddingTop5 u-fontSize32'):
    name = a.find('div')
    if name not in results:
        results.append(name.text)
print(results)

for b in soup.findAll(attrs='ui-caption u-fontSize12 u-baseColor--textNormal u-textColorNormal js-postMetaInlineSupplemental'):
    head = b.find('time')
    if head not in results:
        other_results.append(head.text)

df = pd.DataFrame({'Name': results, 'Head': other_results})
df.to_csv('name.csv', index=False, encoding='utf-8')