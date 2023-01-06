<template>

      <div>
        <div v-if="numberQuestion">

          <p> Saisissez votre nom :<br></p>
          <div class="row justify-content-md-center">
            <input class="m-1 col" type="text" v-model="username" id="name" name="name" size="10">
            <button class="m-1 btn btn-success col-md-auto" type="button" @click="launchNewQuiz"> GO!</button>

          </div>
        </div>
        <div v-else class="text-center">
          Aucune question n'a été inscrite. <br>
          Par conséquent vous ne pouvez pas commencer de nouveau quiz. <br>
          Veuillez vous connecter à l'administration pour en ajouter.
        </div>

      </div>
</template>

<script>
import participationStorageService from "@/services/ParticipationStorageService";
import quizApiService from "@/services/QuizApiService";

export default {
  name: "NewQuizPage",
  data() {
    return {
      username : '',
      numberQuestion : 0
    };
  },
  async created() {
		console.log("Composant Home page 'created'");
	  let quizInfoPromise = quizApiService.getQuizInfo();
	  let quizInfoApiResult = await quizInfoPromise;
    this.numberQuestion = quizInfoApiResult.data.size;
  },
  methods: {
    buttonClickHandler(){
      console.log('Compute username');
      this.username = this.data.username;
    },
    launchNewQuiz(){
      participationStorageService.savePlayerName(this.username.toString());
      const playerName = participationStorageService.getPlayerName();
      console.log("Launch new quiz with " + playerName);
      this.$router.push('/questions-manager');
    },
  }
};
</script>
