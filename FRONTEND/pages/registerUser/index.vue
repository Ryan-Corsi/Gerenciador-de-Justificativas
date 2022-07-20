<template>
  <div class="container">
    <div class="bar"></div>

    <div class="header">
      <div class="coluna_menor">
        <img src="../../static/logo.svg" />
      </div>

      <div class="coluna_maior">
        <p class="title_login">GERENCIADOR DE JUSTIFICATIVAS</p>
      </div>

      <div class="coluna_menor">
        <button class="btn_home" v-on:click="$router.push('/')">Logout</button>
      </div>
    </div>

    <div class="navbar">
      <button v-on:click="$router.push('/registerUser')">
        Cadastrar Usuários
      </button>
      <button v-on:click="$router.push('/visualizarOcorrencias')">
        Visualizar Justificativas
      </button>
    </div>

    <div class="conteudo-form">
      <div class="form_login">
        <form v-on:submit.prevent="verifyRegister()">
          <label class="label_form">Nome:</label>
          <input type="text" class="input_form" v-model="username" />

          <label class="label_form">EDV:</label>
          <input type="text" class="input_form" v-model="edv" />

          <label class="label_form">Área:</label>
          <!-- <input type="text" class="input_form" v-model="area"> -->
          <Dropdown
            class="drop_area"
            v-model="area"
            :options="planArray"
            optionLabel="nome"
            placeholder="Selecione..."
          />

          <div class="div_aling">
            <div class="div_check">
              <input type="checkbox" class="txt_adm" v-model="adm" />
              <label class="label_form">admin</label>
            </div>
          </div>
          <div class="div_aling">
            <button
              type="submit"
              class="btn_form"
              v-on:click="verifyRegister()"
            >
              Cadastrar
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "registerUser",
  data() {
    return {
      username: "",
      edv: "",
      password: "",
      adm: false,
      area: null,
      planArray: [],
    };
  },
methods:{
  
    verifyRegister: function () {
      if (this.username === "" || this.edv === "") {
        alert("Preencha todos os campos!");
      } else if (this.area === "") {
        alert("Selecione todos os campos!");
      } else if (this.edv.length != 8) {
        alert("EDV Inválido!");
      } else {
        this.registerUserDjango();
      }
    },
    registerUserDjango: async function () {
      const body = {
        username: this.username,
        email: "ets@gmail.com",
        password: "tetstet",
      };
      this.$axios
        .post(this.$store.state.BASE_URL + "/api/version/users/", body)
        .then((response) => {
          alert("Usuário cadastrado com sucesso!");
          this.registerUser();
        })
        .catch((error) => {
          alert("Atenção, usuário não cadastrado!");
          console.log(error);
        });
    },
    registerUser: async function () {
      const body = [
        {
          nome: this.username,
          edv: this.edv,
          password: this.password,
          admin: this.adm,
          area: this.area.id,
        },
      ];
      console.log(this.body);
      this.$axios
        .post(this.$store.state.BASE_URL + "/usuarios/", body)
        .then((response) => {
          alert("Usuário Cadastrado com sucesso");
        })
        .catch((error) => {
          alert("Usuário Não cadastrado");
          console.log(error);
        });
    },
  },
  created() {
    this.$axios
      .get(this.$store.state.BASE_URL + "/areas")
      .then((response) => {
        this.planArray = response.data;
      })
      .catch((error) => {
        console.log("Vish, deu ruim!");
        console.log(error);
      });
  },
};
</script>

<style lang="scss" scoped>
@import "@/layouts/pageRegisterUser.scss";
</style>