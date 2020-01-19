
from flask_cors import CORS
from flask import Flask, request, Response
from sqlalchemy.orm import Session

from db_model import DatabaseModel
from garbage_location_service import GarbageLocationService

app = Flask(__name__)
CORS(app)

model: DatabaseModel = DatabaseModel()
session: Session = model.get_session()
garbage_location_service: GarbageLocationService = GarbageLocationService(session)


@app.route('/garbage', methods=['GET', 'POST'])
def garbage():
    if request.method == 'GET':
        garbage_id: int = request.args.get("id")
        if garbage_id is None:
            return garbage_location_service.get_all_garbages()
        else:
            return garbage_location_service.get_garbage_by_id(garbage_id)

    if request.method == 'POST':
        garbage_location_service.create_garbage_location(request)
        return Response(status=200)
    else:
        return "Method is not allowed. Please fuck off."


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
