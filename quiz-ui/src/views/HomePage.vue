<template>
  <h1>Page d'accueil</h1>
  <p>Bienvenue sur notre Quiz. <br> Vous avez à votre disposition {{ numberQuestion }} questions sur le thème des drapeaux de Pays. <br>
     Vous disposez d'un temps illimité pour répondre aux questions. <br>
     Pour chaque question, une seule réponse est correcte. Une bonne réponse rapporte 1 point. Une mauvaise réponse ne fait pas perdre de points.</p>
  <table class="table text-reset table-sm caption-top" style="overflow: hidden;">
    <caption>Classement des participations</caption>
    <thead>
      <td>Position</td>
      <td>Username</td>
      <td>Score</td>
      <td>Date</td>
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


</template>
 <style>
    body {
      min-height: 100vh;
      height: auto;
    }
  </style>
<script>
// {/* <style> <p> Test </p></style> */}
import quizApiService from "@/services/QuizApiService";

export default {
  name: "HomePage",
  data() {
    return {
      registeredScores : [],
      numberQuestion : 0

    };
  },
  components: {

  },
  async created() {
		console.log("Composant Home page 'created'");
	  let quizInfoPromise = quizApiService.getQuizInfo();
	  let quizInfoApiResult = await quizInfoPromise;
    this.registeredScores = quizInfoApiResult.data.scores;
    this.numberQuestion = quizInfoApiResult.data.size;
  }
};
</script>