from models import Question
import sqlite3

def postQuestions(question_json):
    input_question = Question()
    input_question.from_json(question_json)

    # create a connection
    db_connection = sqlite3.connect("./quiz.db")

    # set the sqlite connection in "manual transaction mode"
    # (by default, all execute calls are performed in their own transactions, not what we want)
    db_connection.isolation_level = None

    cur = db_connection.cursor()
    # start transaction
    cur.execute("begin")

    # save the question to db
    insertion_result = cur.execute(
        f"insert into Question (position,title,text,image) values"
        f"('{input_question.position}','{input_question.title}',"
        f"'{input_question.text}','{input_question.image}')")

    # send the request
    cur.execute("commit")

    # # in case of exception, rollback the transaction
    # cur.execute('rollback')


    return input_question.to_json(), 200