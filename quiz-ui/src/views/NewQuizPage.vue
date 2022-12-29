<template>
  <div class="new-quiz-page">
    <h1>New Quiz Page</h1>

    <p> <br><br><br><br><br><br><br><br><br><br><br><br>Saisissez votre nom :<br>
    <input type="text" v-model="username" id="name" name="name" size="10">
    <button class="btn btn-success" type="button" @click="launchNewQuiz"> GO!</button>
    <p>{{ playerName }}</p>
  </p>
  </div>
</template>

<style>
@media (min-width: 1024px) {
  .about {
    min-height: 100vh;
    display: flex;
    align-items: center;
  }
}
</style>

<script>
import participationStorageService from "@/services/ParticipationStorageService";

export default {
  name: "NewQuizPage",
  data() {
    return {
      username : ''
    };
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
