from os import times
import requests_html
import requests
import pandas as pd
from time import time, time_ns

url = 'https://www.youtube.com/watch?v=9mTXKFqJ18w'
channel_link = 'https://www.youtube.com/c/MrReactionWala/about'
t1 = time()
x = requests.get(url)
print(x.status_code)
file_html = open('html_data.txt','w')
file_html.truncate()
file_html.write(str(x.content))
file_html.close()
print('File 1 written in : ', time()-t1)
t2 = time() 

# y = requests_html.HTMLSession()
# z = y.get(url)
# file_html2 = open('html_data2.txt','w+')
# file_html2.write(str(z.content))
# file_html2.close()
# print('File 2 written in : ', time()-t2)

# t3 = time()
# channel_data = requests.get(channel_link)
# file_html3 = open('channel_data.txt','w+')
# file_html3.write(str(channel_data.content))
# file_html3.close()
# print('File 2 written in : ', time()-t3)
