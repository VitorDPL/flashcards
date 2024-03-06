<template>
    <body>
        <div class="titulo">
            <h1>Cadastro de questões</h1>
        </div>

        <div>
            <CadastroDeQuestoes/>
        </div>
    </body>
</template>

<script>
import CadastroDeQuestoes from '@/components/CadastroDeQuestoes.vue';

export default {
    name: 'CadastrarQuestoesRouter',
    components: {
        CadastroDeQuestoes,
    },
}
</script>

<style scoped>

body{
    width: 100vw;
    background-color: var(--cor-fundo);
}

.titulo {
    display: flex;
    padding: 1rem;
    justify-content: center;
    color: var(--cor-texto);
}

</style>