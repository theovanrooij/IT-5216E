<template>
  <div class="d-flex flex-column justify-content-center align-items-center">
  <h1>{{ question.title }}</h1>
  <p>{{ question.text }}</p>
  <img v-if="question.image" :src="question.image" />

  <div class="d-flex justify-content-around w-100">
    <a v-for="(answer, index) in question.possibleAnswers" @click="$emit('answer-selected', index)">{{answer.text}}</a>
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