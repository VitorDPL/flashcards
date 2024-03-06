<template>
    <div class="container-principal">
        <div v-if="questoes.length > 0 && questaoAtual < questoes.length">
            <p class="sub">Questão {{ questaoAtual+1 }}:</p>
            <div class="pergunta">
                <p>Pergunta: </p>
                <!-- .questao pq o backend faz um loop 'for questao in questoes' -->
                <p class="questao">{{ questoes[questaoAtual].questao }}</p>
            </div>
            
            <button @click="exibirResposta" class="exibirResposta">Exibir Resposta</button>

            <p v-show="mostrarResposta" class="texto-resposta">Resposta: </p>
            <p v-if="mostrarResposta" class="resposta">{{ questoes[questaoAtual].resposta }}</p>

            <div class="check" @click="teste"> 
                <label for="errou">Resposta Correta !</label>
                <input type="checkbox" id="errou" v-model="soube_responder">
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

export default {
    name: 'FPReq',
    data() {
        return {
            questoes: [],
            questaoAtual: 0,
            mostrarResposta: false, 
            soube_responder : false,
        };
    },
    mounted() {
        // requisição ao backend para obter as questões
        this.fetchQuestoes();
    },
    props:{
        link_req : String,
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
            if (this.questaoAtual < this.questoes.length) {
                this.questaoAtual++;
                this.mostrarResposta = false; 
            } else {
                console.log('Todas as questões foram exibidas.');
            }

            if (this.soube_responder) {
                console.log('Usuário soube responder a questao.')
                try {
                    this.deletarDoBancoDeErros();
                } catch (error) {
                    console.error('Erro ao deletar a questão.', error);
                }
            }

            this.soube_responder = false;
        },


        async deletarDoBancoDeErros() {
            try {
                // tive que acrescentar essa linha. Estava dando erro pois quando sobrava UMA questão, ela n estava sendo apagada. A intenção era criar um 'else' pra quando só houvesse uma questao e a checkbox 'soube_responder' fosse marcada, ele deletar tudo o que tinha no banco de dados (sem precisar do id, pq só teria ELA), mas nao precisou. Essa linha resolveu.
                if (this.questoes.length > 1)
                console.log(this.questoes[this.questaoAtual - 1]['id'])
                const response = await axios.post('http://127.0.0.1:5000/deletar_questoes_erradas', {
                    id : this.questoes[this.questaoAtual-1]['id']
                });
                console.log('Questão deletada do banco de erros com sucesso.');
            } catch (error) {
                console.error('Erro ao deletar a questão do banco de erros.', error);
            }
},


        exibirResposta() {
            this.mostrarResposta = true; 
        },
        teste() {
            console.log(this.questoes[this.questaoAtual]['id']-1)
            // this.soube_responder = !this.soube_responder
            // console.log(this.soube_responder)
        }
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
    width: 50rem;
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
    color: rgb(0, 255, 0);
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
}

.exibirResposta:hover {
    background-color: white;
}

</style>