import reflex as rx

from typing import Optional, List

from sqlmodel import select

from .model import BlogPostModel


class BlogPostState(rx.State):
    posts:List['BlogPostModel'] = []
    post: Optional['BlogPostModel'] = None

    def load_posts(self):
        with rx.session() as session:
            result = session.exec(
                select(BlogPostModel)
            ).all()
            self.post = result

    # def get_post(self):
    #     with rx.session() as session:
    #         result = session.exec(
    #             select(BlogPostModel)
    #         )
    #         self.posts = result