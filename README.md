# How to Run the Torchlite App
The Torchlite App has two parts:

1. A front-end application (a NextJS web app)
2. A back-end application (a Python Flask application)

At this point in development, either of these applications may be run separately; the front end does not need the back end to run, nor does the back end need the front end to run. (This will change.)

## Running the back end (Flask app)
The back-end Flask application resides in the api/ directory. To run the back-end Flask application, you need to activate its Python virtual environment and start the application.
```
cd api
source venv/bin/activate
FLASK_ENV=development FLASK_APP=api.py flask run
```

## Running the front end (NextJS app)
To start the front-end application, start another interactive shell, move to the top-level directory and run 

```
npm run dev
```
