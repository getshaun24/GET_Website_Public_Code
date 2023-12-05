<template>
    


<div class="first_container">


<div class="left_info">

<p class="info_text" v-html="main_text"></p>

</div>

<div class="right_content">

    <video :class="{ hide_it: is_image }" data-lag=".5" data-speed=".7" class="intro_video" autoplay muted playsinline loop>
                <source :src="video" type="video/mp4">
            </video>

    <img :class="{ hide_it: is_video }" data-lag=".8" class="intro_image" data-speed=".7" :src="image" />


</div>


</div>


</template>


<script setup>




const props = defineProps(['video', 'image', 'is_image', 'is_video', 'main_text'])




</script>


<style scoped>

.hide_it{
    display:none;
}

.first_container{
    width:100%;
    display:grid;
    grid-template-columns: repeat(2, 1fr);
    grid-template-rows: 1fr;
    grid-column-gap: 0px;
    grid-row-gap: 0px;
    margin-top:-50px;
    margin-bottom:15%
}

.intro_video{
    width:50%;
    margin-top:50%;
    margin-left:15%;
    background-color: #000;
    border-radius:20%;
    filter:contrast(1.1);
}

.intro_image{
    width:70%;
    margin-top:35%;
    margin-left:15%;
}


.info_text{
    margin-left:10%;
    margin-top:5%;
    width:80%;
    line-height: 1.5;
    color: #fff;
    display: block;
}











@media only screen and (min-width: 0px) and (max-width: 576px) {

    .right_content{
        display:none;
    }

    .first_container{
    width:100%;
    display:grid;
    grid-template-columns: 1fr;
    grid-template-rows: repeat(1, 1fr); 
    grid-column-gap: 0px;
    grid-row-gap: 0px;
    margin-top:20px;
    margin-bottom:0%
}

.info_text{
    margin-bottom:60%;
}

}

@media only screen and (min-width: 576px) and (max-width: 768px) {

    .right_content{
        display:none;
    }

    .first_container{
    width:100%;
    display:grid;
    grid-template-columns: 1fr;
    grid-template-rows: repeat(1, 1fr); 
    grid-column-gap: 0px;
    grid-row-gap: 0px;
    margin-top:20px;
    margin-bottom:0%
}

}






</style>