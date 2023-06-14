from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import exists, delete
from sqlalchemy_utils import database_exists, create_database
from datetime import datetime
from dotenv import dotenv_values

config = dotenv_values()
engine = create_engine(config.get("DATABASE_URL"))
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

if not database_exists(engine.url):
    create_database(engine.url)


class News(Base):
    __tablename__ = "noticias"
    id = Column(Integer, primary_key=True)
    date = Column(DateTime)
    title = Column(String)
    content = Column(String)
    link = Column(String)

    def __repr__(self):
        return f"Noticia (Titulo = {self.title}, Link = {self.link})"


Base.metadata.create_all(engine)


def add_news(date_, title_, content_, link_):
    if session.query(exists().where(News.link == f"{link_}")).scalar():
        print("Noticia já cadastrada!")
    else:
        news = News(date=datetime.strptime(
            date_, '%d/%m/%Y'), title=title_, content=content_, link=link_)
        session.add(news)
        session.commit()

def delete_by_id(id):
    session.execute(delete(News).where(News.id == id))
    session.commit()
    print(f"Notícia {id} deletada!")