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

              <button class="btn_home" v-on:click="$auth.logout()">Logout</button>

            </div>
        
        </div>

        <div class="conteudo">

        <div class="form_login"> 

          <p class="title_form">Dados da Justificativa:</p>

            <form action="#">

              <label class="label_form">Nome:</label>
              <input type="text" class="input_form_ocorrencia"/> 

              <label class="label_form">EDV:</label>
              <input type="text" class="input_form_ocorrencia"/> 

              <label class="label_form">Data Inicial:</label>
              <input type="date" class="input_form_ocorrencia"/> 

              <label class="label_form">Data Final:</label>
              <input type="date" class="input_form_ocorrencia"/>

              <label class="label_form">Hora Inicial:</label>
              <input type="time" class="input_form_ocorrencia"/> 

              <label class="label_form">Hora Final:</label>
              <input type="time" class="input_form_ocorrencia"/>

              <label class="label_form">Arquivo (caso seja necessário):</label>
              <input type="file" class="input_form_ocorrencia"/>  

              <label class="label_form">Descrição da justificativa:</label>
              <textarea class="input-form-descript" cols="30" rows="5"></textarea>

              <div class="aling_center">

                <button class="btn_form">Registrar</button>

              </div>

            </form>

        </div>
      
      </div>
        
    </div>
    
</template>

<script>
export default {
    name: 'Ocorrência',

    middleware: "auth"
}
</script>

<style lang="scss" scoped>

  @import "@/layouts/pageRegisterOcorrencias.scss";

</style>