# import sqlite3
#
# db=sqlite3.connect("test.db")
# #создание курсора
# c=db.cursor()

# c.execute("""CREATE TABLE articles (
#     title text,
#     full_text text,
#     views integer
#
# )""")
#добавление чего-либо в таблицу
# c.execute("INSERT INTO articles VALUES ('something goood','realy good',10)")

# c.execute("INSERT INTO articles (views) VALUES (9999999)")
# db.commit()
# c.execute("UPDATE articles SET views = 99999 WHERE title = 'something goood'")
# c.execute("SELECT rowid,* FROM articles")
# # c.execute("DELETE FROM articles WHERE views > 1000")
# # c.execute("SELECT rowid,* FROM articles WHERE title = 'something goood'")
# items=c.fetchall()
# for item in items:
#     print(item)
# # print(c.fetchall())
# # print(c.fetchmany(1))
# # print(c.fetchone()[1])
# # for item in c.fetchall():
# #     print(item[1])
# # items=c.fetchall()
# # for item in items:
# #     print(item[1])
#
# #обновление базы данных
# db.commit()
# db.close()


from flask import Flask,render_template,url_for,request,redirect
# from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import sqlite3
def get_db_connection():
    return sqlite3.connect('users.db')

app= Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
# app.config['SQPALCHEMY_TRACK_MODIFICATIONS'] = False
# db1 = SQLAlchemy(app)
#
#
# class Article(db1.Model):
#     id = db1.Column(db1.Integer,primary_key=True)
#     title = db1.Column(db1.String(100), nullable=False)
#     intro = db1.Column(db1.String(300), nullable=False)
#     text = db1.Column(db1.Text, nullable=False)
#     date = db1.Column(db1.DateTime, default=datetime.utcnow)
#
#     def __repr__(self):
#         return '<Article %r>' % self.id





def get_users():
   conn = sqlite3.connect('users.db')
   cursor = conn.cursor()
   cursor.execute("SELECT * FROM users")
   users = cursor.fetchall()
   conn.close()
   return users

@app.route('/')
def index():
    users = get_users()
    return render_template('index.html', users=users)

# #отслеживат главную страницу
# @app.route('/')
# def index():
#     conn = get_db_connection()
#     users = conn.execute('SELECT * FROM users').fetchall()
#     conn.close()
#     return render_template('index.html', users=users)


#обработка другой страницы(about)
@app.route('/about')
def about():
    return render_template('about.html')

#принятие данных из url
@app.route('/user/<string:name>/<int:id>')
def user(name,id):
    return "User page: " + name + " - "+ str(id)


@app.route('/create-user',methods=["POST","GET"])
def create_art():
    if request.method == "POST":
        id=request.form['id']
        name = request.form['name']
        phone = request.form['phone']
        language=request.form['language']
        age=request.form['age']
        try:
            db = get_db_connection()
            c = db.cursor()
            c.execute(f"SELECT id FROM users WHERE registrated = 1")
            items = c.fetchall()
            if not items:
                db = get_db_connection()
                c = db.cursor()
                c.execute(
                    f"INSERT INTO users (id,name,age,phone_number,registrated,language) VALUES ({id},'{name}',{age},'{phone}',1,'{language}')")
                db.commit()
                db.close()
                return redirect('/')

            else:
                return "Такой пользователь уже существует"

        except:
            return "при создании произошла ошибка"
    else:
        return render_template('create-user.html')


@app.route('/delete-user',methods=["POST","GET"])
def delete_all_users():
    if request.method == "POST":
        try:
            db = get_db_connection()
            c = db.cursor()
            c.execute("DELETE FROM users")
            db.commit()
            db.close()
            return redirect('/')
        except:
            return "При удалении что-то пошло не так"
    else:
        return render_template('delete_user.html')
@app.route('/update-user',methods=["POST","GET"])
def update_user():
    if request.method == "POST":
        try:
            id=request.form['id']
            update=request.form['upd'].split()
            db = get_db_connection()
            c = db.cursor()
            c.execute(f"SELECT id FROM users WHERE id = {id}")
            items = c.fetchall()
            if not items:
                return "Пользователь с таким айди не найден"

            else:
                print(update[0])
                if update[0] == "name":
                    db = get_db_connection()
                    c = db.cursor()
                    c.execute(f"UPDATE users SET name = '{update[1]}' WHERE id = {id}")
                    db.commit()
                    db.close()
                    return redirect('/')
                elif update[0] == 'phone_number':
                    db = get_db_connection()
                    c = db.cursor()
                    c.execute(f"UPDATE users SET phone_number = '{update[1]}' WHERE id = {id}")
                    db.commit()
                    db.close()
                    return redirect('/')
                elif update[0] =="language":
                    db = get_db_connection()
                    c = db.cursor()
                    c.execute(f"UPDATE users SET language = '{update[1]}' WHERE id = {id}")
                    db.commit()
                    db.close()
                    return redirect('/')
                elif update[0] == "age":
                    db = get_db_connection()
                    c = db.cursor()
                    c.execute(f"UPDATE users SET age = '{update[1]}' WHERE id = {id}")
                    db.commit()
                    db.close()
                    return redirect('/')
        except:
            return "При изменении что-то пошло не так"
    else:
        return render_template('update-user.html')
if __name__ == "__main__":
    app.run(debug=True)




