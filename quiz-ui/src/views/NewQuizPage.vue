<template>

    <div class="mx-auto my-auto">
      <div class="d-flex flex-column h-100 align-items-center">
        <h1>Nouveau Quiz</h1>
        <p> Saisissez votre nom :<br></p>
        <div class="row justify-content-md-center">
          <input class="m-1 col" type="text" v-model="username" id="name" name="name" size="10">
          <button class="m-1 btn btn-success col-md-auto" type="button" @click="launchNewQuiz"> GO!</button>

        </div>
      </div>
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
