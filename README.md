# WeirdText - Encoder and Decoder

## WeirdText
For each original word in the original text, leaves the first and last character of it in that position, but shuffles (permutate) all the characters in the middle of the word.
Encoder output contains:
1. separator
2. encoded text (with shuffled words)
3. separator
4. sorted list of original words (only words that got shuffled). 

### Example:

Original Text (this is a single string formatted nicely for better viewing!):
```
'This is a long looong test sentence,\n'
'with some big (biiiiig) words!'
```

Encoded Text:
```
'\n—weird—\n'
'Tihs is a lnog loonog tset sntceene,\n'
'wtih smoe big (biiiiig) wdros!'
'\n—weird—\n'
'long looong sentence some test This with words'
```

Decoded Text:
```
'This is a long looong test sentence,\n'
'with some big (biiiiig) words!'
```


## Running the app

First, clone the repository:

```
git clone git@github.com:iluanna/ulam.git
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
