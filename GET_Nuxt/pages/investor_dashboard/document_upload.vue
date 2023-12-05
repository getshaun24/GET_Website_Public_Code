<template>
    


    <div class="dark_mode">
        <InvestorDashDashboardHeader v-bind="active_page"/>
        <InvestorDashLeftSidebar/>
            <GSAPScrollSmoother>
   
          <div class="navigation_header">
            <div class="nav_menu_title">Documents</div>
            <!-- <div class="header_menu">
              <div class="navigation_menu is-active" href="#">xxx</div>
              <div class="navigation_menu" href="#">xxx</div>
              <div class="navigation_menu" href="#">xxx</div>
            </div> -->
          </div>
          <div class="dashboard_inner_section">
              <div class="main_content_container">


               



                <div class="upload_box">

                    <div class="upload_text">
                <h5 class="upload_title">To complete your order,</h5>
                <p>Our KYC partner requires additional information to veryfy yourself.
                    <br><br>
                    We accept xxxx froms of identification.
                    <br>
                    xxx<br>
                    xxx
                </p>
            </div>

                <div ref="dropZoneRef" class="upload_container">
                <img  class="upload_image" src="~assets/content/dashboard/file_upload.png">
                


                <div v-if="drop_success == false">
            <div class="files_open" @click="open">Choose file</div>
                    </div>
                    <div v-else>
                        <div class="files_submit" @click="submit_file">Submit</div>
                    </div>


                <p class="drop_success">{{ dropped_file_name }}</p>
                <p class="drop_success">{{ select_file }}</p>
                <p class="show_drop_error" :class="{hide_it:!show_drop_error}">Filetype Not Supported</p>
            </div>

                </div>







                

              </div>
        </div>
         <!-- div for footer scroll over -->
        <div style="padding-bottom:1px"></div>
    </GSAPScrollSmoother>
    <InvestorDashDashboardFooter/>
</div>





</template>






<script setup>
import { useFileDialog } from '@vueuse/core'
import { useDropZone } from '@vueuse/core'


const show_drop_error = ref(false)
const drop_success_border = ref("black")
const drop_success = ref(false)


const select_file = ref()
const { files, open, reset } = useFileDialog()

// single ref
watch(files, (newfiles) => {
    select_file.value = files.value[0].name
    drop_success_border.value = "green"
    drop_success.value = true
})


const dropped_file_name = ref()
const dropZoneRef = ref()
const { isOverDropZone } = useDropZone(dropZoneRef, onDrop) 
function onDrop(drop_files) {
    dropped_file_name.value = drop_files[0].name
    drop_success_border.value = "green"
    drop_success.value = true
}


const active_page = {is_active: "documents_active"}


</script>













<style scoped>


.hide_it{
    display:none;
}

.files_open{
    padding: 10px;
    color:white;
    background-color:#3a6df0;
    border:1px solid #fff;
    width:200px;
    border-radius:50px;
    text-align:center;
    height:20px;
    cursor:pointer;
    margin-left:50px;
    transition: all 0.5s ease;
}

.files_open:hover{
    background-color:#171717;
    transition: all 0.5s ease;
}

.files_submit{
    padding: 10px;
    color:white;
    background-color:green;
    border:1px solid #fff;
    width:200px;
    border-radius:50px;
    text-align:center;
    height:20px;
    cursor:pointer;
    margin-left:50px;
    transition: all 0.5s ease;
}

.files_submit:hover{
    background-color:#171717;
    transition: all 0.5s ease;
}

.upload_image{
    width:215px;
    margin-bottom:50px;
    background-color:#171717;
    padding:50px;
    border-radius:50px;
    border: 1px solid v-bind(drop_success_border);
    transition: background-color 2s ease, border .5s ease;
}

.upload_image:hover{
    background-color:#3a6df0;
    transition: background-color 30s ease;
}


.upload_box{
    padding-top:20vh;
    padding-bottom:20vh;
display: grid;
grid-template-columns: repeat(2, 1fr);
grid-template-rows: 1fr;
grid-column-gap: 100px;
grid-row-gap: 10%;
    margin-left:12%;
}


.upload_container{
    cursor: pointer;
}

.upload_title{
    text-decoration: underline;
  text-decoration-color: red;
  text-underline-offset: 12px;
}

.drop_success{
    text-decoration: underline;
  text-decoration-color: #3a6df0;
  text-underline-offset: 8px;
}

.show_drop_error{
    text-decoration: underline;
  text-decoration-color: red;
  text-underline-offset: 8px;
}


@media only screen and (min-width: 0px) and (max-width: 576px) {
    .upload_box{
grid-template-columns: 1fr;
grid-template-rows: repeat(2, 1fr);
}
.upload_image{
    margin-bottom:20px
}
.upload_container{
    margin-left:12%
}



}

@media only screen and (min-width: 576px) and (max-width: 768px) {
    .upload_box{
grid-template-columns: 1fr;
grid-template-rows: repeat(2, 1fr);
}
.upload_image{
    margin-bottom:20px
}
.upload_container{
    margin-left:10%
}

}


@media only screen and (min-width: 768px) and (max-width: 992px) {
    .upload_box{
grid-template-columns: 1fr;
grid-template-rows: repeat(2, 1fr);
}
.upload_image{
    margin-bottom:20px
}
.upload_container{
    margin-left:10%
}
}

@media only screen and (min-width: 992px) and (max-width: 1200px) {
    .upload_container{
    margin-top:30%
}
}

@media only screen and (min-width: 1200px) and (max-width: 1400px) {
    .upload_container{
    margin-top:40%
}
}

@media only screen and (min-width: 1400px) and (max-width: 1600px) {
    .upload_container{
    margin-top:40%
}
}

@media only screen and (min-width: 1600px) and (max-width: 5600px) {
    .upload_container{
    margin-top:40%
}
}





















/* ------------------------ CSS For The Dashboard --------------------------------------- */
/* ------------------------ CSS For The Dashboard --------------------------------------- */
/* ------------------------ CSS For The Dashboard --------------------------------------- */
/* ------------------------ CSS For The Dashboard --------------------------------------- */
/* ------------------------ CSS For The Dashboard --------------------------------------- */




.dashboard_inner_section{
margin-bottom: 450px; 
width:calc(100vw - 250px); 
margin-left:250px;
border-bottom: rgba(75, 75, 75, 0.1) .5px solid;
background-color:var(--inner_background);
}

.main_content_container{
width:90%; 
margin-right:10%;
margin-left:5%
}


.navigation_header {
display: flex;
align-items: center;
border-bottom: 1px solid var(--border-color);
height: 58px;
flex-shrink: 0;
margin-top:80px;
width:calc(100vw - 250px); 
margin-left: 250px;
}



.nav_menu_title {
text-decoration: none;
color: var(--theme-color);
padding: 0 30px;
margin-left:25px;
padding-right:50px
}



::-webkit-scrollbar {
width: 3px;
border-radius: 10px;
}

::-webkit-scrollbar-thumb {
background: rgba(0, 149, 255, 0.676);
border-radius: 10px;
}


@media only screen and (min-width: 0px) and (max-width: 576px) {
    .dashboard_inner_section{
width:calc(100vw - 20px); 
margin-left:20px;
}

.navigation_header {
    width:100vw; 
margin-left:20px;
}

}

@media only screen and (min-width: 576px) and (max-width: 768px) {
    .dashboard_inner_section{
width:calc(100vw - 20px); 
margin-left:20px;
}

.navigation_header {
    width:100vw; 
margin-left:20px;
}

}

@media only screen and (min-width: 768px) and (max-width: 992px) {

    .dashboard_inner_section{
width:calc(100vw - 180px); 
margin-left:180px;
}

.navigation_header {
    width:100vw; 
margin-left:150px;
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











