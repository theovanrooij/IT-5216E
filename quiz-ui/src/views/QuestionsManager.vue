<template>
  <div class="questions-manager my-3">
    <h1>Question {{ currentQuestionPosition }} / {{ totalNumberOfQuestion }}</h1>
    <QuestionDisplay :question="currentQuestion" @answer-selected="answerClickedHandler" />
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
      totalNumberOfQuestion : null,
      answersSelected : Array()
    };
  },
  components: {
    QuestionDisplay
  },
  async created() {
    this.currentQuestion = await this.loadQuestionByposition();
    let quizInfoPromise = quizApiService.getQuizInfo();
    let quizInfoApiResult = await quizInfoPromise;
    this.totalNumberOfQuestion = quizInfoApiResult.data.size
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
      let quizSubmitPromise = quizApiService.submitQuiz({
        "playerName": participationStorageService.getPlayerName(),
        "answers" : this.answersSelected
      });
      let quizSubmitApiResult = await quizSubmitPromise
      this.$router.push('/');
    },

  }
};
</script>