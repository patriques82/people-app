### How to setup and run

1. Unzip folder
2. cd into folder
3. python -m venv venv
4. .\venv\Scripts\activate (./venv/bin/activate on MacOS)
5. pip install -r requirements.txt
6. python setupDB.py (setup database table Persons)
7. python app.py (run application)

## TODO

1. Create git repo with branch (main, dev, feature-\*)
2. Create tests for routes "/persons" and "/createPerson"
3. Create yml for github actions
4. Create new route "/" and redirect to route "/persons"
5. Create link in persons.html to "/createPerson"
