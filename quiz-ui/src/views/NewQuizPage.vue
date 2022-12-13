<template>
  <div class="new-quiz-page">
    <h1>New Quiz Page</h1>
     
    <p> <br><br><br><br><br><br><br><br><br><br><br><br>Saisissez votre nom :<br>
    <input type="text" v-model="username" id="name" name="name" size="10">
    <button class="favorite styled" type="button"> GO!</button>
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
export default {
  name: "NewQuizPage",
  data() {
    return { 
      username : ''
    };
  }
}
</script>