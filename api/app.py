from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy, session
from dotenv import dotenv_values
from flask_cors import CORS, cross_origin
from scrapper import get_last_news_from_page

config = dotenv_values()
app = Flask(__name__)
cors = CORS(app)
app.debug = True
# O banco de dados precisa estar na pasta instance (sqlite)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['SQLALCHEMY_DATABASE_URI'] = config.get("DATABASE_URL")
app.config['JSON_SORT_KEYS'] = False

db = SQLAlchemy(app)

class News(db.Model):
    __tablename__ = "noticias"
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime)
    title = db.Column(db.String)
    content = db.Column(db.String)
    link = db.Column(db.String)


@app.get("/noticias")
@cross_origin()
def get_last_news():
    args = request.args
    page = int(args.get("page")) if args.get("page") is not None else 1
    news_per_page = int(args.get("size")) if args.get("size") is not None else 20
    
    all_news = News.query.order_by(News.id.desc()).paginate(page=page, per_page=news_per_page)

    d = {}
    for news in all_news:
        d[news.id] = {"date": news.date, "title":news.title, "content":news.content, "link":news.link, "id":news.id}
    return d

@app.get("/noticias/<int:news_id>")
def get_news_by_id(news_id):
    news = News.query.filter_by(id=news_id).first()
    d = {}
    d[news.id] = {"date": news.date, "title":news.title, "content":news.content, "link":news.link}
    return d

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

@app.post("/noticias/update")
def update_database():
    data = request.form
    if data.get("secret") == config.get("API_SECRET"):
        number_of_pages = int(data.get("range"))
        get_last_news_from_page(number_of_pages)

        return {
            "Message": f"success!"
        }
    else:
        return {
            "Message":"not allowed!"
        }


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)