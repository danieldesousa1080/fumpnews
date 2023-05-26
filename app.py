from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy, session
from dotenv import dotenv_values

config = dotenv_values()
app = Flask(__name__)
app.debug = True
# O banco de dados precisa estar na pasta instance
app.config['SQLALCHEMY_DATABASE_URI'] = config.get("DATABASE_URL")

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
    args = request.args
    page = int(args.get("page")) if args.get("page") is not None else 1
    news_per_page = int(args.get("size")) if args.get("size") is not None else 20
    
    all_news = News.query.order_by(News.id.desc()).paginate(page=page, per_page=news_per_page)

    d = {}
    for news in all_news:
        d[news.id] = {"date": news.date, "title":news.title, "content":news.content, "link":news.link, "id":news.id}
    return jsonify(d)

@app.get("/noticias/<int:news_id>")
def get_news_by_id(news_id):
    news = News.query.filter_by(id=news_id).first()
    d = {}
    d[news.id] = {"date": news.date, "title":news.title, "content":news.content, "link":news.link}
    return jsonify(d)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

@app.get("/noticias/busca/<string:news_title>")
def get_news_by_title(news_title):
    args = request.args
    page = int(args.get("page")) if args.get("page") is not None else 1
    news_per_page = int(args.get("size")) if args.get("size") is not None else 20
    all_news = News.query.filter(News.title.like(f"%{news_title}%")).order_by(News.id.desc()).paginate(page=page, per_page=news_per_page)
    d = {}
    for news in all_news:
        d[news.id] = {"date": news.date, "title":news.title, "content":news.content, "link":news.link}
    return d

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)