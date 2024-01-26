# REST API for a catalog of audiovisual pieces
Implementation of a simple REST API for a catalog of audiovisual pieces, as a project of my Data Representation course.
The service must at least support through that API the following operations:
- Get a list of all parts in the collection.
- Add a new part
- Edit a part of the collection
- Remove a part from the collection
- Get a list of all production companies
- Add a new production company
- Edit a production company
- Delete a production company only if there are no associated parts
- Publish a new evaluation
- Edit an evaluation
- Delete an evaluation
- Get a list of all evaluations of a part and filter that list by date or limit the amount of information obtained (e.g. the first 10 items, the items between 11 and 20, etc.)
- Obtain the number of pieces given a production company
- Obtain the list of evaluations containing a given text.

Also implement a Python client to test this service.
