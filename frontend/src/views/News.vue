<template>
    <div class = "news-container">
        <div class="header">
            <router-link class="home-button" to="/"><ph-house :size="25" /></router-link>
            <div class="search"><ph-magnifying-glass :size="25" /><form @submit.prevent="handleSubmit"><input type="text" placeholder="buscar" v-model="query"></form></div>
            <div class="title">Todas as notícias</div>
        </div>
        <div class="main">
            <div class="news-list">
                <div class="news" v-for="(news) in all_news" @click="()=>set_current_news(news.id)" :class="current_news.id == news.id ? 'active-news': ''">
                        <strong> <ph-article :size="20" /> {{ news.title }}</strong>
                        <p>{{ format_date(news.date) }}</p>
                </div>
                <button @click="()=>get_next_page()" class="more-news">Mais notícias</button>
            </div>
                <div v-if="current_news.content == null">
                    
                </div>
                <div v-else class="news-viewer-container">
                    <a class="open-site" :href="current_news.link" target="blank" ><ph-arrow-square-out :size="26" /></a>
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
            "content": null,
            id: null
        },
        query: ''
      };
    },
    methods: {
        format_date(value){
         if (value) {
           return moment(String(value)).format('DD/MM/YYYY')
          }
        },
        set_current_news(id){
            if (this.current_news.id != id){
                axios
                .get('http://localhost:5000/noticias/' + id)
            .then( response => {
                    this.current_news = {
                        "id": response.data.id,
                        "content": response.data.content,
                        "link": response.data.link
                    }
                })
            }
        }
            
        ,
        get_next_page(){
            this.current_page++
            axios.get(`http://localhost:5000/noticias?page=${this.current_page}&?size=20`)
            .then(
                response => {
                    this.all_news = [...this.all_news, ...response.data]
                }
            )
        },
        handleSubmit() {
            axios
            .get(`http://localhost:5000/noticias/busca/${this.query}?size=20`)
            .then(response => {
                this.all_news = response.data
            })
        }
    },
    mounted () {
      axios
      .get('http://localhost:5000/noticias?page=1&size=20')
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
        list-style: none;
        text-decoration: none;
        svg {
            color: #fff;
        }
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

    .search {
        display: flex;
        flex-wrap: nowrap;
        background-color: #c9c9c9;
        align-items: center;
        height: 40px;
        margin: none;
        padding: 0px 5px 0px 5px;
        border-radius: 10px;

        input {
            height: 50%;
        }
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
        display: flex;
        flex-direction: column;
        height: 100%;
        max-height: 70vh;
        
        border: 2px solid #c9c9c9;
        overflow-y: scroll;
        margin: 20px;
        
    }
    
    .news-viewer {
        border-radius: 10px;
        padding: 40px;
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
        transition: .5s ease;

        strong {
            display: grid;
            grid-template-columns: .1fr .8fr .1fr;

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

    .active-news {
        background-color: lightgreen;
    }

    .open-site {
        display: flex;
        min-width: 40px;
        min-height: 40px;
        border-radius: 50%;
        margin: 10px 10px 0px 0px;
        align-items: center;
        justify-content: center;
        justify-self: center;
        background-color: black;
        position: fixed;
        svg {
            fill: white !important;
        }
        align-self: flex-end;
    }
</style>