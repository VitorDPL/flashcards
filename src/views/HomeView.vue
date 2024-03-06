<template>
  <main>

    <div class="cadastrar_questao">
      <CadastrarQuestaoButton/>
    </div>


    <div class="banco">
      <h1>Banco de Questões</h1>
    </div>

    <div class="container">

      <div class="fundamentos_de_programacao">
        <router-link to="fundamentos_de_programacao">
          <BannerInicial materia="Fundametos De Programação"/>
        </router-link>
      </div>

      <div class="fundamentos_de_bancos_de_dados">
        <router-link to="/fundamento_banco_de_dados">
          <BannerInicial materia="Fundamento Banco de Dados"/>
        </router-link>
      </div>

      <div class="engenharia_de_software">
        <router-link to="/engenharia_de_software">
          <BannerInicial materia="Engenharia de Software"/>
        </router-link>
      </div>

      <div class="redes">
        <router-link to="/redes">
          <BannerInicial materia="Redes"/>
        </router-link>
      </div>

      <div class="sistemas_operacionais">
        <router-link to="/sistemas_operacionais">
          <BannerInicial materia="Sistemas Operacionais"/>
        </router-link>
      </div>

    </div>
    <div>
      <div class="revisar_questoes">
        <h2>Revise as questões incorretas</h2>
        <p>Ao clicar no botão, você revisará todas as questões que errou durante os estudos.</p>
      </div>
      <revisarQuestoesButton/>
    </div>
  </main>
</template>

<script>
import BannerInicial from '@/components/BannerInicial.vue';
import CadastrarQuestaoButton from '@/components/CadastrarQuestaoButton.vue';
import revisarQuestoesButton from '@/components/revisarQuestoesButton.vue';

export default {
  name: 'HomeView',
  components: {
    BannerInicial,
    CadastrarQuestaoButton,
    revisarQuestoesButton
  },

}
</script>

<style scoped>

main {
  margin-top: 3rem;
  background-color: var(--cor-fundo);
  height: 15vh;
  align-items: center;
}

.banco{
  display: flex;
  background-color: var(--cor-fundo);
  width: 100vw;
  color: white;
  justify-content: center;
}

.revisar_questoes{
  display: flex;
  flex-direction: column;
  background-color: var(--cor-fundo);
  width: 100vw;
  color: white;
  justify-content: center;
  margin-top: 8rem;
  text-align: center;
}

.revisar_questoes h2{
  font-size: 2.5rem;
}

.revisar_questoes p {
  font-size: 1.2rem;
}

h1{
  display: inline-block;
  border-bottom: 0.2rem solid white;
}

.container {
  font-family: 'Roboto', sans-serif;
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  align-items: center;
}

.container a {
  text-decoration: none;
}

</style>