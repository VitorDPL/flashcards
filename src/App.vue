<template>

  <NavBar/>

  <!-- <nav>
    <router-link to="/">Home</router-link> |
    <router-link to="/about">About</router-link>
  </nav> -->
  <router-view/>


</template>

<script>
import NavBar from './components/NavBar.vue';
import HomeView from './views/HomeView.vue';


export default {
  name: 'App',
  components: {
    NavBar,
    HomeView,
  }
}
</script>


<style>


html {
  background-color: var(--cor-fundo);
  position: relative;
  height: 00%;
}

*{
  margin: 0px;
  padding: 0px;
}

:root{
  --cor-fundo : #282c34;
  --cor-banner : #ffffff;
  --borda-banner : #7b838a;
  --cor-texto : #ffff;
  --cor-nav-footer : #1e2327;
  --cor-secundaria : #3f4a62;
  --cor-hover : #d4e2ff;
}

</style>
