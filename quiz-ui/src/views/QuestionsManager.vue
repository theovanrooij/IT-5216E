<template>
  <div class="questions-manager">
  <h1>Questions Manager</h1>
  <h1>Question {{ currentQuestionPosition }} / {{ totalNumberOfQuestion }}</h1>
  <QuestionDisplay v-bind:question="currentQuestion" @answer-selected="answerClickedHandler" />
  </div>
 </template>



<script>
import QuestionDisplay from './QuestionDisplay.vue';
import quizApiService from "@/services/QuizApiService";
import participationStorageService from "@/services/ParticipationStorageService";

export default {
  name: "Questions Manager",
  data() {
    return {
      currentQuestion : {
      },
      currentQuestionPosition : 1,
      totalNumberOfQuestion : 4,
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
      var questionPromise = quizApiService.getQuestion(this.currentQuestionPosition);
      var questionApiResult = await questionPromise;
      // console.log(questionApiResult)
      return questionApiResult.data
    },
    async answerClickedHandler(position){

      this.answersSelected.push(position)
      console.log(this.answersSelected)

      if (this.currentQuestionPosition == this.totalNumberOfQuestion) {
        console.log("Score Final",this.score)
      } else {
        this.currentQuestionPosition += 1
        this.currentQuestion = await this.loadQuestionByposition();
      }
    },
    async endQuiz(){
      console.log("endQuiz");
    },

  }
};
</script>