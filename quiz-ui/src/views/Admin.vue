<template>
  <div >
    <h1>Administration</h1>
    <div v-if="token">
      <QuestionList v-if="admin_mode === 'list'" @question-edit="editQuestionHandler"/>
      <!-- <QuestionList v-else-if="admin_mode === 'editQuestion'" @question-edit="editQuestionHandler"/> -->
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
import participationStorageService from "@/services/ParticipationStorageService";
import quizApiService from "@/services/QuizApiService";

export default {
  name: "Administration",
  data() {
    return {
      password : '',
      token : null,
      admin_mode : "list"
    };
  },
  components: {
    QuestionList
  },
  async created() {
    this.token = await participationStorageService.getToken();

  },
  methods: {
    async loginPlayer(){
      var loginPromise = quizApiService.login(this.password);
	    var loginApiResult = await loginPromise;

      if (loginApiResult) {
        participationStorageService.saveToken(loginApiResult.data.token)
        this.token = loginApiResult.data.token
      }
      console.log(loginApiResult)

    },
    async editQuestionHandler(questionId){
      console.log(questionId)
      this.admin_mode = 'editQuestion'
    }
  }
};
</script>
