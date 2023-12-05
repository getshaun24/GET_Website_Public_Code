<template>
    

    <CircleTransition ref="cicle_tansition"/>

    <div class="home_box_hover_section">

<div class="box_hover_grid">

    <div class="box_hover_box" @click="transition_and_route('about')">
        <h6 class="box_hover_text">About</h6>
        <div class="hover_box_arrow_container">
        <img class="hover_box_arrow" src="../../assets/content/homepage/right_arrow.png">
        <img class="hover_box_arrow_2" src="../../assets/content/homepage/right_arrow.png">
    </div>
    <div class="overlay_container">
            <div class="box_overlay_1"></div>
            <div class="box_overlay_2"></div>
        </div>
    </div>
    
    <div class="box_hover_box" @click="transition_and_route('HowItWorks')">
        <h6 class="box_hover_text">Strategy</h6>
        <div class="hover_box_arrow_container">
            <img class="hover_box_arrow" src="../../assets/content/homepage/right_arrow.png">
            <img class="hover_box_arrow_2" src="../../assets/content/homepage/right_arrow.png">
        </div>
    <div class="overlay_container">
            <div class="box_overlay_1"></div>
            <div class="box_overlay_2"></div>
        </div>
    </div>

    <div class="box_hover_box" @click="transition_and_route('investments')">
        <h6 class="box_hover_text">Funds</h6>
        <div class="hover_box_arrow_container">
            <img class="hover_box_arrow" src="../../assets/content/homepage/right_arrow.png">
        <img class="hover_box_arrow_2" src="../../assets/content/homepage/right_arrow.png">
    </div>
    <div class="overlay_container">
            <div class="box_overlay_1"></div>
            <div class="box_overlay_2"></div>
        </div>
    </div>

    <div class="box_hover_box logo_box" @click="random_fund()">


        <div class="container generic_container">
        <div class="loader circle-loader">
            <div class="inner-circle"></div>
            <div class="circle"></div>
        </div>
        </div>

        <img class="get_logo" src="../../assets/content/homepage/get_logo.png">
        <div class="overlay_container">
            <div class="box_overlay_1"></div>
            <div class="box_overlay_2"></div>
        </div>
    </div>

</div>
</div>




</template>


<script setup>

const cicle_tansition = ref('');


function random_fund() {
    const funds = ["agile_elements", "boring_company", "boysterous", "green_worldwide", "helpful", "impossible", "nano", "neuralink", "social_wise", "thermo_ai"];

        const random = Math.floor(Math.random() * funds.length);
        console.log(random, funds[random]);


        navigateTo('fund_pages/' + funds[random])

}

function transition_and_route(route_to) {
    preloadRouteComponents(route_to)
 cicle_tansition.value.animation_and_route(route_to);
}


</script>




<style scoped>



.box_hover_grid{
    display: grid;
grid-template-columns: repeat(4, 1fr);
grid-template-rows: 1fr;
grid-column-gap: 0px;
grid-row-gap: 0px;
z-index:0;
}

.box_hover_box{
    width:100%;
    height:160%;
    border:#fff solid 1px;
    mix-blend-mode: difference;
    background-color: #fff;
    cursor: pointer;
}



.home_box_hover_section{
margin-left:-2px;
position: relative;
z-index:1
}



.box_hover_text{
    color:#fff;
    margin-top:120%;
    margin-left:10%;
    mix-blend-mode: difference;
}

.get_logo{
    width:20vh;
    margin-top:100%;
    margin-left:30%;
    mix-blend-mode: difference;
}

.hover_box_arrow{
    width:30px;
    filter: invert(1);
    margin-left:10%;
    mix-blend-mode: difference;
}

.hover_box_arrow_2{
    width:30px;
    filter: invert(1);
    mix-blend-mode: difference;
    margin-left:-100px;
    margin-top:-30px
}

.hover_box_arrow_container{
    margin-top:-130px;
    border:#fff solid 1px;
    padding:10px;
    width: 40px;
    margin-left:80%;
    border-radius:100%;
    mix-blend-mode: difference;
    display: grid;
    overflow: hidden;
}

.overlay_container{
    position: absolute;
    top:0;
    z-index: 1;
    width:25%;
    height:160%;
    display: flex;
    z-index:-2;
}

.box_overlay_1{
    width:50%;
    background-color:#000;
    height:100%;
}
.box_overlay_2{
    width:50%;
    background-color:#000;
    height:100%;
    margin-left:0%
}

.box_hover_box:hover .box_overlay_1{
  
    transition:all ease .8s;
    width:0%
}

.box_hover_box:hover .box_overlay_2{

    transition: 0.4s;
    width:0%
}

.box_hover_box:hover .hover_box_arrow{
transition: 1s;
margin-left:150%
}
.box_hover_box:hover .hover_box_arrow_2{
transition: 1s;
margin-left:5px;
}











@media screen and (min-width: 2300px) and (max-width: 5600px) {





.box_hover_text{
    font-size:400%
}

.get_logo{
    width:50%;
    margin-left:25%;
}


.hover_box_arrow_container{
    margin-top:-200px;
}



}









@media screen and (min-width: 1900px) and (max-width: 2300px) {







.box_hover_text{
    font-size:400%
}

.get_logo{
    width:50%;
    margin-left:25%;
}


.hover_box_arrow_container{
    margin-top:-200px;
}





}


@media screen and (min-width: 1600px) and (max-width: 1900px) {




.box_hover_text{
    font-size:400%
}

.get_logo{
    width:50%;
    margin-left:25%;
}


.hover_box_arrow_container{
    margin-top:-200px;
}





}





@media screen and (min-width: 1400px) and (max-width: 1600px) {




.box_hover_text{
    font-size:325%
}

.get_logo{
    width:50%;
    margin-left:25%;
}


.hover_box_arrow_container{
    margin-top:-170px;
    margin-left: 75%;
}


}




@media screen and (min-width: 1200px) and (max-width: 1400px) {





.box_hover_text{
    font-size:275%
}

.get_logo{
    width:50%;
    margin-left:25%;
}


.hover_box_arrow_container{
    margin-top:-150px;
    margin-left: 70%;
}


}

@media only screen and (min-width: 992px) and (max-width: 1200px) {







.get_logo{
    width:50%;
    margin-left:25%;
}


.hover_box_arrow_container{
    margin-top:-170px;
    margin-left: 75%;
}

.hover_box_arrow{
    width:20px;
}

.hover_box_arrow_2{
    width:20px;
    margin-top:-20px
}

.hover_box_arrow_container{
    margin-top:-110px;
    margin-left: 75%;
    width: 30px;
}


}



@media only screen and (min-width: 768px) and (max-width: 992px) {



.get_logo{
    width:50%;
    margin-left:25%;
}


.hover_box_arrow_container{
    margin-top:-170px;
    margin-left: 75%;
}

.hover_box_arrow{
    width:15px;
}

.hover_box_arrow_2{
    width:15px;
    margin-top:-15px
}

.hover_box_arrow_container{
    margin-top:-85px;
    margin-left: 68%;
    width: 25px;
}

.home_box_hover_section{
z-index:-1
}




}



@media only screen and (min-width: 576px) and (max-width: 768px) {





.home_box_hover_section{
display:none
}





}

@media only screen and (min-width: 0px) and (max-width: 576px) {



.home_box_hover_section{
display:none
}



}









 /* ---------------------------- SPINNER ----------------------------- */









 /*
 ---- GENERIC PROPERTIES ----
*/

.generic_container {
  margin-bottom: 20px;
position:absolute;
  width: 20vw;
  height: 20vw;
  margin-top:21.25%;
  margin-left:2.5%;
  mix-blend-mode: difference;
  z-index:10
}

.loader {
  height: 100%;
  width: 100%;

  position: relative;
  mix-blend-mode: difference;
  border-radius: 100%;
}

.inner-circle {
  width: 80%;
  height: 80%;

  position: absolute;

  left: 10%;
  top: 10%;

  mix-blend-mode: difference;
  margin: 0 auto;

  border-radius: 100%;
}

/*
 ---- CIRCLE LOADER ----
*/
.circle-loader {
  animation: rotateAnimation 2.5s infinite linear;
  transition: rotateAnimation 2.5s infinite linear;
}

.logo_box:hover .circle-loader .circle {
    transition:background-color .5s ease-in-out .2;
    background-color: #fff;
}







.container .circle-loader .circle {
  width: 10%;
  height: 10%;

  background-color: #000;
  mix-blend-mode: difference;
  margin: 0 auto;
  transition:background-color 1.25s ease-in-out;
  border-radius: 200%;
}




/*
 ---- Animations ----
*/
@keyframes rotateAnimation {
  100% {
    transform: rotate(360deg);
  }
}




</style>