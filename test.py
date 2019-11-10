from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'type your responce here to your professer'

if __name__ == '__main__':
    app.run(debug=True, host='167.172.224.241', port=80)