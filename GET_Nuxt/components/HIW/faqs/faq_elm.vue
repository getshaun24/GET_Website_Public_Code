<template>
    
    <div class="faq_elm">
        <div class="toggle_container" @click="toggle_open">
            <div class="horizontal_line"></div>
            <div class="vertical_line" :class="{ vertical_line_hide: isOpen }"></div>
        </div>
        <h6 class="question">{{ question }}</h6>
        <div class="answer" :class="{ answer_open: isOpen , answer_open_height: isOpen}">{{ answer }}</div>
    </div>

</template>



<script setup>


const isOpen = ref(false)
const delayedOpen = ref(false)


function toggle_open() {
    isOpen.value = !isOpen.value
}




const props = defineProps(['question', 'answer'])


</script>

<style scoped>

.faq_elm{
    margin-bottom:5%;
    border-top: 1px solid rgba(101, 101, 101, 0.5);
}


.question{
    color:rgb(255, 255, 255);
    width:75%;
    margin-left:10%;
    font-size:20px;
    margin-top:5%;
    font-weight:500
}

.answer{
    color:#000;
    width:75%;
    margin-left:10%;
    line-height: .5;
    visibility: hidden;
    height:0px;
    opacity:0;
    margin-top:-2%;
    transition: all linear .3s;
}

.answer_open{
    visibility: visible;
    transition: all ease 1s;
    opacity:1;
    height:100%;
    line-height: 1.5;
    margin-top:0%
}


.toggle_container{
    margin-left:92%;
    margin-top:20px;
    margin-bottom:-100px;
    cursor:pointer;
    height:50px;
    width:50px;
    position: absolute;
}

.horizontal_line{
    width:30px;
    height:1px;
    background-color:#000;
    margin-left:10px;
    margin-top:25px
}

.vertical_line{
    width:1px;
    height:30px;
    background-color:#000;
    margin-left:25px;
    margin-top:-15px;
    transition:all ease 1s;
}

.vertical_line_hide{
    height:0px;
    transition:all ease 1s;
    transform: rotate(180deg);
}







@media only screen and (min-width: 0px) and (max-width: 576px) {
    .question{
    font-size:90%;
    margin-left:5%;
    width:80%;
}

.horizontal_line{
    width:20px;
    margin-left:6px;
    margin-top:3px
}

.vertical_line{
    height:20px;
    margin-left:16px;
    margin-top:-11px;
}

.answer{
    font-size:75%
}

.toggle_container{
    margin-left:88%;
    margin-top:18px;
    margin-bottom:-100px;
    cursor:pointer;
    height:50px;
    width:50px;
    position: absolute;
}


}

@media only screen and (min-width: 576px) and (max-width: 768px) {

    .question{
    font-size:90%;
}

.horizontal_line{
    width:20px;
    margin-left:6px;
    margin-top:3px
}

.vertical_line{
    height:20px;
    margin-left:16px;
    margin-top:-11px;
}

.answer{
    font-size:75%
}


}

@media only screen and (min-width: 768px) and (max-width: 992px) {

    .question{
    font-size:90%;
}

.horizontal_line{
    width:20px;
    margin-left:6px;
    margin-top:3px
}

.vertical_line{
    height:20px;
    margin-left:16px;
    margin-top:-11px;
}

.answer{
    font-size:75%
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