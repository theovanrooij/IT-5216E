<template>
  <form >
    <div class="row g-2 d-flex flex-wrap flex-column my-5 align-items-center">
      <h2 class="text-center">Edition de question</h2>
      <div class="col-md my-3">
        <div class="form-floating">
          <input type="text" class="form-control" id="floatingInputGrid" placeholder="Title" v-model="question.title">
          <label for="floatingInputGrid">Question Title</label>
        </div>
      </div>
      <div class="col-md my-3">
        <div class="form-floating">
          <input type="text" class="form-control" id="floatingInputGrid" placeholder="Text" v-model="question.text">
          <label for="floatingInputGrid">Question Text</label>
        </div>
      </div>
      <div class="row my-3">
        <div class="col-md">
          <div class="form-floating">
            <input type="number" class="form-control" id="floatingInputGrid" placeholder="Position" v-model="question.position">
            <label for="floatingInputGrid">Question number</label>
          </div>
        </div>

        <div class="col-md d-flex align-items-center justify-content-around ">
            <ImageUpload @file-change="imageFileChangedHandler" />
        </div>
      </div>


      <div class="col-md answers d-flex flex-wrap">
        <div class="col-md d-flex flex-wrap flex-column mx-3">
          <div class="col-md ">
            <div class="form-floating">
              <input type="text" class="form-control" id="floatingInputGrid1" v-model="this.firstAnswer.text">
              <label for="floatingInputGrid1">Answer 1 text</label>
            </div>
          </div>
          <div class="col-md my-2 ">
            <div class="form-floating">
              <select class="form-select" id="floatingSelect1" aria-label="Floating label select example" v-model="this.firstAnswer.isCorrect">
                <option selected value=false>False</option>
                <option value=true>True</option>
              </select>
              <label for="floatingSelect1">Answer 1 Truth value</label>
            </div>
          </div>
        </div>

        <div class="col-md d-flex flex-wrap flex-column mx-3">
          <div class="col-md">
            <div class="form-floating">
              <input type="text" class="form-control" id="floatingInputGrid2" v-model="this.secondAnswer.text">
              <label for="floatingInputGrid2">Answer 2 text</label>
            </div>
          </div>
          <div class="col-md my-2">
            <div class="form-floating">
              <select class="form-select" id="floatingSelect2" aria-label="Floating label select example" v-model="this.secondAnswer.isCorrect">
                <option selected value=false>False</option>
                <option value=true>True</option>
              </select>
              <label for="floatingSelect2">Answer 2 Truth value</label>
            </div>
          </div>
        </div>

        <div class="col-md d-flex flex-wrap flex-column mx-3">
          <div class="col-md">
            <div class="form-floating">
              <input type="text" class="form-control" id="floatingInputGrid2" v-model="this.thirdAnswer.text">
              <label for="floatingInputGrid2">Answer 3 text</label>
            </div>
          </div>
          <div class="col-md my-2">
            <div class="form-floating">
              <select class="form-select" id="floatingSelect3" aria-label="Floating label select example" v-model="this.thirdAnswer.isCorrect">
                <option selected value=false>False</option>
                <option value=true>True</option>
              </select>
              <label for="floatingSelect3">Answer 3 Truth value</label>
            </div>
          </div>
        </div>

        <div class="col-md d-flex flex-wrap flex-column mx-3">
          <div class="col-md">
            <div class="form-floating">
              <input type="text" class="form-control" id="floatingInputGrid4" v-model="this.fourthAnswer.text">
              <label for="floatingInputGrid4">Answer 4 text</label>
            </div>
          </div>
          <div class="col-md my-2">
            <div class="form-floating">
              <select class="form-select" id="floatingSelect4" aria-label="Floating label select example" v-model="this.fourthAnswer.isCorrect">
                <option selected value=false>False</option>
                <option value=true>True</option>
              </select>
              <label for="floatingSelect4">Answer 4 Truth value</label>
            </div>
          </div>
        </div>

      </div>
      <button type="button" class="btn btn-success" @click="submit">Valider</button>
    </div>
  </form>
</template>

<script>
import ImageUpload from './ImageUpload.vue';
export default {
  name: "QuestionEdit",
  props: {
    question: {
      type: Object
    },
    emits: ["update:question"]
  },
  data() {
    return {
      image : this.question.image,
      firstAnswer : {
        text : null,
        isCorrect: null
      },
      secondAnswer :{
        text : null,
        isCorrect: null
      },
      thirdAnswer : {
        text : null,
        isCorrect: null
      },
      fourthAnswer :{
        text : null,
        isCorrect: null
      },
    }
  },

  components: {
    ImageUpload
  },
  mounted() {
    // Destructure the first element from the names prop
    if (this.question.possibleAnswers) {
      const [firstAnswer,secondAnswer,thirdAnswer,fourthAnswer] = this.question.possibleAnswers;
      this.firstAnswer = firstAnswer ? firstAnswer : {text:null, isCorrect:null}
      this.secondAnswer = secondAnswer ? secondAnswer : {text:null, isCorrect:null}
      this.thirdAnswer = thirdAnswer ? thirdAnswer : {text:null, isCorrect:null}
      this.fourthAnswer = fourthAnswer ? fourthAnswer : {text:null, isCorrect:null}
    }

  },
  emits: ["update:question"],
  methods: {
    imageFileChangedHandler(b64String) {
      this.image = b64String;
    },
    submit() {
      let possibleAnswersArray = Array()
      if (this.firstAnswer.text) {
        possibleAnswersArray.push({
          text : this.firstAnswer.text,
          isCorrect : this.firstAnswer.isCorrect === "true" ? true : false
        })
      }
      if (this.secondAnswer.text) {
        possibleAnswersArray.push({
          text : this.secondAnswer.text,
          isCorrect : this.secondAnswer.isCorrect === "true" ? true : false
        })
      }
      if (this.thirdAnswer.text) {
        possibleAnswersArray.push({
          text : this.thirdAnswer.text,
          isCorrect : this.thirdAnswer.isCorrect === "true" ? true : false
        })
      }
      if (this.fourthAnswer.text) {
        possibleAnswersArray.push({
          text : this.fourthAnswer.text,
          isCorrect : this.fourthAnswer.isCorrect === "true" ? true : false
        })
      }
      this.$emit('update:question', {
        title : this.question.title,
        text : this.question.text,
        image : this.image,
        position : this.question.position,
        possibleAnswers : possibleAnswersArray
      })
    }
  }
};
</script>