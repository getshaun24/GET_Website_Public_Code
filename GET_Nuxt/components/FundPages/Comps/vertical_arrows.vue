<template>
    
    <div>
    <div class="comp_grid">
    <div class="arrows_container">
        <div class="elm_grid">

            <div class="inner_grid">
            <p class="vertical_text">Electronics</p>
            <p class="main_text"><b>Fingerprint Sensors</b><br>CMOS Image Sensors<br>Semiconductor Manufacturing<br>Memory (NRAM)<br>Conductive inks<br>Printed Electronics</p>
            <img class="arrow_image" src="~/assets/content/fund_pages/nano/right.png">
            <h6 class="big_text">$4.4<br>Billion</h6>
        </div>
        <div class="inner_grid">
            <p class="vertical_text">Energy</p>
            <p class="main_text">Printable Solar<br>Tandem Silicon PV<br>Fuel Cells & Electrolyzers<br>Battery Additives</p>
            <img class="arrow_image" src="~/assets/content/fund_pages/nano/right.png">
            <h6 class="big_text">$2.0<br>Billion</h6>
        </div>
        <div class="inner_grid">
            <p class="vertical_text">Healthcare</p>
            <p class="main_text">Therapeutics<br>Drug Delivery<br>Disease Tracking<br>Pharmaceuticals </p>
            <img class="arrow_image" src="~/assets/content/fund_pages/nano/right.png">
            <h6 class="big_text">$4.8<br>Billion</h6>
        </div>


        </div>
      </div>

      <img class="outer_img" data-lag=".4" src="~/assets/content/fund_pages/nano/nano_14.png">

    </div>

    <p class="outer_text">Nanocarbon has applications across some of the largest sectors globally including Electronic, Energy, and Healthcare. The total addressable markets to Nano-C is over $11.1 Billion. With major commercial contracts imminent, now is the time to get involved.</p>

</div>
</template>


<style scoped>

.comp_grid{
    display: grid;
grid-template-columns: repeat(2, 1fr);
grid-template-rows: repeat(1, 1fr);
grid-column-gap: 0px;
grid-row-gap:0px;
margin-top:7.5%;
}

.arrows_container{
    width:35%;
    margin-left:5%;
    margin-top:5%
}

.elm_grid {
display: grid;
grid-template-columns: repeat(1, 1fr);
grid-template-rows: repeat(3, 1fr);
grid-column-gap: 0px;
grid-row-gap:20px;

}

.inner_grid{
    display: grid;
grid-template-columns: repeat(4, 1fr);
grid-template-rows: repeat(1, 1fr);
grid-column-gap: 10px;
grid-row-gap:0px;
margin-top:-5%

}

.vertical_text{
    writing-mode: vertical-rl;
    text-orientation: upright;
    color: #fff;
    line-height: 0;
    letter-spacing: -.2em;
    font-size:145%;
    text-align: center;
    align-self: center;
}

.main_text{
    font-size:1.5vw;
    align-self: center;
    white-space: nowrap;
    justify-self: left;
    width:20vw
}
.arrow_image{
    width:5vw;
    align-self: center;
    margin:0vw 1vw;
}

.big_text{
    align-self: center;
    text-align:left;
    margin-left:0px
}

.outer_img{
    width:70%;
    margin-top:40%;
    margin-left:10%
}


.outer_text{
    width:70%;
    margin-left:15%;
    text-align: center;
    margin-bottom:7.5%
}



@media only screen and (min-width: 0px) and (max-width: 576px) {
    .comp_grid{
grid-template-columns: repeat(1, 1fr);
grid-template-rows: repeat(2, 1fr);
margin-bottom:-95%;
margin-top:30%
}



.outer_img{
    margin-top:0%;
    margin-left:10%
}
.main_text{
    font-size:3vw;
}
.arrow_image{
    width:8vw;
    margin:0vw 20vw;
}
.big_text{
    margin-left:-12vw
}


}

@media only screen and (min-width: 0px) and (max-width: 380px) {
    .arrows_container{
    width:90%;
    margin-left:2%;
    margin-top:120%
}

.outer_text{
    width:85%;
    margin-left:7.5%;
    text-align: center;
    margin-bottom:30%;
    margin-top:-220%
}

}

@media only screen and (min-width: 380px) and (max-width: 400px) {
    .arrows_container{
    width:90%;
    margin-left:2%;
    margin-top:70%
}

.outer_text{
    width:85%;
    margin-left:7.5%;
    text-align: center;
    margin-bottom:30%;
    margin-top:-170%
}

}

@media only screen and (min-width: 400px) and (max-width: 576px) {
    .arrows_container{
    width:90%;
    margin-left:5%;
    margin-top:5%
}
.outer_text{
    width:85%;
    margin-left:7.5%;
    text-align: center;
    margin-bottom:20%;
    margin-top:40%
}

}

@media only screen and (min-width: 576px) and (max-width: 650px) {
    .comp_grid{
grid-template-columns: repeat(1, 1fr);
grid-template-rows: repeat(2, 1fr);
margin-bottom:-35%
}
.arrows_container{
    width:90%;
    margin-left:5%;
    margin-top:5%
}
.outer_img{
    margin-top:0%;
    margin-left:10%
}
.main_text{
    font-size:3vw;
}
.arrow_image{
    width:8vw;
    margin:0vw 20vw;
}
.big_text{
    margin-left:-12vw
}
}

@media only screen and (min-width: 650px) and (max-width: 768px) {
    .comp_grid{
grid-template-columns: repeat(1, 1fr);
grid-template-rows: repeat(2, 1fr);
}
.arrows_container{
    width:90%;
    margin-left:-7.5%;
    margin-top:15%
}

.outer_img{
    margin-top:-10%;
    margin-left:10%
}
.outer_text{
    width:80%;
    margin-left:10%;
    text-align: center;
    margin-bottom:20%;
    margin-top:-40%
}
}






@media only screen and (min-width: 768px) and (max-width: 850px) {
    .comp_grid{
grid-template-columns: repeat(1, 1fr);
grid-template-rows: repeat(2, 1fr);
}
.arrows_container{
    width:90%;
    margin-left:-5%;
    margin-top:15%;
}

.outer_img{
    margin-top:-20%;
    margin-left:15%
}

.outer_text{
    width:70%;
    margin-left:15%;
    text-align: center;
    margin-bottom:20%;
    margin-top:-35%
}

}

@media only screen and (min-width: 850px) and (max-width: 992px) {
    .comp_grid{
grid-template-columns: repeat(1, 1fr);
grid-template-rows: repeat(2, 1fr);
}
.arrows_container{
    width:90%;
    margin-left:-5%;
    margin-top:10%;
}

.outer_img{
    margin-top:-10%;
    margin-left:10%
}

.outer_text{
    width:70%;
    margin-left:15%;
    text-align: center;
    margin-bottom:20%;
    margin-top:-15%
}

}




@media only screen and (min-width: 992px) and (max-width: 1200px) {
    .outer_img{
    margin-top:27%;
    margin-left:5%
}
.vertical_text{
    letter-spacing: -.18em;
    font-size:125%;
}

.comp_grid{
margin-bottom: 10%;
margin-top:10%
}

}

@media only screen and (min-width: 1200px) and (max-width: 1400px) {
    .inner_grid{
margin-top:-22.5%
}
.outer_img{
    margin-top:-2.5%;
    margin-left:15%
}

.comp_grid{
margin-bottom: 5%;
margin-top:10%
}

}

@media only screen and (min-width: 1400px) and (max-width: 1600px) {
    .inner_grid{
margin-top:-17.5%
}
.outer_img{
    margin-top:-1.75%;
    margin-left:10%
}
.comp_grid{
margin-bottom: 5%;
margin-top:10%
}
}

@media only screen and (min-width: 1600px) and (max-width: 1900px) {
    .inner_grid{
margin-top:-10%
}
.outer_img{
    margin-top:-1.25%;
    margin-left:7.5%
}
.comp_grid{
margin-bottom: 5%;
margin-top:10%
}
}


@media only screen and (min-width: 1900px) and (max-width: 5600px) {
    .inner_grid{
margin-top:-10%
}
.outer_img{
    margin-top:-1%;
    margin-left:5%
}
.comp_grid{
margin-bottom: 5%;
margin-top:10%
}
}




</style>