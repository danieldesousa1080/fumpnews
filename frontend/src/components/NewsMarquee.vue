<template>
    <div class="marquee">
        <ul>
            <div class="spacer"></div>
            <li v-for="(news) in all_news"><a :href="news.link">{{ news.title }}</a></li>
        </ul>
    </div>
        
</template>

<script>

export default {
    props: {
        all_news: Object
    }
}

</script>

<style scoped>

.marquee {
    max-width: 100vw;
    display: flex;
    width: 80%;
    white-space: nowrap;
    overflow: hidden;
    box-sizing: border-box;
}

@media (min-width: 800px) {
    .marquee {
        width: 50%;
    }
}

.marquee ul {
    display: flex;
    animation: marquee 30s linear infinite;
}
@keyframes marquee {
    0%   { transform: translate(0, 0); }
    100% { transform: translate(-100%, 0); }
}

.spacer {
    width: 50vw;
}


ul {
    display: flex;
    list-style: none;
}

li {
    padding-right: 46px;
}

a {
    color: red;
    text-decoration: lightcoral;
}

a:visited {
    color: red;
}

</style>