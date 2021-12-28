from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange

app = FastAPI()

#Models - Pydantic
# Defines the data schema. It does data validation
class Post(BaseModel):
    title: str
    content: str
    published: bool = True #Default value to True
    rating: Optional[int] = None #Optional field. Default value to none.


#Mock data. An Array of Dictionaries
my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1},
    {"title": "title of post 2", "content": "content of post 2", "id": 2},
    {"title": "title of post 3", "content": "content of post 3", "id": 3}]


#Path Operations - FastAPI
@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/posts")
async def get_posts():
    return {"data": my_posts} #FastAPI automatically serializes a python Array into JSON format

@app.post("/posts")
async def create_posts(post: Post):
    post_dict = post.dict() #Convert pydantic model into a python dict
    post_dict['id'] = randrange(0, 1000000)
    my_posts.append(post_dict)
    return {"data": post_dict}


#Tutorial Example: Create a post and read data direclty from the body request. No database needed.
#@app.post("/createposts")
#async def create_posts(payload: dict = Body(...)):
#    print(payload)
#    return {"new_post": f"Title: {payload['title']}  Content: {payload['content']}"}

#Tutorial Example: Get dummy data
#@app.get("/posts")
#async def get_posts():
#    return {"message": "You are getting all the posts"}

#Tutorial Example: Create a post and read data from a pydantic model. No database needed.
#@app.post("/posts")
#async def create_posts(post: Post):
#    print(post.title)
#    print(post.dict()) #Convert pydantic model into a python dict
#    return {"data": post}