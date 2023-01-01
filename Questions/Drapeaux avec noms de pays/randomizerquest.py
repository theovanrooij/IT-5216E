import os
import random


files = []
for file in os.listdir("./base64"):
    files.append(file.split(".")[0])
# print(files)

nb_questions = 20
for i in range(nb_questions) :

    question_random = random.sample(files, k=4)
    print(question_random)
    vrai_pays = random.choice(question_random)
    print(vrai_pays)
    fich = open("./base64/"+str(vrai_pays)+".txt", "r")
    image_vrai_pays =  fich.read()
    fich.close()
   

    fichier = open("question"+str(i+1)+".json", "a",encoding="utf-8")
    fichier.write(
str("""  
{\n\t"text": "Quel est le pays associé à ce drapeau ?",""")
    +str("""\n\t"title": " """) + str(""" Voici un joli pays numéro """+str(i+1)+str(""" ", """)
    +str("""\n\t"image": " """) + str(image_vrai_pays)+ str(""" ", """)
    +str("""\n\t"position": """)+str(i+1)+str(""",""")
    +str("""\n\t"possibleAnswers": [""")
    +str("""\n\t\t{\n\t\t\t"text": " """)+str(question_random[0])+str("""",\n\t\t\t"isCorrect": """)+str(question_random[0]==vrai_pays).lower()+str("""\n\t\t},""")
    +str("""\n\t\t{\n\t\t\t"text": " """)+str(question_random[1])+str("""",\n\t\t\t"isCorrect": """)+str(question_random[1]==vrai_pays).lower()+str("""\n\t\t},""")
    +str("""\n\t\t{\n\t\t\t"text": " """)+str(question_random[2])+str("""",\n\t\t\t"isCorrect": """)+str(question_random[2]==vrai_pays).lower()+str("""\n\t\t},""")
    +str("""\n\t\t{\n\t\t\t"text": " """)+str(question_random[3])+str("""",\n\t\t\t"isCorrect": """)+str(question_random[3]==vrai_pays).lower()+str("""\n\t\t}""")
    +str("""\n\t]""")
    +str("""\n}""")

    ))
    fichier.close()