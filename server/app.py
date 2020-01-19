from flask import Flask, request
from sqlalchemy.orm import Session

from db_model import DatabaseModel, GarbageRemovalEvent

app = Flask(__name__)

model: DatabaseModel = DatabaseModel()
# @app.route('/')
# def hello_world():
#     return "/GET: hello world!"


@app.route('/<id>', methods=['GET', 'POST', 'DELETE'])
def base(id):
    if request.method == 'GET':
        session: Session = model.get_session()
        session.query(GarbageRemovalEvent).first()
        return "/GET: hey man !"

    if request.method == 'POST':
        data = request.files["file"]  # a multidict containing POST data
        return "/POST: with file size {}".format(data.read())

    if request.method == 'DELETE':
        return "/DELETE: hey you tried to delete something"

    else:
        return "/NO METHOD: what are you trying to do"


if __name__ == '__main__':
    # app.jinja_env.auto_reload = True
    # app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(host='0.0.0.0', port=5000)
