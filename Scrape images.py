from bs4 import BeautifulSoup as soup
import requests

URL = "https://www.snapdeal.com/search?"

items = ['mobiles', 'laptop', 'earphones', 'book']

for i in items:
    
    url = requests.get(URL,params={'keyword':i})      #requesting the mentioned url with some queries/keywords passed
    html = soup(url.content)
    images = html.findAll('img',{'class':'product-image'})
    
    image_url = []
    for img in images:
        
        attributes = img.attrs.keys()         #storing attributes of the img tag
        
        #As Snapdeal, used two different attributes for the source url of image
        if 'src' in attributes:
            image_url.append(img.attrs['src'])
        elif 'data-src' in attributes:
            image_url.append(img.attrs['data-src'])
        
        
    #Storing each image of each product    
    for idx,img in enumerate(image_url):
        
        image = requests.get(img)
        with open('{}{}.jpg'.format(i,idx+1), 'wb') as fp:
            fp.write(image.content)
