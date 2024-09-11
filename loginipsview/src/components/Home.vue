<template> 
 
    <div v-if="loaded" class="information"> 
        <h1>Set up your data</h1> 
        <h2>Hi, <span>{{username}}!</span></h2>
        <div class="container_information"> 
        <form v-on:submit.prevent="processSignUp">
            <div>
                <label for="nombre">Username</label>
                <input type="text" id="username" v-model="username" required disabled>
            </div>
            <div>
                <label for="edad">Lastname</label>
                <input type="text" id="lastname" v-model="lastname" required disabled>
            </div>
            <div>
                <label for="password">Password</label>
                <input type="password" id="password" v-model="password" required disabled>
            </div>
            <button type="submit" v-if="!editActive" v-on:click="editData">Edit</button>
            <button type="submit" v-if="editActive" v-on:click="editCancel">Cancell</button>
            <button type="submit" v-on:click="sendForm">Enviar</button>
        </form>
        </div>
    </div> 
    
</template> 
 
<script> 

import { decodeJwt } from 'jose';

import axios from 'axios'; 
 
export default { 
    name: "Home", 
 
    data: function(){ 
        return { 
            username: "",
            lastname: "",
            password: "",
            loaded: false,
            editActive: false,
            userId: "",
            image : ""
             
        } 
    }, 
 
    methods: { 
        getData: async function () { 
            if (localStorage.getItem("token_access") === null || localStorage.getItem("token_refresh") === null) { 
                this.$emit('logOut'); 
                return; 
            } 
 
            await this.verifyToken();
            let token = localStorage.getItem("token_access"); 
            let userId = decodeJwt(token).user_id.toString(); 
            this.userId = userId;
             
            axios.get(`http://localhost:8000/user/${this.userId}/`, {headers: {'Authorization': `Bearer ${token}`}}) 
                .then((result) => { 
                    this.username = result.data.username;  
                    this.loaded = true; 
                    }) 
                .catch(() => { 
                    this.$emit('logOut'); 
                }); 
            axios.get(`http://localhost:8000/user/${this.userId}/`)
                .then((result) => { 
                    
                    this.username = result.data.username,
                    this.lastname = result.data.lastname,
                    this.password = result.data.password

                })
        }, 
        
        editData: function(){
            document.getElementById("username").disabled=false;
            document.getElementById("lastname").disabled=false;
            document.getElementById("password").disabled=false;
            document.getElementById("image").disabled=false;
            this.editActive = true;
        },

        editCancel: function(){
            document.getElementById("username").disabled=true;
            document.getElementById("lastname").disabled=true;
            document.getElementById("password").disabled=true;
            document.getElementById("image").disabled=true;
            
            axios.get(`http://localhost:8000/user/form/${this.userId}/`)
            .then((result) => { 
                this.username = result.data.username,
                this.lastname = result.data.lastname,
                this.password = result.data.password }),
            document.getElementById("username").value=this.username,
            document.getElementById("lastname").value=this.lastname,
            document.getElementById("password").value=this.password,
            this.editActive = false
        },
        onFileChange(event) {
            const file = event.target.files[0];
            if (file) {
            this.fileName = `..src/assets/${file.name}`;
        }
      },
        sendForm: function(){
            this.username = document.getElementById("username").value;
            this.lastname = document.getElementById("lastname").value;
            this.password = document.getElementById("password").value;
            console.log(this.image)
            let formData = {
                user : this.userId,
                username: this.username,
                lastname : this.lastname,
                password : this.password,
                image : this.image
            }

            axios.put( 
                `http://127.0.0.1:8000/user/form/${this.userId}/update`, 
                formData
            ) 
                .then((response) => { 
                    let form = { 
                        user: this.userId,
                        username: response.data.username,
                        lastname: response.data.lastname,
                        password: response.data.password
                    } 
                     
                    this.$emit('formUpdate', form) 
                }) 
                .catch((error) => { 
     console.log(error) 
              alert("ERROR: Fallo la actualización del formulario."); 
 
                }); 

        },
 
        verifyToken: function () { 
            return axios.post("http://localhost:8000/refresh/", {refresh: localStorage.getItem("token_refresh")}, {headers: {}}
 ) 
                .then((result) => { 
                    localStorage.setItem("token_access", result.data.access);        
                }) 
                .catch(() => { 
                    this.$emit('logOut'); 
                }); 
        } 
    }, 
 
    created: async function(){ 
        this.getData(); 
    }, 
} 
</script> 
 
<style> 
    .information{ 
        margin: 0; 
        padding: 0%; 
        width: 100%; 
        height: 100%; 
 
        display: flex; 
        flex-direction: column; 
        justify-content: center;     
        align-items: center; 
    }
    .information h1{ 
        font-size: 50px; 
        color: #0f1316; 
    } 
    .information h2{ 
        font-size: 40px; 
        color: rgb(6, 120, 69); 
    } 
    .information span{ 
        color: crimson; 
        font-weight: bold; 
    } 
    .container_information { 
        border: 3px solid  #283747; 
        border-radius: 10px; 
        width: 25%; 
        display: flex; 
        flex-direction: column; 
        justify-content: center; 
        align-items: center; 
    } 
 
    .information h2{ 
        color: #283747;
        font-size: 40px; 
        text-align: center;
 
    } 
 
    .information form{ 
        width: 100%; 
        text-align: center;
        padding: 2%;
         
    } 
 
    .information input{ 
        height: 40px; 
        width: 100%; 
        text-align: center;
        box-sizing: border-box; 
        padding: 10px 20px; 
        margin: 5px 0; 
 
        border: 1px solid #283747; 
    } 
 
    .information button{ 
        width: 100%; 
        height: 40px; 
 
        color: #E5E7E9; 
        background: #283747; 
        border: 1px solid #E5E7E9; 
 
        border-radius: 5px; 
        padding: 10px 25px; 
        margin: 5px 0 25px 0; 
    } 
 
    .information button:hover{ 
        color: #E5E7E9; 
        background: rgb(6, 120, 52); 
        border: 1px solid #283747; 
        cursor: pointer;
    } 
    
</style>