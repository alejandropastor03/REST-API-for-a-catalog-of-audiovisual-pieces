"""REID
   Resource Models and database
"""

from flask import Blueprint, jsonify, request, Response
from sqlalchemy.exc import IntegrityError
from modelsAlchemy import db, Pieces, Studios, Evaluations
from flask_restful import abort
import xmltodict
import status

# Creates the Flask blueprints
pieces = Blueprint("pieces", __name__)
studios = Blueprint("studios", __name__)
evaluations = Blueprint("evaluations", __name__)

#POST
@pieces.route("/api/pieces", methods = ["POST"])
def add_piece():
    """Adds a piece in the table given a XML or JSON as request.
    """
    #Create a new piece
    if request.content_type == "application/xml":
        xml = xmltodict.parse(request.get_data())
        new_piece = Pieces.from_xml(xml)

    elif request.content_type == "application/json":
        json = request.get_json()
        if json == None:
            abort(status.HTTP_415_UNSUPPORTED_MEDIA_TYPE, message=f"JSON not valid!")
        new_piece = Pieces.from_json(json)
    
    else:
        abort(status.HTTP_415_UNSUPPORTED_MEDIA_TYPE, message=f"Not a JSON or XML!")

    if new_piece == None:
        abort(status.HTTP_400_BAD_REQUEST, message=f"Missing data!")

    try:
        db.session.add(new_piece)
        db.session.commit()

    except IntegrityError:
        # Fail to store new data.
        abort(status.HTTP_400_BAD_REQUEST, message=f"Piece {new_piece.name} already exists")

    return new_piece.to_xml(), status.HTTP_202_ACCEPTED

@studios.route("/api/studios", methods = ["POST"])
def add_studio():
    """Adds a studio in the table given a XML or JSON as request.
    """
    #Create a new studio
    if request.content_type == "application/xml":
        xml = xmltodict.parse(request.get_data())
        new_studio = Studios.from_xml(xml)

    elif request.content_type == "application/json":
        json = request.get_json()
        if json == None:
            abort(status.HTTP_415_UNSUPPORTED_MEDIA_TYPE, message=f"JSON not valid!")
        new_studio = Studios.from_json(json)

    else:
        abort(status.HTTP_415_UNSUPPORTED_MEDIA_TYPE, message=f"Not a JSON or XML!")

    if new_studio == None:
        abort(status.HTTP_400_BAD_REQUEST, message=f"Missing data!")

    try:
        db.session.add(new_studio)
        db.session.commit()

    except IntegrityError:
        # Fail to store new data.
        abort(status.HTTP_400_BAD_REQUEST, message=f"Studio {new_studio.name} already exists")

    return new_studio.to_xml(), status.HTTP_202_ACCEPTED
        
@evaluations.route("/api/evaluations", methods = ["POST"])
def add_evaluation():
    """Adds a evaluation in the table given a XML or JSON as request.
    """
    #Create a new evaluation
    if request.content_type == "application/xml":
        xml = xmltodict.parse(request.get_data())
        new_evaluation = Evaluations.from_xml(xml)

    elif request.content_type == "application/json":
        json = request.get_json()
        if json == None:
            abort(status.HTTP_415_UNSUPPORTED_MEDIA_TYPE, message=f"JSON not valid!")
        new_evaluation = Evaluations.from_json(json)

    else:
        abort(status.HTTP_415_UNSUPPORTED_MEDIA_TYPE, message=f"Not a JSON or XML!")

    if new_evaluation == None:
        abort(status.HTTP_400_BAD_REQUEST, message=f"Missing data!")

    try:
        db.session.add(new_evaluation)
        db.session.commit()

    except IntegrityError:
        # Fail to store new data.
        abort(status.HTTP_400_BAD_REQUEST, message=f"Evaluation already exists")

    return new_evaluation.to_xml(), status.HTTP_202_ACCEPTED

#GET 
@pieces.route("/api/pieces/<int:id>", methods = ["GET"])
def get_piece(id: int):
    """Returns the piece with the given id
    """
    piece = Pieces.query.filter(Pieces.id == id).first()

    if piece is None:
        abort(status.HTTP_404_NOT_FOUND, message=f"Piece {id} does not exists")
        
    if request.content_type == "application/json":
        return jsonify(piece.to_json()), status.HTTP_202_ACCEPTED  
    elif request.content_type == "application/xml":    
        xml_data = piece.to_xml()
        response = Response(xml_data, mimetype="application/xml")
        return response, status.HTTP_202_ACCEPTED
    else: # Invalid format
        abort(status.HTTP_415_UNSUPPORTED_MEDIA_TYPE, message=f"Not a JSON or XML!")

@studios.route("/api/studios/<int:id>", methods = ["GET"])
def get_studio(id: int):
    """Returns the studio with the given id
    """
    studio = Studios.query.filter(Studios.id == id).first()

    if studio is None:
        abort(status.HTTP_404_NOT_FOUND, message=f"Studio {id} does not exists")
        
    if request.content_type == "application/json":
        return jsonify(studio.to_json()), status.HTTP_202_ACCEPTED  
    elif request.content_type == "application/xml":    
        xml_data = studio.to_xml()
        response = Response(xml_data, mimetype="application/xml")
        return response, status.HTTP_202_ACCEPTED
    else: # Invalid format
        abort(status.HTTP_415_UNSUPPORTED_MEDIA_TYPE, message=f"Not a JSON or XML!")

@evaluations.route("/api/evaluations/<int:id>", methods = ["GET"])
def get_evaluation(id: int):
    """Returns the evaluation with the given id
    """
    evaluation = Studios.query.filter(Studios.id == id).first()

    if evaluation is None:
        abort(status.HTTP_404_NOT_FOUND, message=f"Evaluation {id} does not exists")
        
    if request.content_type == "application/json":
        return jsonify(evaluation.to_json()), status.HTTP_202_ACCEPTED  
    elif request.content_type == "application/xml":    
        xml_data = evaluation.to_xml()
        response = Response(xml_data, mimetype="application/xml")
        return response, status.HTTP_202_ACCEPTED
    else: # Invalid format
        abort(status.HTTP_415_UNSUPPORTED_MEDIA_TYPE, message=f"Not a JSON or XML!")

@pieces.route("/api/pieces", methods = ["GET"])
def all_pieces():
    """Returns all the pieces of the collection
    """
    all_pieces = Pieces.query.all()
    if request.content_type == "application/json":
        json_data = list(map(Pieces.to_json, all_pieces))
        return jsonify(json_data), status.HTTP_202_ACCEPTED
    elif request.content_type == "application/xml":
        xml_data = "".join(map(Pieces.to_xml, all_pieces))
        xml_data = f"<Pieces> {xml_data} </Pieces>"
        response = Response(xml_data, mimetype="application/xml")
        return response, status.HTTP_202_ACCEPTED
    else: # Invalid format
        abort(status.HTTP_415_UNSUPPORTED_MEDIA_TYPE, message=f"Not a JSON or XML!")

@studios.route("/api/studios", methods = ["GET"])
def all_studios():
    """ Returns all the studios
    """
    all_studios = Studios.query.all()
    if request.content_type == "application/json":
        json_data = list(map(Studios.to_json, all_studios))
        return jsonify(json_data), status.HTTP_202_ACCEPTED
    elif request.content_type == "application/xml":
        xml_data = "".join(map(Studios.to_xml, all_studios))
        xml_data = f"<Studios> {xml_data} </Studios>"
        response = Response(xml_data, mimetype="application/xml")
        return response, status.HTTP_202_ACCEPTED
    else: # Invalid format
        abort(status.HTTP_415_UNSUPPORTED_MEDIA_TYPE, message=f"Not a JSON or XML!")

@evaluations.route("/api/pieces/<int:id_piece>/evaluations", methods = ["GET"])
def evaluations_filter(id_piece: int):
    """Returns all the evaluations in a specific date (default 2022-12-13)
        or from start (default 0) to end default (100)
    """
    date = request.args.get("date", default = "2022-12-13")
    start = request.args.get("start", default = 0, type = int)
    end = request.args.get("end", default = 100, type = int)
    evaluations = Evaluations.query.filter(Evaluations.date == date, Evaluations.piece == id_piece).all()
    if evaluations is None:
        abort(status.HTTP_404_NOT_FOUND, message=f"Evaluations Not Founded")
    
    evaluations = evaluations[start:(start + end)]
    if request.content_type == "application/json":
        json_data = list(map(Evaluations.to_json, evaluations))
        return jsonify(json_data), status.HTTP_202_ACCEPTED
    elif request.content_type == "application/xml":
        xml_data = "".join(map(Evaluations.to_xml, evaluations))
        xml_data = f"<Evaluations> {xml_data} </Evaluations>"
        response = Response(xml_data, mimetype="application/xml")
        return response, status.HTTP_202_ACCEPTED
    else: # Invalid format
        abort(status.HTTP_415_UNSUPPORTED_MEDIA_TYPE, message=f"Not a JSON or XML!")

@pieces.route("/api/studios/<int:studio_id>/pieces", methods = ["GET"])
def pieces_by_studio(studio_id: int):
    """Returns the number of pieces with the given studio
    """
    #We obtain all the pieces and filter by studio
    pieces = Pieces.query.filter(Pieces.studio == studio_id).all()

    if pieces is None:
        abort(status.HTTP_404_NOT_FOUND, message=f"Studio {studio_id} does not have pieces")

    #We obtain the number of pieces
    pieces = len(pieces)
    if request.content_type == "application/json":
        json_data = {
            "number of pieces": pieces
        }
        return jsonify(json_data), status.HTTP_202_ACCEPTED

    elif request.content_type == "application/xml":
        xml_data = f"""
        <Pieces>
            <number> {pieces} </number>
        </Pieces>
        """
        response = Response(xml_data, mimetype="application/xml")
        return response, status.HTTP_202_ACCEPTED
    else: # Invalid format
        abort(status.HTTP_415_UNSUPPORTED_MEDIA_TYPE, message=f"Not a JSON or XML!")

@evaluations.route("/api/evaluations", methods = ["GET"])
def get_evaluations_pattern():
    """Returns all evaluations whose text contains a pattern
    """
    pattern = request.args.get("pattern", default="")
    evaluations = Evaluations.query.filter(Evaluations.text.contains(pattern)).all()
    if evaluations is None:
        abort(status.HTTP_404_NOT_FOUND, message=f"No evaluation contains that pattern")
    
    if request.content_type == "application/json":
        json_data = list(map(Evaluations.to_json, evaluations))
        return jsonify(json_data), status.HTTP_202_ACCEPTED
    elif request.content_type == "application/xml":    
        xml_data = "".join(map(Evaluations.to_xml, evaluations))
        xml_data = f"<Evaluations> {xml_data} </Evaluations>"
        response = Response(xml_data, mimetype="application/xml")
        return response, status.HTTP_202_ACCEPTED
    else: # Invalid format
        abort(status.HTTP_415_UNSUPPORTED_MEDIA_TYPE, message=f"Not a JSON or XML!")

#DELETE
@pieces.route("/api/pieces/<int:id>", methods = ["DELETE"])
def delete_piece(id: int):
    """Delete a piece by id
    """
    #First we must delete all the evaluations that reference this piece
    evaluations = Evaluations.query.filter(Evaluations.piece == id).all()
    for evaluation in evaluations:
        delete_evaluation(evaluation.id)
        
    #We get the piece
    piece = Pieces.query.filter(Pieces.id == id).first()
    if piece == None:
        abort(status.HTTP_404_NOT_FOUND, message=f"Piece {id} does not exists")

    db.session.delete(piece)
    db.session.commit()

    return "", status.HTTP_204_NO_CONTENT

@studios.route("/api/studios/<int:id>", methods = ["DELETE"])
def delete_studio(id: int):
    """Delete a studio by id only if it does not have any associated pieces
    """
    studio = Studios.query.filter(Studios.id == id).first()
    if studio == None:
        abort(status.HTTP_404_NOT_FOUND, message=f"Studio {id} does not exists")
    
    pieces = Pieces.query.filter(Pieces.studio == id).all()
    if pieces is None:
        abort(status.HTTP_400_BAD_REQUEST, message = f"Studio {id} has associated pieces")
    
    db.session.delete(studio)
    db.session.commit()

    return "", status.HTTP_204_NO_CONTENT

@evaluations.route("/api/evaluations/<int:id>", methods = ["DELETE"])
def delete_evaluation(id: int):
    """Delete an evaluation by id
    """
    evaluation = Evaluations.query.filter(Evaluations.id == id).first()
    if evaluations == None:
        abort(status.HTTP_404_NOT_FOUND, message=f"Evaluation {id} does not exists")

    db.session.delete(evaluation)
    db.session.commit()

    return "", status.HTTP_204_NO_CONTENT

#PUT
@pieces.route("/api/pieces/<int:id>", methods = ["PUT"])
def update_piece(id: int):
    """Update a piece from the collection
    """
    piece = Pieces.query.filter(Pieces.id == id).first()
    if piece == None:
        abort(status.HTTP_404_NOT_FOUND, message=f"Piece {id} does not exists")

    if request.content_type == "application/xml":
        piece.update_xml(request.get_data())
    elif request.content_type == "application/json":
        piece.update_json(request.get_json())
    else:
        abort(status.HTTP_415_UNSUPPORTED_MEDIA_TYPE, message=f"Not a JSON or XML!")

    db.session.commit()

    return piece.to_xml(), status.HTTP_202_ACCEPTED

@studios.route("/api/studios/<int:id>", methods = ["PUT"])
def update_studio(id: int):
    """Update a studio
    """
    studio = Studios.query.filter(Studios.id == id).first()
    if studio == None:
        abort(status.HTTP_404_NOT_FOUND, message=f"Studio {id} does not exists")

    if request.content_type == "application/xml":
        studio.update_xml(request.get_data())
    elif request.content_type == "application/json":
        studio.update_json(request.get_json())
    else:
        abort(status.HTTP_415_UNSUPPORTED_MEDIA_TYPE, message=f"Not a JSON or XML!")

    db.session.commit()

    return studio.to_xml(), status.HTTP_202_ACCEPTED

@evaluations.route("/api/evaluations/<int:id>", methods = ["PUT"])
def update_evaluation(id: int):
    """Update an evaluation
    """
    evaluation = Evaluations.query.filter(Evaluations.id == id).first()
    if evaluation == None:
        abort(status.HTTP_404_NOT_FOUND, message=f"Evaluation {id} does not exists")

    if request.content_type == "application/xml":
        evaluation.update_xml(request.get_data())
    elif request.content_type == "application/json":
        evaluation.update_json(request.get_json())
    else:
        abort(status.HTTP_415_UNSUPPORTED_MEDIA_TYPE, message=f"Not a JSON or XML!")

    db.session.commit()

    return evaluation.to_xml(), status.HTTP_202_ACCEPTED

