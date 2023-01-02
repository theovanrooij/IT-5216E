<template>
  <div >
    <h1>Administration</h1>
    <div v-if="token">
      <div class="addQuestion" @click="addQuestionHandler">
        ADD QUESTION
      </div>
      <div class="deleteAllQuestions" @click="deleteAllQuestions">
        DELETE ALL QUESTIONS
      </div>
      <div class="deleteAllParticipations" @click="deleteAllParticipations">
        DELETE ALL PARTICIPATIONS
      </div>
      <QuestionList v-if="admin_mode === 'list'" :question_list="question_list" @question-edit="editQuestionHandler" @question-delete="deleteQuestionById"/>
      <QuestionEdit v-else-if="admin_mode === 'editQuestion'" :question="question" @update:question="updateQuestion"/>
      <QuestionEdit v-else-if="admin_mode === 'newQuestion'" :question="emptyQuestion" @update:question="postQuestion"/>

      <table class="table text-reset table-sm caption-top" style="overflow: hidden;">
      <caption>Gestionnaire des questions</caption>
      <thead>
        <td>Position</td>
        <td>Questions</td>
        <td>EDIT</td>
        <td>DELETE</td>
      </thead>
      <tbody>
        <tr v-for="(scoreEntry,index) in registeredScores">
          <td>{{ index }}</td>
          <td>{{ scoreEntry.playerName }} </td>
          <td>{{ scoreEntry.score }}</td>
          <td>{{ scoreEntry.date }}</td>
        </tr>
      </tbody>
    </table>






    </div>
    <div v-else class="loginForm">
      <p>Saisissez le mot de passe :</p>
      <input type="text" v-model="password" id="name" name="name" size="10">
      <button class="btn btn-success" type="button" @click="loginPlayer">Connexion</button>
    </div>

  </div>
</template>

<script>
import QuestionList from './QuestionList.vue';
import QuestionEdit from './QuestionEdit.vue';
import participationStorageService from "@/services/ParticipationStorageService";
import quizApiService from "@/services/QuizApiService";

export default {
  name: "Administration",
  data() {
    return {
      password : '',
      token : null,
      admin_mode : "list",
      question : null,
      question_list : Array(),
      forceUpdateValue: false,
      emptyQuestion : {
        text : null,
        title : null,
        image : null,
        position : null,
        possibleAnswers : null
      }
    };
  },
  components: {
    QuestionList,
    QuestionEdit
  },
  async created() {

    this.token = participationStorageService.getToken();
    this.updateQuestionList()
  },
  methods: {
    async loginPlayer(){
      let loginPromise = quizApiService.login(this.password);
	    let loginApiResult = await loginPromise;

      if (loginApiResult) {
        participationStorageService.saveToken(loginApiResult.data.token)
        this.token = loginApiResult.data.token
      }

    },
    addQuestionHandler(){
      this.admin_mode = 'newQuestion'
    },
    async deleteAllQuestions(){
      // TODO: Gérer les erreurs
      await quizApiService.deleteAllQuestions(this.token)
      this.token = participationStorageService.getToken()
      this.updateQuestionList()
      this.admin_mode = 'list'
    },
    async deleteQuestionById(questionPosition){
      // TODO: Gérer les erreurs
      let questionPromise = quizApiService.getQuestion(questionPosition);
	    let questionApiResult = await questionPromise;
      console.log(questionApiResult)
      await quizApiService.deleteQuestionById(questionApiResult.data.id,this.token)
      this.updateQuestionList()
    },
    async deleteAllParticipations(){
      // TODO: Gérer les erreurs
      await quizApiService.deleteAllParticipations(this.token)
      this.token = participationStorageService.getToken()
    },
    async updateQuestionList(){

      this.question_list = Array()
      let quizInfoPromise = quizApiService.getQuizInfo();
      let quizInfoApiResult = await quizInfoPromise;

      for (let i = 1; i <= quizInfoApiResult.data.size; i++) {
        try {
          let questionPromise = quizApiService.getQuestion(i);
          let questionApiResult = await questionPromise;
          this.question_list.push(questionApiResult.data)
        } catch (error){
          console.log(error)
        }
      }
    },
    async editQuestionHandler(questionPosition){
      let questionPromise = quizApiService.getQuestion(questionPosition);
	    let questionApiResult = await questionPromise;
      this.admin_mode = 'editQuestion'
      this.question=questionApiResult.data
    },
    async updateQuestion(new_question){
      // TODO: Gérer les erreurs
      await quizApiService.updateQuestion(this.question.id,new_question,this.token);
      this.token = participationStorageService.getToken();
      this.updateQuestionList()
      this.admin_mode = 'list'

    },
    async postQuestion(new_question){
      console.log(new_question)
      await quizApiService.postQuestion(new_question,this.token);
      this.token = participationStorageService.getToken();
      this.updateQuestionList()
      this.admin_mode = 'list'
    },
  }
};
</script>
