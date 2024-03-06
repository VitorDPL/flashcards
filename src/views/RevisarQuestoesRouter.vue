<template>
    <body>
        <div class="titulo">
            <h1>Banco de Questões Erradas</h1>
        </div>
        <div class="pagina"><PaginaReqQuestoesErradas :link_req="link_req"/></div>
    </body>
</template>

<script>
import PaginaReqQuestoesErradas from '@/components/PaginaReqQuestoesErradas.vue';

export default {
    name: 'RevisarQuestoesRouter',
    components: {
        PaginaReqQuestoesErradas
    },
    data(){
        return{
            link_req : 'http://127.0.0.1:5000/get_questoes_erradas'
        }
    }
}
</script>

<style scoped>

body{
    background-color: var(--cor-fundo);
    color: white;
    display: flex;
    flex-direction: column;
    align-items: center;
    flex-wrap: wrap;
}

.titulo{
    justify-content: center;
    padding: 2rem;
}

.pagina {
    display: flex;
    align-items: center;
    height: 100%;
}

</style>