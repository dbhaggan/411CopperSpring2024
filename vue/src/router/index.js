import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '../components/HomePage.vue'
import LoginPage from '../components/Login.vue'
import SignupComponent from '../components/SignUp.vue'
import SmartFeedback from '../components/SmartFeedback.vue'
import PracticePage from '../components/PracticePage.vue'
import GeneratorSettingsPage from '../components/generator-settings.vue'
import AppSettingsPage from '../components/app-settings.vue'

const routes = [
    {
        path: "/home", name: "home", component: HomePage
    },
    {
        path: "/login", name: "login", component: LoginPage
    },
    {
        path: "/signup", name: "signup", component: SignupComponent
    },
    {
        path: "/app-settings", name: "app-settings", component: AppSettingsPage
    },
    {
        path: "/practice", name: "practice", component: PracticePage
    },
    {
        path: "/generator-settings", name: "generator-settings", component: GeneratorSettingsPage
    },
    {
        path: "/feedback", name: "feedback", component: SmartFeedback
    }
]

const router = createRouter(
    {
        history: createWebHistory(process.env.BASE_URL),
        routes
    }
)

export default router 
