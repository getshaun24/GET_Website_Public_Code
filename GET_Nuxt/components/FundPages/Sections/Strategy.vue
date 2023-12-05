<template>
    


<div class="strategy_container">

<div class="strategy_image_container">
<img :class="{ hide_it: is_video }" data-speed=".9" class="strategy_image" :src="image" />


<video v-if="current_find_page == 'impossible'" :class="{ hide_it: is_image }" data-lag=".5" class="strategy_video" autoplay muted playsinline loop controls>
                <source :src="video" type="video/mp4">
</video>

<video v-else :class="{ hide_it: is_image }" data-lag=".5" class="strategy_video" autoplay muted playsinline loop>
                <source :src="video" type="video/mp4">
</video>



</div>
<div class="text_container" data-lag=".1">
    <h4>{{ title }}</h4>
    <p class="para" v-html="text"></p>
    <div v-if="has_invest_button" class="invest_button">
    <br>
    <FundPagesCompsMagneticButtonSmall/>
    </div>
</div>

</div>

</template>


<script setup>



const props = defineProps(['video', 'image', 'is_image', 'is_video', 'title', 'text', 'container_margin_top', 'container_margin_bottom', 'image_margin_calc', 'image_margin_mobile_calc', 'text_margin_mobile', 'has_invest_button', 'current_find_page'])


</script>

<style scoped>

.hide_it{
    display:none;
}

.strategy_container{
    display:grid;
    grid-template-columns: repeat(2, 1fr);
    grid-template-rows: 1fr;
    grid-column-gap: 20px;
    grid-row-gap: 0px;
    width:90%;
    margin-left:5%;
    margin-top:v-bind(container_margin_top);
}

.strategy_image{
    width:100%;
    margin-left:-8%
}

.strategy_video{
    width:90%;
    margin-top:40%

}
.para{
    width:80%;
}

.invest_button{
    position:absolute
}

@media only screen and (min-width: 0px) and (max-width: 380px) {
    .strategy_container{
    display:grid;
    grid-template-columns: 1fr;
    grid-template-rows: repeat(2, 1fr); 
    grid-column-gap: 0px;
    grid-row-gap: 0px;
    width:80%;
    margin-left:10%;
    margin-top:-115%;
    margin-bottom:v-bind(container_margin_bottom);
}

.strategy_image{
    margin-left:0%;
    margin-top:calc(150% * v-bind(image_margin_mobile_calc));
}


.strategy_video{
    margin-top:0%;
    margin-bottom:-225%;
    z-index:-1;
    position: relative;
}
.para{
    width:100%;
    margin-bottom:v-bind(text_margin_mobile);
}

.text_container{
    margin-top:0%;
    mix-blend-mode: difference;
}

.invest_button{
    margin-top:210%
}

}


@media only screen and (min-width: 380px) and (max-width: 430px) {
    .strategy_container{
    display:grid;
    grid-template-columns: 1fr;
    grid-template-rows: repeat(2, 1fr); 
    grid-column-gap: 0px;
    grid-row-gap: 0px;
    width:80%;
    margin-left:10%;
    margin-top:-135%;
    margin-bottom:calc(v-bind(container_margin_bottom) * 1.35);
}

.strategy_image{
    margin-left:0%;
    margin-top:calc(180% * v-bind(image_margin_mobile_calc));
}


.strategy_video{
    margin-top:0%;
    margin-bottom:-215%;
    z-index:-1;
    position: relative;
}
.para{
    width:100%;
    margin-bottom:v-bind(text_margin_mobile);
}

.text_container{
    margin-top:0%;
    mix-blend-mode: difference;
}
.invest_button{
    margin-top:210%
}

}



@media only screen and (min-width: 430px) and (max-width: 576px) {

    .strategy_container{
    display:grid;
    grid-template-columns: 1fr;
    grid-template-rows: repeat(2, 1fr); 
    grid-column-gap: 0px;
    grid-row-gap: 0px;
    width:80%;
    margin-left:10%;
    margin-top:-80%;
    margin-bottom:v-bind(container_margin_bottom);
}

.strategy_image{
    margin-left:0%;
    margin-top:calc(110% * v-bind(image_margin_mobile_calc));
}


.strategy_video{
    margin-top:0%;
    margin-bottom:-150%;
    z-index:-1;
    position: relative;
}
.para{
    width:100%;
    margin-bottom:v-bind(text_margin_mobile);
}

.text_container{
    margin-top:0%;
}

.invest_button{
    margin-top:210%
}

}

@media only screen and (min-width: 576px) and (max-width: 768px) {

    .strategy_container{
    display:grid;
    grid-template-columns: 1fr;
    grid-template-rows: repeat(2, 1fr); 
    grid-column-gap: 0px;
    grid-row-gap: 0px;
    width:80%;
    margin-left:10%;
}

.strategy_image{
    margin-left:0%;
    margin-top:calc(1% * v-bind(image_margin_mobile_calc));
}

.para{
    width:100%;
}

.text_container{
    margin-top:-15%
}

}

@media only screen and (min-width: 768px) and (max-width: 992px) {

    .strategy_container{
    display:grid;
    grid-template-columns: 1fr;
    grid-template-rows: repeat(2, 1fr); 
    grid-column-gap: 0px;
    grid-row-gap: 0px;
    width:80%;
    margin-left:10%;
}

.strategy_image{
    margin-left:0%;
    margin-top:calc(1% * v-bind(image_margin_mobile_calc));
}

.para{
    width:100%;
}

.text_container{
    margin-top:-5%
}

}

@media only screen and (min-width: 992px) and (max-width: 1200px) {
    .strategy_image{
    margin-top:calc(1% * v-bind(image_margin_calc));
}
}

@media only screen and (min-width: 1200px) and (max-width: 1400px) {
    .strategy_image{
    margin-top:calc(1% * v-bind(image_margin_calc));
}
}

@media only screen and (min-width: 1400px) and (max-width: 1600px) {
}

@media only screen and (min-width: 1600px) and (max-width: 5600px) {
}





</style>