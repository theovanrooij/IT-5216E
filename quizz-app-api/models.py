# Exemple de création de classe en python
class Question():

    def init(self,id:int,position:int,title:str,text:str,image:str) :
        self.id = id
        self.position = position
        self.title = title
        self.text = text
        self.image = image

    def to_json(self):
        question_json = dict()
        for key, value in self.__dict__.items():
            if value is not None:
                question_json[key] = value
        return question_json

    def from_json(self,question_json):
        for k,v in question_json.items() :
            setattr(self,k,v)
