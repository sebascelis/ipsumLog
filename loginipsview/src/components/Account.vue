<template> 
 
    <div v-if="loaded" class="information"> 
        <h1>Hi, <span>{{username}}!</span></h1> 
        <h2>Set up your security questions</h2>
        <div class="container_information"> 
        <form v-on:submit.prevent="sendForm">
            <div>
                <label for="nombre">Favorite Color</label>
                <input type="text" id="firstQuestion" v-model="firstQuestion" required disabled>
            </div>
            <div>
                <label for="edad">Favorite Food</label>
                <input type="text" id="secondQuestion" v-model="secondQuestion" required disabled>
            </div>
            <div>
                <label for="thirdQuestion">Favorite Artist</label>
                <input type="text" id="thirdQuestion" v-model="thirdQuestion" required disabled>
            </div>
            <div>
                <label for="fourImage">Profile image</label>
                <input type="file" id="image" @change="onFileChange" required disabled>
            </div>
            <button type="submit" v-if="!editActive" v-on:click="editData">Edit</button>
            <button type="submit" v-if="editActive" v-on:click="editCancel">Cancell</button>
            <button type="submit">Enviar</button>
        </form>
        </div>
    </div> 
    
</template> 
 
<script> 

import { decodeJwt } from 'jose';

import axios from 'axios'; 
 
export default { 
    name: "Account", 
 
    data: function(){ 
        return { 
            firstQuestion: "",
            secondQuestion: "",
            thirdQuestion: "",
            username : "",
            loaded: false,
            editActive: false,
            userId: "",
            image: ""
             
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
            axios.get(`http://localhost:8000/user/form/${this.userId}/`)
                .then((result) => { 
                    
                    this.firstQuestion = result.data.firstQuestion,
                    this.secondQuestion = result.data.secondQuestion,
                    this.thirdQuestion = result.data.thirdQuestion,
                    this.image = `..assets/${result.data.image}`
                
                })
        }, 
        editData: function(){
            document.getElementById("firstQuestion").disabled=false;
            document.getElementById("secondQuestion").disabled=false;
            document.getElementById("thirdQuestion").disabled=false;
            document.getElementById("image").disabled=false;
            this.editActive = true;
        },

        editCancel: function(){
            document.getElementById("firstQuestion").disabled=true;
            document.getElementById("secondQuestion").disabled=true;
            document.getElementById("thirdQuestion").disabled=true;
            document.getElementById("image").disabled=true;
            
            axios.get(`http://localhost:8000/user/form/${this.userId}/`)
            .then((result) => { 
                this.username = result.data.username,
                this.lastname = result.data.lastname,
                this.password = result.data.password }),
            document.getElementById("firstQuestion").value=this.username,
            document.getElementById("secondQuestion").value=this.lastname,
            document.getElementById("thirdQuestion").value=this.password,
            this.editActive = false
        },
        sendForm: function(){
            document.getElementById("firstQuestion").value;
            document.getElementById("secondQuestion").value;
            document.getElementById("thirdQuestion").value;
            document.getElementById("image").files[0].name;
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

        getImage(e){
        let image = e.target.files[0];
        let reader = new FileReader();
        reader.readAsDataURL(image);
        reader.onload = e => {
            this.avatar = e.target.result;
        }
        this.loaded = true; 
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
        font-size: 60px; 
        color: #0f1316; 
    } 
    .information h2{ 
        font-size: 40px; 
        color: #283747; 
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
        width: 70%; 
        text-align: center;
         
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