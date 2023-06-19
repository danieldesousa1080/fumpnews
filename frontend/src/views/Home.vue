<template>
    <div id="app">
      <main>
        <h1>F{{secondLetter}}mp News</h1>
        <NewsMarquee :all_news="all_news"/>
        <RouteButton></RouteButton>
      </main>
      <footer>
        Made with {{ getEmogi }} by <a target="_blank" href="//github.com/danieldesousa1080">Daniel de Sousa</a>
      </footer>
    </div>
   
</template>
  
<script>
  import axios from "axios"
  
  import NewsMarquee from '@/components/NewsMarquee.vue';
  import RouteButton from '@/components/RouteButton.vue';

  export default {
    data() {
      return {
        all_news: null
      };
    },
    computed: {
        secondLetter() {
            return Math.random() < 0.01 ? "â" : "u";
        },
        getEmogi(){
          if (Math.random() < 0.8){
            return "❤️"
          } else {
            var emogis = ["🥵","🥹","😌","🤖","😅","😖","✍️","🕵🏽‍♂️","🥷🏽","🫰🏾","🖖🏾","☕","😵‍💫"]
            return emogis[Math.floor(Math.random()*emogis.length)];
          }
  
        }
    },
    components: { NewsMarquee, RouteButton },
  
    mounted () {
      axios
      .get('http://localhost:5000/noticias?size=5')
      .then( response => {
          console.log(response)
          this.all_news = response.data
      })

      const el = this.$refs.News

      console.log(el)
      }
  };
</script>
  
<!-- Use preprocessors via the lang attribute! e.g. <style lang="scss"> -->
<style>
  
  * {
    padding: 0px;
    margin: 0px;
  }
  
  
  #app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    margin-top: 60px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: space-around;
    height: 100vh;
    padding: 0px;
    margin: 0px;
  }
  
  main {
    padding-top: 10%;
    width: 100%;
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
  
  footer {
    font-size: 1.2rem;
    text-decoration: none;
  }
  
  footer a {
    text-decoration: none;
  }
  
</style>