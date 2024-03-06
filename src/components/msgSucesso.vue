<template>
    <div>
        <p>{{ message }}</p>
    </div>
</template>

<script>
export default {
    name:'msgSucesso',
    props:{
        message : String
    }
}
</script>

<style scoped>

div {
    display: flex;
    background-color: rgba(0, 255, 106, 0.745);
    height: 3rem;
    text-align: center;
    align-items: center;
    justify-content: center;
    font-size: 2rem;
    font-weight: 700;
    color: white;
}

</style>