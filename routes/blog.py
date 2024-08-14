from serializers.blog import DecodeBlogs,DecodeBlog
from fastapi import APIRouter
from models.blog import BlogModel , UpdateBlogModel
from config.config import blogs_collection
import datetime
from bson import ObjectId



blog_root = APIRouter()

# Post Request
@blog_root.post("/new/blog")
def NewBlog(doc:BlogModel):
    doc_dict = dict(doc)                    # type: ignore
    
    current_date = datetime.date.today()
    doc_dict["date"] = str(current_date)    # type: ignore

    res = blogs_collection.insert_one(doc_dict)
    
    doc_id = str(res.inserted_id)

    return {
        "status":"ok",
        "message": "Blog Posted successfully",
        "_id": doc_id
    }

# Getting Blog Request

@blog_root.get("/all/blogs")
def AllBlogs():
    res = blogs_collection.find()
    decoded_data = DecodeBlogs(res)

    return {
        "status":"ok",
        "data": decoded_data
    }

# Single blog
@blog_root.get("/blog/{_id}")
def Getblog(_id:str):
    res = blogs_collection.find_one({'_id': ObjectId(_id)})
    decoded_blog = DecodeBlog(res)

    return {
        "status":"ok",
        "data": decoded_blog
    }
    

@blog_root.patch("/update/{_id}")
def UpdateBlog(_id : str, doc:UpdateBlogModel):
    req = dict(doc.model_dump(exclude_unset=True))

    # update on database
    blogs_collection.update_one(
        {'_id': ObjectId(_id)}, 
        {"$set": req}
    )

    return  {
        "status":"ok",
        "data": "Blog Updated Susscefully"
    }



# Delete Once Blog
@blog_root.delete("/delete/{_id}")
def DeleteBlog(_id:str):
    blogs_collection.delete_one({'_id': ObjectId(_id)})

    return {
        "status":"ok",
        "data": "Blog Deleted Susscefully"
    }




# from serializers.blog import DecodeBlogs, DecodeBlog
# from fastapi import APIRouter
# from models.blog import BlogModel, UpdateBlogModel
# from config.config import blogs_collection
# import datetime
# from bson import ObjectId

# blog_root = APIRouter()

# # Post Request
# @blog_root.post("/new/blog")
# def new_blog(doc: BlogModel):
#     """
#     Create a new blog post
#     """
#     try:
#         doc_dict = doc.dict(exclude_unset=True)  # Use dict() method from Pydantic
#         current_date = datetime.date.today()
#         doc_dict["date"] = str(current_date)

#         res = blogs_collection.insert_one(doc_dict)
#         doc_id = str(res.inserted_id)

#         return {
#             "status": "ok",
#             "message": "Blog Posted successfully",
#             "_id": doc_id
#         }
#     except Exception as e:
#         return {
#             "status": "error",
#             "message": str(e)
#         }

# # Getting Blog Request
# @blog_root.get("/all/blogs")
# def all_blogs():
#     """
#     Get all blog posts
#     """
#     try:
#         res = blogs_collection.find()
#         decoded_data = DecodeBlogs(res)

#         return {
#             "status": "ok",
#             "data": decoded_data
#         }
#     except Exception as e:
#         return {
#             "status": "error",
#             "message": str(e)
#         }

# # Single blog
# @blog_root.get("/blog/{_id}")
# def get_blog(_id: str):
#     """
#     Get a single blog post by ID
#     """
#     try:
#         if not ObjectId.is_valid(_id):
#             return {
#                 "status": "error",
#                 "message": "Invalid ID"
#             }

#         res = blogs_collection.find_one({'_id': ObjectId(_id)})
#         if res is None:
#             return {
#                 "status": "error",
#                 "message": "Blog not found"
#             }

#         decoded_blog = DecodeBlog(res)

#         return {
#             "status": "ok",
#             "data": decoded_blog
#         }
#     except Exception as e:
#         return {
#             "status": "error",
#             "message": str(e)
#         }

# @blog_root.patch("/update/{_id}")
# def update_blog(_id: str, doc: UpdateBlogModel):
#     """
#     Update a blog post
#     """
#     try:
#         if not ObjectId.is_valid(_id):
#             return {
#                 "status": "error",
#                 "message": "Invalid ID"
#             }

#         req = doc.dict(exclude_unset=True)

#         # update on database
#         blogs_collection.update_one(
#             {'_id': ObjectId(_id)},
#             {"$set": req}
#         )

#         return {
#             "status": "ok",
#             "data": "Blog Updated Successfully"
#         }
#     except Exception as e:
#         return {
#             "status": "error",
#             "message": str(e)
#         }
