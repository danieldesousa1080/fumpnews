from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import exists, delete
from datetime import datetime

engine = create_engine("sqlite:///test.db", echo=True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class News(Base):
    __tablename__ = "noticias"
    id = Column(Integer, primary_key=True)
    date = Column(DateTime)
    title = Column(String)
    link = Column(String)

    def __repr__(self):
        return f"Noticia (Titulo = {self.title}, Link = {self.link})"


Base.metadata.create_all(engine)


def add_news(date_, title_, link_):
    if session.query(exists().where(News.link == f"{link_}")).scalar():
        print("Noticia já cadastrada!")
    else:
        news = News(date=datetime.strptime(
            date_, '%d/%m/%Y'), title=title_, link=link_)
        session.add(news)
        session.commit()

def delete_by_id(id):
    session.execute(delete(News).where(News.id == id))
    session.commit()
    print(f"Notícia {id} deletada!")