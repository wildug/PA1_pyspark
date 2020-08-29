import requests as r
from bs4 import BeautifulSoup
import time

delta = time.time()
x=0
def do():
	global x
	page = r.get("https://www.finanzen.net/index/dax").content
	soup = BeautifulSoup(page,features="html.parser")
	price = soup.findAll('div',{'class':'col-xs-5 col-sm-4 text-sm-right text-nowrap'})[0].text

	#value of dax index in points
	price = price.replace(".","").replace(",",".").strip()[:-3]

	# alternates between training and testing folder 
	if x % 2 ==0:
		with open("./training/data.txt", "w") as f:
			f.write("("+price+",["+str(time.time())[:-3]+"])")
		print("("+price+",["+str(time.time())[:-3]+"])")

	else:
		with open("./testing/data.txt", "w") as f:
			f.write("("+price+",["+str(time.time())[:-3]+"])")
		print("("+price+",["+str(time.time())[:-3]+"])")
	x+=1

do()    
while True:
	if time.time()-delta > 300:
		do()
		delta = time.time()
		time.sleep(257)
	time.sleep(1)

