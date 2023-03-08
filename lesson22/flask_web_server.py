import datetime

from flask import Flask, request, jsonify

app = Flask("sample_web_app")

@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route("/valeria")
def valeria():
    return f"The name is: {request.args.get('name')}"

@app.route("/beauty")
def beauty():
    return "<div><p style='color: red'>HELLO</p>" \
           "<img src='static/funny_cat.jpg' >" \
           "</div>"

# api/movies - GET (list), POST (create)
# api/movies/564 - GET(single movie), PUT/PATCH(update movie), DELETE

# users/valeria/addresses/1
@app.route("/users/<string:username>/addresses/<int:address_id>", methods=['GET','POST'])
def get_user_data(username, address_id):
    print(request.method)
    print(request.args)
    print(request.data)
    return f"the username is: {username}"

@app.route("/today")
def get_today():
    today = datetime.date.today()
    return jsonify({'today': today})


@app.route("/api/movies", methods=['POST'])
def create_movie():
    print(request.form)
    return "created"


# running from commandline or code
# debugging
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
    # app.run(debug=True, port=5001)


# path parameter
#/api/coutries/<country_name>

# query param
# /api/nationalize?name=slava&age=25

# body