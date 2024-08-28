<template> 
  <div id="app" class="app"> 
 
    <div class="header"> 
 
      <h1>Ipsum Technology</h1> 
      <nav> 
        <button v-if="is_auth" v-on:click="loadHome"> Home </button> 
        <button v-if="is_auth" v-on:click="loadAccount"> Questions </button> 
        <button v-if="is_auth"  v-on:click="logOut"> Log Out</button> 
        <button v-if="!is_auth" v-on:click="loadLogIn" > Log In </button> 
        <button v-if="!is_auth" v-on:click="loadSignUp" > Sign Up </button> 
      </nav> 
    </div> 
     
 
    <div class="main-component"> 
      <router-view   
        v-on:completedLogIn="completedLogIn" 
        v-on:completedSignUp="completedSignUp" 
        v-on:logOut="logOut" 
      > 
      </router-view> 
    </div> 
  </div> 
  <footer>  </footer>
</template> 

<script> 
export default { 
  name: 'App', 
 
  data: function(){ 
      return{ 
        is_auth: false 
      } 
  }, 
 
  components: { 
  }, 
 
  methods:{ 
    verifyAuth: function() { 
      this.is_auth = localStorage.getItem("isAuth") || false; 
      if (this.is_auth == false) 
        this.$router.push({ name: "logIn" }); 
      else 
        this.$router.push({ name: "home" });
    }, 
 
    loadLogIn: function(){ 
      this.$router.push({name: "logIn"}) 
    }, 
 
    loadSignUp: function(){ 
      this.$router.push({name: "signUp"}) 
    }, 
 
    completedLogIn: function(data) {
      localStorage.setItem("isAuth", true); 
      localStorage.setItem("email", data.email); 
      localStorage.setItem("username", data.username);
      localStorage.setItem("token_access", data.token_access); 
      localStorage.setItem("token_refresh", data.token_refresh); 
      alert("Autenticación Exitosa"); 
      this.verifyAuth(); 
    }, 
 
    completedSignUp: function(data) {
      alert("Registro Exitoso"); 
      this.completedLogIn(data); 
    },
    
    loadHome: function() { 
      this.$router.push({ name: "home" }); 
    }, 

    logOut: function () { 
      localStorage.clear(); 
      alert("Sesión Cerrada"); 
      this.verifyAuth(); 
    },

    loadAccount: function () { 
      this.$router.push({ name: "account" }); 
    }, 

    formUpdate: function(){
      alert("Save your changes")
      this.$router.push({ name: "home "});
    }
  }, 
 
  created: function(){ 
    this.verifyAuth() 
  } 
 
} 
</script> 

<style> 
 
  body{ 
    margin: 0 0 0 0;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  } 

  .header{ 
    margin: 0%; 
    padding: 0; 
    width: 100%; 
    height: 10vh;  
    min-height: 100px; 
 
    background-color: #283747 ; 
    color:#E5E7E9  ; 
 
    display: flex; 
    justify-content: space-between; 
    align-items: center; 
  } 
 
  .header h1{ 
    width: 20%; 
    text-align: center; 
  } 
 
  .header nav { 
    height: 100%; 
    width: 20%; 
 
    display: flex; 
    justify-content: space-around; 
    align-items: center; 
 
    font-size: 20px; 
  } 
 
  .header nav button{ 
    color: #E5E7E9; 
    background: #283747; 
    border: 1px solid #E5E7E9; 
 
    border-radius: 5px; 
    padding: 10px 20px; 
  } 
 
  .header nav button:hover{ 
    color: #ffffff; 
    background: rgb(6, 120, 52); 
    border: 1px solid #E5E7E9;
    
    cursor: pointer; 
  } 
 
   
  .main-component{ 
    /*background-image: url('./assets/Group.jpg');
    background-image: linear-gradient(to top, #f2f2f2, #666666, #333);
    */
    background-position: top;
    background-color: #d1d1d1;
    
    height: 80vh; 
    margin: 0%; 
    padding: 0%; 
  } 

  footer{
    background-color: #283747;
    height: 80px;
    margin: -20px;
  }
 
</style>  