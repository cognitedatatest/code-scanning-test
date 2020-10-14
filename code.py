from flask import request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from database.users import User

@app.route('hello')
def hello():
    id = request.args.get("id")
    stmt = text("SELECT * FROM users where id=%s" % id) # Query is constructed based on user inputs
    query = SQLAlchemy().session.query(User).from_statement(stmt) # Noncompliant
    user = query.one()
    return "Hello %s" % user.username

def addition(a, b):
    return eval("%s + %s" % (a, b))

def minus(a, b):
    return a-b

if __name__ == "__main__":

    func_input = {"a":"1", "b":"2"}
    result1 = addition(func_input['a'], func_input['b'])

    print("The addition result is %d." % result1)

    a = int(input("a: "))
    b = int(input("b: "))
    result2 = minus(a,b)

    print("The minus result is %d." % result2)