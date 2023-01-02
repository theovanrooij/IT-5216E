# Exemple de création de classe en python

class Answer() :
    def init(self,text:str,isCorrect:bool,id=None) :

        self.text = text
        self.isCorrect = isCorrect
        self.id_question = None
        self.id=None

    def to_json(self,idAnswer=False):
        question_json = dict()
        for key, value in self.__dict__.items():
            if value is not None and not key =="id" :
                question_json[key] = value
        if idAnswer :
            question_json["id"] = self.id
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

    def to_json(self,idAnswer=False):
        question_json = dict()
        for key, value in self.__dict__.items():
            if value is not None and not key == "possibleAnswers":
                question_json[key] = value
        question_json["possibleAnswers"] = [answer.to_json(idAnswer) for answer in self.possibleAnswers]
        return question_json

    def from_json(self,question_json):
        for k,v in question_json.items() :
            setattr(self,k,v)
