
<template>
    
    <div class="timer_container">
    <h6 class="countdown_timer">{{ finalTime }}</h6>
</div>

    <div class="flow_grid">

<div class="ball_container">
    <div :class="[current_num == 1 ? 'flow_ball_current' : 'flow_ball_done']">
        <p :class="[current_num > 1 ? 'ball_title_done' : 'ball_title']" >Basic Info</p>
    </div>
    <div class="flow_bar bar_1" :class="{flow_bar_start: flow_bar_start}"></div>
</div>
<div class="ball_container">
    <div :class="[current_num == 2 ? 'flow_ball_current' : current_num > 2 ? 'flow_ball_done' : 'flow_ball']">
        <p  :class="[current_num > 2 ? 'ball_title_done' : 'ball_title']">Investor Verification</p>
    </div>
    <div class="flow_bar bar_2" :class="{flow_bar_start: flow_bar_start}"></div>
</div>
<div class="ball_container">
    <div :class="[current_num == 3 ? 'flow_ball_current' : current_num > 3 ? 'flow_ball_done' : 'flow_ball']">
        <p  :class="[current_num > 3 ? 'ball_title_done' : 'ball_title']">KYC</p></div>
    <div class="flow_bar bar_3" :class="{flow_bar_start: flow_bar_start}"></div>
</div>
<div class="ball_container">
    <div :class="[current_num == 4 ? 'flow_ball_current' : current_num > 4 ? 'flow_ball_done' : 'flow_ball']">
        <p :class="[current_num > 4 ? 'ball_title_done' : 'ball_title']" >Agreements</p></div>
    <div class="flow_bar bar_4" :class="{flow_bar_start: flow_bar_start}"></div>
</div>

<div class="ball_container">
    <div class="flow_ball bar_5" :class="{flow_bar_start: flow_bar_start}">
        <p class="ball_title">Confirm & Transfer</p></div>
</div>


</div>



</template>


<script setup>


const props = defineProps(['current_num'])



// sleep time expects milliseconds
function sleep (time) {
  return new Promise((resolve) => setTimeout(resolve, time));
}



const flow_bar_start = ref(true)

onMounted(() => {


    sleep(700).then(() => {
        flow_bar_start.value = false
    });


})

function str_pad_left(string, pad, length) {
  return (new Array(length + 1).join(pad) + string).slice(-length);
}



const cookie_options = {default:()=> 1200, watch:true, maxAge:1800}
const cookie_options_remove = {default:()=> 0, watch:true, maxAge:1}
const timer_status = useCookie('timer_status', {default:()=> 'pre_start', watch:true, maxAge:1800})
const finalTime = ref('')
const minutes = ref()
const seconds = ref()
const timer_color = ref('rgb(25, 120, 237)')
const red_timer = ref(0)
// const milli_seconds =ref()

if(props.current_num == 2 || props.current_num == 4){
    timer_status.value = 'live'
}

if(props.current_num == 1 && timer_status.value == 'timed_out'){
    timer_color.value = 'rgb(0,0,0,0)'
    timer_status.value = 'pre_start'
}
if(props.current_num == 1 && timer_status.value == 'live'){
    timer_color.value = 'rgb(25, 120, 237)'
}


if (timer_status.value == 'live'){
const countdown_timer = useCookie('countdown_timer', cookie_options)
setInterval(() => {
  if (countdown_timer.value === 0) {
    if (red_timer.value != 1){
    countdown_timer.value = 600    
    timer_color.value = 'red'
    red_timer.value = 1
  } else {
    red_timer.value = 2
    timer_status.value = 'timed_out'
    countdown_timer.value = 0 
    countdown_timer.value = useCookie('countdown_timer', cookie_options_remove)  
  }      
  } else {
    countdown_timer.value--
  } 
    minutes.value = Math.floor(countdown_timer.value / 60);
    seconds.value = countdown_timer.value - minutes.value * 60;       
    // milli_seconds.value = countdown_timer.value - minutes.value * 60;       
    finalTime.value = str_pad_left(minutes.value, '0', 2) + ':' + str_pad_left(seconds.value, '0', 2);     
}, 1000)
} else{
    if (timer_status.value != 'pre_start'){
    timer_color.value = 'red'
    finalTime.value = "00:00"
    }
}



</script>





    <style scoped>

.timer_container{
    display:flex;
    justify-content: center;
    margin-bottom: 10%;
    margin-top:-2%
}
.countdown_timer{
    color:v-bind(timer_color);
    position: absolute;
    font-size:20px

}
    .flow_grid{
    display: grid;
    grid-template-columns: 1fr 1fr 1fr 1fr 1fr;
    grid-template-rows: 1fr;
    grid-column-gap: 0px;
    grid-row-gap: 0px;
    margin-left:5vw;
    margin-top:180px;
    width:90vw;
    position: relative;
}

.flow_ball{
    width:12vw;
    height:12vw;
    border-radius:50%;
    background-color:rgb(239, 239, 239);
    z-index:1;
}

.flow_bar{
    background-color:rgb(25, 120, 237);
    z-index:0;
    width:3vw;
    height:4px;
    margin-top:6vw;
    margin-left:2vw;
    margin-right:2vw;
}

.flow_ball_current{
    width:12vw;
    height:12vw;
    border-radius:50%;
    background-color:#fff;
    border: 3px solid rgb(25, 120, 237);
}

.flow_ball_done{
    width:12vw;
    height:12vw;
    border-radius:50%;
    background-color:rgb(25, 120, 237);
    z-index:1;
    color:#fff;
    mix-blend-mode: normal;
}


.ball_title{
    font-weight:600;
    position: absolute;
    text-align:center;
    display: flex;
  justify-content: center;
  align-items: center;
  font-size:2vw;
    width:12vw;
  height:8vw
}


.ball_title_done{
    font-size:2vw;
    font-weight:600;
    position: absolute;
    width:12vw;
    text-align:center;
    display: flex;
  justify-content: center;
  align-items: center;
  height:8vw;
  color:#fff;
  mix-blend-mode: normal;
}



.ball_container{
    display: grid;
grid-template-columns: repeat(2, 1fr);
grid-template-rows: 1fr;
grid-column-gap: 0px;
grid-row-gap: 0px;
}





.flow_bar_start{
    opacity:0;
    margin-left:-4vw;
    transform: rotate(45deg);
    transition: all 1.5s ease-in-out;
}

.bar_1{
    transition: all 1s ease-in-out .1s;
}

.bar_2{
    transition: all 1s ease-in-out .2s;
}

.bar_3{
    transition: all 1s ease-in-out .3s;
}

.bar_4{
    transition: all 1s ease-in-out .4s;
}

.bar_5{
    transition: all 1s ease-in-out .5s;
}





@media only screen and (min-width: 0px) and (max-width: 576px) {

    .flow_grid{
    margin-left:5vw;
    margin-top:120px;
}

.timer_container{
    display:flex;
    justify-content: center;
    margin-bottom: 10%;
    margin-top:-5%
}


}

@media only screen and (min-width: 576px) and (max-width: 768px) {

    .flow_grid{
    margin-left:5vw;
    margin-top:120px;
}


}

@media only screen and (min-width: 768px) and (max-width: 992px) {

    .flow_grid{
    margin-left:5vw;
    margin-top:120px;
}


}

@media only screen and (min-width: 992px) and (max-width: 1200px) {

  

}

@media only screen and (min-width: 1200px) and (max-width: 1400px) {
}

@media only screen and (min-width: 1400px) and (max-width: 1600px) {
}

@media only screen and (min-width: 1600px) and (max-width: 5600px) {
}

</style>
