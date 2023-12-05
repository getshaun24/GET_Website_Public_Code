<template>
    
    <div class="dark_mode" style="overflow-x:hidden">
        <InvestorDashDashboardHeader v-bind="active_page" />
        <InvestorDashLeftSidebar v-bind="active_page"/>
        <GSAPScrollSmoother>
            
            <div class="navigation_header">
                <div class="nav_menu_title">Notifications</div>
                <!-- <div class="header_menu">
                    <div class="navigation_menu is-active" href="#">xxx</div>
                    <div class="navigation_menu" href="#">xxx</div>
                    <div class="navigation_menu" href="#">xxx</div>
                </div> -->
            </div>
            <div class="dashboard_inner_section">
                <div class="main_content_container">


                    <InvestorDashInfoTableMain :table_name="table_name" :table_headers="table_headers" 
                  :table_buttons="table_buttons"  :record_count="record_count" :table_row_style="table_row_style" />

                </div>
            </div>
            
            <!-- div for footer scroll over -->
            <div style="padding-bottom:1px"></div>
            
        </GSAPScrollSmoother>
        <InvestorDashDashboardFooter/>
        
    </div>
    
    
    
    
    
</template>






<script setup>
import image1 from '~/assets/content/investments/invest_1.png'
import image2 from '~/assets/content/investments/invest_4.jpg'
import image3 from '~/assets/content/investments/invest_3.png'
import image4 from '~/assets/content/investments/invest_6.jpg'
import { ref, onBeforeMount } from "vue"
const config = useRuntimeConfig()
const cookie_options = {default:()=> '', watch:true, maxAge:1800}
const notification_count = useCookie('notification_count', cookie_options)
onBeforeMount(() => { notification_count.value = 0; if (authCookieRefresh()) { get_notifications()} })


const investor_ID = useCookie('investor_ID', cookie_options)
const active_page = {is_active: "notifications"}

// ---------------------  Table Component Data --------------------- //
const table_name = ref('All Notifications')
const table_row_style = ref('notifications_table')
const table_headers = ref(['Event Name', 'Date-Time', 'Event ID'])
const table_buttons = ref([])
const record_count = ref('')
const table_data = ref([])
provide('table_data', table_data)
// ---------------------  Table Component Data --------------------- //




const csrf_cookie = useCookie('csrf_access_token')

function get_notifications() {


fetch(`${config.flask_url}/api/investor_dashboard/notifications/`, {
    method: 'POST',
    mode: 'cors',
    headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'X-CSRF-TOKEN': csrf_cookie.value
    },
    credentials: 'include',
    body: JSON.stringify({investor_ID: investor_ID.value})
})
.then((response) => response.json())
.then((data) => {

    table_data.value = data.table_data
    record_count.value = data.table_data.length
})
.catch(error => {

    // alert("Error")
    console.error('There was an error!', error);
});


}

</script>
    
    
    
    
    
    
    
    
    
    
    
    
    
    <style scoped>
    
    
    .header_menu {
        display: flex;
        align-items: center;
    }
    
    .is-active {
        color: var(--header_menu_hover) !important;
        border-bottom: 3.5px solid var(--header_menu_hover) !important;
    }
    
    
    
    
    .navigation_menu {
        padding: 20px 30px;
        padding-bottom: 18px;
        text-decoration: none;
        color: var(--inactive-color);
        border-bottom: 2px solid transparent;
        transition: 0;
        cursor: pointer;
    }
    
    .navigation_menu:hover {
        color: var(--header_menu_hover);
        font-weight: bold;
    }
    
    
    
    
    .dashboard_inner_section{
        margin-bottom: 450px; 
        width:calc(100vw - 250px); 
        margin-left:250px;
        border-bottom: rgba(75, 75, 75, 0.1) .5px solid;
        background-color:var(--inner_background);
    }
    
    .main_content_container{
        width:80%; 
        margin-right:10%;
        margin-left:10%
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
        background-color:#000
    }
    
    
    
    .nav_menu_title {
        text-decoration: none;
        color: var(--theme-color);
        padding: 0 30px;
        margin-left:25px;
        padding-right:50px;
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
            width:100vw;
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











