"""REID
   Run the API
"""
from modelsAlchemy import db, Pieces, Studios, Evaluations
from apiAlchemy import create_api

api = create_api()
db.init_app(api)

# DEBUG Show all the routes
print(api.url_map)

with api.app_context():
    
    db.drop_all()
    db.create_all()

    studio1 = Studios("Estudio 1", "email1@email.com", "+34-123456789")
    studio2 = Studios("Estudio 2", "email2@email.com", "+34-234567891")
    studio3 = Studios("Estudio 3", "email3@email.com", "+1-123456789")
    studio4 = Studios("Estudio 4", "email4@email.com", "+34-987654321")

    piece1 = Pieces("Piece 1", "2022-12-16", "band", "vocal", "spanish", 1, "This piece...")
    piece2 = Pieces("Piece 2", "2018-11-14", "composer", "instrumental", "spanish", 1, "This piece...")
    piece3 = Pieces("Piece 3", "1987-07-13", "band", "intrumental", "french", 2, "This piece...")
    piece4 = Pieces("Piece 4", "1967-05-22", "composer", "vocal", "english", 2, "This piece..." )
    
    evaluation1 = Evaluations(1, 4, "2021-08-11", "The piece is good")
    evaluation2 = Evaluations(1, 2, "2021-08-11", "The piece is bad")
    evaluation3 = Evaluations(2, 5, "2022-01-14", "The piece is good")
    evaluation4 = Evaluations(3, 1, "2017-11-02", "The piece is bad")

    #Add studios
    db.session.add(studio1)
    db.session.add(studio2)
    db.session.add(studio3)
    db.session.add(studio4)
    db.session.commit()

    #Add pieces
    db.session.add(piece1)
    db.session.add(piece2)
    db.session.add(piece3)
    db.session.add(piece4)
    db.session.commit()

    #Add evaluations
    db.session.add(evaluation1)
    db.session.add(evaluation2)
    db.session.add(evaluation3)
    db.session.add(evaluation4)
    db.session.commit()


if __name__ == '__main__':
    api.run(port=5000, debug=True)