<template>
    <div class = "news-container">
        <div v-html="content" class="news-content"></div>
        <a :href="link" target="_blank">Saber Mais</a>
    </div>
</template>

<script>

export default {
    props: {
        content: HTMLAllCollection,
        link: String 
    }
}
</script>

<style scoped lang="scss">
    .news-container {
        border: 2px solid green;
    }
    ::v-deep {
        div {
            display: flex;
            flex-direction: column;
            max-width: 500px;
            align-items: center;
            max-height: 500px;
            overflow: scroll;
            padding: 40px;

        }
        .arialGreen12Strong, .line16 {
            display: none;
        }

        td {
            a {
                display: none;
            }
        }

        img {
            display: none;
        }
    }
</style>