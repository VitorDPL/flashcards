<template>
    <main>
        <div class="container_principal">
            {{ materia }}
        </div>
    </main>
</template>

<script>
export default {
    name: 'BannerInicial',
    props: {
        materia : String
    }
}
</script>

<style scoped>

main{
    padding: 1rem;
}

.container_principal{
    background-color: var(--cor-banner);
    display: flex;
    border: 0.5rem solid var(--borda-banner);
    padding: 1rem;
    font-size: 2rem;
    width: 20rem;
    height: 10rem;
    text-align: center;
    color: black;
    border-radius: 1rem;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    transition: 0.5s ease;
    font-weight: 700;
}

.container_principal:hover {
    background-color: var(--cor-hover);
    color: black;
    width: 21rem;
    height: 11rem;
    border-left: 0.5rem solid rgb(0, 255, 17);
    border-top: 0.5rem solid  rgb(0, 255, 17);
}

</style>