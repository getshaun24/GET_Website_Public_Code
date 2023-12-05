<template>
    

    <h4 class="title" >Customer/Userbase</h4>


<div class="userbase_container">
    <div>
<p>The Biggest Possible returns in the smallest places.</p>
<p>Projected Revenue</p>
<h2 class="big_num">$294 Million</h2>
<p>A free guide to your investment in our Nanotech fund</p>
<br>
<a target="_blank" href="https://thisisget.com/public_decks/GET_Resources_Nanotech_Deck.pdf" class="next_button_guide">Free Guide</a>
</div>

<div class="logo_images">
<img class="img" data-lag=".2" src="~/assets/content/fund_pages/nano/user_logos/logo_1.png" />
<img class="img" data-lag=".5" src="~/assets/content/fund_pages/nano/user_logos/logo_2.png" />
<img class="img" data-lag=".2" src="~/assets/content/fund_pages/nano/user_logos/logo_3.png" />
<img class="img" data-lag=".5" src="~/assets/content/fund_pages/nano/user_logos/logo_6.jpg" />
<img class="img" data-lag=".2" src="~/assets/content/fund_pages/nano/user_logos/logo_5.png" />
<img class="img" data-lag=".5" src="~/assets/content/fund_pages/nano/user_logos/logo_4.png" />
<img class="img" data-lag=".2" src="~/assets/content/fund_pages/nano/user_logos/logo_7.jpg" />
<img class="img" data-lag=".5" src="~/assets/content/fund_pages/nano/user_logos/logo_8.png" />
<img class="img" data-lag=".2" src="~/assets/content/fund_pages/nano/user_logos/logo_9.png" />
</div>

</div>

</template>


<script setup>

function button_click(){
   console.log('xxx')
}
</script>

<style scoped>


.title{
    margin-left:5%;
}

.userbase_container{
    display:grid;
    grid-template-columns: repeat(2, 1fr);
    grid-template-rows: 1fr;
    grid-column-gap: 100px;
    grid-row-gap: 0px;
    width:90%;
    margin-left:5%;
    margin-top:5%;
}

.logo_images{
    display: grid;
grid-template-columns: repeat(2, 1fr);
grid-template-rows: repeat(5, 1fr);
grid-column-gap: 50px;
grid-row-gap: 50px;
}

.img{
    width:100%
}

.img:nth-child(5){
    padding-top:12.5%
}

.img:nth-child(6){
    padding-top:12.5%
}


.big_num{
    text-decoration: underline;
  text-decoration-color: #c5920f;
  text-underline-offset: 8px;  
  text-decoration-thickness: 4px;
}


.next_button{
    width:60%;
    height:40px;
    background-color:rgb(25, 120, 237) ;
    margin-left: 20%;
    margin-top:7%;
    border-radius:100px;
    border:#fff solid 0px;
    cursor:pointer;
    font-size:130%;
    color:#fff;
    box-shadow: 0px 5px 12px rgba(0, 0, 0, 0.2);
    outline: 0px solid rgba(19, 218, 218, 0.6);
    transition: box-shadow 0.3s ease-in-out, transform 0.3s ease-in-out;
}


.next_button:hover{
  box-shadow: 0px 10px 15px rgb(25, 120, 237, .5);
  transform: translateY(-3px);
  outline: 3px solid rgba(19, 218, 218, 0.6);
  transition: outline 12s ease 1s;
} 



.next_button_guide{
    width:60%;
    height:40px;
    padding:5px 40px;
    background-color:rgb(25, 120, 237) ;
    margin-left: 20%;
    margin-top:7%;
    border-radius:100px;
    border:#fff solid 0px;
    cursor:pointer;
    font-size:130%;
    color:#fff;
    box-shadow: 0px 5px 12px rgba(0, 0, 0, 0.2);
    outline: 0px solid rgba(19, 218, 218, 0.6);
    transition: box-shadow 0.3s ease-in-out, transform 0.3s ease-in-out;
}


.next_button_guide:hover{
  box-shadow: 0px 10px 15px rgb(25, 120, 237, .5);
  transform: translateY(-3px);
  outline: 3px solid rgba(19, 218, 218, 0.6);
  transition: outline 12s ease 1s;
} 

@media only screen and (min-width: 0px) and (max-width: 380px) {
    .userbase_container{
    grid-template-columns: 1fr;
    grid-template-rows: repeat(2, 1fr); 
}

.title{
    margin-left:5%;
    font-size: 230%;
    margin-bottom:-4%
}

.logo_images{
grid-row-gap: 30px;
}

.next_button{
margin-bottom:10%
}
.next_button_guide{
margin-bottom:10%
}

}

@media only screen and (min-width: 380px) and (max-width: 430px) {
    .userbase_container{
    grid-template-columns: 1fr;
    grid-template-rows: repeat(2, 1fr); 
}

.title{
    margin-left:5%;
    font-size: 230%;
    margin-bottom:-4%
}

.logo_images{
grid-row-gap: 30px;
margin-top:-15%
}

.next_button{
margin-bottom:40%
}

.next_button_guide{
margin-bottom:40%
}
}


@media only screen and (min-width: 430px) and (max-width: 576px) {
    .userbase_container{
    grid-template-columns: 1fr;
    grid-template-rows: repeat(2, 1fr); 
}

.title{
    margin-left:5%;
    font-size: 230%;
    margin-bottom:-4%
}

.logo_images{
grid-row-gap: 25px;
}

}


@media only screen and (min-width: 576px) and (max-width: 768px) {
    .userbase_container{
    grid-template-columns: 1fr;
    grid-template-rows: repeat(2, 1fr); 
}

.title{
    margin-left:5%;
    font-size: 230%;
    margin-bottom:-4%
}
}




/* 


@media only screen and (min-width: 768px) and (max-width: 992px) {
}

@media only screen and (min-width: 992px) and (max-width: 1200px) {
}

@media only screen and (min-width: 1200px) and (max-width: 1400px) {
}

@media only screen and (min-width: 1400px) and (max-width: 1600px) {
}

@media only screen and (min-width: 1600px) and (max-width: 5600px) {
}
 */




</style>