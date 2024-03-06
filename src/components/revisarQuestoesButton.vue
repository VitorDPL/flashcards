<template>
    <main>
        <button>
            <router-link to="/questoes_erradas">
                <h1>Revisar Questões</h1>
            </router-link>
        </button>
    </main>
</template>

<script>
export default {
    name: 'revisarQuestoesBurron'
}
</script>

<style scoped>

main {
    justify-content: center;
    display: flex;
    background-color: var(--cor-fundo);
    color: white;
}

main button {
    height: 4rem;
    width: 80vw;
    cursor: pointer;
    border-radius: 1rem;
    transition: 0.5s ease;
    border: 0.5rem solid var(--borda-banner);

}

main button a {
    text-decoration: none;
}

main button:hover {
    background-color: var(--cor-hover);
    height: 5rem;
    width: 82vw;
    color: black;
    border-left: 0.5rem solid red;
    border-top: 0.5rem solid red;
}

</style>