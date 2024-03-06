<template>
    <body>
        <div class="titulo">
            <h1>Engenharia de Software</h1>
        </div>
        <div class="pagina"><PaginaReq :link_req="link_req" :link_delete="link_delete"/></div>
    </body>
</template>

<script>
import PaginaReq from '@/components/PaginaReq.vue';

export default {
    name: 'EngSoftRouter',
    components: {
    PaginaReq
    },
    data(){
        return{
            link_req : 'http://127.0.0.1:5000/questoes_engenharia_de_software',
            link_delete : 'http://127.0.0.1:5000/deletar_questao_engsoftw'
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