<template>

    <div class="header_class">
      


      <div class="downward_dome"></div>
      <div class="dome_overlay"></div>
      <div class="black_circle" ></div>
      <div class="white_circle" ></div>
  
      <CircleTransition ref="cicle_tansition"/>
  <!-- 
          <div class="header_container"> -->
            <div class="">

              <PrivacyBanner/>
  
            <HeaderCompsLogoCube class='hide_on_fund_route' @logo_cube_clicked="transition_and_route('/')"/>
  
  
              <div class="header_menu">
                      <NuxtLink class="header_menu_item login_item" to="/login_pages/login">Login</NuxtLink>
  
  
                  
                  <div class="header_menu_item" style="margin-top:-60px">
  
                      <div @click="modal_open" style="cursor: pointer;" class="cube_container_modal" @mouseenter="startTurning_modal" @mouseleave="stopTurning_modal">
      <div class="cube_modal" :style="{ transform: `rotateY(${cube_modal}deg)` }">
        <div class="face_modal front_modal"><img class="header_logo_modal" src="~/assets/content/homepage/burger.png" alt=""></div>
        <div class="face_modal back_modal">X</div>
        <div class="face_modal top_modal"></div>
        <div class="face_modal bottom_modal">X</div>
        <div class="face_modal left_modal">X</div>
        <div class="face_modal right_modal"><img class="header_logo_modal" src="~/assets/content/homepage/burger.png" alt=""></div>
      </div>
    </div>
                  </div>
              </div>
          </div>
          
  
  
          <div v-show="menu_modal_open" class="menu_modal">
  
              <div class="menu_modal_container">
                <div class="grid_container_1">
                  <div class="menu_modal_grid">
                      <div class="menu_modal_item item_1">
                          <div @click="close_and_route('/')"><img class="menu_arrow" src="../assets/content/homepage/arrow_medium_light.svg"><span class="move">Home</span></div>
                      </div>
                      <div class="menu_modal_item item_2">
                          <div @click="close_and_route('/investments')" ><img class="menu_arrow" src="../assets/content/homepage/arrow_medium_light.svg"><span class="move">Investments</span></div>
                      </div>
                      <div class="menu_modal_item item_3">
                          <div @click="close_and_route('/HowItWorks')"><img class="menu_arrow" src="../assets/content/homepage/arrow_medium_light.svg"><span class="move">How It Works</span></div>
                      </div>
                      <div class="menu_modal_item item_4">
                          <div @click="close_and_route('/about')"><img class="menu_arrow" src="../assets/content/homepage/arrow_medium_light.svg"><span class="move">About Us</span></div>
                      </div>
                      <div class="menu_modal_item item_5">
                          <div @click="close_and_route('/contact')"><img class="menu_arrow" src="../assets/content/homepage/arrow_medium_light.svg"><span class="move">Contact</span></div>
                      </div>
              </div>
            </div>
  
  
                  <div class="modal_info">
                          <div class="info_grid">
                              <div class="info_item">
                                  <div class="info_item_title">GET Equity Partners</div>
                                  <div class="info_item_sub_text">Venture Studio</div>
                              </div>
  
                              <div class="info_item">
                                  <div class="info_item_title">Financial District</div>
                                  <div class="info_item_sub_text">New York, New York</div>
                              </div>
                              <div class="info_item">
                                  <div class="info_item_title">Historic Navy Yard</div>
                                  <div class="info_item_sub_text">Charleston, South Carolina</div>
                              </div>
                              <div class="info_item">
                                  <div class="info_item_title">Chrysler Building</div>
                                  <div class="info_item_sub_text">New York, New York</div>
                              </div>
  
  
  
                              <div class="info_item contact_item">
                                  <div class="info_item_title">contact@thisisget.com</div>
                                  <div class="info_item_title">press@thisisget.com</div>
                              </div>
    
  
                  </div>
  
  
          </div>
      </div>
  </div>
  
  </div>
  
  </template>
  
  
  <script setup>
  import { ref, onMounted, onUnmounted, nextTick } from 'vue';
  import { from_header_menu } from "../stores/menu_transition.js"
  import { page_to } from "../stores/page_to.js"
  import { gsap } from 'gsap'
  
  
  const cube = ref(0);
      const cube_not_reset = ref(true);
      let i = ref(0)
      const cube_modal = ref(true);
      const cube_not_reset_modal = ref(true);
  
  

const menu_modal_open = useCookie('menu_modal_open', {default:()=> false, watch:true, maxAge:1800})
  

  
  // sleep time expects milliseconds
  function sleep (time) {
    return new Promise((resolve) => setTimeout(resolve, time));
  }
  
  
  const header_opacity = ref(0)
  
  
  
  
  const route_to = page_to()
  const menu_store = from_header_menu()
  
  // --------------------------------
    // --------------------------------
      // --------------------------------

  const tl_1 = gsap.timeline();
  const tl_2 = gsap.timeline();
  const tl_3 = gsap.timeline();
  const tl_4 = gsap.timeline();
  const tl_5 = gsap.timeline();
  
  
  onMounted(() => {
    console.log('xxx route', route_to.current_page_to)
    tl_1.to(".downward_dome", {duration: 1.4, yPercent: 100, ease: "power2.in"})
        .to(".dome_overlay", {duration: 1.5, autoAlpha: 0, ease: "power4.in"}, "<")
        .to(".downward_dome", {delay: 1.5, autoAlpha: 0})

        if (menu_modal_open.value == true){
          tl_5.to(".grid_container_1", {delay: .7, duration: .8, yPercent:150});
          tl_4.to(".modal_info", {delay: .7, duration:.8, yPercent:150}).restart()
          header_opacity.value = 1;
          cube_modal.value = (-90);
          sleep(1600).then(() => {menu_modal_open.value = false, gsap.to(".modal_info", {duration: .001, x:400})})
        } else {
          tl_5.to(".grid_container_1", {delay:0, duration: .01, yPercent:150});
        }

        if (!String(route_to.current_page_to).includes('fund_pages')){
          header_opacity.value = 1;
          sleep(1600).then(() => { menu_modal_open.value = false;  gsap.to(".modal_info", {duration: .001, x:400}) })
        } 
        else{
          tl_1.to(".downward_dome", {delay:0, duration:.01, autoAlpha: 0})
          menu_modal_open.value = false;
          sleep(1400).then(() => { header_opacity.value = 1; })
        }
  
  })



  const pause_click = ref(false);
  
  function modal_open() {
  
    if (pause_click.value == false){
    pause_click.value = true
    sleep(1500).then(() => { pause_click.value = false })
    }else{
        pause_click.value = true
        return
      }
  
      cube_modal.value = (-180);

      
  

      if (menu_modal_open.value == false){

        tl_2.to(".black_circle", {duration: 3, yPercent: -100, xPercent: 100, scale: 2.25})
        .to(".dome_overlay", {duration: 1, autoAlpha: 1}, "<").restart()
        .to(".white_circle", {duration: 3, yPercent: 100, xPercent: -100, scale: 2.25}, "<").restart();

        tl_3.to(".modal_info", {duration: .1, yPercent:0}).restart()
            .to(".modal_info", {delay: 1.6, duration: .8, x:-400}, "<").restart();
  
        tl_5.to(".grid_container_1", {delay: 1, duration: .8, yPercent:0})

        menu_modal_open.value = !menu_modal_open.value;
  
      }else{
        tl_1.restart()
        tl_2.progress(0).pause();
        tl_4.to(".modal_info", {delay: .7, duration: .8, yPercent:150})
        tl_5.to(".grid_container_1", {delay: .7, duration: .8, yPercent:150});

        sleep(1500).then(() => { tl_3.progress(0).pause(); })
        sleep(1600).then(() => {  menu_modal_open.value = !menu_modal_open.value;})
        sleep(1700).then(() => { cube_modal.value = (-90);})
        
      }
  
  
      
  }
  
  
  
  
  function startTurning_modal() {
      if (menu_modal_open.value == true){
          cube_modal.value = (-180);
      }else{
          cube_modal.value = (-90);
      }
  }
  

  async function startTurning_modal_ticker() {
        await nextTick();
  function myLoop() {         //  create a loop function
      setTimeout(function() {   //  call a 3s setTimeout when the loop is called
        cube_modal.value -= 10   //  your code here
      i++;                    //  increment the counter
      if (i < 5000 || cube_not_reset_modal.value == true) {           //  if the counter < 10, call the loop function
      myLoop();             //  ..  again which will trigger another 
      } else{
        cube_not_reset_modal.value = true;    
      cube_modal.value=0;
      }                      //  ..  setTimeout()
      }, 30)
      }
      myLoop(); 
  }
  


  function stopTurning_modal() {
      if (menu_modal_open.value == true){
          cube_modal.value = (-270);
      }else{
          cube_modal.value = 0;
      }
      cube_not_reset_modal.value = false;
  }
  
  
  const nuxtApp = useNuxtApp()
  nuxtApp.hook('page:start', () => {
    startTurning_modal_ticker()
    if (String(route_to.current_page_to).includes('fund_pages')){
    sleep(1600).then(() => { stopTurning_modal()})
    } else {
      sleep(1000).then(() => { stopTurning_modal()})
    }
  })
  
  

  
  function close_and_route(route_to){
    preloadRouteComponents(route_to)
    menu_store.toggle_from_menu()
    console.log(route_to)
    navigateTo(route_to)
  }
  
  
  
  onBeforeRouteLeave(() => {
  
    if (String(route_to.current_page_to).includes('fund_pages')){
      header_opacity.value = 0;
      tl_1.to(".downward_dome", {delay:0, duration:.01, autoAlpha: 0})
    } else {
      header_opacity.value = 1;
    }
  
   })
  
  
  
  const cicle_tansition = ref(null);
  function transition_and_route(route_to) {
  cicle_tansition.value.animation_and_route(route_to);
  }
  
  
  
  </script>
  
  <style scoped>
  
  
  
  
  .hide_on_fund_route{
    opacity:v-bind(header_opacity);
  }
  

  
  .downward_dome{
    width:150%;
    height:120%;
    border-top-left-radius: 50%;
    border-top-right-radius: 50%;
    background-color:#fff;
    z-index:300;
    left:-25%;
    top:-20%;
    opacity:1;
    position:fixed;
    transition:  margin-top 1.5s ease-in;
  }

  .dome_overlay{
    width:100vw;
      height:100vh;
      background-color:rgba(114, 114, 114, 0.3);
      z-index:100;
      position:fixed;
      top:0;
      left:0;
  }
  
  .black_circle{
    width:100vw;
    height:100vw;
    border-radius:100%;
    background-color:#000;
    z-index:800;
    left:-100%;
    top:100%;
    position:fixed;
  }

  .white_circle{
    width:100vw;
    height:100vw;
    border-radius:100%;
    background-color:#fff;
    z-index:800;
    left:100%;
    top:-100%;
    position:fixed;
  }
  
  
  
  .menu_modal_container{
      margin-top:15%;
      display:flex;
  }
  
  
  .menu_modal{
      width:100%;
      height:100vh;
      position:fixed;
      z-index:900;
      top:0;
      left:0;
  }
  
  
  
  
  .menu_modal_item{
          color:#000;
          font-size:6.5vw;
          line-height: 1;
          cursor:pointer;
      }
  
  
  
  
      .modal_info{
          width:35%;
          height:66vh;
          margin-left:100%;
          border-left:#000 solid 4px;
      }
  
  
  
  .menu_modal_grid{
      width:65%;
      height:70vh;
      display: grid;
  grid-template-columns: 1fr;
  grid-template-rows: repeat(5, 1fr);
  grid-column-gap: 0px;
  grid-row-gap: 0px;
  width:100%;
  overflow: hidden;
      }

      .grid_container_1{
        width:90%;
        margin-left:7%;
        position: absolute;
      }
  
      .info_grid{
          display: grid;
  grid-template-columns: 1fr;
  grid-template-rows: repeat(6, 1fr);
  grid-column-gap: 0px;
  grid-row-gap: 20px;
      }
  
      .contact_item{
          margin-top:5px;
      }
      .info_item_title{
          font-size:20px;
          color:#000;
          padding:5px 40px
      }
      .info_item_sub_text{
          font-size:20px;
          color:#000;
          padding:5px 40px
      }
  
  
      .modal_info{
          width:35%;
          height:66vh;
          border-left:#000 solid 4px;
      }
  
      .menu_arrow{
      width:15%;
      margin-left:-15%;
      margin-top:-25%;
      margin-right:5%
  }
  
  
  .menu_modal_item:hover .menu_arrow{
      transition: all ease 1s;
      margin-left:-260px;
      margin-right:20px;
  }
  
  .menu_modal_item:hover{
      padding-left:320px;
      transition: all ease 1s;
  }
  
  .menu_modal{
  
      width:100%;
      height:100vh;
      position:fixed;
      z-index:900;
      top:0;
      left:0
  }
  
  .move{
      position: absolute;
      margin-top:1%;
      color:#000
  }
  
  .header_container{
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      grid-template-rows: 1fr;
      grid-column-gap: 0px;
      grid-row-gap: 0px;
      padding: 0 100px;
      align-items: center;
      height: 100px;
      mix-blend-mode: difference;
      position: fixed;
      width:100%;
      z-index:0;
      opacity:v-bind(header_opacity);
      transition: all 0s ease;
  }
  
  
  
  
  .header_logo{
      display: flex;
      justify-content: center;
      align-items: center;
  }
  
  .header_menu{
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      grid-template-rows: 1fr;
      grid-column-gap: 0px;
      grid-row-gap: 0px;
      width:10%;
      right:60px;
      margin-top:50px;
      position: fixed;
      z-index:1000;
      mix-blend-mode: difference;
      opacity:v-bind(header_opacity);
  }
  
  .header_menu_item{
      display: flex;
      justify-content: center;
      align-items: center;
      font-size: 20px;
      font-weight: 600;
      color: #fff;
      transition: all ease .4s;
      mix-blend-mode: difference;
  }
  
  .login_item{
      margin-top:-30px;
      mix-blend-mode: difference;
  
  }
  
  
  
  
  
  
  .cube_container_modal {
      width: 100px;
      height: 80px;
      perspective: 1000px;
      margin-top:-45px;
      margin-left:-50px;
    }
  
    .cube_modal {
      width: 50px;
      height: 50px;
      position: relative;
      transform-style: preserve-3d;
      transform: rotateY(0deg);
      transition: transform 0.5s;
      margin-top:25px;
      margin-left:50px;
      margin-top:50px
    }
  
  
    .face_modal {
      position: absolute;
      width: 50px;
      height: 50px;
      text-align: center;
      font-size: 30px;
      color: white;
      background-color: #000;
      border: #fff 1px solid;
      line-height: 50px;
    }
  
    .front_modal {
      transform: translateZ(25px);;
    }
    
  
    .back_modal {
      transform: rotateY(180deg) translateZ(25px);
    }
  
    .top_modal {
      transform: rotateX(90deg) translateZ(25px);
    }
  
    .bottom_modal {
      transform: rotateX(-90deg) translateZ(25px);
    }
  
    .left_modal {
      transform: rotateY(-90deg) translateZ(25px);
    }
  
    .right_modal {
      transform: rotateY(90deg) translateZ(25px);
    }
  
    .header_logo_modal{
      width:30px;
      mix-blend-mode: difference;
      filter: invert(1);
      margin-top:8px
  }
  
  
  
  
  
  
  
  @media only screen and (min-width: 0px) and (max-width: 430px) {
  
  
    
  
  
  
      .cube {
      width: 40px;
      height: 40px;
      position: relative;
      transform-style: preserve-3d;
      transform: rotateY(45deg);
      transition: transform 0.5s;
      margin-left:25px;
      margin-top:2px;
    }
  
    .cube {
      transform: translateY(180px);
    }
  
    .face {
      position: absolute;
      width: 40px;
      height: 40px;
      text-align: center;
      font-size: 50px;
      color: white;
      background-color: #000;
      border: #fff 1px solid;
      line-height: 40px;
    }
  
    .front {
      transform: translateZ(20px);;
    }
    
  
    .back {
      transform: rotateY(180deg) translateZ(20px);
    }
  
    .top {
      transform: rotateX(90deg) translateZ(20px);
    }
  
    .bottom {
      transform: rotateX(-90deg) translateZ(20px);
    }
  
    .left {
      transform: rotateY(-90deg) translateZ(20px);
    }
  
    .right {
      transform: rotateY(90deg) translateZ(20px);
    }
  
    .header_logo{
      width:40px;
      mix-blend-mode: difference;
  }
  
  .modal_info{
          width:45%;
          margin-left:calc(100% + 600px);
      }

  
  
  .face_modal {
      position: absolute;
      width: 25px;
      height: 25px;
      text-align: center;
      font-size: 15px;
      color: white;
      background-color: #000;
      border: #fff 1px solid;
      line-height: 25px;
    }
  
    .front_modal {
      transform: translateZ(12.5px);;
    }
    
  
    .back_modal {
      transform: rotateY(180deg) translateZ(12.5px);
    }
  
    .top_modal {
      transform: rotateX(90deg) translateZ(12.5px);
    }
  
    .bottom_modal {
      transform: rotateX(-90deg) translateZ(12.5px);
    }
  
    .left_modal {
      transform: rotateY(-90deg) translateZ(12.5px);
    }
  
    .right_modal {
      transform: rotateY(90deg) translateZ(12.5px);
    }
  
  
    .header_logo_modal{
      width:15px;
      mix-blend-mode: difference;
      filter: invert(1);
      margin-top: 5px;
  }
  
  .header_menu_item{
      font-size: 15px;
      color: #fff;
      margin-top:-20px
  }
  
  .login_item{
      margin-top:-60px;
      margin-right:25px;
  }
  
  .info_item_title{
    font-size:80%
  }
  
  .info_item_sub_text{
    font-size:60%
  }
  
  .info_grid{
    margin-left:-10%
  }
  
  .white_circle_3{
    width:280vw;
    height:320vw;
    left:-90vw;
    top:-90vw;
  }
  
  
  .cube_container_modal{
    margin-left:-62px
  }
  
  }
  
  
  @media only screen and (min-width: 0px) and (max-width: 380px) {
  .header_container{
      width:55%;
  }
  
  .header_menu{
    right:90px;
  }

  .black_circle{
    width:200vw;
    height:200vw;
  }

  .white_circle{
    width:200vw;
    height:200vw;
  }
  
  .menu_modal_container{
      margin-top:40%;
  }

  .downward_dome{
    width:180%;
    left:-45%;
  }
  
  }
  
  @media only screen and (min-width: 380px) and (max-width: 430px) {
  .header_container{
      width:65%;
  }
  
  .header_menu{
    right:90px;
  }

  .black_circle{
    width:190vw;
    height:190vw;
  }

  .white_circle{
    width:190vw;
    height:190vw;
  }
  
  .menu_modal_container{
      margin-top:40%;
  }
  
  .downward_dome{
    width:250%;
    left:-70%;
  }
  
  
  }
  
  @media only screen and (min-width: 430px) and (max-width: 576px) {
  
  .header_container{
    width:65%;
  }
  
  .login_item{
  margin-right:30px;
  }

      .menu_modal_grid{
  
  margin-left:3%;
      }
  
      .header_menu{
    right:90px;
  }

  .black_circle{
    width:180vw;
    height:180vw;
  }

  .white_circle{
    width:180vw;
    height:180vw;
  }
  
  .modal_info{
    margin-left:calc(100% + 200px);
    width:45%;
  }
    
  .info_item_title{
    font-size:90%
  }
  
  .info_item_sub_text{
    font-size:60%
  }

  .info_grid{
    margin-left:-10%
  }

  .menu_modal_container{
      margin-top:40%;
      margin-left:-5%
  }
  
  .downward_dome{
    width:250%;
    left:-70%;
  }
  
  }
  
  
  @media only screen and (min-width: 576px) and (max-width: 768px) {
  
  
  .header_container{
    width:82%;
  }
  
  
  
  .cube {
  width: 40px;
  height: 40px;
  position: relative;
  transform-style: preserve-3d;
  transform: rotateY(45deg);
  transition: transform 0.5s;
  margin-left:25px;
  margin-top:2px;
  }
  
  .cube {
  transform: translateY(180px);
  }
  
  .face {
  position: absolute;
  width: 40px;
  height: 40px;
  text-align: center;
  font-size: 50px;
  color: white;
  background-color: #000;
  border: #fff 1px solid;
  line-height: 40px;
  }
  
  .front {
  transform: translateZ(20px);;
  }
  
  
  .back {
  transform: rotateY(180deg) translateZ(20px);
  }
  
  .top {
  transform: rotateX(90deg) translateZ(20px);
  }
  
  .bottom {
  transform: rotateX(-90deg) translateZ(20px);
  }
  
  .left {
  transform: rotateY(-90deg) translateZ(20px);
  }
  
  .right {
  transform: rotateY(90deg) translateZ(20px);
  }
  
  .header_logo{
  width:40px;
  mix-blend-mode: difference;
  }
  
  
  
  
  .face_modal {
  position: absolute;
  width: 25px;
  height: 25px;
  text-align: center;
  font-size: 15px;
  color: white;
  background-color: #000;
  border: #fff 1px solid;
  line-height: 25px;
  }
  
  .front_modal {
  transform: translateZ(12.5px);;
  }
  
  
  .back_modal {
  transform: rotateY(180deg) translateZ(12.5px);
  }
  
  .top_modal {
  transform: rotateX(90deg) translateZ(12.5px);
  }
  
  .bottom_modal {
  transform: rotateX(-90deg) translateZ(12.5px);
  }
  
  .left_modal {
  transform: rotateY(-90deg) translateZ(12.5px);
  }
  
  .right_modal {
  transform: rotateY(90deg) translateZ(12.5px);
  }
  
  
  .header_logo_modal{
  width:15px;
  mix-blend-mode: difference;
  filter: invert(1);
  margin-top: 5px;
  }
  
  .header_menu_item{
  font-size: 15px;
  color: #fff;
  margin-top:-20px
  }
  
  .login_item{
  margin-top:-60px;
  margin-right:25px;
  }
  
  
  .info_item_title{
    font-size:100%
  }
  
  .info_item_sub_text{
    font-size:70%
  }
  
  .info_grid{
    margin-left:-10%
  }
  
  
  .black_circle{
    width:140vw;
    height:140vw;
  }

  .white_circle{
    width:140vw;
    height:140vw;
  }

  .modal_info{
    margin-left:calc(100% + 180px);
  }
  
  .menu_modal_container{
      margin-top:30%;
      margin-left:-5%
  }

  .downward_dome{
    width:250%;
    left:-70%;
  }
  
  
  }
  
  
  
  
  
  
  @media only screen and (min-width: 768px) and (max-width: 992px) {
  
  
  .header_container{
  width:92%;
  }
  
  
  
  .cube {
  width: 60px;
  height: 60px;
  position: relative;
  transform-style: preserve-3d;
  transform: rotateY(45deg);
  transition: transform 0.5s;
  margin-left:25px;
  margin-top:2px;
  }
  
  .cube {
  transform: translateY(180px);
  }
  
  .face {
  position: absolute;
  width: 60px;
  height: 60px;
  text-align: center;
  font-size: 50px;
  color: white;
  background-color: #000;
  border: #fff 1px solid;
  line-height: 60px;
  }
  
  .front {
  transform: translateZ(30px);;
  }
  
  
  .back {
  transform: rotateY(180deg) translateZ(30px);
  }
  
  .top {
  transform: rotateX(90deg) translateZ(30px);
  }
  
  .bottom {
  transform: rotateX(-90deg) translateZ(30px);
  }
  
  .left {
  transform: rotateY(-90deg) translateZ(30px);
  }
  
  .right {
  transform: rotateY(90deg) translateZ(30px);
  }
  
  .header_logo{
  width:60px;
  mix-blend-mode: difference;
  }
  
  
  
  
  .face_modal {
  position: absolute;
  width: 35px;
  height: 35px;
  text-align: center;
  font-size: 15px;
  color: white;
  background-color: #000;
  border: #fff 1px solid;
  line-height: 35px;
  }
  
  .front_modal {
  transform: translateZ(17.5px);;
  }
  
  
  .back_modal {
  transform: rotateY(180deg) translateZ(17.5px);
  }
  
  .top_modal {
  transform: rotateX(90deg) translateZ(17.5px);
  }
  
  .bottom_modal {
  transform: rotateX(-90deg) translateZ(17.5px);
  }
  
  .left_modal {
  transform: rotateY(-90deg) translateZ(17.5px);
  }
  
  .right_modal {
  transform: rotateY(90deg) translateZ(17.5px);
  }
  
  
  .header_logo_modal{
  width:25px;
  mix-blend-mode: difference;
  filter: invert(1);
  margin-top: 5px;
  }
  
  .header_menu_item{
  font-size: 20px;
  color: #fff;
  margin-top:-20px
  }
  
  .login_item{
  margin-top:-47.5px;
  margin-right:25px;
  }
  
  .info_item_title{
    font-size:100%
  }
  
  .info_item_sub_text{
    font-size:70%
  }
  
  .info_grid{
    margin-left:-10%
  }
  
  .black_circle{
    width:120vw;
    height:120vw;
  }

  .white_circle{
    width:120vw;
    height:120vw;
  }
  
  .modal_info{
    margin-left:calc(100% + 120px);
  }
  
  }
  
  
  
  @media only screen and (min-width: 992px) and (max-width: 1200px) {
  
      .header_container{
  width:95%;
  }
  .login_item{
  margin-top:-30px;
  margin-right:25px;
  
  }
  
  .info_item_title{
    font-size:100%
  }
  
  .info_item_sub_text{
    font-size:70%
  }
  
  .info_grid{
    margin-left:-10%
  }

  .black_circle{
    width:120vw;
    height:120vw;
  }

  .white_circle{
    width:120vw;
    height:120vw;
  }

  .modal_info{
    margin-left:calc(100% + 50px);
  }
  
  
  }

  
  @media only screen and (min-width: 1200px) and (max-width: 1400px) {
  
  .header_container{
  width:97%;
  }
  
  .login_item{
  margin-top:-30px;
  margin-right:25px;
  
  }
  
  .info_item_title{
    font-size:100%
  }
  
  .info_item_sub_text{
    font-size:70%
  }
  
  .info_grid{
    margin-left:-10%
  }
  
  
  
  }
  

  
  
  </style>