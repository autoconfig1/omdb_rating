#!/usr/local/bin/python3.7
import requests
import json
import sys
if len(sys.argv)==1 or len(sys.argv)==2:
    print('Usage is wrong:')
    print('omdb_cli.py -movie batman')
    exit(1)
url='http://www.omdbapi.com/?t='
movie_name=sys.argv[2]
api_key='&apikey=33b26873'
full_url=url+movie_name+api_key
r=requests.get(full_url)
r_json=json.loads(r.text)
if r_json['Response']=="True":
    for item in r_json['Ratings']:
        if item['Source']=='Rotten Tomatoes':
            print('Rotten Tomatoes rating of movie:'+movie_name+'  is: '+str(item['Value']))
else:
    print("Error occured:"+str(r_json['Error']))
