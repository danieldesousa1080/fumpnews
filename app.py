from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy, session

app = Flask(__name__)
app.debug = True
# O banco de dados precisa estar na pasta instance
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///teste_html.db'

db = SQLAlchemy(app)

class News(db.Model):
    __tablename__ = "noticias"
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime)
    title = db.Column(db.String)
    content = db.Column(db.String)
    link = db.Column(db.String)


@app.get("/noticias")
def get_last_news():
    all_news = News.query.order_by(News.id.desc()).paginate(page=1, per_page=40)
    d = {}
    for news in all_news:
        d[news.id] = {"date": news.date, "title":news.title, "content":news.content, "link":news.link}

    return jsonify(d)

@app.get("/noticias/<int:page>")
def get_news_by_page(page):
    all_news = News.query.paginate(page=page, per_page=40)
    d = {}
    for news in all_news[::-1]:
        d[news.id] = {"date": news.date, "title":news.title, "content":news.content, "link":news.link}
    return jsonify(d)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()