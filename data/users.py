import datetime
import sqlalchemy
from .db_session import SqlAlchemyBase


class User(SqlAlchemyBase):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    first_name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    full_name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    chat_id = sqlalchemy.Column(sqlalchemy.String, index=True, unique=True)
    is_active = sqlalchemy.Column(sqlalchemy.Boolean, default=False)
    subscription_start = sqlalchemy.Column(sqlalchemy.Date, nullable=True,
                                           default=sqlalchemy.sql.null())
    subscription_end = sqlalchemy.Column(sqlalchemy.Date, nullable=True,
                                         default=sqlalchemy.sql.null())
    subscription_duration = sqlalchemy.Column(sqlalchemy.Integer,
                                              nullable=True,
                                              default=sqlalchemy.sql.null())
    created_date = sqlalchemy.Column(sqlalchemy.DateTime,
                                     default=datetime.datetime.now)

    def __str__(self):
        return f'User(full_name: {self.full_name}, chat_id: {self.chat_id})'

    def __repr__(self):
        return f'User(full_name: {self.full_name}, chat_id: {self.chat_id})'
