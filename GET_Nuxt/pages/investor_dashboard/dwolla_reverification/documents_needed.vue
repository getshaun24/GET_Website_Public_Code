<template>
    


    <div class="dark_mode">
        <div class="background_blur"></div>
        <div class="z_scope">
        <InvestorDashDashboardHeader v-bind="active_page"/>
        <InvestorDashLeftSidebar/>
    </div>
            <GSAPScrollSmoother>
   
          <div class="navigation_header">
            <div class="nav_menu_title">KYC Verification Documents Needed</div>
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


                <div class="upload_box">

                    <div class="upload_text">
                <h5 class="upload_title">To complete<br>your order,</h5>
                <p>Our KYC partner requires additional information to veryfy yourself.
                    <br><br>
                    Acceptible froms of identification include:
                    <br>
                    <ul>
                    <li>Passport</li>
                    <li>Liscense</li>
                    <li>ID Card</li>
                </ul>
                All documents must be a color scan of U.S. government-issued identification.
                <br> <br><br>
                Documents must be no larger then <i>10MB</i> in size.
                <br> <br>
                 Documents must be in one of the following supported file types:
                    <br>
                    <ul>
                    <li>.jpg</li>
                    <li>.jpeg</li>
                    <li>.png</li>
                    <li>.pdf</li>
                </ul>
                </p>
            </div>

                <div ref="dropZoneRef" class="upload_container">
                <img  class="upload_image" src="~assets/content/dashboard/file_upload.png">

                <p  v-if="drop_success == true && dropped_file_name != ''" class="drop_success">{{ dropped_file_name }}</p>
                <p  v-if="drop_success == true && uploaded_file != ''" class="drop_success">{{ select_file }}</p>
                <p  class="show_drop_error" :class="{hide_it:!show_drop_error}">Filetype Not Supported</p>


                <div v-if="drop_success == true" class="input_wrap doc_wrap">
            <select v-model="verification_type" required class="select_black withholding_input">
                    <option value="" disabled selected hidden></option>
                    <option value="passport">Passport</option>
                    <option value="license">License</option>
                    <option value="idCard">ID Card</option>
            </select>
                <label class="label_black withholding_label">Document Type</label>
        </div>


                

                <div class="upload_button">
                <div v-if="drop_success == false">
            <div class="files_open" @click="open">Choose file</div>
                    </div>
                    <div v-else>
                        <div class="files_submit" @click="submit_file">Submit</div>
                    </div>
        
                    

            </div>

                </div>

            </div>
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




// onBeforeMount(() => { if (authCookieRefresh()) {get_investor_overview()} })

const config = useRuntimeConfig()
const csrf_cookie = useCookie('csrf_access_token')
const show_drop_error = ref(false)
const drop_success_border = ref("black")
const drop_success = ref(false)
const uploaded_file = ref('')
const cookie_options = {default:()=> '', watch:true, maxAge:1800}
const investor_ID = useCookie('investor_ID', cookie_options)

const select_file = ref()
const { files, open, reset } = useFileDialog()

// single ref
watch(files, (newfiles) => {
    uploaded_file.value = newfiles[0]
    select_file.value = newfiles[0].name
    drop_success_border.value = "green"
    drop_success.value = true
})







const dropped_file_name = ref('')
const dropZoneRef = ref()
const { isOverDropZone } = useDropZone(dropZoneRef, onDrop) 
function onDrop(drop_files) {

    uploaded_file.value = drop_files[0]
    dropped_file_name.value = drop_files[0].name
    drop_success_border.value = "green"
    drop_success.value = true

}


const active_page = {is_active: "documents_active"}



function submit_file() {

    const upload_data = new FormData()
    upload_data.append('file', uploaded_file.value)
    upload_data.append('investor_ID', investor_ID.value)

    fetch(`${config.flask_url}/api/dwolla_reverification/documents_needed/`, {
        method: 'post',
        mode: 'cors',
        credentials: 'include',
        headers: {
            'X-CSRF-TOKEN': csrf_cookie.value
        },
        body: upload_data
    })
    .then((response) => response.json())
    .then((data) => {
        full_name.value = data.full_name
        notification_count.value = data.notification_count;
        table_data.value = data.table_data;
        record_count.value = data.table_data.length
    })
    .catch(error => {
        //  alert("Error")
        console.error('There was an error!', error);
    });
}


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
    transition: all 0.5s ease;
}

.files_submit:hover{
    background-color:#171717;
    transition: all 0.5s ease;
}

.upload_image{
    width:50%;
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
    padding-bottom:20vh;
display: grid;
grid-template-columns: repeat(2, 1fr);
grid-template-rows: 1fr;
grid-column-gap: 100px;
grid-row-gap: 10%;
    margin-left:6%;
}


.upload_container{
    cursor: pointer;
    display:flex;
    flex-direction:column;
    align-items:center;
    justify-content:center;

}

.upload_title{
    text-decoration: underline;
  text-decoration-color: red;
  text-underline-offset: 6px;
  text-decoration-skip-ink: none;

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

.doc_wrap{
    width:70%;
    margin-bottom:10%
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
    margin-left:-8%
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
    margin-left:-8%
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
    margin-left:-8%
}
}

@media only screen and (min-width: 992px) and (max-width: 1200px) {
    .upload_container{
    margin-top:30%;
    margin-left:-15%
}
}

@media only screen and (min-width: 1200px) and (max-width: 1400px) {
    .upload_container{
    margin-top:40%;
    margin-left:-15%
}
}

@media only screen and (min-width: 1400px) and (max-width: 1600px) {
    .upload_container{
    margin-top:40%;
    margin-left:-15%
}
}

@media only screen and (min-width: 1600px) and (max-width: 5600px) {
    .upload_container{
    margin-top:40%;
    margin-left:-15%
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











