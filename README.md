# README!

This project is a starting flask API application that has already implemented API auto documentation with swagger/redocs, data validation with marshmallow and flask-smorest, db connections using sqlalchemy and logging handlers that centralize all logs and send emails to admins when bugs are faced by the users.

Install
-------

    sudo apt install python3.8-venv python3.8-dev python3.8-distutils # For Debian-like systems.
    git clone https://github.com/rabizao/starter_flask.git
    cd starter_flask/backend
    python3.8 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt

Use

Start the API:
---

    source venv/bin/activate
    cd backend/
    flask run

Access documentation:
---

    http://localhost:5000/docs or http://localhost:5000/docs/swagger
