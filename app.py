
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from dbconnect import db_connect

app = Flask(__name__)
CORS(app)
app.config["SECRET KEY"] = "ada29fkg rt569aqptuh38fjkc vn44345ncvsfi39dfdf34sdfsf"


# Route to render the index.html page
@app.route('/')
def home():
    return render_template('index.html')


# Route to handle form submission
@app.route('/submit', methods=['POST'])
def submit_form():
    data = request.json
    print(f"Received data: {data}")

    for key, value in data.items():
        match key:
            case 'criteria':
                criteria = value
            case 'payload':
                payload = value
            case _:
                return jsonify({"message": "Wrong data submitted"})

    print(f"Received data: {criteria} {payload}")

    response_text = db_connect(criteria, payload)

    print(response_text)
    
    response_tuple = response_text[0]
    print(response_tuple[0])
    response_msg = {'CustID'    : response_tuple[0],
                    'FirstName' : response_tuple[1],
                    'LastName'  : response_tuple[2],
                    'BirthDate' : response_tuple[3],
                    'Gender'    : response_tuple[4]
                    }
    
    # You can process the data here (e.g., save to DB, perform some logic, etc.)

    return jsonify(response_msg)


if __name__ == '__main__':
    app.run(debug=True)
