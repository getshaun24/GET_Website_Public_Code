<template>
    


<div :class="{width_size:is_mobile}" class="bottom_container">


    <div>
<h5 class="aim_text">3 Years.<br>
3 Times your investment. 
<br>
This is our aim.
</h5>
<p >
    Our goal is to bring these opportunities to the widest possible segment of the population, to make sure that isn’t more than just the top financial institutions and ultra-wealthy who are getting the opportunity to invest in promising pre-IPO companies. That said, in accordance with the SEC we may only open this investment to “Accredited” or “Qualified” investors.
</p>
</div>
<div>
<div class="button_container">
<FundPagesCompsMagneticButtonBig/>
</div>
<p>
    If you are accredited and see the value that GET and our growing roster of investors do, then let’s figure out how to bring you into the family.
</p>
</div>
</div>


</template>

<script setup>

import { useWindowSize } from '@vueuse/core'

const { width, height } = useWindowSize()

const is_mobile = ref(false)
if(width.value < 900){
is_mobile.value = true
} else{
    is_mobile.value = false
}

</script>

<style scoped>



.bottom_container{
    display:grid;
    grid-template-columns: repeat(2, 1fr);
    grid-template-rows: 1fr;
    grid-column-gap: 100px;
    grid-row-gap: 0px;
    width:90%;
    margin-left:5%;
    margin-top:5%;
    height:100%;
    padding-bottom:10%;
}

.button_container{
        margin-top:52%;
        margin-left:7.5%;
        z-index:1;
    }




@media only screen and (min-width: 0px) and (max-width: 380px) {
    .bottom_container{
    display:grid;
    grid-template-columns: 1fr;
    grid-template-rows: repeat(2, 1fr); 
    padding-bottom:0%;
    width:90% !important;
}

.button_container{
        margin-top:30%;
        margin-left:10%;
        z-index:1;;
        margin-bottom:20%
    }

    .width_size{
        width:90%;
        margin-left:2.5%
    }


}

@media only screen and (min-width: 380px) and (max-width: 430px) {
    .bottom_container{
    display:grid;
    grid-template-columns: 1fr;
    grid-template-rows: repeat(2, 1fr); 
    padding-bottom:0%;
    margin-bottom:-30%
}

.button_container{
        margin-top:15%;
        margin-left:10%;
        z-index:1;
        margin-bottom:20%
    }

    .width_size{
        width:80%;
        margin-left:2.5%
    }

}


    @media only screen and (min-width: 430px) and (max-width: 576px) {
        .bottom_container{
    display:grid;
    grid-template-columns: 1fr;
    grid-template-rows: repeat(2, 1fr); 
    padding-bottom:0%;
}

.button_container{
        margin-top:10%;
        margin-left:18%;
        z-index:1;
        margin-bottom:20%
    }

    .width_size{
        width:90%;
        margin-left:2.5%
    }

}

@media only screen and (min-width: 576px) and (max-width: 768px) {

    .bottom_container{
    display:grid;
    grid-template-columns: 1fr;
    grid-template-rows: repeat(2, 1fr); 
    padding-bottom:0%;
}

.button_container{
        margin-top:15%;
        margin-left:25%;
        z-index:1;
    }

    .aim_text{
    white-space: nowrap;
}




}

@media only screen and (min-width: 768px) and (max-width: 992px) {

    .button_container{
        margin-top:20%;
        margin-left:10%;
        z-index:1;
        margin-bottom:30%
    }

    .aim_text{
    white-space: nowrap;
}


}

@media only screen and (min-width: 992px) and (max-width: 1100px) {

.button_container{
    margin-top:40%;
    margin-left:-10%;
    z-index:1;
    margin-bottom:35%
}

.aim_text{
    white-space: nowrap;
}

}

@media only screen and (min-width: 1100px) and (max-width: 1200px) {

    .button_container{
        margin-top:35%;
        margin-left:5%;
        z-index:1;
        margin-bottom:30%
    }

    .aim_text{
    white-space: nowrap;
}

}

@media only screen and (min-width: 1200px) and (max-width: 1400px) {

    .aim_text{
    font-size:300%
}

.button_container{
        margin-top:32%;
        margin-left:7.5%;
        z-index:1;
        margin-bottom:30%
    }

    .aim_text{
    white-space: nowrap;
}



}

@media only screen and (min-width: 1400px) and (max-width: 1600px) {

    .button_container{
        margin-top:40%;
        margin-left:12.5%;
        z-index:1;
        margin-bottom:30%
    }

    .aim_text{
    white-space: nowrap;
}

}

@media only screen and (min-width: 1600px) and (max-width: 5600px) {

    .button_container{
        margin-top:25%;
        margin-left:17.5%;
        z-index:1;
        margin-bottom:30%
    }

    .aim_text{
    white-space: nowrap;
}

}

</style>