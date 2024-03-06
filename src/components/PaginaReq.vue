<template>
    <div class="container-principal">
        <!-- fechar-modal é um EMIT enviado do componente filho. -->
        <div v-show="show_modal" class="modal-container"><Modal @fechar-modal="fechar_modal" @excluir-questao="excluir_questao_function"/></div>
        <div class="excluir_questao" v-if="questoes.length > 0">
            <button @click="apagarQuestao1">
                Apagar Questão
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-trash" viewBox="0 0 16 16">
                    <path d="M5.5 5.5A.5.5 0 0 1 6 6v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5m2.5 0a.5.5 0 0 1 .5.5v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5m3 .5a.5.5 0 0 0-1 0v6a.5.5 0 0 0 1 0z"/>
                    <path d="M14.5 3a1 1 0 0 1-1 1H13v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V4h-.5a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1H6a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1h3.5a1 1 0 0 1 1 1zM4.118 4 4 4.059V13a1 1 0 0 0 1 1h6a1 1 0 0 0 1-1V4.059L11.882 4zM2.5 3h11V2h-11z"/>
                  </svg>
            </button>
        </div>
        <div v-if="questoes.length > 0 && questaoAtual < questoes.length">
            <p class="sub">Questão {{ questaoAtual+1 }}:</p>
            <div class="pergunta">
                <p>Pergunta: </p>
                <!-- .questao pq o backend faz um loop 'for questao in questoes' -->
                <p class="questao">{{ questoes[questaoAtual].questao }}</p>
            </div>
            
            <button @click="exibirResposta" class="exibirResposta" v-show="exibirRespostaButton">Exibir Resposta</button>

            <p v-show="mostrarResposta" class="texto-resposta">Resposta: </p>
            <p v-if="mostrarResposta" class="resposta">{{ questoes[questaoAtual].resposta }}</p>

            <div class="check"> 
                <label for="errou">Não soube responder</label>
                <input type="checkbox" id="errou" v-model="nao_soube_responder">
            </div>

            <button @click="proximaQuestao" class="botao-proximo">Próxima Questão</button>
        </div>
        <div v-else>
            <p>Todas as questões já foram exibidas.</p>
            <router-link to="/" class="back-to-home"> Voltar para a página principal </router-link>
        </div>
    </div>

</template>

<script>
import axios from 'axios';
import Modal from '@/components/Modal.vue';

export default {
    name: 'FPReq',
    data() {
        return {
            questoes: [],
            questaoAtual: 0,
            mostrarResposta: false, 
            nao_soube_responder : false,
            show_modal : false,
            exibirRespostaButton : true,
        };
    },
    components:{
        Modal
    },
    mounted() {
        // requisição ao backend para obter as questões
        this.fetchQuestoes();
    },
    props:{
        link_req : String,
        link_delete : String,
    },
    methods: {
        async fetchQuestoes() {
            try {
                const response = await axios.get(this.link_req);
                this.questoes = response.data;
                console.log(response.data);
            } catch (error) {
                console.error('Erro ao obter questões:', error);
            }
        },
        proximaQuestao() {
            console.log(this.questoes.length)
            if (this.questaoAtual < this.questoes.length) {
                this.questaoAtual++;
                this.mostrarResposta = false; 
            } else {
                console.log('Todas as questões foram exibidas.');
            }
            if (this.nao_soube_responder === true) {
                console.log('Não soube responder acionado.')
                try {
                    this.enviarAoBancoDeErros();
                }catch(error){
                    console.error('Erro ao enviar a questão ao banco de erros.', error);
                }
            }

            this.nao_soube_responder = false

        },

        async enviarAoBancoDeErros() {
            try{
                const response = await axios.post('http://127.0.0.1:5000/questoes_erradas', {
                    // esse -1 aí embaixo é pq ele tava enviando A PRÓXIMA questão, não a atual.
                    pergunta : this.questoes[this.questaoAtual-1]['questao'],
                    resposta : this.questoes[this.questaoAtual-1]['resposta'],
                })
                }catch(error){
                    console.error('Erro ao enviar a questão ao banco de erros.', error)
            }
        },

                
        apagarQuestao1() {
            this.show_modal = true;
            this.exibirRespostaButton = true;
        },

        exibirResposta() {
            this.mostrarResposta = true; 
        },

        fechar_modal(){
            console.log('Fechando o modal');
            this.show_modal = false
        },
        async excluir_questao_function(){
            // aqui, o '-1', após o this.questaoAtual não é necessário.
            console.log(this.questoes[this.questaoAtual]['id']);
            // if (this.questoes.length > 1)
            try{
                const response = await axios.post(this.link_delete, {
                    id : this.questoes[this.questaoAtual]['id']
                });
                this.show_modal = false
                this.proximaQuestao();
            }catch(error){
                console.error('Erro ao deletar a questão: ', error)
            }
        }
        // teste() {
        //     console.log(this.questoes[this.questaoAtual]['questao'])
        //     console.log(this.questoes[this.questaoAtual]['resposta'])
        //     this.nao_soube_responder = !this.nao_soube_responder
        //     console.log(this.nao_soube_responder)
        // }
    },
};
</script>

<style scoped>



.container-principal{
    display: flex;
    flex-wrap: wrap;
    padding: 1rem;
    justify-content: center;
    align-items: center;
    border: 0.2rem solid white;
    border-radius: 1rem;
    min-width: 50rem;
    height: 50rem;
    position: relative;
    background-color: var(--cor-secundaria);
}

.container-principal p {
    font-size: 2rem;
    font-weight: 700;
}

.container-principal button {
    padding: 1rem;
    border-radius: 1rem;
    cursor: pointer;
}

.botao-proximo{
    display: block;
    position: absolute;
    bottom: 5rem;
    right: 5rem;
    width: 15rem;
    font-size: 1.2rem;
    font-weight: 700;
    transition: 0.5s ease;
}

.botao-proximo:hover {
    background-color: var(--cor-hover);
    color: black;
    width: 16rem;
    border-left: 0.5rem solid rgb(0, 255, 17);
    border-top: 0.5rem solid  rgb(0, 255, 17);
}

.sub{
    border-bottom: 0.2rem solid white;
    position: absolute;
    top: 30px;
    right: 42%;

    justify-content: center;
}
.questao {
    padding: 1rem;
}

.exibirResposta{
    background-color: rgb(211, 255, 146);
    margin: 1rem 0rem;
}

.resposta{
    padding: 1rem;
}

.back-to-home{
    display: flex;
    color: white;
    text-align: center;
    justify-content: center;
    padding: 5rem;
    font-size: 1.5rem;
    font-weight: 700;
}

.pergunta {
    border-bottom: 0.1rem solid white;
    margin-bottom: 1rem;
}

.check {
    display: flex;
    position: absolute;
    bottom: 6rem;
    left: 2rem;
    font-size: 1.2rem;
    color: red;
    font-weight: 700;
    text-align: center;
    align-items: center;
    justify-content: center;
}

.check input {
    margin: 1rem;
    height: 1.4rem;
    width: 1.4rem;
}


.pergunta{
    position: absolute;
    left: 1rem;
    top: 10rem;
}

.texto-resposta {
    position: absolute;
    left: 1rem;
}

.resposta {
    position: absolute;
    left: 1rem;
    margin-top: 1.7rem;
}

.exibirResposta{
    font-size: 1.2rem;
    font-weight: 700;
    border: 0.2rem solid black;
    transition: 0.5s ease-in;
    z-index: 1;
}

.exibirResposta:hover {
    background-color: white;
}

.excluir_questao {
    display: flex;
    position: absolute;
    top: 2rem;
    right: 1rem;
}

.excluir_questao button {
    padding: 0.8rem 1rem;
    transition: 0.5s ease;
}

.excluir_questao button:hover {
    background-color: rgb(255, 103, 103);
}

.modal-container{
    z-index: 10;
    
}

</style>