import axios from "axios";

import participationStorageService from "@/services/ParticipationStorageService";

const instance = axios.create({
	baseURL: `${import.meta.env.VITE_API_URL}`,
  json: true
});

export default {
  async call(method, resource, data = null, token = null) {
    let headers = {
      "Content-Type": "application/json",
    };
    if (token != null) {
      headers.authorization = "Bearer " + token;
    }

    return instance({
      method,
      headers: headers,
      url: resource,
      data,
    })
      .then((response) => {
        return { status: response.status, data: response.data };
      })
      .catch((error) => {
        console.error(error);
        if (error.response.status == 401) {
          participationStorageService.saveToken('')
        }
      });
  },
  getQuizInfo() {
    return this.call("get", "quiz-info");
  },
  getQuestion(position) {
    return this.call("get", "questions?position="+position);
  },
  login(password) {
    return this.call("post", "login",{"password":password});
  },
  updateQuestion(questionID,question,token) {
    return this.call("put", "questions/"+questionID,question,token);
  },
  postQuestion(question,token) {
    return this.call("post", "questions",question,token);
  },
  deleteAllQuestions(token) {
    return this.call("delete", "questions/all",null,token);
  },
  deleteQuestionById(idQuestion,token) {
    return this.call("delete", "questions/"+idQuestion,null,token);
  },
  deleteAllParticipations(token) {
    return this.call("delete", "participations/all",null,token);
  },
  submitQuiz(quizSubmission){
    return this.call("post", "participations",quizSubmission);
  }

};