#!/usr/bin/python3
"""
New view for City objects that handles default Restful API actions
"""
from flask import jsonify, abort, request, make_response
from api.v1.views import app_views
from models import storage
from models.place import Place
from models.state import State
from models.city import City


@app_views.route('/places', methods=['GET'], strict_slashes=False)
def retrieve_places():
    """ retrieve all places """
    places = []
    all_places = storage.all('Place').values()
    for place in all_places:
        places.append(place.to_dict())
    return make_response(jsonify(places))


@app_views.route('/cities/<city_id>/places', methods=['GET'],
                 strict_slashes=False)
def jsonify_places_1(city_id):
    """ Function that returns a JSON """
    the_obj = storage.get(City, city_id)
    if the_obj is None:
        abort(404)
    my_list = []
    for obj in the_obj.places:
        my_list.append(obj.to_dict())
    return jsonify(my_list)


@app_views.route('/places/<place_id>', methods=['GET'], strict_slashes=False)
def jsonify_places_2(place_id):
    the_obj = storage.get(Place, place_id)
    if the_obj is None:
        abort(404)
    return jsonify(the_obj.to_dict())


@app_views.route('/places/<place_id>', methods=['DELETE'],
                 strict_slashes=False)
def jsonify_places_3(place_id):
    the_obj = storage.get(Place, place_id)
    if the_obj is None:
        abort(404)
    storage.delete(the_obj)
    storage.save()
    return jsonify({}), 200


@app_views.route('/cities/<city_id>/places', methods=['POST'],
                 strict_slashes=False)
def jsonify_places_4(city_id):
    try:
        json_post = request.get_json()
        the_obj = storage.get(City, city_id)
        if the_obj is None:
            abort(404)
        if not json_post:
            return make_response(jsonify({'error': 'Not a JSON'}), 400)
        if 'user_id' not in json_post:
            return make_response(jsonify({'error': 'Missing user_id'}), 400)
        if 'name' not in json_post:
            return make_response(jsonify({'error': 'Missing name'}), 400)
        json_post['city_id'] = city_id
        new = Place(**json_post)
        new.save()
        return make_response(jsonify(new.to_dict()), 201)
    except:
        abort(404)


@app_views.route('/places/<place_id>', methods=['PUT'], strict_slashes=False)
def jsonify_places_5(place_id):
    the_obj = storage.get(Place, place_id)
    json_put = request.get_json()
    if the_obj is None:
        abort(404)
    if not json_put:
        return make_response(jsonify({'error': 'Not a JSON'}), 400)
    for key, value in json_put.items():
        if key not in ['id', 'created_at', 'city_id', 'update_at', 'user_id']:
            setattr(the_obj, key, value)
    storage.save()
    return make_response(jsonify(the_obj.to_dict()), 200)
