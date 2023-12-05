<template>
    
<div>

    <img data-lag=".2" class="company_hightlights_image" :src="image" />


<h4 class="company_highlights_title">Company Highlights</h4>
<div class="company_highlights">

<p class="company_highlights_text" v-html="left_side_text">

</p>


<div class="company_highlights_inner">
<p class="company_highlights_text" v-html="right_side_text_1">

</p>
<p class="company_highlights_text" v-html="right_side_text_2">

</p>

</div>


</div>
</div>

</template>


<script setup>

const props = defineProps(['left_side_text', 'right_side_text_1', 'right_side_text_2', 'image'])

</script>

<style scoped>



.company_highlights{
    width:80%;
    margin-left:10%;
    margin-top:5%;
    display:grid;
    grid-template-columns: repeat(2, 1fr);
    grid-template-rows: 1fr;
    grid-column-gap: 100px;
    grid-row-gap: 0px;
}

.company_highlights_inner{
    display:grid;
    grid-template-columns: repeat(2, 1fr);
    grid-template-rows: 1fr;
    grid-column-gap: 50px;
    grid-row-gap: 0px;
}
.company_highlights_title{
    margin-left:10%;
    margin-top:10%
}



.company_hightlights_image{
    width:60%;
    margin-left:20%;
    margin-bottom:0%;
    margin-top:15%
}

.company_highlights_text{
    font-size:80%
}



@media only screen and (min-width: 0px) and (max-width: 376px) {

.company_highlights{
width:80%;
margin-left:10%;
margin-top:0%;
display:grid;
grid-template-columns: 1fr;
grid-template-rows: repeat(2, 1fr); 
grid-column-gap: 0px;
grid-row-gap: 50px;
}

.company_highlights_inner{
margin-top:-30%
}

.company_highlights_text{
    font-size:80%
}

.company_hightlights_image{
    margin-top:10%
}

.company_highlights_title{
    margin-top:10%
}
}


@media only screen and (min-width: 376px) and (max-width: 430px) {

.company_highlights{
width:80%;
margin-left:10%;
margin-top:0%;
display:grid;
grid-template-columns: 1fr;
grid-template-rows: repeat(2, 1fr); 
grid-column-gap: 0px;
grid-row-gap: 50px;
}

.company_highlights_inner{
margin-top:-18%
}

.company_highlights_text{
    font-size:80%
}

.company_hightlights_image{
    margin-top:10%
}

.company_highlights_title{
    margin-top:10%
}
}





@media only screen and (min-width: 430px) and (max-width: 500px) {

    .company_highlights{
    width:80%;
    margin-left:10%;
    margin-top:0%;
    display:grid;
    grid-template-columns: 1fr;
    grid-template-rows: repeat(2, 1fr); 
    grid-column-gap: 50px;
    grid-row-gap: 0px;
}

.company_highlights_inner{
    margin-top:-10%
}

.company_highlights_text{
    font-size:80%
}

.company_hightlights_image{
    margin-top:0%
}

.company_highlights_title{
    margin-top:0%
}

}


@media only screen and (min-width: 500px) and (max-width: 530px) {

.company_highlights{
width:80%;
margin-left:10%;
margin-top:0%;
display:grid;
grid-template-columns: 1fr;
grid-template-rows: repeat(2, 1fr); 
grid-column-gap: 50px;
grid-row-gap: 0px;
}

.company_highlights_inner{
margin-top:-10%
}

.company_highlights_text{
    font-size:90%
}

.company_hightlights_image{
    margin-top:0%;
}
.company_highlights_title{
    margin-top:0%
}

}


@media only screen and (min-width: 530px) and (max-width: 576px) {

.company_highlights{
width:80%;
margin-left:10%;
margin-top:0%;
display:grid;
grid-template-columns: 1fr;
grid-template-rows: repeat(2, 1fr); 
grid-column-gap: 50px;
grid-row-gap: 0px;
}

.company_highlights_inner{
margin-top:0%
}

.company_highlights_text{
    font-size:90%
}

.company_hightlights_image{
    margin-top:0%
}
.company_highlights_title{
    margin-top:0%
}

}


@media only screen and (min-width: 576px) and (max-width: 650px) {


.company_highlights_inner{
margin-top:-14%
}


}


@media only screen and (min-width: 650px) and (max-width: 768px) {


.company_highlights_inner{
margin-top:-12%
}


}




@media only screen and (min-width: 576px) and (max-width: 768px) {

    .company_highlights{
width:80%;
margin-left:10%;
margin-top:0%;
display:grid;
grid-template-columns: 1fr;
grid-template-rows: repeat(2, 1fr); 
grid-column-gap: 0px;
grid-row-gap: 0px;
}

.company_highlights_text{
    font-size:90%
}


}

@media only screen and (min-width: 768px) and (max-width: 992px) {

.company_highlights_text{
    font-size:80%
}

}

@media only screen and (min-width: 992px) and (max-width: 1200px) {

    .company_highlights_text{
    font-size:80%
}
}

@media only screen and (min-width: 1200px) and (max-width: 1400px) {
}

@media only screen and (min-width: 1400px) and (max-width: 1600px) {
}

@media only screen and (min-width: 1600px) and (max-width: 5600px) {
}






</style>