# WeirdText - Encoder and Decoder

## Running the app

First, clone the repository:

```
git clone git@github.com:greyli/flask-examples.git
```

Then change into the ulam folder:

```
cd ulam
```

Create a virtual environment and install all the dependencies:

```
python3 -m venv venv  # on Windows, use "python -m venv venv" instead
. venv/bin/activate   # on Windows, use "venv\Scripts\activate" instead
pip install -r requirements.txt
```

Run the application

```
flask run
```

The application will be available on http://127.0.0.1:5000

## Endpoints

### /v1/encode
Here the user can submit the text to encode and will obtain the encoded text as a result.

### /v1/decode
Here the user can submit the encoded text to decode and will obtain the decoded (original) text as a result.
