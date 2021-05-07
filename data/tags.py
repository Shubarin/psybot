import sqlalchemy
from .db_session import SqlAlchemyBase

association_table = sqlalchemy.Table(
    'post_to_tag',
    SqlAlchemyBase.metadata,
    sqlalchemy.Column('posts', sqlalchemy.Integer,
                      sqlalchemy.ForeignKey('posts.id')),
    sqlalchemy.Column('tags', sqlalchemy.Integer,
                      sqlalchemy.ForeignKey('tags.id'))
)


class Tags(SqlAlchemyBase):
    __tablename__ = 'tags'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True,
                           autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.String, nullable=True)
