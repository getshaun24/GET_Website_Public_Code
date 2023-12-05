<template>
    

    <div class="invest_dial_grid">



    <div class="container">

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 520" class="results__dial">
    <title>Investor Dial</title>
    <g class="results__dial-circles">
        <path ref="circOuter" class="results__dial-outer" d="M260,64c110.46,0,200,89.54,200,200S370.46,464,260,464,60,374.46,60,264,149.54,64,260,64" fill="none" stroke="#64d3de" stroke-miterlimit="10" opacity="0.6" />
        <path ref="circTrack" class="results__dial-track" d="M260,86A178,178,0,1,1,82,264,178,178,0,0,1,260,86" fill="none" :stroke="stroke_update_1" stroke-miterlimit="10" stroke-width="8" />
        <path ref="trackPerc" class="results__dial-track-perc" d="M260,86A178,178,0,1,1,82,264,178,178,0,0,1,260,86" fill="none" :stroke="stroke_update_2" stroke-miterlimit="10" stroke-width="8" />
    </g>
    <g class="results__dial-markers" fill="#64d3de">
        <rect ref="dial_marker_1" class="results__dial-marker" x="260" y="55" width="1" height="9" />
        <rect ref="dial_marker_2" class="results__dial-marker" x="260" y="55" width="1" height="9" />
        <rect ref="dial_marker_3" class="results__dial-marker" x="260" y="55" width="1" height="9" />
        <rect ref="dial_marker_4" class="results__dial-marker" x="260" y="55" width="1" height="9" />
        <rect ref="dial_marker_5" class="results__dial-marker" x="260" y="55" width="1" height="9" />
        <rect ref="dial_marker_6" class="results__dial-marker" x="260" y="55" width="1" height="9" />
    </g>
    <g class="results__dial-percent-text" fill="#64d3de" font-size="18">
        <text ref="dial_num_1" x="255" y="43.99">0%</text>
        <text ref="dial_num_2" x="395" y="95">1%</text>
        <text ref="dial_num_3" x="480" y="225">2%</text>
        <text ref="dial_num_4" x="445" y="375">3%</text>
        <!-- <text ref="dial_num_1" x="255" y="43.99">0%</text>
        <text ref="dial_num_2" x="388" y="86.99">10%</text>
        <text ref="dial_num_3" x="471" y="199.99">20%</text>
        <text ref="dial_num_4" x="470" y="340.99">30%</text>
        <text ref="dial_num_5" x="381" y="454.99">40%</text>
        <text ref="dial_num_6" x="250" y="495.99">50%</text>
        <text ref="dial_num_7" x="105" y="454.99">60%</text>
        <text ref="dial_num_8" x="20" y="340.99">70%</text>
        <text ref="dial_num_9" x="15" y="199.99">80%</text>
        <text ref="dial_num_10" x="105" y="86.99">90%</text>
        <text ref="dial_num_11" x="240" y="43.99">100%</text> -->
    </g>
    <g class="">
        <text class="results__dial-perc-text results__text" x="250" y="203.98" fill="rgb(0, 112, 149)">
            <tspan baseline-shift="super">$</tspan>
            <tspan fill="rgb(0, 112, 149)" class="results__dial-saving">
           {{ investment_amount.toString().replace(/\D/g, "").replace(/\B(?=(\d{3})+(?!\d))/g, ",") }}</tspan>
        </text>
        <text class="results__dial-effect results__text" x="185" y="236.67" font-size="16" fill="#64d3de">Investment Amount
            <tspan x="175" dy="24"></tspan>
        </text>
        <text ref="resultsText" class="results__dial-results results__text" text-anchor="middle" x="265" y="318" fill="#64d3de">
            <tspan ref="perc" class="results__dial-perc" text-anchor="start">{{ percentage }}</tspan>
            <tspan baseline-shift="super">%</tspan>
        </text>
    </g>
    <g  ref="drag" class="results__dial-drag" fill="rgb(0, 112, 149)">
        <g ref="dragInner" class="results__dial-drag-inner" >
            <circle ref="dragPadHit" class="results__dial-drag-hit" cx="260" cy="35" r="30" fill="white" opacity="0" />
            <circle ref="dragPad" class="results__dial-drag-pad" cx="260" cy="35" :r="scale_pad" />
            <g class="results__dial-drag-arrows" fill="white">
                <polygon points="266.73 38.66 266 37.96 268.55 35.48 266 33.01 266.73 32.3 270 35.48 266.73 38.66" />
                <polygon points="253.27 38.66 254 37.96 251.45 35.48 254 33.01 253.27 32.3 250 35.48 253.27 38.66" />
                <rect x="251" y="35" width="18" height="1" />
            </g>
        </g>
        <rect ref="dragLine" class="results__dial-drag-line" x="260" y="55" width="1" height="35" />
    </g>
</svg>


<div @click="update_max_rotation" class="ten_x" :class="{hide_it:!is_x}">10x</div>
<div @click="update_max_rotation" class="ten_x" :class="{hide_it:is_x}">1x</div>
</div>



<div class="invest_input_container">
<div class="input_wrap">
         <input @keyup="update_val" v-model="dynamic_investment_amount"  class="input_white invest_input_mod" placeholder=' ' required/>
         <label class="label_white invest_place_mod">Enter desired investment amount</label>
 </div>
 <p class="multiple_of_text" :class="{hide_it:!show_multiple_of}">Must be a multiple of $1000</p>
</div>  
</div>  

</template>




<script setup>


        import { gsap } from 'gsap'
         import { Draggable } from 'gsap/Draggable'
        import { DrawSVGPlugin } from 'gsap/DrawSVGPlugin';
        //import { DrawSVGPlugin } from "gsap/dist/DrawSVGPlugin";
         import { InertiaPlugin } from 'gsap/InertiaPlugin';
         import { useScrollLock } from '@vueuse/core'

         const cookie_options = {default:()=> '', watch:true, maxAge:1800}


    //  gsap.registerPlugin(DrawSVGPlugin, Draggable);

    if (process.client) {
  gsap.registerPlugin(DrawSVGPlugin, Draggable, InertiaPlugin);
}
/*  ==========================================================================
    Dial
    ========================================================================== */

            // sleep time expects milliseconds
            function sleep (time) {
          return new Promise((resolve) => setTimeout(resolve, time));
        }







const stroke_update_1 = ref('#50afb8')
const stroke_update_2 = ref('rgb(0, 112, 149)')



const show_multiple_of = ref(false)

const investment_amount = useCookie('investment_amount', cookie_options)
const snap_value = ref(10);
const is_x = ref(true)
const x_amount = ref(100) 
const circOuter = ref('circOuter')
const circTrack = ref('circTrack')
const trackPerc = ref('trackPerc')
const track_update = ref(0)


const dial_marker_1 = ref('dial_marker_1')
const dial_marker_2 = ref('dial_marker_2')
const dial_marker_3 = ref('dial_marker_3')
const dial_marker_4 = ref('dial_marker_4')
const dial_marker_5 = ref('dial_marker_5')
const dial_marker_6 = ref('dial_marker_6')

const dial_num_1 = ref('dial_num_1')
const dial_num_2 = ref('dial_num_2')
const dial_num_3 = ref('dial_num_3')
const dial_num_4 = ref('dial_num_4')
const dial_num_5 = ref('dial_num_5')
const dial_num_6 = ref('dial_num_6')

const drag = ref('drag')
const dragPad = ref('dragPad')
const dragPadHit = ref('dragPadHit')
const dragLine = ref('dragLine')
const dragInner = ref('dragInner')
const resultsText = ref('resultsText')


const dialTL = gsap.timeline();

const dial_marker_array = [dial_marker_1, dial_marker_2, dial_marker_3, dial_marker_4, dial_marker_5, dial_marker_6]
const dial_num_array = [dial_num_1, dial_num_2, dial_num_3, dial_num_4, dial_num_5, dial_num_6]

const val = ref();
const percentage = ref();

const drag_it = ref();

const touch_action = ref('auto')



const dynamic_investment_amount = ref('')

//  Show value in input when user returns to page
onMounted(() => {
    if (investment_amount.value != ''){
    dynamic_investment_amount.value = '$' + investment_amount.value.toString().replace(/\D/g, "").replace(/\B(?=(\d{3})+(?!\d))/g, ",");}

})


// single ref
watch(dynamic_investment_amount, (new_dynamic_investment_amount) => {
    percentage.value = ((new_dynamic_investment_amount.replace(/[^0-9]/g, '') / 2000000) * 100).toFixed(2);
})



const input_update_count = ref(0)

const scale_pad = ref(20)



function update_max_rotation(){
    if (is_x.value == true){
        x_amount.value = 1000
        is_x.value = false
        investment_amount.value = investment_amount.value * 10
        percentage.value = percentage.value * 10
        if(investment_amount.value > 2000000){
            investment_amount.value = 2000000
            percentage.value = 100
        }
        snap_value.value = 10
        dynamic_investment_amount.value = '$' + investment_amount.value.toString().replace(/\D/g, "").replace(/\B(?=(\d{3})+(?!\d))/g, ",");
    } else {
        x_amount.value = 100
        is_x.value = true
        investment_amount.value = investment_amount.value / 10
        if(investment_amount.value > 2000000){
            investment_amount.value = 2000000
            percentage.value = 100
        }
        percentage.value = percentage.value / 10
        dynamic_investment_amount.value = '$' + investment_amount.value.toString().replace(/\D/g, "").replace(/\B(?=(\d{3})+(?!\d))/g, ",");
    }
}





function update_val(){
    dynamic_investment_amount.value = '$' + dynamic_investment_amount.value.toString().replace(/\D/g, "").replace(/\B(?=(\d{3})+(?!\d))/g, ",");

    investment_amount.value = dynamic_investment_amount.value.replace(/[^0-9]/g, '');


    val.value = investment_amount.value / x_amount.value


    gsap.to(drag.value, {
        duration: 5,
		rotation: val.value,
        ease: "power3.inOut",
	});
    gsap.to(trackPerc.value, {
		drawSVG: track_update.value + "% " + ((val.value / 180) * 100) / 2 + "%",
        duration: 5,
        ease: "power3.inOut",
        onUpdate: update_strokes()
	});

    sleep(2000).then(() => { 
    if (investment_amount.value % 1000 !== 0){
        show_multiple_of.value = true
    } else{
        show_multiple_of.value = false
    }
});
}






onMounted(() => {



gsap.set(".results__dial", {
	visibility: "visible"
});

gsap.set([trackPerc.value, circOuter.value, circTrack.value], {
	transformOrigin: "50% 50%",
	drawSVG: "0% 0%"
});

gsap.set(drag.value, {
	transformOrigin: "50% 259", // set rotationY to the center of the dial
	rotation: 0
});

gsap.set(dial_marker_array.value, {
	transformOrigin: "50% 209" // set rotationY to the center of the dial
	// rotation: 0
});


dialTL
	.to(circTrack.value, {
        duration: 0.8,
		drawSVG: "0% 100%",
		ease: "power4.inOut"
	})

	.to(
		circOuter.value,{
            duration: 0.8,
			drawSVG: "0% 100%",
			ease: "power3.inOut"
		},
		"-=0.6"
	)

	.from(
		dial_marker_array.value,
		{
            duration: 0.8,
			cycle: {
				rotation: function (i) {
					return 180 - 36 * i;
				}
			},
			ease: "power2.inOut"
		},
		0.1,
		"-=0.4"
	)

	.from(
		dial_num_array.value,
		{
            duration: 0.8,
			autoAlpha: 0,
			x: 20,
			ease: "power2.inOut"
		},
		0.1,
		"-=0.6"
	)

	.from(
		dragLine.value,
		{
            duration: 0.3,
			scaleY: 0,
			transformOrigin: "0% 100%",
			ease: "power2.inOut"
		},
		"-=1.2"
	)

	.from(
		dragInner.value,
		{
            duration: 0.5,
			scale: 0,
			y: 20,
			transformOrigin: "center center",
			ease: "elastic(0.9, 0.3)" 
		},
		"-=0.9"
	)

	.from(
		resultsText.value,
		{
            duration: 0.8,
			autoAlpha: 0,
			y: 20,
			ease: "power2"
		},
		0.1,
		"-=1.4"
	)

	.to(
		trackPerc.value,
		{
            duration: 0.8,
			drawSVG: "0% 10%", // animate to the default 10%
			ease:"power4.inOut"
		},
		"-=0.4"
	)

	.to(
		drag.value,
		{
            duration: 3,
			rotation: 36, // animate to the default 10%
			ease: "power4.inOut",
            drawSVG: "0% " + ((val.value / 180) * 100) / 2 + "%"
		},
		"-=1.0"
	);






drag_it.value = Draggable.create(drag.value, {
	type: "rotation",
	inertia: true,
	 bounds: { maxRotation: 20000, minRotation: 0 },
	snap: function (endValue) {
		return Math.round(endValue / 10) * 10;
	},
    onDrag:drag_algo,
    onThrowUpdate: drag_algo,
    // onDragEnd: pad_scale,
    onThrowComplete: pad_scale,

})

function pad_scale(){scale_pad.value = 20;     touch_action.value = 'auto'}

function drag_algo(){
    touch_action.value = 'none'
    scale_pad.value = 28

    if (is_x.value == true){
        this.applyBounds({ maxRotation: 20000, minRotation: 0 });
                val.value = 20000
            } else {
                this.applyBounds({ maxRotation: 0, minRotation: 2000 });
                val.value = 2000
            }

    if(investment_amount.value > 2000000){
            // drag_it.endDrag();
            investment_amount.value = 2000000
            percentage.value = 100
    } else{
        val.value = gsap.getProperty(drag.value, "rotation")
	investment_amount.value = Math.round(x_amount.value * val.value);
    percentage.value = ((investment_amount.value / 2000000) * 100).toFixed(2);
    update_strokes()
    gsap.set(trackPerc.value, {
		drawSVG: track_update.value + "% " + ((val.value / 180) * 100) / 2 + "%"
	});
    dynamic_investment_amount.value = '$' + investment_amount.value.toString().replace(/\D/g, "").replace(/\B(?=(\d{3})+(?!\d))/g, ",");
    show_multiple_of.value = false

}}

})









function update_strokes(){
    if (val.value < 360){
        track_update.value = 0
        stroke_update_1.value = '#0054ff'
    stroke_update_2.value = '#008dff'
    }
    if (val.value > 360){
        track_update.value = 100
    stroke_update_1.value = '#008dff' 
    stroke_update_2.value = '#00b4ff'
    }
    if (val.value > 720){
        track_update.value = 200
    stroke_update_1.value = '#00b4ff' 
    stroke_update_2.value = '#0054ff'
    }
    if (val.value > 1080){
        track_update.value = 300
    stroke_update_1.value = '#0054ff' 
    stroke_update_2.value = '#008dff'
    }
    if (val.value > 1440){
        track_update.value = 400
    stroke_update_1.value = '#008dff'
    stroke_update_2.value = '#00b4ff'
    }
    if (val.value > 1800){
        track_update.value = 500
    stroke_update_1.value = '#00b4ff'
    stroke_update_2.value = '#00d2f4' 
    }
    if (val.value > 1800 + 360){
        track_update.value = 600
    stroke_update_1.value = '#00d2f4'
    stroke_update_2.value = '#00eba6'
    }
    if (val.value > 1800 + 720){
        track_update.value = 700
    stroke_update_1.value = '#00eba6' 
    stroke_update_2.value = '#0afd4f'
    }
    if (val.value > 1800 + 1080){
        track_update.value = 800
    stroke_update_2.value = '#0afd4f' 
    stroke_update_1.value = '#50afb8'
    }
    if (val.value > 1800 + 1800){
        track_update.value = 900
    stroke_update_1.value = 'rgb(0, 112, 149)' 
    stroke_update_2.value = '#50afb8'
    }
    if (val.value > 1800 + 1800 + 360){
        track_update.value = 1000
    stroke_update_2.value = 'rgb(0, 112, 149)' 
    stroke_update_1.value = '#50afb8'
    }
    if (val.value > 1800 + 1800 + 720){
        track_update.value = 1100
    stroke_update_1.value = 'rgb(0, 112, 149)' 
    stroke_update_2.value = '#50afb8'
    }
    if (val.value > 1800 + 1800 + 1080){
        track_update.value = 1200
    stroke_update_2.value = 'rgb(0, 112, 149)' 
    stroke_update_1.value = '#50afb8'
    }
    if (val.value > 1800 + 1800 + 1800){
        track_update.value = 1300
    stroke_update_1.value = 'rgb(0, 112, 149)' 
    stroke_update_2.value = '#50afb8'
    }

}





</script>












<style scoped>




.hide_it{
    display:none;
}

/*  ==========================================================================
    General
    ========================================================================== */


.invest_dial_grid{
    display: grid;
grid-template-columns: repeat(2, 1fr);
margin-left: 6%;
}


.invest_input_container{
    margin-top: 35%;
    margin-left: -5%;
    width: 60%;
}



/* .invest_input_mod{
font-size:7vw;
height:7vw;
font-weight: 100;
} */


.multiple_of_text{
    font-size:15px;
    color:rgb(181, 51, 12);
    margin-left:10%
}


    .container {
  position: relative;
  margin-top: 10%;
  margin-left: 5%;
  width: 40vw;
  height: 40vw;
}


.ten_x {
  font-size:25px;
  background-color: rgb(0, 112, 149);
  padding:10px 20px;
  border-radius: 50px;
  width:50px;
  color:#fff;
  text-align: center;
  margin-left:5%;
  margin-top:-10%;
  cursor: pointer;
}



/*  ==========================================================================
   Variables etc
   ========================================================================== */
.results__dial-percent-text text, body {
  font-style: normal;
  font-weight: 400;
}

.results__dial-saving, .results__dial-perc, .results__dial-perc-text,
.results__dial-results {
  font-style: normal;
  font-weight: 700;
}

/*  ==========================================================================
    Dial
    ========================================================================== */
.results__dial {
  visibility: hidden;
}
.results__dial text,
.results__dial tspan {
  -webkit-user-select: none;
     -moz-user-select: none;
      -ms-user-select: none;
          user-select: none;
}

/*  Percentage Markers
    ========================================================================== */
.results__dial-percent-text text {
  -webkit-font-smoothing: subpixel-antialiased;
}

/*  Text
    ========================================================================== */
.results__dial-perc-text,
.results__dial-results {
  font-feature-settings: "tnum" 1;
  text-anchor: middle;
}

.results__dial-perc-text,
.results__dial-results {
  font-size: 24px;
}

.results__dial-perc {
  text-anchor: middle;
  font-size: 48px;
  -webkit-font-smoothing: subpixel-antialiased;
}

.results__dial-saving {
  font-size: 48px;
  -webkit-font-smoothing: subpixel-antialiased;
}

/*  Dragger
    ========================================================================== */
.results__dial-drag-arrows,
.results__dial-drag-pad {
  pointer-events: none;
  transition: all .25s ease;
}

.results__dial-drag-hit {
  cursor: pointer;
  transition: all .25s ease;
}








@media only screen and (min-width: 0px) and (max-width: 380px) {

    .invest_dial_grid{
    display: grid;
grid-template-columns: repeat(1, 1fr);
grid-template-rows: repeat(2, 1fr);
margin-left: 6%;
margin-bottom:-40%
}

.container {
  position: relative;
  margin-top: 0%;
  margin-left: 2%;
  width: 80vw;
  height: 80vw;
}

.ten_x {
  font-size:18px;
  background-color: rgb(0, 112, 149);
  padding:5px 20px;
  width:60px;
  margin-left:75%;
  margin-top: 8%;
}

.invest_input_container{
    margin-top: 5%;
    margin-left: -5%;
    width: 60%;
}


}


@media only screen and (min-width: 380px) and (max-width: 576px) {


    .invest_dial_grid{
    display: grid;
grid-template-columns: repeat(1, 1fr);
grid-template-rows: repeat(2, 1fr);
margin-left: 6%;
margin-bottom:-55%
}

.container {
  position: relative;
  margin-top: 0%;
  margin-left: 2%;
  width: 80vw;
  height: 80vw;
}

.ten_x {
  font-size:18px;
  background-color: rgb(0, 112, 149);
  padding:5px 20px;
  width:60px;
  margin-left:75%;
  margin-top: 8%;
}

.invest_input_container{
    margin-top: 5%;
    margin-left: -5%;
    width: 60%;
}


    
}




@media only screen and (min-width: 380px) and (max-width: 576px) {

    html{
    touch-action: v-bind(touch_action);
}

body{
    touch-action: v-bind(touch_action);
}
}

/* 

@media only screen and (min-width: 576px) and (max-width: 768px) {
}

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














