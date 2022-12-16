# Exemple de création de classe en python

class Answer() :
    def init(self,text:str,isCorrect:bool) :
        self.text = text
        self.isCorrect = isCorrect
        self.id_question = None

    def to_json(self):
        question_json = dict()
        for key, value in self.__dict__.items():
            if value is not None:
                question_json[key] = value
        return question_json

    def from_json(self,question_json):
        for k,v in question_json.items() :
            setattr(self,k,v)

class Question():

    def init(self,id:int,position:int,title:str,text:str,image:str,possibleAnswers=list[Answer]) :
        self.id = id
        self.position = position
        self.title = title
        self.text = text
        self.image = image
        self.possibleAnswers = possibleAnswers

    def to_json(self):
        question_json = dict()
        for key, value in self.__dict__.items():
            if value is not None:
                question_json[key] = value
        return question_json

    def from_json(self,question_json):
        for k,v in question_json.items() :
            setattr(self,k,v)
