import logging

import sqlalchemy as sa
import sqlalchemy.orm as orm
from sqlalchemy.orm import Session
import sqlalchemy.ext.declarative as dec

SqlAlchemyBase = dec.declarative_base()

__factory = None


def global_init(db_file):
    global __factory

    if __factory:
        return

    if not db_file or not db_file.strip():
        raise Exception("Необходимо указать файл базы данных.")

    conn_str = f'sqlite:///{db_file.strip()}?check_same_thread=False'
    print(f"Подключение к базе данных по адресу {conn_str}")

    engine = sa.create_engine(conn_str, echo=False)
    __factory = orm.sessionmaker(bind=engine)

    from . import __all_models

    SqlAlchemyBase.metadata.create_all(engine)


def create_session() -> Session:
    global __factory
    return __factory()


def get_or_create(model, **kwargs):
    session = create_session()
    instance = session.query(model).filter_by(**kwargs).first()
    if instance:
        logging.info(f'add {instance}')
        return instance
    else:
        instance = model(**kwargs)
        session.add(instance)
        session.commit()
        return instance


# def get_or_create(model, defaults=None, **kwargs):
#     session = create_session()
#     instance = session.query(model).filter_by(**kwargs).one_or_none()
#     if instance:
#         return instance
#     else:
#         kwargs |= defaults or {}
#         instance = model(**kwargs)
#         try:
#             session.add(instance)
#             session.commit()
#             logging.info(f'add {instance}')
#         except Exception as e:
#             session.rollback()
#             instance = session.query(model).filter_by(**kwargs).one()
#             logging.error(e)
#             return instance, False
#         else:
#             return instance, True