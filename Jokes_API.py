import csv
import requests
import json

FILE = "C:/Users/ID.csv"    #dataset to get 'id' query for the api
URL = "http://api.icndb.com/jokes/"    #web api site


#dict to store joke with respect to the id
data = {
    'id' : [],
    'jokes' : []
}


with open(FILE,'r') as fp: 
    for count,line in enumerate(csv.reader(fp)): 
        if count>0:
            data['id'].append(line[0])


for idx in data['id']:
    new_url = URL + idx
    joke = requests.get(new_url)
    d = json.loads(joke.content)     #json content returned by the api
    S = d['value']['joke']
    if ',' in S:
        S = '"' + S + '"'
    
    data['jokes'].append(S)


#writing jokes to a csv file
with open("result.csv","w") as fp:
    
    fp.write("ID,Joke\n")
    for i in range(len(data['id'])):
        S = data['id'][i] + ',' + data['jokes'][i] + '\n'
        print(S)
        fp.write(S)
            
            
