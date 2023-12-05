<template>
    


<div class="cube_grid">


<div class="cube_container_hiw">
    <div class="cube_hiw" >
      <div class="face_hiw front_hiw">
        <img class="header_logo" src="~/assets/content/homepage/get_logo.png">
      </div>
      <div class="face_hiw back_hiw">E</div>
      <div class="face_hiw top_hiw"></div>
      <div class="face_hiw bottom_hiw"></div>
      <div class="face_hiw left_hiw">T</div>
      <div class="face_hiw right_hiw">G</div>
  </div>
</div>


<div class="cube_info">
    <div class="cube_info_grid">

    <div class="info_elm"><h4 class="info_title">Reserve Investments</h4><p class="info_text">
        You can review offering documents for live offerings and reserve investments in GETs investment funds. We provide proprietary analysis in our offering documents including recent price history, valuation and cap tables.
      </p></div>

      <div class="info_elm"><h4 class="info_title">Fund Investments</h4><p class="info_text">
        You can review offering documents for live offerings and reserve investments in GETs investment funds. We provide proprietary analysis in our offering documents including recent price history, valuation and cap tables.
      </p></div>
      
      <div class="info_elm"><span class="cube_end_elm"></span><h4 class="info_title">Manage Portfolio</h4><p class="info_text">
        You can review offering documents for live offerings and reserve investments in GETs investment funds. We provide proprietary analysis in our offering documents including recent price history, valuation and cap tables.
      </p></div>




    </div>
</div>
  

</div>



</template>





<style scoped>





.cube_grid{
    display: grid;
grid-template-columns: repeat(2, 1fr);
grid-template-rows: 1fr;
grid-column-gap: 0px;
grid-row-gap: 0px;
margin-top:-15%;
}

.cube_info{
    width:60%;
    margin-left:15%;
}
.cube_info_grid{
    display: grid;
grid-template-columns: repeat(1, 1fr);
grid-template-rows: repeat(3, 1fr);
grid-column-gap: 0px;
grid-row-gap: 0px;
}


.info_elm{
    margin-top:50vh;
}

.header_logo{
    width: var(--full_cube);
    mix-blend-mode: difference;
}



  .cube_hiw {
    width: var(--full_cube);
    height: var(--full_cube);
    position: relative;
    transform-style: preserve-3d;
    transform: rotateY(45deg);
    margin-left:25%;
    margin-top:2px;
    transition: all .25s ease;
  }

  .cube_hiw {
    transform: translateY(180px);
  }

  .face_hiw {
    position: absolute;
    width: var(--full_cube);
    height: var(--full_cube);
    text-align: center;
    font-size: 400px;
    color: white;
    background-color: #000;
    border: #fff 1px solid;
    line-height: var(--full_cube);
  }

  .front_hiw {
    transform: translateZ(var(--half_cube));
  }
  

  .back_hiw {
    transform: rotateY(180deg) translateZ(var(--half_cube));
  }

  .top_hiw {
    transform: rotateX(90deg) translateZ(var(--half_cube));
  }

  .bottom_hiw {
    transform: rotateX(-90deg) translateZ(var(--half_cube));
  }

  .left_hiw {
    transform: rotateY(-90deg) translateZ(var(--half_cube));
  }

  .right_hiw {
    transform: rotateY(90deg) translateZ(var(--half_cube));
  }









@media only screen and (min-width: 0px) and (max-width: 380px) {


  *{
    --full_cube: 130px;
    --half_cube: 65px;
  }

  .cube_grid{
margin-top:-30%;
padding-top: 20%;
}


  .cube_container_hiw{
    margin-left:-15%;
    margin-top:0%;
  }

  .face_hiw {
    font-size: 950%;
  }
  .cube_info{
    margin-left:0%;
}

.info_title{
    font-size: 200%;
}

.info_text{
    font-size: 95%;
}
.info_elm{
    margin-top:20vh;
}



}







@media only screen and (min-width: 380px) and (max-width: 576px) {



    *{
    --full_cube: 130px;
    --half_cube: 65px;
  }

  .cube_grid{
margin-top:-30%;
padding-top: 20%;
}


  .cube_container_hiw{
    margin-left:-15%;
    margin-top:0%;
  }

  .face_hiw {
    font-size: 950%;
  }
  .cube_info{
    margin-left:0%;
}

.info_title{
    font-size: 200%;
}

.info_text{
    font-size: 95%;
}
.info_elm{
    margin-top:20vh;
}



}

@media only screen and (min-width: 576px) and (max-width: 768px) {
  *{
    --full_cube: 200px;
    --half_cube: 100px;
  }

  .cube_container_hiw{
    margin-left:-8%;
    margin-top:60%
  }

  .face_hiw {
    font-size: 1500%;
  }
  .cube_info{
    margin-left:10%;
}


}



@media only screen and (min-width: 768px) and (max-width: 992px) {
  *{
    --full_cube: 325px;
    --half_cube: 162.5px;
  }

  .cube_container_hiw{
    margin-left:-8%;
    margin-top:25%
  }
  .cube_info{
    margin-left:20%;
}


}

@media only screen and (min-width: 992px) and (max-width: 1200px) {

  *{
    --full_cube: 400px;
    --half_cube: 200px;
  }
  .cube_container_hiw{
    margin-left:-5%;
    margin-top:45%
  }
}

@media only screen and (min-width: 1200px) and (max-width: 1400px) {

  *{
    --full_cube: 440px;
    --half_cube: 220px;
  }
  .cube_container_hiw{
    margin-left:-5%;
    margin-top:45%
  }

}

@media only screen and (min-width: 1400px) and (max-width: 1600px) {

  *{
    --full_cube: 480px;
    --half_cube: 240px;
  }
  .cube_container_hiw{
    margin-left:0%;
    margin-top:45%
  }

}

@media only screen and (min-width: 1600px) and (max-width: 5600px) {

  *{
    --full_cube: 520px;
    --half_cube: 260px;
  }
  .cube_container_hiw{
    margin-left:0%;
    margin-top:45%
  }

}








</style>