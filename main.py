from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()

#Models - Pydantic
# Defines the data schema. It does data validation
class Post(BaseModel):
    title: str
    content: str
    published: bool = True #Default value to True
    rating: Optional[int] = None #Optional field. Default value to none.


#Path Operations - FastAPI
@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/posts")
async def get_posts():
    return {"message": "You are getting all the posts"}

@app.post("/posts")
async def create_posts(post: Post):
    print(post.title)
    print(post.dict()) #Convert pydantic model into a python dict
    return {"data": post}

#Example: Get data direclty from the body request
#@app.post("/createposts")
#async def create_posts(payload: dict = Body(...)):
#    print(payload)
#    return {"new_post": f"Title: {payload['title']}  Content: {payload['content']}"}