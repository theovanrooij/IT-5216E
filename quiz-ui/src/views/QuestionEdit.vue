<template>
  <form >
    <div class="row g-2 d-flex flex-wrap flex-column">
      <div class="col-md">
        <div class="form-floating">
          <input type="text" class="form-control" id="floatingInputGrid" placeholder="Title" v-model="question.title">
          <label for="floatingInputGrid">Question Title</label>
        </div>
      </div>
      <div class="col-md">
        <div class="form-floating">
          <input type="text" class="form-control" id="floatingInputGrid" placeholder="Text" v-model="question.text">
          <label for="floatingInputGrid">Question Text</label>
        </div>
      </div>
      <div class="col-md">
        <div class="form-floating">
          <input type="number" class="form-control" id="floatingInputGrid" placeholder="Position" v-model="question.position">
          <label for="floatingInputGrid">Question number</label>
        </div>
      </div>

      <div class="col-md">
        <div class="form-floating">
          <textarea class="form-control" placeholder="Leave a comment here" id="floatingTextarea" style="height: 100px" v-model="question.image"></textarea>
          <label for="floatingTextarea">Image</label>
        </div>
      </div>

      <div class="col-md answers d-flex flex-wrap">
        <div class="col-md d-flex flex-wrap flex-column">
          <div class="col-md">
            <div class="form-floating">
              <input type="text" class="form-control" id="floatingInputGrid" v-model="this.firstAnswer.text">
              <label for="floatingInputGrid">Answer 1 text</label>
            </div>
          </div>
          <div class="col-md">
            <div class="form-floating">
              <select class="form-select" id="floatingSelect" aria-label="Floating label select example" v-model="this.firstAnswer.isCorrect">
                <option selected value=false>False</option>
                <option value=true>True</option>
              </select>
              <label for="floatingSelect">Answer 1 Truth value</label>
            </div>
          </div>
        </div>

        <div class="col-md d-flex flex-wrap flex-column">
          <div class="col-md">
            <div class="form-floating">
              <input type="text" class="form-control" id="floatingInputGrid" v-model="this.secondAnswer.text">
              <label for="floatingInputGrid">Answer 2 text</label>
            </div>
          </div>
          <div class="col-md">
            <div class="form-floating">
              <select class="form-select" id="floatingSelect" aria-label="Floating label select example" v-model="this.secondAnswer.isCorrect">
                <option selected value=false>False</option>
                <option value=true>True</option>
              </select>
              <label for="floatingSelect">Answer 2 Truth value</label>
            </div>
          </div>
        </div>

        <div class="col-md d-flex flex-wrap flex-column">
          <div class="col-md">
            <div class="form-floating">
              <input type="text" class="form-control" id="floatingInputGrid" v-model="this.thirdAnswer.text">
              <label for="floatingInputGrid">Answer 3 text</label>
            </div>
          </div>
          <div class="col-md">
            <div class="form-floating">
              <select class="form-select" id="floatingSelect" aria-label="Floating label select example" v-model="this.thirdAnswer.isCorrect">
                <option selected value=false>False</option>
                <option value=true>True</option>
              </select>
              <label for="floatingSelect">Answer 3 Truth value</label>
            </div>
          </div>
        </div>

        <div class="col-md d-flex flex-wrap flex-column">
          <div class="col-md">
            <div class="form-floating">
              <input type="text" class="form-control" id="floatingInputGrid" v-model="this.fourthAnswer.text">
              <label for="floatingInputGrid">Answer 4 text</label>
            </div>
          </div>
          <div class="col-md">
            <div class="form-floating">
              <select class="form-select" id="floatingSelect" aria-label="Floating label select example" v-model="this.fourthAnswer.isCorrect">
                <option selected value=false>False</option>
                <option value=true>True</option>
              </select>
              <label for="floatingSelect">Answer 4 Truth value</label>
            </div>
          </div>
        </div>

      </div>
      <button type="button" class="btn btn-success" @click="submit">Valider</button>
      <!-- @click="$emit('question-edit-bdd', question.position)" -->
    </div>
  </form>
  {{ question.possibleAnswers }}
</template>

<script>
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
  mounted() {
    // Destructure the first element from the names prop
    if (this.question.possibleAnswers) {
      const [firstAnswer,secondAnswer,thirdAnswer,fourthAnswer] = this.question.possibleAnswers;
      this.firstAnswer = firstAnswer ? firstAnswer : {text:null, isCorrect:null}
      this.secondAnswer = secondAnswer ? firstAnswer : {text:null, isCorrect:null}
      this.thirdAnswer = thirdAnswer ? firstAnswer : {text:null, isCorrect:null}
      this.fourthAnswer = fourthAnswer ? firstAnswer : {text:null, isCorrect:null}
    }

  },
  emits: ["update:question"],
  methods: {
    submit() {
      let possibleAnswersArray = Array()
      if (this.firstAnswer.text) {
        possibleAnswersArray.push({
          text : this.firstAnswer.text,
          isCorrect : this.firstAnswer.isCorrect
        })
      }
      if (this.secondAnswer.text) {
        possibleAnswersArray.push({
          text : this.secondAnswer.text,
          isCorrect : this.secondAnswer.isCorrect
        })
      }
      if (this.thirdAnswer.text) {
        possibleAnswersArray.push({
          text : this.thirdAnswer.text,
          isCorrect : this.thirdAnswer.isCorrect
        })
      }
      if (this.fourthAnswer.text) {
        possibleAnswersArray.push({
          text : this.fourthAnswer.text,
          isCorrect : this.fourthAnswer.isCorrect
        })
      }

      this.$emit('update:question', {
        title : this.question.title,
        text : this.question.text,
        image : "blablabla",
        position : this.question.position,
        possibleAnswers : possibleAnswersArray
      })
    }
  }
};
</script>