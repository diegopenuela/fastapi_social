from typing import Optional
from fastapi import FastAPI, Response, status, HTTPException
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


#Logic - Methods
def find_post(id):
    for p in my_posts:
        if p['id'] == id:
            return p

def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p['id'] == id:
            return i


#Path Operations - FastAPI
@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/posts")
async def get_posts():
    return {"data": my_posts} #FastAPI automatically serializes a python Array into JSON format

@app.post("/posts", status_code=status.HTTP_201_CREATED) 
async def create_posts(post: Post):  #FastAPI performs data validation for post based on Model
    post_dict = post.dict() #Convert pydantic model into a python dict
    post_dict['id'] = randrange(0, 1000000)
    my_posts.append(post_dict)
    return {"data": post_dict}

@app.get("/posts/{id}")
async def get_post(id: int): #FastAPI enforces data validation and type conversion based on the type defined for each param
    post = find_post(id)

    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"post with id: {id} was not found")
    return {"post_detail": post}

@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(id: int):
    #Find the index in the array
    index = find_index_post(id)

    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"post with id: {id} was not found")
    else:
        my_posts.pop(index)
        return Response(status_code=status.HTTP_204_NO_CONTENT)


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