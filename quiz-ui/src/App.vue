<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>



<template>

  <header>
    <div class="wrapper">
      <h2>
        <nav class="navbar sticky-top bg-body-tertiary w-60">
        <RouterLink to="/">
          <svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="currentColor" class="bi bi-house" viewBox="0 0 16 16">
            <path d="M8.707 1.5a1 1 0 0 0-1.414 0L.646 8.146a.5.5 0 0 0 .708.708L2 8.207V13.5A1.5 1.5 0 0 0 3.5 15h9a1.5 1.5 0 0 0 1.5-1.5V8.207l.646.647a.5.5 0 0 0 .708-.708L13 5.793V2.5a.5.5 0 0 0-.5-.5h-1a.5.5 0 0 0-.5.5v1.293L8.707 1.5ZM13 7.207V13.5a.5.5 0 0 1-.5.5h-9a.5.5 0 0 1-.5-.5V7.207l5-5 5 5Z"/>
          </svg>
        </RouterLink>
        <RouterLink to="/new-quiz-page"> <img src="./assets/favicon.ico" style="width:40px;height:40px;margin-right:5px;">DRAPQUIZ</RouterLink>


          <RouterLink to="/administration" style="right:'0'">Admin</RouterLink>
          <!-- <RouterLink to="/about">About</RouterLink> -->
        </nav>
        </h2>
        <hr>
    </div>
  </header>
  <div class="d-flex flex-column h-100 w-100 align-items-center">
  <RouterView />
  </div>
</template>

<style>
  #app{
    color:black;
  }


  caption{
    font-size: 25px;
    margin:10px;
  }

  .router-link-exact-active{
    color:black;
  }

  header{
    padding: 20px;
  }
</style>