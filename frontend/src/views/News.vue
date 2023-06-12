<template>
    <div class = "news-container">
        <div class="header">
            <router-link class="home-button" to="/"><ph-house :size="25" /></router-link>
            <div class="title">Todas as notícias</div>
        </div>
        <div class="main">
            <div class="news-list">
                <div class="news" v-for="(news) in all_news">
                    <a :href="news.link" target="_blank">
                        <strong> <ph-article :size="20" /> {{ news.title }}</strong>
                        <p>{{ format_date(news.date) }}</p>
                    </a>
                </div>
            </div>
            
        </div>
    </div>
</template>

<script>
import axios from 'axios';
import moment from 'moment';

export default {
    data() {
      return {
        all_news: null
      };
    },
    methods: {
        format_date(value){
         if (value) {
           return moment(String(value)).format('DD/MM/YYYY')
          }
        }
    },
    props: {

    },
    mounted () {
      axios
      .get('http://localhost:5000/noticias?size=20')
      .then( response => {
        console.log(response)
          this.all_news = response.data
      })
      }
}
</script>

<style scoped lang="scss">
    a {
        color: black;
        text-decoration: none;
    }
    .news-container {
        display: flex;
        flex-direction: column;
        width: 100vw;
        height: 100vh;
        align-items: center;
    }

    .header {
        display: flex;
        margin-top: 20px;
        width: 100%;
        justify-content: space-around;
    }
    
    .home-button {
        width: 40px;
        height: 40px;
        border-radius: 100%;
        background-color: #D9D9D9;
        display: flex;
        justify-content: center;
        align-items: center;
        font-size: 1rem;
        padding: 0px;
        margin: 0px;
    }

    .title {
        width: 80vw;
        height: 40px;
        border-radius: 20px;
        background-color: #D9D9D9;
        display: flex;
        align-items: center;
        justify-content: center;
    }

    .main {
        padding-top: 60px;
        display: flex;
        width: 90%;
    }

    .news-list {
        display: flex;
        flex-direction: column;
        align-items: center;
        width: 100%;
    }

    .news {
        width: 90%;
        a {
            cursor: pointer;
            display: flex;
            justify-content: space-between;
            background-color: #D9D9D9;
            padding: 20px;
            margin: 10px;
            width: 100%;
            border-radius: 10px;
            color: #000;
            text-decoration: none;
         :visited, :focus {
            color: #000;
            text-decoration: none;
         }
        }

        strong {
            display: flex;
            align-items: center;

            svg {
                padding-right: 5px;
            }
        }

    }
</style>