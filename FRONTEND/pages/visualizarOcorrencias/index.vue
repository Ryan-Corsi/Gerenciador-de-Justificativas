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

                <button v-on:click="$router.push('/registerUser')">Cadastrar Usuários</button>
                <button v-on:click="$router.push('/visualizarOcorrencias')">Visualizar Justificativas</button>

            </div>

            <div class="content-views">
            
            
            
            </div>
    
        </div>
        
    </template>

    <script>
    export default {
        name: 'visualizarOcorrencias'
    }
    </script>

    <style lang="scss" scoped>

    @import "@/layouts/pageRegisterOcorrencias.scss";

    </style>