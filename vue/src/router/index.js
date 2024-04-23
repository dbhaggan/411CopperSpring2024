import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '../components/HomePage.vue'
import LoginPage from '../components/Login.vue'
import SignupPage from '../components/SignUp.vue'
import SmartFeedback from '../components/SmartFeedback.vue'
import Vexflowcomponent from '../components/PracticePage.vue'
import GeneratorSettingsPage from '../components/generator-settings.vue'
import AppSettingsPage from '../components/app-settings.vue'
import InstrumentRequest from '../components/InstrumentRequest.vue'
import InstrumentPage from '../components/instrument-selection.vue'

const routes = [
    {
        path: "/", name: "/", component: HomePage
    },
    {
        path: "/home", name: "home", component: HomePage
    },
    {
        path: "/login", name: "login", component: LoginPage
    },
    {
        path: "/signup", name: "signup", component: SignupPage
    },
    {
        path: "/app-settings", name: "app-settings", component: AppSettingsPage
    },
    {
        path: "/practice", name: "practice", component: Vexflowcomponent
    },
    {
        path: "/generator-settings", name: "generator-settings", component: GeneratorSettingsPage
    },
    {
        path: "/feedback", name: "feedback", component: SmartFeedback
    },
    {
        path: "/instrument", name: "instrument", component: InstrumentPage
    },
    {
        path: "/request", name: "request", component: InstrumentRequest
    }
]

const router = createRouter(
    {
        history: createWebHistory(process.env.BASE_URL),
        routes
    }
)

export default router 
