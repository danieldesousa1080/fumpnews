<template>
    <router-link to="noticias" @mouseenter.native="(event) => {console.log(event)}">Todas as noticias</router-link>
</template>

<script>

</script>

<style scoped lang="scss">
a {

    display: flex;
    justify-content: center;
    align-items: center;
    width: 18rem;
    height: 3rem;
    color: white;
    text-decoration: none;
    border-radius: 10px;
    background-color: #7369FF;
    padding: 5px;

    transition: 0.5s ease;

}

a:hover {
        background-color: #9790ff;
    }
</style>