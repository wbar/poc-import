from flask import Flask
from flask import request
from flask import jsonify
import random
import datetime
import string

app = Flask(__name__)


@app.route('/shipments/<int:shipment_id>/status', methods=['POST'])
def set_shipment_status(shipment_id):
    data = request.get_json(force=True)
    if 'status' in data and data['status'] == 'imported':
        return '', 200
    return 'Wrong request', 400


@app.route('/shipments', methods=['GET'])
def shipments():
    """
    This is simple mocking service for shipments list
    :return:
    """
    assert request.path == '/shipments'
    assert request.method == 'GET'
    assert 'status' in request.args

    # variable used to calculate ID based of day and minutes
    now = datetime.datetime.now()

    starting_id = int('%s%s%s%s%s0' % (
        (now.year - 2000),
        now.month if now.month > 9 else '0%d' % now.month,
        now.day if now.day > 9 else '0%d' % now.day,
        now.hour if now.hour > 9 else '0%d' % now.hour,
        now.minute if now.minute > 9 else '0%d' % now.minute,
    ))
    result = []
    for i in xrange(random.randint(0, 9)):
        result.append({
            'id': starting_id + i,
            'from': ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10)),
            'to': ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10)),
            'status': request.args.get('status', 'unknown')
        })
    return jsonify(shipments=result)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return 'use GET: "/shipments" or POST "/shipments/<ID>/status"'

if __name__ == '__main__':
    app.debug = True
    app.run()
