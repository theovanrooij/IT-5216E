<template>
  <h1>Home page</h1>

  <div v-for="scoreEntry in registeredScores" v-bind:key="scoreEntry.date">
    {{ scoreEntry.playerName }} - {{ scoreEntry.score }}
  </div>
  <router-link to="/start-new-quiz-page">Démarrer le quiz !</router-link>
</template>

<script>
// {/* <style> <p> Test </p></style> */}
import quizApiService from "@/services/QuizApiService";

export default {
  name: "HomePage",
  data() {
    return {
      registeredScores : []
    };
  },
  components: {

  },
  async created() {
		console.log("Composant Home page 'created'");
	  let quizInfoPromise = quizApiService.getQuizInfo();
	  let quizInfoApiResult = await quizInfoPromise;
    this.registeredScores = quizInfoApiResult.data.scores;
  }
};
</script>