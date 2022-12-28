<template>
  <div class="questions-manager">
    <h1>Questions Manager</h1>
    <h1>Question {{ currentQuestionPosition }} / {{ totalNumberOfQuestion }}</h1>
    <QuestionDisplay :question="currentQuestion" @answer-selected="answerClickedHandler" />
  </div>
</template>



<script>
import QuestionDisplay from './QuestionDisplay.vue';
import quizApiService from "@/services/QuizApiService";

export default {
  name: "Questions Manager",
  data() {
    return {
      currentQuestion : {
      },
      currentQuestionPosition : 1,
      totalNumberOfQuestion : 10,
      answersSelected : Array()
    };
  },
  components: {
    QuestionDisplay
  },
  async created() {
    this.currentQuestion = await this.loadQuestionByposition();

  },

  methods: {
    async loadQuestionByposition(){
      let questionPromise = quizApiService.getQuestion(this.currentQuestionPosition);
      let questionApiResult = await questionPromise;
      return questionApiResult.data
    },
    async answerClickedHandler(position){

      this.answersSelected.push(position)

      if (this.currentQuestionPosition == this.totalNumberOfQuestion) {
        this.endQuiz()
      } else {
        this.currentQuestionPosition += 1
        this.currentQuestion = await this.loadQuestionByposition();
      }
    },
    async endQuiz(){
      console.log("endQuiz");
      console.log(this.answersSelected)
    },

  }
};
</script>