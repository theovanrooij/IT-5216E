<template>
  <h1>Home page</h1>

  <div v-for="scoreEntry in registeredScores" v-bind:key="scoreEntry.date">
  {{ scoreEntry.playerName }} - {{ scoreEntry.score }}
  <router-link to="/start-new-quiz-page">Démarrer le quiz !</router-link>

</div>

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
		// console.log("Composant Home page 'created'");
	  var quizInfoPromise = quizApiService.getQuizInfo();
	  var quizInfoApiResult = await quizInfoPromise;
    this.registeredScores = quizInfoApiResult.data.scores;
  }
};
</script>