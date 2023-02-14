def great(movie):
    if(movie['imdb']>5.5):
        return True
    else:
          return False
def sub(movies):
    list=[]
    for i in range(len(movies)):
         c=movies[i];
         if c['imdb']>5.5:
            list.append(c)
    return list
def cat(movies,name):
     list=[]
     for i in movies:
        c=i['category']
        if name.lower()==c.lower():
            list.append(i)
     return list
def avg(movies):
    s=0
    m=len(movies)
    for i in movies:
        s=s+i['imdb']
    s=s/m
    return s
def avgcat(movies,cat_name):
    c=cat(movies,cat_name)
    s=avg(c)
    return s
movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]


a=int(input())
c=great(movies[a])
if c==True:
     print("True")
else:
     print("False")
list=sub(movies)
print(list)
b=input()
list=cat(movies,b)
print(list)
print(avg(movies))
c=input()
list=avgcat(movies,c)
print(list)