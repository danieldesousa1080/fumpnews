<template>
    <div class = "news-container">
        <div class="header">
            <router-link class="home-button" to="/"><ph-house :size="25" /></router-link>
            <div class="title">Todas as notícias</div>
        </div>
        <div class="main">
            <div class="news-list">
                <div class="news" v-for="(news) in all_news" @click="()=>set_current_news(news.id)">
                        <strong> <ph-article :size="20" /> {{ news.title }}</strong>
                        <p>{{ format_date(news.date) }}</p>
                </div>
                <button @click="()=>get_next_page()" class="more-news">Mais notícias</button>
            </div>
                <div v-if="current_news.content == null">
                </div>
                <div v-else class="news-viewer-container">
                    <div class="news-viewer" v-html="current_news.content"></div>
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
        current_page: 1,
        all_news: null,
        current_news: {
            "content": null
        }
      };
    },
    methods: {
        format_date(value){
         if (value) {
           return moment(String(value)).format('DD/MM/YYYY')
          }
        },
        set_current_news(id){
            axios
            .get('http://localhost:5001/noticias/' + id)
            .then( response => {
                this.current_news = {
                    "id": response.data.id,
                    "content": response.data.content,
                    "link": response.data.link
                }

            })
        },
        get_next_page(){
            this.current_page++
            axios.get(`http://localhost:5001/noticias?page=${this.current_page}&?size=20`)
            .then(
                response => {
                    this.all_news = [...this.all_news, ...response.data]
                }
            )
        }
    },
    mounted () {
      axios
      .get('http://localhost:5001/noticias?page=1&size=20')
      .then( response => {
          this.all_news = response.data
      })
      }
}
</script>

<style scoped lang="scss">
    @import url("../assets/reset.css");

    *{
        margin: 0px;
        padding: 0px;
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
        display: grid;
        grid-template-columns:.4fr .6fr;
        width: 90%;
        height: 80vh!important;
    }

    .news-list {
        display: flex;
        flex-direction: column;
        align-items: center;
        width: 100%;
        overflow-x: hidden;
        overflow-y: scroll;
        height: 100%;
        
    }

    .news-viewer-container {
        height: 100%;
        max-height: 70vh;
        padding: 40px;
        border: 2px solid #c9c9c9;
        overflow-y: scroll;
        margin: 20px;
        
    }
    
    .news-viewer {
        border-radius: 10px;
    }

    .news {
        width: 90%;
        cursor: pointer;
        display: flex;
        justify-content: space-between;
        background-color: #D9D9D9;
        padding: 20px;
        margin: 10px;
        width: 95%;
        border-radius: 10px;
        color: #000;
        text-decoration: none;

        strong {
            display: flex;
            align-items: center;

            svg {
                padding-right: 5px;
            }
        }
    }
    :deep {

        * {
            color: #000!important;
        }
        img {
            display: none;
        }
        .arialGreen12Strong {
            display: none;
        }
        .line16 {
            display: none;
        }

        a {
            color: red!important;
        }
    }

    .more-news {
        width: 150px;
        height: 100px!important;
        border-radius: 0px;
        border: none;
        padding: 5px;
        background-color:gray;
        color: white!important;
        cursor: pointer;
    }
</style>