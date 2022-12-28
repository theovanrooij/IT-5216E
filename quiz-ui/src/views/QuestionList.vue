<template>
  <ul>
    <li v-for="question in questions">{{ question.text }} <span @click="$emit('question-edit', question.id)">EDIT</span></li>
  </ul>
</template>

<script>

import quizApiService from "@/services/QuizApiService";
export default {
  name: "QuestionList",
  data() {
    return {
      questions : Array()
    };
  },
  props: {
    question: {
      type: Object
    },
    emits: ["question-edit"]
  },
  async created() {

    for (var i = 1; i <= 10; i++) {
      let questionPromise = quizApiService.getQuestion(i);
      let questionApiResult = await questionPromise;
      this.questions.push(questionApiResult.data)
    }
  }
};
</script>
