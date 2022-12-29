<template>
  <ul>
    <li v-for="question in question_list">{{ question.text }} <span @click="$emit('question-edit', question.position)">EDIT</span></li>
  </ul>
</template>

<script>
export default {
  name: "QuestionList",
  data() {
    return {
      questions : Array()
    };
  },
  props: {
    question_list: {
      type: Object
    },
    emits: ["question-edit"]
  }
};
</script>
