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
            </div>
                <div v-if="current_news.content == null">
                </div>
                <div v-else class="news-viewer" v-html="current_news.content"></div>
                <a v-if="current_news.content !== null" :href="current_news.link" target="blank" class="link-flutuante">Abrir no site</a>
            </div>
    </div>
</template>

<script>
import axios from 'axios';
import moment from 'moment';

export default {
    data() {
      return {
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
        removerHrefCodigoHTML(codigoHTML) {
            const padrao = /href\s*=\s*"[^"]*"/g;
            const novoCodigoHTML = codigoHTML.replace(padrao, '');
            return novoCodigoHTML;
        },
        set_current_news(id){
            axios
            .get('http://localhost:5000/noticias/' + id)
            .then( response => {
                this.current_news = {
                    "id": response.data.id,
                    "content": this.removerHrefCodigoHTML(response.data.content),
                    "link": response.data.link
                }
                console.log(this.current_news.content)

            })
        },
    },
    mounted () {
      axios
      .get('http://localhost:5000/noticias?size=20')
      .then( response => {
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
        display: grid;
        grid-template-columns:.4fr .6fr;
        width: 90%;
        height: 80vh;
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

    .news-viewer {
        border: 2px solid #c9c9c9;
        margin: 20px;
        border-radius: 10px;
        height: 100%;
        overflow-y: scroll;
        padding-left: 20px;
        padding-right: 20px;
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
    }

    .link-flutuante {
        position: absolute;
        border: 2px green solid;
        background-color: lightgreen;
        width: 100px;
        padding: 10px;
        display: flex;
        justify-content: center;
        align-items: center;
        right: 140px;
        bottom: 80px;
    }
</style>