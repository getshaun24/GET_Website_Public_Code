<template>
    

<div class="highlights_section">


<img data-lag=".5" data-speed=".6" class="hightlights_image_desktop" :src="image" />

    <div class="highlights_text">

        <h3>Investment Highlights</h3>
        <div class="investment_highlights_grid">

            <div>
            <h5 class="highlights_elm title_underline">{{ title_1 }}</h5>
       
            <h5 class="highlights_elm">{{ info_1 }}</h5>
            </div>

               
            <div>
            <h5 class="highlights_elm title_underline">{{ title_2 }}</h5>
       
            <h5 class="highlights_elm">{{ info_2 }}</h5>
            </div>

               
            <div>
            <h5 class="highlights_elm title_underline">{{ title_3 }}</h5>
       
            <h5 class="highlights_elm">{{ info_3 }}</h5>
            </div>

            <div>
            <h5 class="highlights_elm title_underline">{{ title_4 }}</h5>
       
            <h5 class="highlights_elm">{{ info_4 }}</h5>
            </div>

            <div>
            <h5 class="highlights_elm title_underline">{{ title_5 }}</h5>
       
            <h5 class="highlights_elm">{{ info_5 }}</h5>
            </div>
            
        </div>
    </div>

    <img data-lag=".5" data-speed=".65" class="hightlights_image_mobile" :src="image" />

</div>


</template>


<script setup>



const props = defineProps(['title_1', 'info_1', 'title_2', 'info_2', 'title_3', 'info_3', 'title_4', 'info_4', 'title_5', 'info_5', 'image', 'image_margin'])

</script>


<style scoped>




.highlights_section{
    width:90%;
    margin-left:5%;
    display:grid;
    grid-template-columns: repeat(2, 1fr);
    grid-template-rows: 1fr;
    grid-column-gap: 100px;
    grid-row-gap: 0px;
}

.hightlights_image_desktop{
    width:80%;
    object-fit: cover;
    object-position: center;
    margin-top:v-bind(image_margin);
}

.hightlights_image_mobile{
    object-fit: cover;
    object-position: center;
    margin-top:v-bind(image_margin);
}

.investment_highlights_grid{
    display:grid;
    grid-template-columns: repeat(1, 1fr);
    grid-template-rows: repeat(5, 1fr);
    grid-column-gap: 10px;
    grid-row-gap: 0px;
    width:100%;
}

.highlights_line{
    width:40%;
    height:3px;
    background-color:rgb(14, 85, 166);
    margin-top:-22px;
    margin-bottom:-10px
}


.highlights_elm{
    font-size:150%;
}

.title_underline{
    text-decoration: underline;
  text-decoration-color: #f1aa59;
  text-underline-offset: 8px;
}



@media only screen and (min-width: 0px) and (max-width: 376px) {


.highlights_section{
width:90%;
margin-left:5%;
display:grid;
grid-template-columns: repeat(2, 1fr);
grid-template-rows: 1fr;
grid-column-gap: 100px;
grid-row-gap: 0px;
}

.highlights_elm{
font-size:100%
}


.hightlights_image_desktop{
display:none
}

.hightlights_image_mobile{
display:none
}

.highlights_text{
margin-left:7%
}
}


@media only screen and (min-width: 376px) and (max-width: 576px) {


    .highlights_section{
    width:90%;
    margin-left:5%;
    display:grid;
    grid-template-columns: repeat(2, 1fr);
    grid-template-rows: 1fr;
    grid-column-gap: 100px;
    grid-row-gap: 0px;
}

.highlights_elm{
    font-size:100%
}


.hightlights_image_desktop{
    display:none
}

.hightlights_image_mobile{
    display:none
}

.highlights_text{
    margin-left:7%
}
}




@media only screen and (min-width: 576px) and (max-width: 625px) {

    .hightlights_image_mobile{
    width:220px;
    margin-left:-35%
}

}

@media only screen and (min-width: 625px) and (max-width: 700px) {

    .hightlights_image_mobile{
    width:250px;
    margin-left:-22%
}
}
@media only screen and (min-width: 700px) and (max-width: 768px) {

.hightlights_image_mobile{
width:250px;
margin-left:-12%

}

}

@media only screen and (min-width: 576px) and (max-width: 768px) {
    .highlights_section{
    width:90%;
    margin-left:5%;
    display:grid;
    grid-template-columns: repeat(2, 1fr);
    grid-template-rows: 1fr;
    grid-column-gap: 100px;
    grid-row-gap: 0px;
}

.highlights_elm{
    font-size:120%
}



.hightlights_image_desktop{
    display:none
}




}

@media only screen and (min-width: 768px) and (max-width: 992px) {

    .highlights_section{
    width:90%;
    margin-left:5%;
    display:grid;
    grid-template-columns: repeat(2, 1fr);
    grid-template-rows: 1fr;
    grid-column-gap: 100px;
    grid-row-gap: 0px;
}

.highlights_elm{
    font-size:150%;
    line-height: .5;
}



.hightlights_image_desktop{
    display:none
}

.hightlights_image_mobile{
    width:100%;
    margin-left:-20%
}



}

@media only screen and (min-width: 992px) and (max-width: 1200px) {

    .hightlights_image_mobile{
    display:none
}


}

@media only screen and (min-width: 1200px) and (max-width: 1400px) {


    .hightlights_image_mobile{
    display:none
}


}

@media only screen and (min-width: 1400px) and (max-width: 1600px) {


    .hightlights_image_mobile{
    display:none
}


}

@media only screen and (min-width: 1600px) and (max-width: 5600px) {


    .hightlights_image_mobile{
    display:none
}


}





</style>