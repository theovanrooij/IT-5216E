import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '../views/HomePage.vue'
import QuestionDisplay from '../views/QuestionDisplay.vue'
import QuestionsManager from '../views/QuestionsManager.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'HomePage',
      component: HomePage
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue')
    },
    {
      path: '/new-quiz-page',
      name: 'new-quiz-page',
      component: () => import('../views/NewQuizPage.vue')
    },
    {
      path: '/questions-manager',
      name: 'questions-manager',
      component: QuestionsManager
    },
    {
      path: '/question-display',
      name: 'question-display',
      component: QuestionDisplay
    },
  ]
})

export default router
