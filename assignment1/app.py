from flask import Flask, request
import os

app = Flask(__name__)

ENV_DISPLAY_LIMIT = 10

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def main(path):

    path = f"Your path: {path}"

    args = 'Arguments:<br>' + '<br>'.join([f"{k} = {v}" for k,v in request.args.items()])

    #Limit to X items so that it's readable
    env = 'Environment:<br>' + '<br>'.join([f"{k} = {limited_to(v, 10)}" for k,v in os.environ.items()][:ENV_DISPLAY_LIMIT])

    return f"{path}<br><br>{args}<br><br>{env}"

def limited_to(string: str, limit: int, endC: str = "...") -> str:
    """Limit the given string to max X characters"""
    if len(string) < limit:
        return string
    return f"{string[:limit]}{endC}"