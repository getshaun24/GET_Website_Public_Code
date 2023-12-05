<template>

    <div style="z-index:-1;">
    <div class="placeholder_img" :style='{ backgroundImage: "url(" + image + ")", }'></div>
    <div class="landing_circle_box">
        <div class="landing_circle" data-lag=".2">
            <img class="circle_arrow" src="~/assets/content/homepage/right_arrow.png">
        </div>
    </div>
    
    
    
    
    
    
    <div class="landing">
    
    <div class="landing_image_container">
        <img data-speed="auto" class="landing_image" :src="image" />
    
        <div class="landing_info_container" data-lag="1" data-speed=".8">
    
            <div class="title_container">
                <div class="flex_inner">
            <h4 class="landing_title">{{ title }}</h4>
                </div>
            <div class="landing_title_line"></div>
        </div>
    
            <div class="invest_now_container">
                <p class="capacity_text">Previous Offering at Capacity</p>
            <FundPagesFundsNextAiReserveMagneticSmall/>
        </div>
    </div>
    
    
    </div>
    
    </div>
    
    </div>
    </template>
    
    <script setup>
    import { ref, watchEffect } from 'vue'
    import { useWindowScroll } from '@vueuse/core'
    import { useWindowSize } from '@vueuse/core'
    
    
     const props = defineProps(['title', 'title_color', 'text_align', 'line_width', 'line_margin', 'image', 'image_width', 'font_calc'])
    
    
    const landing_circle_scale = ref("150vw")
    const landing_circle_top = ref("0vh")
    const circle_color = ref("#fff")
    const landing_img_scale = ref(4)
    const info_margin = ref("-100vh")
    const info_opacity = ref(0)
    const border_color = ref("#000")
    const border_radius = ref("0%")
    const circle_box_opacity = ref(1)
    
    const placeholder_display = ref("block")
    const placeholder_opacity = ref(0)
    
    
    const { width, height } = useWindowSize()
    
    
    
            // sleep time expects milliseconds
            function sleep (time) {
              return new Promise((resolve) => setTimeout(resolve, time));
            }
    
            sleep(2).then(() => { 
    landing_img_scale.value = 4
    })
    
    
    
            sleep(10).then(() => { 
    
                landing_circle_scale.value = "80px"
                landing_circle_top.value = "50vh"
                circle_color.value = "#000"
                landing_img_scale.value = 1
                placeholder_opacity.value = 1
                info_opacity.value = 1;
                border_radius.value = "50%"
    
                if(width.value > 992){
                info_margin.value = "-15vh";
                }else if(width.value < 992 && width.value > 768){
                info_margin.value = "0vh";
                }
                else{
                    info_margin.value = "7vh";
                    circle_box_opacity.value = 0;
                }
            })
    
            sleep(1900).then(() => { 
            landing_circle_top.value = "80vh"
            border_color.value = "#fff"
    
            })
    
            sleep(2300).then(() => { 
                placeholder_opacity.value = 0
            })
    
        sleep(2500).then(() => { 
             placeholder_display.value = "none";
            })
    
    
    console.log(props.font_calc)
    
    </script>
    
    
    <style scoped>
    
    .capacity_text{
        text-align: left;
        color:#fff;
        font-weight: 900;
    }
    
    .placeholder_img{
        position: fixed;
        width: 100%;
        height: 100%;
        background-size: 100% 100vh;
        background-position: center;
        background-repeat: no-repeat;
        z-index:1000;
        transition: transform 1.5s ease-in-out, opacity .2s ease-in-out !important;
        top:0;
        left:0;
        opacity: v-bind(placeholder_opacity);
        display:v-bind(placeholder_display);
        transform: scale(v-bind(landing_img_scale)) !important;
        will-change: transform, opacity, blur;
    }
    
    
    .landing_circle_box{
        
        display: flex;
        align-items: center;
        justify-content: center;
        width:100%;
            z-index:10 !important;
            opacity: v-bind(circle_box_opacity);
            transition:all 3s ease-in-out;
    }
    .landing_circle{
        position:absolute;
        width:v-bind(landing_circle_scale);
        height:v-bind(landing_circle_scale);
        background-color:v-bind(circle_color);
        z-index:20 !important;
        top:v-bind(landing_circle_top);
        border-radius:v-bind(border_radius);
        border:1px solid v-bind(border_color);
        transition: width 1.5s cubic-bezier(0.16, 1.08, 0.38, 0.98), height 1.5s cubic-bezier(0.16, 1.08, 0.38, 0.98), top 2s cubic-bezier(0.16, 1.08, 0.38, 0.98) .5s, background-color 1.5s ease .1s, border 1.5s ease .25s;
    }
    
    .circle_arrow{
        width:25px;
        filter: invert(1);
        position: absolute;
        transform: rotate(90deg);
        top:26px;
        left:28px
    
    }
    
    
    .landing_image_container{
      position: relative;
     min-height: 100vh;
     width: 100%;
     overflow: hidden;
     align-items: center;
    justify-content: center;
    display: flex;
    transition:border-bottom-right-radius 30s ease-in-out, border-bottom-left-radius 30s ease-in-out;
    }
    
      /* Add non-firefox CSS code here */
    @supports not( -moz-appearance:none ){
      .landing_image_container:hover{
        border-bottom-right-radius: 100% 10%;
    border-bottom-left-radius: 100% 10%;
    }
    
    }
    
    
    
    .landing_image{
      position: absolute;
      width: 100%;
      transform: scale(v-bind(landing_img_scale)) !important;
      transition: all 1.5s ease-out;
      z-index:-10;
    }
    
    
    
    .landing_info_container{
        background-color:rgba(255, 255, 255, 0.25);
        width:850px;
        margin-top:v-bind(info_margin);
        opacity:v-bind(info_opacity);
        backdrop-filter: blur(15px) saturate(135%);
        -webkit-backdrop-filter: blur(15px) saturate(135%);
        -moz-backdrop-filter: blur(15px) saturate(135%);
        border-radius:20px;
        height:300px;
        display:grid;
        grid-template-columns: 1fr;
        grid-template-rows: repeat(2, 1fr);
        grid-column-gap: 0px;
        grid-row-gap: 0px;
        border: 1px solid rgba(255,255,255,0.2);
        box-shadow: 5px 5px 5px rgba(69, 159, 239, 0.05);
        z-index: 100;
        transition:margin-top 1s ease 1.8s, opacity 1s ease 1.8s;
        
    }
    
    .title_container{
        width:100%;
        /* display: flex; */
        /* justify-content: center */
    
    }
    
    .landing_title{
        color: v-bind(title_color);
        text-align:v-bind(text_align);
        line-height: 0;
        white-space: nowrap;
        mix-blend-mode: normal !important;
    }
    
    .landing_title_line{
        width:90%;
        height:3px;
        background-color:rgb(7, 51, 90);
        margin-top:-25px;
    }
    
    
        .invest_now_container{
            display:flex;
            justify-content:center;
            align-items:center;
            flex-direction: column;
            margin-top:-50px;
        }
    
    
    
    
    .flex_inner{
        display:flex;
        justify-content:center
    
    }
    
    
    
     @media only screen and (min-width: 0px) and (max-width: 430px) {
    
    .landing_info_container{
        width:80%;
        height:150px;
    }
    
    .landing_image_container{
      position: relative;
     min-height: 50vh;
     width: 100%;
     height:250%
    }
    
    .placeholder_img{
        width: 100%;
        min-height: 200vh;
        height: 200vh;
        background-size: 100% 50vh;
        background-color: rgba(0, 0, 0, 0.9);
        margin-top:-75vh;
        backdrop-filter: blur(15px) saturate(135%);
    }
    
    .landing_image{
      position: absolute;
      bottom: 0vh;
      width: 100%;
      height: 100%;
    }
    
    
    .landing_title{
        font-size:calc(200% * v-bind(font_calc));
        margin-top:12.5%;
        margin-left:-.5%;
    }
    
    .landing_title_line{
        width: 90%;
        margin-left: 5%;
        margin-top:-7%;
    }
    
    
    
    
    
    .placeholder_img{
    
        width: 100%;
        height: 100%;
        background-size: 200% 120vh;
    
    }

    .capacity_text{
        margin-top:20%
    }


    }
    
    
    
    @media only screen and (min-width: 430px) and (max-width: 576px) {
    .landing_info_container{
        width:80%;
        height:150px;
    }
    .landing_image_container{
      position: relative;
     min-height: 50vh;
     width: 100%;
     height:250%
    }
    
    .placeholder_img{
        width: 100%;
        min-height: 200vh;
        height: 200vh;
        background-size: 100% 50vh;
        background-color: rgba(0, 0, 0, 0.9);
        margin-top:-75vh;
        backdrop-filter: blur(15px) saturate(135%);
    }
    
    .landing_image{
      position: absolute;
      bottom: 0vh;
      width: 100%;
      height: 100%;
    }
    .landing_title{
        font-size:calc(225% * v-bind(font_calc));
        margin-top:12.5%;
        margin-left:-.5%;
    }
    .landing_title_line{
        width: 90%;
        margin-left: 5%;
        margin-top:-7%;
    }

    .capacity_text{
        margin-top:20%
    }


    }
    
    
    
    @media only screen and (min-width: 576px) and (max-width: 768px) {
    
    
    
    .landing_info_container{
        width:70%;
        height:175px;
    }
    
    .landing_image_container{
      position: relative;
     min-height: 65vh;
     width: 100%;
     height:250%
    }
    
    .landing_image{
      position: absolute;
      bottom: 0vh;
      width: 100%;
      height: 100%;
    }
    
    
    .landing_title{
        font-size:calc(300% * v-bind(font_calc));
        margin-top:9.5%;
        margin-left:-1%;
    }
    
    .landing_title_line{
        width: 90%;
        margin-left: 5%;
        margin-top:-6%;
    }
    
    .capacity_text{
        margin-top:15%
    }

    
    
    }
    
    @media only screen and (min-width: 768px) and (max-width: 992px) {
    
    
    
    .landing_info_container{
        width:60%;
        height:200px;
    }
    
    .landing_image_container{
      position: relative;
     min-height: 75vh;
     width: 100%;
     height:250%
    }
    
    .placeholder_img{
        width: 100%;
        min-height: 200vh;
        height: 200vh;
        background-size: 100% 75vh;
        background-color: rgba(0, 0, 0, 0.9);
        margin-top:-65vh;
        backdrop-filter: blur(15px) saturate(135%);
    }
    
    .landing_image{
      position: absolute;
      bottom: 0vh;
      width: 100%;
      height: 100%;
    }
    
    
    .landing_title{
        font-size:calc(300% * v-bind(font_calc));
        margin-top:9.5%;
        margin-left:-1%;
    }
    
    .landing_title_line{
        width: 90%;
        margin-left: 5%;
        margin-top:-5%;
    }
    

    
    
    }
    
    @media only screen and (min-width: 992px) and (max-width: 1200px) {
    
    
    .landing_info_container{
        width:60%;
        height:225px;
    }
    
    .landing_image_container{
      position: relative;
     width: 100%;
     height:200%;
    }
    
    
    .landing_image{
      position: absolute;
      bottom: 0vh;
      width: 100%;
      height: 100%;
    }
    
    
    .landing_title{
        font-size:calc(400% * v-bind(font_calc));
        margin-top:7.5%;
    }
    
    .landing_title_line{
        width: 90%;
        margin-left: 5%;
        margin-top:-5%;
    }
    

    }
    
    @media only screen and (min-width: 1200px) and (max-width: 1400px) {
    
        .landing_title{
        margin-top:7.5%;
    }
        .landing_title_line{
        width: 90%;
        margin-left: 5%;
        margin-top:-5%;
    }
    
    
    }
    
    @media only screen and (min-width: 1400px) and (max-width: 1600px) {
        .landing_title{
        margin-top:7.5%;
    }
        .landing_title_line{
        width: 90%;
        margin-left: 5%;
        margin-top:-4%;
    }
    
    
    }
    
    @media only screen and (min-width: 1600px) and (max-width: 5600px) {
    
        .landing_title{
        margin-top:7.5%;
    }
        .landing_title_line{
        width: 90%;
        margin-left: 5%;
        margin-top:-4%;
    }
    
    
    }
    
    
    
    
    
    
    
    
    
    
    </style>