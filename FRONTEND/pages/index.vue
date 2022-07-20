<template>
  
    <div class="container">

      <div class="bar"></div>

      <div class="header">

        <div class="coluna_menor">
          <img src="../static/logo.svg" />
        </div>

        <div class="coluna_maior">
          <p class="title_login">GERENCIADOR DE JUSTIFICATIVAS</p>
        </div>

        <div class="coluna_menor"></div>

      </div>

      <div class="conteudo">

        <div class="form_login"> 

          <p class="title_form">Login</p>

              <label class="label_form">EDV:</label>
              <input type="text" class="input_form" v-model="user.username"/> 

              <label class="label_form">Senha:</label>
              <input type="password" class="input_form" v-model="user.password"/> 

              <div class="aling_center">

                <button class="btn_form" v-on:click="makeLogin()">Logar</button>

              </div>

            <div class="aling_center">

                <button class="first_change" v-on:click="$router.push('/novoLogin')">Primeiro login? Clique aqui!</button>

            </div>
            
        </div>
      
      </div>
    
    </div>


</template>

<script>
export default {
  name: 'IndexPage',

  data(){

    return{

      usuarios: [],

      user:{
        username:'',
        password: ''
      }

    }

  },

  methods:{

      makeLogin: async function(){
      
      this.$auth.loginWith("local", {data: this.user} ).then((response)=>{
        
        this.$axios.get("http://localhost:8000/usuarios").then((response) =>{
          
          this.usuarios = response.data
          
          let verifyAcess = false;
          let verifyAdmin = false;
          
          for(let i = 0; i < this.usuarios.length; i++){

            if(this.usuarios[i].edv == this.user.username){

              if(this.usuarios[i].admin == true){

                verifyAdmin = true

              }

              if(this.usuarios[i].primeiroAcesso == true){

                verifyAcess = true;
                
              }  

               break   

            }

          }

          if(verifyAcess == true){

            window.location.replace("./novaSenha/")

          } else if(verifyAdmin == true) {

            window.location.replace("./administrador/")

          } else {

            window.location.replace("./ocorrencias/")

          }

        })
      
      }).catch((response)=>{

        console.log(response);
        this.user.username = "";
        this.user.password = "";
        
      }

      )

    }

  }

}

</script>

<style lang="scss" scoped>

  @import "@/layouts/pagesWithForms.scss";

</style>