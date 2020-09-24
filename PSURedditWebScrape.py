import requests
from bs4 import BeautifulSoup
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

headers = {'User-Agent': 'Mozilla/5.0'}
url = 'https://old.reddit.com/r/PennStateUniversity/top/?sort=top&t=all'

request_response = requests.get(url,headers=headers)

soup = BeautifulSoup(request_response.content, 'html.parser')

attrs = {'class':'thing','data-promoted':'false'}
posts = soup.find_all('div', attrs=attrs)
#print(posts[0])

amtofposts = 25

#titlesplusflairs = [posts[i].find('p',class_='title').text for i in range(amtofposts)]

titles = [posts[i].find('a',class_='title').text for i in range(amtofposts)]

authors = [posts[i].find('a',class_='author').text for i in range(amtofposts)]

upvotes = [int(posts[i].find('div',class_='score likes').text) for i in range(amtofposts)]

timestampsunix = [int((int(posts[i]['data-timestamp']) / 1000)) for i in range(amtofposts)]

timestamps = [(datetime.fromtimestamp(timestampsunix[i])) for i in range(amtofposts)]
timestampsformatted = [(timestamps[i].hour + (timestamps[i].minute / 60)) for i in range(amtofposts)]

timeupvotemat = pd.DataFrame({
    'Hour Posted':timestampsformatted,
    'Amount of Upvotes':upvotes,
})

print(timeupvotemat)


timeupvotemat.plot.scatter(x='Hour Posted' , y= 'Amount of Upvotes')
plt.show()

lrx = timeupvotemat['Hour Posted'].values.reshape(-1,1)
lry = timeupvotemat['Amount of Upvotes'].values.reshape(-1,1)

reg = LinearRegression().fit(lrx,lry)
#print(reg.coef_)
#print(reg.intercept_)
#print(reg.score(lrx,lry))


timeupvotemat.plot.scatter(x='Hour Posted' , y= 'Amount of Upvotes')
plt.plot([0,24],[reg.intercept_,reg.intercept_+(reg.coef_*24)])
plt.xlim(0,24)
plt.show()


lrx2 = np.square(timeupvotemat['Hour Posted'])

xsquaremat = pd.DataFrame({
    'Hour Posted':timeupvotemat['Hour Posted'],
    'Hour Posted^2':lrx2,
})
reg2 = LinearRegression().fit(xsquaremat,lry)
print(reg2.coef_)
print(reg2.intercept_)
print(reg2.score(xsquaremat,lry))

timeupvotemat.plot.scatter(x='Hour Posted' , y= 'Amount of Upvotes')