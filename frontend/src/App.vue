<template>
  <div id="app">
    <h1>F{{secondLetter}}mp News</h1>
    <NewsMarquee/>
  </div>
</template>

<script>
import NewsMarquee from './components/NewsMarquee.vue';

export default {
  methods: {},
  computed: {
      secondLetter() {
          return Math.random() < 0.05 ? "â" : "u";
      }
  },
  components: { NewsMarquee, Response }
};
</script>

<!-- Use preprocessors via the lang attribute! e.g. <style lang="scss"> -->
<style>

* {
  padding: 0px;
}
  
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  margin-top: 60px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

h1 {
    text-align: center;
    font-size: 8rem;
}

.how_to{
  padding: 40px;
  border-radius: 10px;
  width: 80%;
}

  
@media (min-width: 400px){
    
  .how_to {
    border: 2px #2c3e50 solid;
  }
}
  
  @media (max-width: 400px){
    h1 {
      margin: none;
      font-size: 5rem;
    }
    
    .how_to {
      width: 100%;
      align-self: flex-start;
      padding: 0px;
    }
  }
  
  @media (min-width: 900px){
    .how_to {
      max-width: 60%;
    }
  }
  

button {
  background: none;
  border: solid 1px;
  border-radius: 2em;
  font: inherit;
  padding: 0.75em 2em;
}
</style>