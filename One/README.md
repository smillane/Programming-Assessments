# Backend task

Modern web applications are often designed such that the frontend and backend are decoupled, where the backend supplies data for the frontend to render, but the backend is ignorant of what the frontend is actually rendering. This interface often takes the form of a REST api. Make a REST api that meets the following criteria:

- The api exposes 3 endpoints:
    - `GET /api/user/{id}` returns a user, if it exists in storage, by the id field.
    - `GET /api/users` returns all users in storage.
    - `POST /api/user` adds a user (defined in the body of the request) to storage. This endpoint should return the User's Id.
- User objects can be stored in-memory (we don't expect you to set up a database for this assessment).
- User objects have the following fields (types):
    - Id (type doesn't matter, so long as each User object has a unique Id value)
    - Name (string)
    - Age (number/int)
    - Email (string)
    - ParentOrGuardian (string, optional)
- The api/service should assign Users submitted to the `/api/user` endpoint a unique Id (Id is not submitted as part of the request).


## Backend task solution

Tested using CLI and another python file.

I created test.py, with post/get commands for the respective tests. Also tested if you searched for a userid that wasn't present.

Results of running test.py

4

5

1

2

[[1, {'name': 'sean', 'age': 28, 'email': 'testemail@email.com', 'parentOrGuardian': 'myself'}], [2, {'name': 'john', 'age': 28, 'email': 'testemail@email.com', 'parentOrGuardian': 'myself'}], [3, {'name': 'vaughan', 'age': 28, 'email': 'testemail@email.com', 'parentOrGuardian': 'myself'}], [4, {'name': 'sean', 'age': 28, 'email': 'testemail@email.com', 'parentOrGuardian': 'myself'}], [5, {'name': 'sean', 'age': 28, 'email': 'testemail@email.com', 'parentOrGuardian': None}]]

{'message': 'User does not exist'}