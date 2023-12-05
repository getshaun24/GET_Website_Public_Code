<template>

<div>

<Header/>

<GSAPScrollSmoother>


<div ref="top_line" class="top_line"></div>

    <div class="contact_img_container">
<img ref="contact_image" class="contact_img" src="~/assets/content/contact/map.jpg">
</div>


<div class="form_container_desktop">
<div class="grid_container">

    <div class="col_1">
        <h4 class="content_title">Contact</h4>
    </div>
    <div class="col_2">
        <h6 class="form_title">Talk to Us. We Can Help.</h6>

        <div class="form_input_container">
        <input type="text" class="form_input" v-model="first_name" placeholder="First Name">
        <input type="text" class="form_input" v-model="contact_email" placeholder="Email">
    </div>
    </div>
    <div class="col_3">

        <div class="form_input_container">
        <input type="text" class="form_input" v-model="last_name" placeholder="Last Name">
        <div>
        <input ref="phone_focused" @keyup="remove_chrs" @keypress="onPhoneKeyPress" maxlength="17" type="text" class="form_input" v-model="phone" placeholder="Phone">
        <span v-if="show_international" class="international_toggle" @click="international_toggle"> {{ inter_text }}</span>
        </div>
    </div>

        <div class="left_box_line"></div>

</div>


    <div class="col_4">
        <div class="contact_info">
    <p class="contact_elm">212-328-9178</p>
    <p class="contact_elm">Johnnie Dodds Blvd. #103-224, Mount Pleasant, SC 29464</p>
<p class="contact_elm">support@thisisget.com</p>
</div>

    </div>
</div>

<textarea class="form_input_area" placeholder="Message" v-model="message" ></textarea>

<button @click="submit_contact_message" class="submit_button">Submit</button>

</div>




<div class="mobile_grid">

    <h3 class="content_title">Contact</h3>


        <p class="form_title">Talk to Us. We Can Help.</p>

     
    <div class="mobile_form_background">

        <div class="form_input_container">
        <input type="text" class="form_input" v-model="first_name" placeholder="First Name">
        <input type="text" class="form_input" v-model="last_name" placeholder="Last Name">
        <input type="text" class="form_input" v-model="contact_email" placeholder="Email">
        <input ref="phone_focused" @keyup="remove_chrs" @keypress="onPhoneKeyPress" maxlength="17"  type="text" class="form_input" v-model="phone" placeholder="Phone">
        <span v-if="show_international" class="international_toggle" @click="international_toggle"> {{ inter_text }}</span>
        <textarea class="form_input_area" placeholder="Message" v-model="message" ></textarea>

        <button @click="submit_contact_message" class="submit_button">Submit</button>
    </div>

    <div class="contact_info">
    <p class="contact_elm">212-328-9178</p>
    <p class="contact_elm">Johnnie Dodds Blvd. #103-224, Mount Pleasant, SC 29464</p>
    <p class="contact_elm">support@thisisget.com</p>
    </div>




    </div>


</div>







<div class="scrub_container">
<ScrubText v-bind="scrub_text_1"/>
</div>



<div ref="map_button" class="map_button"></div>

<div class="body_video">
    <h1 class="contact_message">Welcome To The Family</h1>
    <div class="video_overlay"></div>
    <video class="contact_video" autoplay muted playsinline loop>
                <source src="../assets/content/homepage/home_333.mp4" type="video/mp4">
            </video>
</div>

<div style="background-color:#000; z-index:10">
<Footer/>
</div>

</GSAPScrollSmoother>


</div>

</template>


<script setup>

        const config = useRuntimeConfig()
        
        const scrub_text_1 = {text:"Let's Talk", duration:100}

        const first_name = ref('')
        const last_name = ref('')
        const contact_email = ref('')
        const phone = ref('')
        const message = ref('')


        function submit_contact_message (){

            if (first_name.value == '' || last_name.value == '' || contact_email.value == '' || phone.value == '' || message.value == ''){
                alert('Please fill out all fields')
                return
            }


            fetch(`${config.flask_url}/api/contact_and_subscribe/`, {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({first_name:first_name.value, last_name:last_name.value, contact_email:contact_email.value, phone:phone.value, message:message.value})
    })
    .then((response) => response.json())
    .then((data) => {


        if (data.status == 'success_contact_sent') {
            alert(data.message)
        } else {
            alert(data.message)
        }

    })
    .catch(error => {
        alert('Error')
        start_loader.value = false;
        console.error('There was an error!', error);
    });



        }






        function onPhoneKeyPress(e) {
    const key = e.keyCode || e.charCode;
    const len_phone = phone.value.length

    if (!is_international.value){
    if (key !== 8 || key !==  46) {
    if(len_phone == 12){
        phone.value = phone.value + '-'
        }
    else if (len_phone == 7){   
        phone.value = phone.value + ') '
        }
    else if (len_phone == 0){   
        phone.value = '+1 ('
        }}

    }else{
        if (len_phone == 0){   
        phone.value = '+'
        }
}



}

function remove_chrs() {
    phone.value = phone.value.toString().replace(/[^0-9-()-+ ]/g, '');
}




const is_international = ref(false)
const is_international_color = ref('#1b91ebb3')
const inter_text = ref('International ?')
const inter_margin = ref('-32%')
const show_international = ref(false)


function international_toggle() {
    is_international.value = !is_international.value
    if (is_international.value) {
        is_international_color.value = '#06ae46'
        phone.value = '+' + phone.value.toString().replace(/[^0-9]/g, '').substring(1);
        inter_text.value = 'U.S. ?'
        phone_focused.value.focus()
        sleep(1110).then(() => {show_international.value = true})
        sleep(800).then(() => { inter_opacity.value = 1, inter_margin.value = '-27%' })
} else{
        is_international_color.value = '#1b91ebb3'
        phone.value = '+1 ('
        inter_text.value = 'International ?'
        phone_focused.value.focus()
        sleep(1110).then(() => {show_international.value = true})
        sleep(800).then(() => { inter_opacity.value = 1, inter_margin.value = '-32%' })
}
}


const inter_opacity = ref(1)
const phone_focused = ref()
const { focused } = useFocus(phone_focused)

watch(focused, (focused) => {
  if (focused) {
    show_international.value = true
    sleep(10).then(() => { inter_opacity.value = 1, inter_margin.value = '-27%' })
  }
  else{
    sleep(1100).then(() => {show_international.value = false})
    sleep(800).then(() => { inter_opacity.value = 0, inter_margin.value = '-32%' })
  }
})

    
      

</script>




<style scoped>



.grid_container{
    display: grid;
    grid-template-columns: 1fr 1fr 1fr 1fr;
    grid-template-rows: 1fr 1fr 1fr 1fr;
    grid-template-areas: 
    "col_1 col_2 col_3 col_4"
    "col_1 col_2 col_3 col_4"
    "col_1 col_2 col_3 col_4"
    "col_1 col_2 col_3 col_4";
    width: 100vw;
    z-index:1;
    position:absolute;
    top:0

}

.col_1{
    grid-area: col_1;
    background-color: #181818;
    border:rgba(255, 255, 255, 0.15) solid 1px;
    height:144vh;
}

.col_2{
    grid-area: col_2;
    background-color: #181818;
    border:rgba(255, 255, 255, 0.15) solid 1px;
    height:120vh;
    border-right:0;
    border-left:0
}

.col_3{
    grid-area: col_3;
    background-color: #181818;
    border:rgba(255, 255, 255, 0.15) solid 1px;
    border-left: 0px;
    height:132vh
}

.col_4{
    grid-area: col_4;
    background-color: #18181800;
}

.left_box_line{
    border:rgba(255, 255, 255, 0.15) solid 1px;
    height:12vh;
    border-right:rgba(255, 255, 255, 0) solid 1px;
    border-top:rgba(255, 255, 255, 0) solid 1px;
    border-bottom:rgba(255, 255, 255, 0) solid 1px;
    position:absolute;
    bottom:12vh
}

.contact_img_container{
  position: absolute;
 height: 100vh;
 width: 100%;
 object-fit: cover;
 top:0;
 z-index:-2
}
.contact_img{
  position: absolute;
  height: 70vw;
  top:0;
  left:-35%;
  object-fit: cover;
  object-position: center;
  z-index:-1
}

.top_line{
    height:120px;
    border-bottom:rgba(255, 255, 255, 0.15) solid 1px;
    z-index:10
}

.content_title{
    margin-top:12.5%;
    margin-left:2.5%;
    position:absolute;
    font-size:250%
}

.form_title{
    margin-top:22%;
    margin-left:2%;
    position:absolute;
    font-size:170%
}

.form_input{
    border-bottom:#fff solid 1px;
    margin-top:25%;
    color:#fff;
    padding:10px;
    margin-left:8%;
    background-color: #18181800;
    width:75%;
    margin-right: 25px;
}

.form_input_container{
    margin-top:95%;
    position:relative;
}

.form_input_area{
    border-bottom:#fff solid 1px;
    margin-top:27%;
    color:#fff;
    padding:10px;
    margin-left:27%;
    background-color: #18181800;
    width:45%;
    height:75px;
    position:absolute;
    border:none;
    border-bottom:#fff solid 1px;
    z-index:10
}

.submit_button{
    background-color: #fff;
    border-bottom:#fff solid 1px;
    margin-top:40%;
    color:rgb(0, 0, 0);
    padding:10px;
    margin-left:27.5%;
    font-size:25px;
    background-color: #18181800;
    width:45%;
    height:100px;
    position:absolute;
    border:none;
    border-bottom:#fff solid 1px;
    background-color: #fff;
    cursor:pointer;
    z-index:10
}

.submit_button:hover{
    color:#fff;
    border: #fff solid 1px;
    background-color: #181818;
    transition: all 0.5s ease;
}

.body_video{
    height:100vh;
    background-color: rgb(0, 0, 0);
    margin-top:115%;
    z-index:100;
    position:relative;
    width:100%;
    overflow:hidden;

}


.map_button{
    height:80px;
    background-color: rgb(35, 161, 245);
    margin-top:-52%;
    z-index:100;
    position:absolute;
    width:80px;
    margin-left:49%;
    border-radius:100%;
    z-index:-1;
}



.contact_video{
    width:55%;
    margin-left:22.5%;
    margin-top:7.5%
}

.video_overlay{
    width:100%;
    height:100vh;
    margin-top:0%;
    background-color: rgb(0, 0, 0);
    opacity:0.85;
    position:absolute;
    z-index:10;
    top:0;
    left:0
}

.contact_message{
    margin-top:35%;
    font-size:7vw;
    position:absolute;
    color:#fff;
    z-index:100;
    text-align: center;
    width:100%
}

.contact_info{
    margin-top:400px;
    width:75%;
    margin-left:12.5%;
    }



.scrub_container{
    margin-top:20%
}


.international_toggle{
    font-size:10%;
    color: v-bind(is_international_color);
    margin-left:v-bind(inter_margin);
    padding:0px 5px 5px 5px;
    margin-top:38.5%;
    word-spacing: .05rem;
    cursor:pointer;
    position:absolute;
    opacity:v-bind(inter_opacity);
    z-index: 1000;
    transition: all .5s ease-in-out;
}










@media only screen and (min-width: 0px) and (max-width: 576px) {


    .international_toggle{
    margin-top:11.5%;
}



    .grid_container{
        display:none
    }

    .form_container_desktop{
        display:none
    }


.contact_img{
  height: 180vw;
  left:-165%;
}

.map_button{
    height:50px;
    width:50px;
    margin-left:50%;
}

.mobile_form_background{
    background-color: #181818;
    height: 80vh;
    min-height: 510px;
    position: absolute;
    top:0;
    width:60%;
    z-index:1
}

.top_line{
    height:70px;
    background-color: #181818;
    z-index:50
}

.scrub_container{
    margin-top:40%;
    z-index:0
}

.content_title{
    margin-top:-25px;
    margin-left:30px;
    font-size:25px;
    position:absolute;
    z-index:10
}

.form_title{
    margin-top:20px;
    margin-left:30px;
    z-index:2;
    font-size:14px
}

.form_input_container{
    margin-top:195px;
    position:relative;
    z-index:2;
}


.form_input{
    margin-top:20px;
    padding:10px;
    margin-left:25px;
    font-size:10px;
    width:70%
}

.form_input_area{
    margin-top:70px;
    margin-left:-87.5%;
    font-size:10px;
    width:70%;
    height:20px;
}


.submit_button{
    margin-top:150px;
    margin-left:-85%;
    font-size:11px;
    width:40%;
    height:30px;
    border-radius:50px
}

.contact_info{
    margin-top:-190px;
    width:50%;
    margin-left:110%;
    }


.contact_elm{
    font-size:12px
}


.body_video{
    height:50vh;

}

.contact_video{
    margin-top:5%
}


.contact_message{
    margin-top:130px;
}

}

@media only screen and (min-width: 0px) and (max-width: 390px) {
.form_input_area{
    margin-top:50px;
    margin-left:10%;
    font-size:10px;
    width:70%;
    height:20px;
}

.submit_button{
    margin-top:120px;
    margin-left:10%;
    font-size:11px;
    width:40%;
    height:30px;
    border-radius:50px
}

.international_toggle{
    margin-top:4%;
    margin-left: 57%;
}


}

@media only screen and (min-width: 576px) and (max-width: 675px) {
.form_input_area{
    margin-top:70px;
    margin-left:-82.5%;
    font-size:10px;
    width:70%;
    height:20px;
}

}

@media only screen and (min-width: 675px) and (max-width: 768px) {
.form_input_area{
    margin-top:70px;
    margin-left:-80%;
    font-size:10px;
    width:70%;
    height:20px;
}

}

@media only screen and (min-width: 576px) and (max-width: 768px) {
  
    .international_toggle{
    margin-top:8%;
}


    .grid_container{
        display:none
    }

    .form_container_desktop{
        display:none
    }

.contact_img{
  height: 150vw;
  left:-125%;
}

.map_button{
    height:50px;
    width:50px;
    margin-left:57%;
}

.mobile_form_background{
    background-color: #181818;
    height: 80vh;
    min-height: 530px;
    position: absolute;
    top:0;
    width:60%;
    z-index:1
}

.top_line{
    height:70px;
    background-color: #181818;
    z-index:50
}

.scrub_container{
    margin-top:40%;
    z-index:0
}

.content_title{
    margin-top:-35px;
    margin-left:30px;
    font-size:25px;
    position:absolute;
    z-index:10
}

.form_title{
    margin-top:25px;
    margin-left:30px;
    z-index:2;
    font-size:14px
}

.form_input_container{
    margin-top:215px;
    position:relative;
    z-index:2;
}


.form_input{
    margin-top:20px;
    padding:10px;
    margin-left:30px;
    font-size:10px;
    width:70%
}



.submit_button{
    margin-top:140px;
    margin-left:-83%;
    font-size:11px;
    width:40%;
    height:30px;
    border-radius:50px
}

.contact_info{
    margin-top:-200px;
    width:50%;
    margin-left:110%;
    }


.contact_elm{
    font-size:20px
}


.body_video{
    height:50vh;

}

.contact_video{
    margin-top:5%
}


.contact_message{
    margin-top:130px;
}
}

@media only screen and (min-width: 768px) and (max-width: 905px) {
    .international_toggle{
    margin-top:4%;
    margin-left: 57%;
}
}

@media only screen and (min-width: 992px) and (max-width: 1062px) {
    .international_toggle{
    margin-top:4%;
    margin-left: 57%;
}
}


@media only screen and (min-width: 768px) and (max-width: 992px) {



    .mobile_grid{
        display:none
    }

    .top_line{
    height:90px;
    border-bottom:rgba(255, 255, 255, 0.15) solid 1px;
    z-index:10
}

.content_title{
    margin-top:20%;
    margin-left:2.5%;
    position:absolute;
    font-size:250%
}

.form_title{
    margin-top:30%;
    margin-left:15px;
    position:absolute;
}


.form_input_container{
    margin-top:145%;
}

.form_input{
    border-bottom:#fff solid 1px;
    margin-top:40px;
    padding:10px;
    margin-left:10%;
    font-size:15px;
    width:70%
}



.form_input_area{
    margin-top:35%;
    padding:10px;
    margin-left:27%;
    font-size:15px;
    width:42.5%;
    height:50px;
}


.submit_button{
    margin-top:50%;
    padding:10px;
    margin-left:27.5%;
    font-size:15px;
    width:45%;
    height:50px;
}


.contact_img{
  height: 120vw;
  left:-100%;
}


.col_1{
    grid-area: col_1;
    background-color: #181818;
    border:rgba(255, 255, 255, 0.15) solid 1px;
    height:129vh;
}

.col_2{
    grid-area: col_2;
    background-color: #181818;
    border:rgba(255, 255, 255, 0.15) solid 1px;
    height:105vh;
    border-right:0;
    border-left:0
}

.col_3{
    grid-area: col_3;
    background-color: #181818;
    border:rgba(255, 255, 255, 0.15) solid 1px;
    border-left: 0px;
    height:117vh
}

.col_4{
    grid-area: col_4;
    background-color: #18181800;
}

.contact_info{
    margin-top:120%;
    margin-left:10%;
    }

    .contact_elm{
    font-size:18px
}

.scrub_container{
    margin-top:40%;
    z-index:0
}


.map_button{
    height:80px;
    width:80px;
    margin-left:45%;
}

.contact_video{
    margin-top:5%
}


.contact_message{
    margin-top:25%;
}


.body_video{
    height:80vh;
    margin-top:100%;
}



}

@media only screen and (min-width: 992px) and (max-width: 1200px) {
    .mobile_grid{
        display:none
    }

    .form_input_area{
    margin-top:25%;
    padding:10px;
    margin-left:27%;
    width:42.5%;
    height:75px;
}

.submit_button{
    margin-top:40%;
    padding:10px;
    margin-left:27.5%;
    font-size:25px;
    background-color: #18181800;
    width:45%;
    height:80px;
    background-color: #fff;
}

.scrub_container{
    margin-top:40%;
    z-index:0
}


.contact_img{
  height: 110vw;
  left:-80%;
}

.col_1{
    grid-area: col_1;
    background-color: #181818;
    border:rgba(255, 255, 255, 0.15) solid 1px;
    height:129vh;
}

.col_2{
    grid-area: col_2;
    background-color: #181818;
    border:rgba(255, 255, 255, 0.15) solid 1px;
    height:105vh;
    border-right:0;
    border-left:0
}

.col_3{
    grid-area: col_3;
    background-color: #181818;
    border:rgba(255, 255, 255, 0.15) solid 1px;
    border-left: 0px;
    height:117vh
}

.col_4{
    grid-area: col_4;
    background-color: #18181800;
}



}

@media only screen and (min-width: 1200px) and (max-width: 1400px) {
    .mobile_grid{
        display:none
    }


.col_1{
    grid-area: col_1;
    background-color: #181818;
    border:rgba(255, 255, 255, 0.15) solid 1px;
    height:154vh;
}

.col_2{
    grid-area: col_2;
    background-color: #181818;
    border:rgba(255, 255, 255, 0.15) solid 1px;
    height:130vh;
    border-right:0;
    border-left:0
}

.col_3{
    grid-area: col_3;
    background-color: #181818;
    border:rgba(255, 255, 255, 0.15) solid 1px;
    border-left: 0px;
    height:142vh
}

.form_input_area{
    margin-top:27%;
    padding:10px;
    margin-left:27%;
    width:42.5%;
    height:75px;
}

.submit_button{
    margin-top:42.5%;
    padding:10px;
    margin-left:27.5%;
    font-size:25px;
    background-color: #18181800;
    width:45%;
    height:80px;
    background-color: #fff;
}


.contact_video{
    width:55%;
    margin-left:22.5%;
    margin-top:0%
}

.contact_message{
    margin-top:25%;
}



}

@media only screen and (min-width: 1400px) and (max-width: 1600px) {
    .mobile_grid{
        display:none
    }

    .col_1{
    grid-area: col_1;
    background-color: #181818;
    border:rgba(255, 255, 255, 0.15) solid 1px;
    height:159vh;
}

.col_2{
    grid-area: col_2;
    background-color: #181818;
    border:rgba(255, 255, 255, 0.15) solid 1px;
    height:135vh;
    border-right:0;
    border-left:0
}

.col_3{
    grid-area: col_3;
    background-color: #181818;
    border:rgba(255, 255, 255, 0.15) solid 1px;
    border-left: 0px;
    height:147vh
}


}

@media only screen and (min-width: 1600px) and (max-width: 5600px) {
    .mobile_grid{
        display:none
    }

    .col_1{
    grid-area: col_1;
    background-color: #181818;
    border:rgba(255, 255, 255, 0.15) solid 1px;
    height:169vh;
}

.col_2{
    grid-area: col_2;
    background-color: #181818;
    border:rgba(255, 255, 255, 0.15) solid 1px;
    height:145vh;
    border-right:0;
    border-left:0
}

.col_3{
    grid-area: col_3;
    background-color: #181818;
    border:rgba(255, 255, 255, 0.15) solid 1px;
    border-left: 0px;
    height:157vh
}

.form_input_area{
    margin-top:29.5%;
    padding:10px;
    margin-left:27%;
    width:42.5%;
    height:75px;
}


.contact_video{
    width:45%;
    margin-left:27.5%;
    margin-top:0%
}

.contact_message{
    margin-top:20%;
}


}













</style>
