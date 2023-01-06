<template>
  <div class="d-flex flex-column justify-content-center align-items-center w-80">
    <h1>{{ question.title }}</h1>
    <p>{{ question.text }}</p>
    <img v-if="question.image" :src="question.image" height="450"/>

    <div class="row justify-content-md-center my-5">
      <a class=" col mx-3 d-flex align-items-center text-center " v-for="(answer, index) in question.possibleAnswers" @click="$emit('answer-selected', index)">{{answer.text}}</a>
    </div>

  </div>
</template>


<script>
export default {
  name: "QuestionDisplay",
  props: {
    question: {
      type: Object
    },
    emits: ["answer-selected"]
  }
};
</script>