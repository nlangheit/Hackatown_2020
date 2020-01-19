from typing import List

from flask import Flask, request
from flask_cors import CORS
from sqlalchemy.orm import Session

from db_model import DatabaseModel, GarbageLocation
from garbage_location_service import GarbageLocationService

app = Flask(__name__)
CORS(app)

model: DatabaseModel = DatabaseModel()
session: Session = model.get_session()
garbage_location_service: GarbageLocationService = GarbageLocationService(session)

# @app.route('/')
# def hello_world():
#     return "/GET: hello world!"


@app.route('/garbage', methods=['GET', 'POST', 'DELETE'])
def garbage():
    if request.method == 'GET':
        id: str = request.args.get("id")
        if id is None:
            # get all garbages
            # all_garbages: List[GarbageLocation] = session.query(GarbageLocation).all()
            # return "/GET: hey man ! im gonna get you all the garbages!"
            return garbage_location_service.get_all_garbages()
        else:
            # get specific garbage
            # garbage_wanted: GarbageLocation = session.query(GarbageLocation).filter(GarbageLocation.id.is_(id))
            # return "/GET: hey man ! heres your garbage: {}".format(id)
            return dict(garbage_location_service.get_garbage_by_id(123).as_dict())

    if request.method == 'POST':
        # create new garbage
        # data = request.form  # a multidict containing POST data
        # garbage_location_service.create_garbage_location()
        return "/POST: with name: {} , with file size {}".format(
            request.form.get(
                'name', "Cannot get name :("
            ),
            # request.files.get("file").read()
            request.files.get("file").read()
        )

    if request.method == 'DELETE':
        return "/DELETE: hey you tried to delete something"

    else:
        return "/NO METHOD: what are you trying to do"


if __name__ == '__main__':
    # app.jinja_env.auto_reload = True
    # app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(host='0.0.0.0', port=5000)
