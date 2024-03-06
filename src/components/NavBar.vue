<template>
    <nav>
        <div class="container">
            <div class="icon">
                <router-link to="/"><img src="../assets/icon.png" alt="logo"></router-link>
            </div>
            <div>
                <router-link to="/">Página Inicial</router-link>
            </div>
        </div>
    </nav>
</template>

<script>
export default {
    name: 'NavBar'
}
</script>

<style scoped>

nav{
    display: flex;
    display: 100vw;
    position: relative;
}

div {
    display: flex;
    height: 3rem;
    align-items: center;
    background-color: var(--cor-secundaria);
    width: 100vw;
}

div a {
    text-decoration: none;
    margin: 0rem 1rem;
    font-weight: 700;
    color: white;
    position: absolute;
    left: 5rem;
}

div a:hover{
    margin-top: 1rem;
}

div img {
    height: 2.5rem;
}

.container{
    padding: 0.3rem;
}

.icon a{
    position: absolute;
    left: 0;
}

</style>