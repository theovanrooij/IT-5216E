from models import Question,Answer
from datetime import datetime
import sqlite3


def getDbCursor() :
    # create a connection
    db_connection = sqlite3.connect("./quiz.db")

    # set the sqlite connection in "manual transaction mode"
    # (by default, all execute calls are performed in their own transactions, not what we want)
    db_connection.isolation_level = None

    cur = db_connection.cursor()
    # start transaction
    cur.execute("begin")
    return cur

def executeStatement(statement_list) :
    cur = getDbCursor()
    try:
    # Use the cursor to execute an INSERT statement
        for statement in statement_list :
            cur.execute(statement)
        # send the request
        return cur, 200
    except sqlite3.Error as e:
    # If an error occurred, print the error message
        print(f"An error occurred: {e.args[0]}")
        cur.execute('rollback')
        return {"error" : e.args[0]}, 500

def executeInsertStatement(statement_list) :
    response,status_code = executeStatement(statement_list)
    if status_code == 200 :
        response.execute("commit")
        return {"id":response.lastrowid},status_code
    else :
        return response, status_code

def executeSelectStatement(statement_list):
    response,status_code = executeStatement(statement_list)
    if status_code == 200 :
        return response,status_code
    else :
        return response, status_code

def executeUpdateStatement(statement_list):
    response,status_code = executeStatement(statement_list)
    if status_code == 200 :
        response.execute("commit")
        return {},204
    else :
        return response, status_code

def executeDeleteStatement(statement_list):
    response,status_code = executeStatement(statement_list)
    if status_code == 200 :
        response.execute("commit")
        return {},204
    else :
        return response, status_code

def rebuildDB():
    rebuildRequest,rebuildStatus = executeStatement([
            """CREATE TABLE "Question" (
        "id"	INTEGER NOT NULL,
        "position"	INTEGER NOT NULL,
        "title"	TEXT NOT NULL,
        "text"	TEXT NOT NULL,
        "image"	TEXT,
        PRIMARY KEY("id")
    );
    ""","""CREATE TABLE "Reponse" (
        "id"    INTEGER UNIQUE,
        "id_question"    INTEGER,
        "text"    TEXT,
        "isCorrect"    INTEGER,
        PRIMARY KEY("id"),
        FOREIGN KEY("id_question") REFERENCES "Question"("id")
    )""","""CREATE TABLE "Participation" (
        "id"    INTEGER,
        "playerName"    TEXT NOT NULL,
        "score"    INTEGER NOT NULL,
        "date" TEXT NOT NULL,
        PRIMARY KEY("id")
    );
    """
        ])
    if not rebuildStatus == 200 :
        return rebuildRequest,rebuildStatus
    rebuildRequest.execute("commit")
    return "Ok",200

def deleteAllQuestions():
    return executeDeleteStatement(["DELETE FROM Reponse","DELETE FROM Question"])

def deleteQuestionByID(id):
    question_json,status = getQuestionByID(id)

    if status == 200 :
        return executeDeleteStatement([f"DELETE FROM Question where id = {id}",
            f"UPDATE Question SET position = position - 1 "
            f"WHERE position >= {question_json['position']!r}"])

    return question_json,status

def postQuestions(question_json):
    input_question = Question()
    input_answers = [Answer() for answer in question_json["possibleAnswers"]]

    for i,answer_json in enumerate(question_json["possibleAnswers"]) :
        input_answers[i].from_json(answer_json.copy())

    question_json["possibleAnswers"] = input_answers
    input_question.from_json(question_json)

    sql_request_list = []

    question_by_position = getQuestionByPosition(input_question.position)
    if question_by_position[1] == 200 :
        sql_request_list.append(
            f"UPDATE Question SET position = position + 1 "
            f"WHERE position >= {input_question.position!r}")


    sql_request_list.append(f"insert into Question (position,title,text,image) values"
        f"({input_question.position!r},{input_question.title!r},"
        f"{input_question.text!r},{input_question.image!r})")

    insert_question,status_question = executeInsertStatement(sql_request_list)

    if not status_question == 200 :
        return insert_question,status_question

    insert_answer_string = ""
    for answer in input_answers :
       insert_answer_string += f"({insert_question['id']!r},{answer.text!r},{answer.isCorrect!r}),"

    insert_answer,status_answer = executeInsertStatement([
        f"insert into Reponse (id_question,text,isCorrect) values"
        f"{insert_answer_string[:-1]}"])

    if not status_answer == 200 :
        return insert_answer,status_answer

    return insert_question,status_question


def updateQuestion(question_json,idQuestion):
    idQuestion = int(idQuestion)
    input_question = Question()

    input_answers = [Answer() for answer in question_json["possibleAnswers"]]

    for i,answer_json in enumerate(question_json["possibleAnswers"]) :
        input_answers[i].from_json(answer_json.copy())

    question_json["possibleAnswers"] = input_answers
    input_question.from_json(question_json)

    question_json,status = getQuestionByID(idQuestion,True)
    if status == 200 :
        sql_request_list = list()
        if int(input_question.position) < question_json["position"] :
            sql_request_list.append(
            f"UPDATE Question SET position = -1 "
            f"WHERE id = {idQuestion!r}")

            sql_request_list.append(
            f"UPDATE Question SET position = position + 1 "
            f"WHERE position >= {input_question.position!r} and position < {question_json['position']!r}")
        elif int(input_question.position) > question_json["position"] :

            sql_request_list.append(
            f"UPDATE Question SET position = -1 "
            f"WHERE id = {idQuestion!r}")

            sql_request_list.append(
            f"UPDATE Question SET position = position - 1 "
            f"WHERE position <= {input_question.position!r} and position > {question_json['position']!r}")

        sql_request_list.append(
            f"UPDATE Question SET position = {input_question.position!r},"
            f"title = {input_question.title!r},"
            f"text = {input_question.text!r},"
            f"image = {input_question.image!r} WHERE id = {idQuestion!r}")

        sql_request_list.append(f"DELETE FROM Reponse WHERE id_question = {idQuestion!r}")

        insert_answer_string = ""
        for answer in input_answers :
            insert_answer_string += f"({idQuestion!r},{answer.text!r},{answer.isCorrect!r}),"

        sql_request_list.append(
            f"insert into Reponse (id_question,text,isCorrect) values"
            f"{insert_answer_string[:-1]}")


        return executeUpdateStatement(sql_request_list)
    return question_json,status


def selectQuestion(statement,idAnswer=False):
    response,status_code = executeSelectStatement(statement)
    if status_code == 200 :
        for id,position,title,text,image,answers in response :
            answers_split = answers.split("|")
            input_answers = [Answer() for answer in answers_split]

            for i,answer_tuple in enumerate(answers_split) :
                answer_tuple = answer_tuple.split("/-/")

                answer_dict = {"id":answer_tuple[0],"text":answer_tuple[1],"isCorrect":True if answer_tuple[2] == "1" else False}
                input_answers[i].from_json(answer_dict)

            question = Question()
            question.init(id,position,title,text,image,input_answers)
            return question.to_json(idAnswer), 200
        return {"message":"Question non trouv??e"},404
    else :
        return response, status_code


def getQuestionByID(id,idAnswer=False):
    return selectQuestion([f"SELECT Question.*, group_concat(Reponse.id||'/-/'||Reponse.text||'/-/'||Reponse.isCorrect,'|') as possibleAnswers FROM Reponse LEFT JOIN Question on Question.id = Reponse.id_question where Question.id = {id} GROUP BY Question.id"],idAnswer)

def getQuestionByPosition(position,idAnswer=False):
    return selectQuestion([f"SELECT Question.*, group_concat(Reponse.id||'/-/'||Reponse.text||'/-/'||Reponse.isCorrect,'|')"
    f" as possibleAnswers FROM Reponse LEFT JOIN Question on Question.id = Reponse.id_question where position = {position}  GROUP BY Question.id "],idAnswer)

def getQuizInfo():
    question_number,status = executeSelectStatement([f"SELECT COUNT(*) FROM Question"])

    if not status == 200 :
        return question_number,status

    participationRequest,participationStatus = executeSelectStatement([f"SELECT playerName,score,date FROM Participation ORDER BY score DESC"])
    if not participationStatus == 200 :
        return participationRequest,participationStatus
    list_participation = []
    for participation in participationRequest :
        list_participation.append({"playerName":participation[0],"score":participation[1],"date":participation[2]})


    return {"size":question_number.fetchone()[0],"scores":list_participation},200



def postParticipations(participation_json):
    quizInfoApiResult =getQuizInfo()
    if quizInfoApiResult[1] != 200 :
        return {"error":"Probl??me de r??cup??ration des informations du quiz"},500

    nombre_questions = quizInfoApiResult[0]["size"]

    if len(participation_json["answers"]) < nombre_questions :
        return {"error":"Le nombre des r??ponses est inf??rieur au nombre de questions"},400
    elif len(participation_json["answers"]) > nombre_questions :
        return {"error":"Le nombre des r??ponses est sup??rieur au nombre de questions"},400

    answersSummaries = []
    score = 0
    for i,reponse_submit in enumerate(participation_json["answers"]) :

        info_question = getQuestionByPosition(i+1)
        if info_question[1]!= 200 :
            return {"error":"Erreur dans la r??cup??ration des questions"},500

        possibleAnswers = info_question[0]["possibleAnswers"]

        for j,reponse in enumerate(possibleAnswers) :
            if reponse['isCorrect'] == True :
                isCorrect = False
                if j+1 == int(reponse_submit) :
                    score+=1
                    isCorrect = True
                answersSummaries.append((j+1,isCorrect))

    playerName = participation_json.get("playerName")
    insert_answers,status_answers = executeInsertStatement([f"INSERT INTO Participation (playerName,score,date) values ('{playerName}', '{score}', '{datetime.now().strftime('%d/%m/%y %H:%M:%S')}')"])

    if status_answers == 200 :
        return {
        "answersSummaries":answersSummaries,
        "score":score,
        "playerName":playerName
    },200

    return insert_answers,status_answers

def deleteAllParticipations():
    return executeDeleteStatement(["DELETE FROM Participation"])

