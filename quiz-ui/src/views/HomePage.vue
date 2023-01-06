<script setup>
import { RouterLink } from 'vue-router'
</script>


<template>
  <h3 class="mb-4">Bienvenue sur DrapQuiz !</h3>
  <p>Vous avez à votre disposition {{ numberQuestion }} questions sur le thème des drapeaux de Pays. <br>
     Vous disposez d'un temps illimité pour répondre aux questions. <br>
     Pour chaque question, une seule réponse est correcte. Une bonne réponse rapporte 1 point. Une mauvaise réponse ne fait pas perdre de points.</p>
     <RouterLink to="/new-quiz-page"><button type="button" class="btn btn-primary btn-lg btn-block my-3 ">Jouer</button></RouterLink>

  <caption>Podium</caption>
  <div id="podium">
    <span class="podium_name">{{ registeredScores[1].playerName }}</span>
    <span class="podium_name">{{ registeredScores[0].playerName }}</span>
    <span class="podium_name">{{ registeredScores[2].playerName }}</span>
  </div>
  <table class="table text-reset table-sm caption-top table-striped table-hover text-center" v-if="registeredScores.length">
    <caption class="text-center">Classement des participations</caption>
    <thead>
      <tr>
        <th>Position</th>
        <th>Username</th>
        <th>Score</th>
        <th>Date</th>
      </tr>
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

  <table class="table text-reset table-sm caption-top" v-else>
    <caption>Il n'y a aucune participation pour le moment.</caption>

  </table>
  <div>
    par DANG Méline, TA Christophe, VAN ROOIJ Théo :
    <a href="https://github.com/theovanrooij/IT-5216E/">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-github" viewBox="0 0 16 16">
        <path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.012 8.012 0 0 0 16 8c0-4.42-3.58-8-8-8z"/>
      </svg>
    </a>

  </div>
</template>

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


<style>
  #podium{
    min-height:232px;
    width:500px;
    background-image: url("../assets/podium.png");

  }

  #podium span{
    font-size: larger;
    display:inline-block;
    width:32%;
    text-align:center;
    position:relative;
}
#podium span:nth-child(1){ top:55px;left:40px }
#podium span:nth-child(2){ top:0px;left:5px; }
#podium span:nth-child(3){ top:70px;right:30px; }
</style>