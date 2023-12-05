<template>
    

<div class="revenue_container">

<div class="revenue_text" data-lag=".1">
    <div class="revenue_text_container">
    <h4>{{ title }}</h4>
    <p class="para" v-html="text">
       
    </p>
    </div>
</div>

<img data-lag=".5" class="revenue_image" :src="image" />


</div>




<div class="revenue_container_mobile">

    <img data-lag=".5" class="revenue_image" :src="image" />

<div class="revenue_text" data-lag=".1">
    <div class="revenue_text_container">
    <h2 class="title_mobile">{{ title }}</h2>
    <p class="para" v-html="text">
       
    </p>
    </div>
</div>

</div>





</template>


<script setup>


const props = defineProps(['image', 'image_margin', 'title', 'text'])

</script>



<style scoped>



.revenue_container{
    display:grid;
    grid-template-columns: repeat(2, 1fr);
    grid-template-rows: 1fr;
    grid-column-gap: 20px;
    grid-row-gap: 0px;
    width:90%;
    margin-left:5%;
    margin-top:10%;
    margin-bottom:10%
}

.revenue_container_mobile{
    display:grid;
    grid-template-columns: 1fr;
    grid-template-rows: repeat(2, 1fr); 
    grid-column-gap: 20px;
    grid-row-gap: 0px;
    width:90%;
    margin-left:5%;
    margin-top:10%;
    margin-bottom:10%
}



.revenue_image{
    width:80%;
    margin-top:v-bind(image_margin);
    margin-left:-10%;
}

.revenue_text{
    margin-left:10%
}

.revenue_text_container{
    margin-top:30%
}

.para{
    width:80%
}



@media only screen and (min-width: 0px) and (max-width: 500px) {

    .title_mobile{
        font-size:310%;
    }
}

@media only screen and (min-width: 0px) and (max-width: 576px) {


.revenue_container{
    display:none;
}

.revenue_text_container{
    margin-top:0%
}

.revenue_image{
    width:90%;
    margin-left:5%;
}


.para{
    width:90%
}



}

@media only screen and (min-width: 576px) and (max-width: 768px) {


    .revenue_container{
    display:none;
}

.revenue_text_container{
    margin-top:0%
}

.revenue_image{
    width:90%;
    margin-left:5%;
}


.para{
    width:90%
}


}

@media only screen and (min-width: 768px) and (max-width: 992px) {
.revenue_container{
    display:none;
}

.revenue_text_container{
    margin-top:0%
}

.revenue_image{
    width:90%;
    margin-left:5%;
}


.para{
    width:90%
}


}

@media only screen and (min-width: 992px) and (max-width: 1200px) {
    .revenue_container_mobile{
        display:none;
    }
}

@media only screen and (min-width: 1200px) and (max-width: 1400px) {
    .revenue_container_mobile{
        display:none;
    }
}

@media only screen and (min-width: 1400px) and (max-width: 1600px) {
    .revenue_container_mobile{
        display:none;
    }
}

@media only screen and (min-width: 1600px) and (max-width: 5600px) {
    .revenue_container_mobile{
        display:none;
    }
}





</style>