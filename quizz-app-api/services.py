from models import Question
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

def executeStatement(statement) :
    cur = getDbCursor()
    try:
    # Use the cursor to execute an INSERT statement
        cur.execute(statement)
        # send the request

        return cur, 200
    except sqlite3.Error as e:
    # If an error occurred, print the error message
        print(f"An error occurred: {e.args[0]}")
        cur.execute('rollback')
        return {"error" : {e.args[0]}}, 500

def executeInsertStatement(statement) :
    response,status_code = executeStatement(statement)
    if status_code == 200 :
        response.execute("commit")
        return {"id":response.lastrowid},status_code
    else :
        return response, status_code

def executeSelectStatement(statement):
    response,status_code = executeStatement(statement)
    if status_code == 200 :
        return response,status_code
    else :
        return response, status_code

def executeUpdateStatement(statement):
    response,status_code = executeStatement(statement)
    if status_code == 200 :
        response.execute("commit")
        return {},204
    else :
        return response, status_code

def executeDeleteStatement(statement):
    response,status_code = executeStatement(statement)
    if status_code == 200 :
        response.execute("commit")
        return {},204
    else :
        return response, status_code

def deleteAllQuestions():
    return executeDeleteStatement("DELETE FROM Question")

def deleteQuestionByID(id):
    question_json,status = getQuestionByID(id)

    if status == 200 :
        return executeDeleteStatement(f"DELETE FROM Question where id = {id}")

    return question_json,status

def postQuestions(question_json):
    input_question = Question()
    input_question.from_json(question_json)

    return executeInsertStatement(
        f"insert into Question (position,title,text,image) values"
        f"({input_question.position!r},{input_question.title!r},"
        f"{input_question.text!r},{input_question.image!r})")

def updateQuestion(question_json,idQuestion):
    input_question = Question()
    input_question.from_json(question_json)

    question_json,status = getQuestionByID(idQuestion)

    if status == 200 :

        return executeUpdateStatement(
            f"UPDATE Question SET position = {input_question.position!r},"
            f"title = {input_question.title!r},"
            f"text = {input_question.text!r},"
            f"image = {input_question.image!r} WHERE id = {idQuestion!r}")
            
    return question_json,status


def selectQuestion(statement):
    response,status_code = executeSelectStatement(statement)
    if status_code == 200 :
        for id,position,title,text,image in response :
            question = Question()
            question.init(id,position,title,text,image)
            return question.to_json(), 200
        return {"message":"Question non trouvée"},404
    else :
        return response, status_code


def getQuestionByID(id):
    return selectQuestion(f"SELECT * FROM Question where id = {id}")

def getQuestionByPosition(position):
    return selectQuestion(f"SELECT * FROM Question where position = {position}")