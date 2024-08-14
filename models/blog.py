from pydantic import BaseModel
from typing import Optional, List

class BlogModel(BaseModel):
    title: str
    sub_title : str
    content : str
    author: str
    tags: list[str]


# class UpdateBlogModel(BaseModel):
#     title: Optional[str] = None
#     sub_title: Optional[str] = None
#     content: Optional[str] = None
#     author: Optional[str] = None
#     tags: Optional[List[str]] = None

class UpdateBlogModel(BaseModel):
    title: str = None 
    sub_title : str = None 
    content : str = None 
    author: str = None 
    tags: list[str] = None 
    