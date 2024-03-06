<template>
    <header>
        <msgSucesso :message="mensagem" v-show="mostrarMsgSucesso"/>
    </header>
    <form @submit="enviarQuestao">
        <div class="container">
            <div class="inputs-container">
                <div class="inputs-pergunta">
                    <label for="pergunta"> Pergunta: </label>
                    <input type="text" id="pergunta" v-model="pergunta" required>
                </div>
                <div class="inputs-respostas">
                    <label for="resposta"> Resposta: </label>
                    <input type="text" id="resposta" v-model="resposta" required>
                </div>
                <div class="materia">
                    <label for="materia">Matéria</label>
                    <select name="materia" id="materia" v-model="materia" required>
                        <option value="FundamentosDeProgramacao">Fundamentos de Programação</option>
                        <option value="FundamentosDeBancoDeDados">Fundamentos de Banco de Dados</option>
                        <option value="EngenhariaDeSoftware">Engenharia de Software</option>
                        <option value="Redes">Redes</option>
                        <option value="SistemasOperacionais">Sistemas Operacionais</option>
                    </select>
                </div>
                <div class="botao">
                    <button type="submit">Enviar</button>
                </div>
            </div>
        </div>
    </form>
</template>

<script>
import axios from 'axios';
import msgSucesso from '@/components/msgSucesso.vue';

export default {
    name: 'CadastroDeQuestoes',
    components: {
        msgSucesso
    },
    data() {
        return {
            pergunta: '',
            resposta: '',
            materia: null,
            mensagem : 'Questão cadastrada com sucesso  !',
            mostrarMsgSucesso : false
        };
    },
    methods: {
        async enviarQuestao(e) {
            e.preventDefault();

            if (!this.materia) {
                console.error('Não foi possível enviar os dados. Erro: a matéria não foi selecionada.');
                // this.materia === 'FundamentosDeProgramacao' é o value definido la no html.
            } else if (this.materia === 'FundamentosDeProgramacao') {
                console.log('Fundamentos de Programação Escolhido!');
                try {
                    const response = await axios.post('http://127.0.0.1:5000/fundamentos_de_programacao', {
                        pergunta: this.pergunta,
                        resposta: this.resposta,
                        materia: this.materia,
                    });

                    this.mostrarMsgSucesso = true;

                    setTimeout(() => {
                        this.mostrarMsgSucesso = false;
                    }, 3000);

                    this.pergunta = '';
                    this.resposta = '';

                    console.log(this.mensagem)
                    console.log('Resposta do servidor:', response.data);
                } catch (error) {
                    console.error('Erro ao enviar os dados:', error);
                }
            } else if (this.materia === 'FundamentosDeBancoDeDados') {
                console.log('Fundamentos de Banco de Dados Escolhido!');
                try {
                    const response = await axios.post('http://127.0.0.1:5000/fundamentos_de_banco_de_dados', {
                        pergunta: this.pergunta,
                        resposta: this.resposta,
                        materia: this.materia,
                    });

                    this.mostrarMsgSucesso = true;

                    setTimeout(() => {
                        this.mostrarMsgSucesso = false;
                    }, 3000);

                    this.pergunta = '';
                    this.resposta = '';

                    console.log('Resposta do servidor:', response.data);
                } catch (error) {
                    console.error('Erro ao enviar os dados:', error);
                }
            } else if (this.materia === 'EngenhariaDeSoftware'){
                try {
                    const response = await axios.post('http://127.0.0.1:5000/engenharia_de_software', {
                        pergunta: this.pergunta,
                        resposta: this.resposta,
                        materia: this.materia,
                    });

                    this.mostrarMsgSucesso = true;

                    setTimeout(() => {
                        this.mostrarMsgSucesso = false;
                    }, 3000);

                    this.pergunta = '';
                    this.resposta = '';

                    console.log('Engenharia de Software.')
                    console.log('Resposta do servidor:', response.data);
                } catch (error) {
                    console.error('Erro ao enviar os dados:', error);
                }
            } else if (this.materia === 'Redes') {
                console.log('Redes escolhida !');fd
                try {
                    const response = await axios.post('http://127.0.0.1:5000/redes', {
                        pergunta: this.pergunta,
                        resposta: this.resposta,
                        materia: this.materia,
                    });

                    this.mostrarMsgSucesso = true;

                    setTimeout(() => {
                        this.mostrarMsgSucesso = false;
                    }, 3000);

                    this.pergunta = '';
                    this.resposta = '';

                    console.log('Engenharia de Software.')
                    console.log('Resposta do servidor:', response.data);
                } catch (error) {
                    console.error('Erro ao enviar os dados:', error);
                }
            } else if (this.materia === 'SistemasOperacionais')
                console.log('Sistemas Operacionais escolhida !');               
                try {
                    const response = await axios.post('http://127.0.0.1:5000/sistemas_operacionais', {
                        pergunta: this.pergunta,
                        resposta: this.resposta,
                        materia: this.materia,
                    });

                    this.mostrarMsgSucesso = true;

                    setTimeout(() => {
                        this.mostrarMsgSucesso = false;
                    }, 3000);

                    this.pergunta = '';
                    this.resposta = '';

                    console.log('Resposta do servidor:', response.data);
                } catch (error) {
                    console.error('Erro ao enviar os dados:', error);
                }
        },
    },
};
</script>

<style scoped>


div {
    color: var(--cor-texto);
}

.inputs-container{
    width: 100vw;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    height: 93.8vh;
}

.inputs-pergunta input, .inputs-respostas input {
    width: 85vw;
    padding: 1rem;
    margin: 1rem;
    font-weight: 700;
    font-size: 1.8rem;
    border-radius: 1rem;
}


.inputs-pergunta label, .inputs-respostas label {
    font-weight: 700;
    padding: 1rem;
    text-align: center;
    align-items: center;
    font-size: 1.8rem;
}

.materia{
    display: flex;
    justify-content: center;
    text-align: center;
    align-items: center;
}

.materia label {
    font-weight: 700;
    margin-right: 1rem;
    margin-top: 2rem;
    margin-bottom: 2rem;
}

.materia select {
    width: 100%;
    padding: 0.5rem;
    margin-bottom: 2rem;
    margin-top: 2rem;
    border-radius: 1rem;
    cursor: pointer;
    padding: 0.8rem;
    font-size: 1rem;
}

.materia select option {
    text-align: center;
}

.botao button {
    width: 50vw;
    margin-top: 1rem;
    font-size: 1.2rem;
    padding: 0.5rem;
    border-radius: 1rem;
    cursor: pointer;
    transition: 0.5s ease;
}

.botao button:hover {
    background-color: rgb(193, 255, 122);
}

</style>
