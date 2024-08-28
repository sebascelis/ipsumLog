import { createRouter, createWebHistory } from "vue-router"; 
import App from './App.vue'; 
 
import LogIn from './components/LogIn.vue' 
import SignUp from "./components/SignUp.vue";
import Home from "./components/Home.vue"; 
import Account from "./components/Account.vue";
import form from "./components/form.vue";
import { compactDecrypt } from "jose";
import Form from "./components/form.vue";


const routes = [{ 
  path: '/', 
  name: 'root', 
  component: App 
  }, 
  { 
  path: '/user/logIn', 
  name: "logIn", 
  component: LogIn 
  }, 
  { 
    path: '/user/signUp', 
    name: "signUp", 
    component: SignUp
    },
    { 
      path: '/home', 
      name: "home", 
      component: Home
      },
      { 
        path: '/user/account', 
        name: "account", 
        component: Account
        },
      {
        path: '/user/form',
        name: "form",
        component: Form
      }
  ]; 

  const router = createRouter({ 
    history: createWebHistory(), 
    routes, 
  }); 

  export default router; 
