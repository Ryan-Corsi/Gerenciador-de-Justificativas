<template>
  
    <div class="container">

      <div class="bar"></div>

      <div class="header">

        <div class="coluna_menor">
          <img src="@/static/logo.svg" />
        </div>

        <div class="coluna_maior">
          <p class="title_login">GERENCIADOR DE JUSTIFICATIVAS</p>
        </div>

        <div class="coluna_menor">
          <button class="btn_home" v-on:click="$router.push('/')">Voltar</button>
        </div>

      </div>

      <div class="conteudo">

        <div class="form_login"> 

          <p class="title_form">Primeira senha</p>


              <label class="label_form">Insira o EDV:</label>
              <input type="text" class="input_form" v-model="user.username"/> 

              <div class="aling_center">

                <button class="btn_form" v-on:click="pesquisarSenha()">Verificar</button>

              </div>


            <div class="aling_center">

                <p class="first_pass">Esta é sua primeira senha: {{this.senha}}</p>

            </div>

        </div>
      
      </div>
    
    </div>

</template>

<script>
export default {
  name: 'novoLogin',

  data(){

    return{

      senha: 'Pesquise seu edv',
      usuarios: [],

      user:{
        username: ''
      }

    }


  },

  methods:{

    pesquisarSenha: function(){

      this.$axios.get("http://localhost:8000/usuarios").then((response) =>{ 

        this.usuarios = response.data;

        for(let i = 0; i < this.usuarios.length; i++){

          if(this.usuarios[i].edv == this.user.username){

            this.senha =  this.usuarios[i].senha;
            this.username = '';
            break


          }

        }

      })

    }


  }


}
</script>

<style lang="scss" scoped>

  @import "@/layouts/pagesWithForms.scss";

</style>