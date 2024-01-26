"""REID
    Client for the API

    Since the examples to test the two versions have been created randomly, it is possible that 
    they interfere with each other. Therefore, it is necesary to restart the api between 
    the execution of one function and the other.
"""

import requests

URL = "http://127.0.0.1:5000"

def print_response(action, response):
    print("Request:")
    print(f"-> Action: {action}")
    print(f"-> URI: {response.url}")
    print("Answer:")
    print(f"-> Status: {response.status_code}")
    body = response.content.decode("utf-8")
    print(f"-> Body:\n{body}")
    print(f"-> Header:\n{response.headers}\n\n")

def xml_version():

    headers = {
        "content-type": "application/xml"
    }

    #List all pieces
    body = ""
    response = requests.get(URL + "/api/pieces", data=body, headers=headers)
    print_response("GET", response)

    #Add a new piece
    body = """
    <Piece>
        <piece_name>Piece 5</piece_name>
        <date>2011-12-27</date>
        <author>band</author>
        <genre>instrumental</genre>
        <nationality>spanish</nationality>
        <studio>1</studio>
        <summary>This piece...</summary>
    </Piece>
    """
    response = requests.post(URL + "/api/pieces", data=body, headers=headers)
    print_response("POST", response)

    #Edit a piece
    body = """
    <Piece>
        <piece_name>Piece 2</piece_name>
        <date>2004-12-17</date>
        <author>band</author>
        <genre>vocal</genre>
        <nationality>spanish</nationality>
        <studio>2</studio>
        <summary>This piece...</summary>
    </Piece>
    """
    response = requests.put(URL + "/api/pieces/2", data=body, headers=headers)
    print_response("PUT", response)

    #Delete a piece
    body = ""
    response = requests.delete(URL + "/api/pieces/3", data=body, headers=headers)
    print_response("DELETE", response)

    #List all studios
    body = ""
    response = requests.get(URL + "/api/studios", data=body, headers=headers)
    print_response("GET", response)

    #Add a studio
    body = """
    <Studio>
        <studio_name>Studio 5</studio_name>
        <email>email5@email.com</email>
        <phone>+99-123456789</phone>
    </Studio>
    """
    response = requests.post(URL + "/api/studios", data=body, headers=headers)
    print_response("POST", response)

    #Edit a studio
    body = """
    <Studio>
        <studio_name>Studio 2</studio_name>
        <email>email2222@email.com</email>
        <phone>+22-222256789</phone>
    </Studio>
    """
    response = requests.put(URL + "/api/studios/2", data=body, headers=headers)
    print_response("PUT", response)

    #Delete a studio
    body = ""
    response = requests.delete(URL + "/api/studios/3", data=body, headers=headers)
    print_response("DELETE", response)

    #Add an evaluation
    body = """
    <Evaluation>
        <piece_id>1</piece_id>
        <note>4</note>
        <date>2014-09-14</date>
        <text>The piece is good</text>
    </Evaluation>
    """
    response = requests.post(URL + "/api/evaluations", data=body, headers=headers)
    print_response("POST", response)

    #Edit an evaluation
    body = """
    <Evaluation>
        <piece_id>2</piece_id>
        <note>2</note>
        <date>2015-09-14</date>
        <text>The piece is bad</text>
    </Evaluation>
    """
    response = requests.put(URL + "/api/evaluations/3", data=body, headers=headers)
    print_response("PUT", response)

    #Delete an evaluation
    body = ""
    response = requests.delete(URL + "/api/evaluations/3", data=body, headers=headers)
    print_response("DELETE", response)

    #List all evaluations and filter by date and by amount
    body = ""
    response = requests.get(URL + "/api/pieces/1/evaluations?date=2021-08-11&start=1&end=2",\
        data=body, headers=headers)
    print_response("GET", response)

    #Obtain the number of pieces made by a studio
    body = ""
    response = requests.get(URL + "/api/studios/2/pieces", data=body, headers=headers)
    print_response("GET", response)

    #Filter evaluations by text
    body = ""
    response = requests.get(URL + "/api/evaluations?pattern=good", data=body, headers=headers)
    print_response("GET", response)

def json_version():

    headers = {
        "content-type": "application/json"
    }

    # List all pieces
    body = ""
    response = requests.get(URL + "/api/pieces", data=body, headers=headers)
    print_response("GET", response)

    #Add a new piece
    body = """
    [{
        "piece_name": "Piece 6",
        "date": "2015-08-19",
        "author": "composer",
        "genre": "vocal",
        "nationality": "spanish",
        "studio": 2,
        "summary": "This piece..."
    }]
    """
    response = requests.post(URL + "/api/pieces", data=body, headers=headers)
    print_response("POST", response)

    #Edit a piece
    body = """
    [{
        "piece_name": "Piece 2",
        "date": "2015-04-19",
        "author": "composer",
        "genre": "instrumental",
        "nationality": "spanish",
        "studio": 1,
        "summary": "This piece..."
    }]
    """
    response = requests.put(URL + "/api/pieces/2", data=body, headers=headers)
    print_response("PUT", response)

    #Delete a piece
    body = ""
    response = requests.delete(URL + "/api/pieces/3", data=body, headers=headers)
    print_response("DELETE", response)

    #List all studios
    body = ""
    response = requests.get(URL + "/api/studios", data=body, headers=headers)
    print_response("GET", response)

    #Add a studio
    body = """
    [{
            "studio_name": "Studio 6",
            "email": "email6@email.com",
            "phone": "+56-565656556"
    }]
    """
    response = requests.post(URL + "/api/studios", data=body, headers=headers)
    print_response("POST", response)

    #Edit a studio
    body = """
    [{
            "studio_name": "Studio 2",
            "email": "e2m2a2i2l@email.com",
            "phone": "+56-222222222"
    }]
    """
    response = requests.put(URL + "/api/studios/2", data=body, headers=headers)
    print_response("PUT", response)

    #Delete a studio
    body = ""
    response = requests.delete(URL + "/api/studios/3", data=body, headers=headers)
    print_response("DELETE", response)

    #Add an evaluation
    body = """
    [{
            "piece_id": 2,
            "note": 4,
            "date": "2017-08-11",
            "text": "The piece is good"
    }]
    """
    response = requests.post(URL + "/api/evaluations", data=body, headers=headers)
    print_response("POST", response)

    #Edit an evaluation
    body = """
    [{
            "piece_id": 2,
            "note": 2,
            "date": "2017-08-11",
            "text": "The piece is bad"
    }]
    """
    response = requests.put(URL + "/api/evaluations/3", data=body, headers=headers)
    print_response("PUT", response)

    #Delete an evaluation
    body = ""
    response = requests.delete(URL + "/api/evaluations/3", data=body, headers=headers)
    print_response("DELETE", response)

    #List all evaluations and filter by date and by amount
    body = ""
    response = requests.get(URL + "/api/pieces/1/evaluations?date=2021-08-11&start=1&end=2",\
        data=body, headers=headers)
    print_response("GET", response)

    #Obtain the number of pieces made by a studio
    body = ""
    response = requests.get(URL + "/api/studios/1/pieces", data=body, headers=headers)
    print_response("GET", response)

    #Filter evaluations by text
    body = ""
    response = requests.get(URL + "/api/evaluations?pattern=bad", data=body, headers=headers)
    print_response("GET", response)

#TESTS
#xml_version()
#json_version()

