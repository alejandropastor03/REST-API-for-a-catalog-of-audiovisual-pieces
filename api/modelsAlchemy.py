"""REID
   Pieces, Studios and Evaluations tables in sqlAlchemy
"""

import flask_sqlalchemy
from flask import url_for
import xmltodict

db = flask_sqlalchemy.SQLAlchemy()

class Pieces(db.Model):
    """This class models all the columns needed in the table Pieces"""
    #Table name and columns
    __tablename__ = 'pieces'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(250), unique = True, nullable = False)
    date = db.Column(db.Date, nullable = False)
    author = db.Column(db.String(250), nullable = False)
    genre = db.Column(db.String(250), nullable = False)
    nationality = db.Column(db.String(250), nullable = False)
    studio = db.Column(db.Integer, db.ForeignKey("studios.id"))
    summary = db.Column(db.String(250))

    def __init__(self, name: str, date: str, author: str, genre:str, nationality: str,\
        studio: int, summary: str) -> None:
        """Adds a piece to the table
        
        Args:
            name: name of the piece
            date: date when the piece was produced
            author: can be band or composer
            genre: can be vocal or instrumental
            nationality: the country where the piece was produced
            studio: the id of the studio responsible for the piece
            summary: a historical summary of the piece
        """
        # We will automatically generate the new id
        self.name = name
        self.date = date
        self.author = author
        self.genre = genre
        self.nationality = nationality
        self.studio = studio
        self.summary = summary

    def to_json(self) -> dict:
        """From piece to JSON
        """
        resource = {
            "url": url_for("pieces.get_piece", id = self.id),
            "id": self.id,
            "piece_name": self.name,
            "date": self.date,
            "author": self.author,
            "genre": self.genre,
            "nationality": self.nationality,
            "studio": self.studio,
            "summary": self.summary
        }
        return resource

    @staticmethod
    def from_json(data: list) -> None:
        """From JSON to piece.
        
        Args:
            data: input JSON.
        """
        try:
            #all lower
            name = data[0].get("piece_name").rstrip().lower()
            date = data[0].get("date").rstrip().lower()
            author = data[0].get("author").rstrip().lower()
            genre = data[0].get("genre").rstrip().lower()
            nationality = data[0].get("nationality").rstrip().lower()
            studio = data[0].get("studio")
            summary = data[0].get("summary").rstrip().lower()

            return Pieces(name, date, author, genre, nationality, studio, summary)
        
        except KeyError:
            return None

        except IndexError:
            return None

    def to_xml(self) -> str:
        """From piece to XML.
        """
        xml_data = f"""
        <Piece>
            <uri>{url_for("pieces.get_piece", id = self.id)}</uri>
            <id>{self.id}</id>
            <piece_name>{self.name}</piece_name>
            <date>{self.date}</date>
            <author>{self.author}</author>
            <genre>{self.genre}</genre>
            <nationality>{self.nationality}</nationality>
            <studio>{self.studio}</studio>
            <summary>{self.summary}</summary>
        </Piece>
        """
        return xml_data
    
    @staticmethod
    def from_xml(data: dict) -> None:
        """From XML to a new piece.

        Args:
            data: XML as dict
        """
        try:
            #All are strings
            name = data["Piece"]["piece_name"].rstrip().lower()
            date = data["Piece"]["date"].rstrip().lower()
            author = data["Piece"]["author"].rstrip().lower()
            genre = data["Piece"]["genre"].rstrip().lower()
            nationality = data["Piece"]["nationality"].rstrip().lower()
            studio = data["Piece"]["studio"].rstrip().lower()
            summary = data["Piece"]["summary"].rstrip().lower()

            return Pieces(name, date, author, genre, nationality, studio, summary)
        
        except KeyError:
            return None

        except IndexError:
            return None

    def update_xml(self, data: dict) -> None:
        """Update a piece from a XML.

        Args: 
            data: XML as dict.
        """
        data = xmltodict.parse(data)
        try:
            self.name = data["Piece"]["piece_name"].rstrip().lower()
            self.date = data["Piece"]["date"].rstrip().lower()
            self.author = data["Piece"]["author"].rstrip().lower()
            self.genre = data["Piece"]["genre"].rstrip().lower()
            self.nationality = data["Piece"]["nationality"].rstrip().lower()
            self.studio = data["Piece"]["studio"].rstrip().lower()
            self.summary = data["Piece"]["summary"].rstrip().lower()

        except:
            pass
    
    def update_json(self, data: dict) -> None:
        """Update a piece from JSON.

        Args: 
            data: input JSON.
        """
        try:
            self.name = data[0].get("piece_name").rstrip().lower()
            self.date = data[0].get("date").rstrip().lower()
            self.author = data[0].get("author").rstrip().lower()
            self.genre = data[0].get("genre").rstrip().lower()
            self.nationality = data[0].get("nationality").rstrip().lower()
            self.studio = data[0].get("studio")
            self.summary = data[0].get("summary").rstrip().lower()
        
        except:
            pass

class Studios(db.Model):
    """This class models all the columns needed in the table Studios"""
    #Table name and columns
    __tablename__ = 'studios'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(250), unique = True, nullable = False)
    email = db.Column(db.String(250), unique = True, nullable = False)
    phone = db.Column(db.String(250), unique = True, nullable = False)

    def __init__(self, name: str, email: str, phone: str) -> None:
        """Adds a studio to the table
        
        Args:
            name: name of the studio
            email: email of the studio
            phone: phone of the studio
        """
        #We will automatically generate the new id
        self.name = name
        self.email = email
        self.phone = phone

    def to_json(self) -> dict:
        """From studio to JSON
        """
        resource = {
            "url": url_for("studios.get_studio", id = self.id),
            "id": self.id,
            "studio_name": self.name,
            "email": self.email,
            "phone": self.phone
        }
        return resource

    @staticmethod
    def from_json(data: dict) -> None:
        """From JSON to studio.
        
        Args:
            data: input JSON
        """
        try:
            #all lower
            name = data[0].get("studio_name").rstrip().lower()
            email = data[0].get("email").rstrip().lower()
            phone = data[0].get("phone").rstrip().lower()

            return Studios(name, email, phone)

        except KeyError:
            return None

        except IndexError:
            return None

    def to_xml(self) -> str:
        """From studio to XML.
        """
        xml_data = f"""
        <Studio>
            <uri>{url_for("studios.get_studio", id = self.id)}</uri>
            <id>{self.id}</id>
            <studio_name>{self.name}</studio_name>
            <email>{self.email}</email>
            <phone>{self.phone}</phone>
        </Studio>
        """
        return xml_data

    @staticmethod
    def from_xml(data: dict) -> None:
        """From XML to a new studio.

        Args:
            data: XML as dict
        """
        try:
            #All are strings
            name = data["Studio"]["studio_name"].rstrip().lower()
            email = data["Studio"]["email"].rstrip().lower()
            phone = data["Studio"]["phone"].rstrip().lower()

            return Studios(name, email, phone)

        except KeyError:
            return None

        except IndexError:
            return None

    def update_xml(self, data: dict) -> None:
        """Update a studio from a XML.

        Args: 
            data: XML as dict.
        """
        data = xmltodict.parse(data)
        try:
            self.name = data["Studio"]["studio_name"].rstrip().lower()
            self.email = data["Studio"]["email"].rstrip().lower()
            self.phone = data["Studio"]["phone"].rstrip().lower()

        except:
            pass

    def update_json(self, data: dict) -> None:
        """Update a studio from JSON.

        Args: 
            data: input JSON.
        """
        try:
            self.name = data[0].get("studio_name").rstrip().lower()
            self.email = data[0].get("email").rstrip().lower()
            self.phone = data[0].get("phone").rstrip().lower()
        
        except:
            pass

class Evaluations(db.Model):
    """This class models all the columns needed in the table Evaluations"""
    #Table name and columns
    __tablename__ = 'evaluations'
    id = db.Column(db.Integer, primary_key = True)
    piece = db.Column(db.Integer, db.ForeignKey("pieces.id"))
    note = db.Column(db.Integer, nullable = False)
    date = db.Column(db.Date, nullable = False)
    text = db.Column(db.String(250), nullable = False)

    def __init__(self, piece: int, note: int, date: str, text: str) -> None:
        """Adds a evaluation to the table
        
        Args:
            piece: piece to which the evaluation corresponds
            note: from 1 to 5
            date: date of the evaluation
            text: text of the evaluation
        """
        #We will automatically generate the new id
        self.piece = piece
        self.note = note
        self.date = date
        self.text = text

    def to_json(self) -> dict:
        """From evaluation to JSON
        """
        resource = {
            "url": url_for("evaluations.get_evaluation", id = self.id),
            "id": self.id,
            "piece_id": self.piece,
            "note": self.note,
            "date": self.date,
            "text": self.text
        }
        return resource

    @staticmethod
    def from_json(data: dict) -> None:
        """From JSON to evaluation.
        
        Args:
            data: input JSON.
        """
        try:
            #all lower
            piece = data[0].get("piece_id")
            note = data[0].get("note")
            date = data[0].get("date").rstrip().lower()
            text = data[0].get("text").rstrip().lower()

            return Evaluations(piece, note, date, text)

        except KeyError:
            return None

        except IndexError:
            return None

    def to_xml(self) -> str:
        """From evaluation to XML.
        """
        xml_data = f"""
        <Evaluation>
            <uri>{url_for("evaluations.get_evaluation", id = self.id)}</uri>
            <id>{self.id}</id>
            <piece_id>{self.piece}</piece_id>
            <note>{self.note}</note>
            <date>{self.date}</date>
            <text>{self.text}</text>
        </Evaluation>
        """
        return xml_data

    @staticmethod
    def from_xml(data: dict) -> None:
        """From XML to a new evaluation.

        Args:
            data: XML as dict
        """
        try:
            #All are strings
            piece = data["Evaluation"]["piece_id"].rstrip().lower()
            note = data["Evaluation"]["note"].rstrip().lower()
            date = data["Evaluation"]["date"].rstrip().lower()
            text = data["Evaluation"]["text"].rstrip().lower()

            return Evaluations(piece, note, date, text)

        except KeyError:
            return None

        except IndexError:
            return None

    def update_xml(self, data: dict) -> None:
        """Update a evaluation from a XML.

        Args: 
            data: XML as dict.
        """
        data = xmltodict.parse(data)
        try:
            self.piece = data["Evaluation"]["piece_id"].rstrip().lower()
            self.note = data["Evaluation"]["note"].rstrip().lower()
            self.date = data["Evaluation"]["date"].rstrip().lower()
            self.text = data["Evaluation"]["text"].rstrip().lower()

        except:
            pass

    def update_json(self, data: dict) -> None:
        """Update a evaluation from JSON.

        Args: 
            data: input JSON.
        """
        try:
            self.piece = data[0].get("piece_id")
            self.note = data[0].get("note")
            self.date = data[0].get("date").rstrip().lower()
            self.text = data[0].get("text").rstrip().lower()
        
        except:
            pass
    
