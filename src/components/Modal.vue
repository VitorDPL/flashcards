<template>
    <div class="background">
        <div class="container">
            <h1>Apagar Questão?</h1>
            <div class="botoes">
                <button @click="excluirPergunta">Sim</button>
                <button @click="cancelarExclusao">Não</button>
            </div>
        </div>
    </div>
</template>

<script>


export default {
    name: 'Modal',
    methods: {
        excluirPergunta() {
            console.log('O usuário deseja excluir a pergunta.');
            this.$emit('excluir-questao');
        },
        cancelarExclusao() {
            console.log('O usuário não deseja excluir a pergunta.')
            // componente filho executa uma função do componente pai.
            this.$emit('fechar-modal'); 
        },
    },
}
</script>

<style scoped>
.background {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    background-color: rgba(255, 26, 26, 0.344);
}

.container {
    display: flex;
    flex-direction: column;
    width: 80%;
    max-width: 600px;
    background-color: rgba(255, 45, 45, 0.9);
    border-radius: 1rem;
    justify-content: center;
    align-items: center;
    text-align: center;
    padding: 1rem;
}

.container h1 {
    display: flex;
}

.botoes {
    display: flex;
    justify-content: center;
    padding: 2rem;
}

.botoes button {
    max-width: 10rem;
    padding: 1rem;
    margin-right: 5%;
    margin-left: 5%;
    font-weight: 700;
    font-size: 2rem;
    cursor: pointer;
}
</style>
