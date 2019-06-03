# Omdb Rating
Simple Coding Homework Assignment

## Langurage used
Python 3.7 

## Assignment
Created python program with folowing usage format and dockerized this program

## Commands to Run inside docker

```
git clone https://github.com/autoconfig1/omdb_rating.git
cd omdb_rating
docker build -t my_prg ./
docker run my_prg /omdb_cli.py -movie batman
```
### Output ###
```
Rotten Tomatoes rating of movie:batman  is: 70%
```

## Commands to python program outside docker

We need to just plan python code to run

``` 
python omdb_cli.py -movie batman
```
### Output ###
```
Rotten Tomatoes rating of movie:batman  is: 70%
``` 

Then we will get rotten tomoto for batman movies

