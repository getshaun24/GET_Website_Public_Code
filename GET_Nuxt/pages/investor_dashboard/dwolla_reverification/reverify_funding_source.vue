<template>
    


    <div class="dark_mode">
        <div class="background_blur"></div>
        <div class="z_scope">
        <InvestorDashDashboardHeader v-bind="active_page"/>
        <InvestorDashLeftSidebar/>
    </div>
            <GSAPScrollSmoother>
   
          <div class="navigation_header">
            <div class="nav_menu_title">Re-Verify Funding Source</div>
            <!-- <div class="header_menu">
              <div class="navigation_menu is-active" href="#">xxx</div>
              <div class="navigation_menu" href="#">xxx</div>
              <div class="navigation_menu" href="#">xxx</div>
            </div> -->
          </div>
          <div class="dashboard_inner_section">
              <div class="main_content_container">



                <div style="padding-bottom:10vh"></div>               
                <div class="form_container">


                <h5 style="margin-left:20%; padding:20%">Plaid ?</h5>
            </div>

            <div style="padding-bottom:15vh"></div>




                

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



.background_blur{
    background-color: rgba(255, 255, 255, 0.005);
    position: fixed;
    width: 100vw;
    height: 100vh;
    z-index: 0;
    opacity: 1;
    backdrop-filter: blur(4px);
    left:0;
    top:0
}



.form_container{
        background-color: #000;
        border-radius:50px;
        padding-top:5%
    }


.z_scope :deep(.left_side){
z-index:-1
}

.z_scope :deep(.header){
z-index:-1
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
background-color: #000000cc;
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











