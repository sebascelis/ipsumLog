<template> 
    <div class="logIn_user"> 
        <div class="container_logIn_user"> 
            <h2>Log In</h2> 
                <form v-on:submit.prevent="processLogInUser"> 
                    <input type="text" v-model="user.email" placeholder="Email"> 
                    <br> 
                    <input type="password" v-model="user.password" placeholder="Password"> 
                    <br> 
                    <button type="submit">Log In</button> 
                </form> 
        </div> 
    </div> 
</template> 

<script> 
import axios from 'axios'; 
 
export default { 
    name: "LogIn", 
 
    data: function(){ 
        return { 
            user: { 
                email:"",
                username: "", 
                password:""
            } 
        } 
    }, 
 
    methods: { 
        processLogInUser: function(){ 
            axios.post( 
                "http://localhost:8000/login/",  
                this.user,   
                {headers: {}} 
                ) 
                .then((result) => { 
                    let dataLogIn = { 
                        email: this.user.email, 
                        token_access: result.data.access, 
                        token_refresh: result.data.refresh, 
                    } 
                     
                    this.$emit('completedLogIn', dataLogIn) 
                }) 
                .catch((error) => { 
                     
                    if (error.response.status == "401") 
                        alert("ERROR 401: Credenciales Incorrectas."); 
                     
                }); 
        } 
    } 
} 
</script> 
<style> 
 
    .logIn_user{ 
        margin: 0; 
        padding: 0%; 
        height: 100%; 
        width: 100%; 
     
        display: flex; 
        justify-content: center; 
        align-items: center; 
    } 
 
    .container_logIn_user { 
        border: 3px solid  #283747; 
        border-radius: 10px; 
        width: 25%; 
        height: 60%; 
        margin: 20px;
        display: flex; 
        flex-direction: column; 
        justify-content: center; 
        align-items: center; 
    } 
 
    .logIn_user h2{ 
        color: #283747; 
        font-size: 40px;
 
    } 
    .logIn_user form{ 
        width: 70%; 
         
    } 
 
    .logIn_user input{ 
        height: 40px; 
        width: 100%; 
        border-radius: 10px;
        box-sizing: border-box; 
        padding: 10px 20px; 
        margin: 5px 0; 
  
    } 
 
    .logIn_user button{ 
        width: 100%; 
        height: 40px; 
 
        color: #E5E7E9; 
        background: #283747; 
        border: 1px solid #E5E7E9; 
 
        border-radius: 5px; 
        padding: 10px 25px; 
        margin: 5px 0; 
    } 
 
    .logIn_user button:hover{ 
        color: #E5E7E9; 
        background: rgb(6, 120, 52); 
        border: 1px solid #283747; 
        cursor: pointer;
    } 
 
</style> 