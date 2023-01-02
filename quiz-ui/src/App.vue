<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <header>

    <div class="wrapper">
      <nav class="navbar sticky-top bg-body-tertiary w-60">
        <div class="container-fluid">
          <RouterLink to="/">Home</RouterLink>
          <RouterLink to="/new-quiz-page">Démarrer le Quiz !</RouterLink>
          <RouterLink to="/administration">Administration</RouterLink>
          <RouterLink to="/about">About</RouterLink>
        </div>
      </nav>

    </div>
  </header>
  <div class="d-flex flex-column h-100 w-100 align-items-center">
  <RouterView />
  </div>
</template>