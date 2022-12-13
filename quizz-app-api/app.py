from flask import Flask,request
from flask_cors import CORS
import jwt_utils
import services
app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
	x = 'world'
	return f"Hello, {x}"

@app.route('/quiz-info', methods=['GET'])
def GetQuizInfo():
	return {"size": 0, "scores": []}, 200

@app.route('/login', methods=['POST'])
def Login():
    payload = request.get_json()

    user_password = payload.get("password")
    if jwt_utils.secret == user_password:
        token = jwt_utils.build_token()
        return {"token":token},200
    return 'Unauthorized', 401

@app.route('/questions', methods=['POST'])
def postQuestions():
   #Récupérer le token envoyé en paramètre
    request.headers.get('Authorization')
    #récupèrer un l'objet json envoyé dans le body de la requète
    question_json = request.get_json()
    return services.postQuestions(question_json)

if __name__ == "__main__":
    app.run()