<template>

    <div>

        <div class="loader_container" v-if="start_loader">
<InvestFlowLoadersApiLoader/>
   </div>

    
        
        <div class="modal_container" :class="{modal_hide_anim: modal_exit_anim, modal_hide_disp: modal_exit_display}">
        <div class="modal_popup" :class="{modal_bix_hide_anim: modal_exit_anim}" ref="modal">

            <!-- <div @click="modal_leave" class="modal_exit">
                <div class="horizontal_line"></div>
                <div class="vertical_line"></div>
            </div> -->


<!-- ------------------------------------------------------------ Modal Info ------------------------------------------------------------ -->
<!-- ------------------------------------------------------------ Modal Info ------------------------------------------------------------ -->




<div v-if="investing_as == 'individual'" class="form_container">


<div class="upload_box">

    <div class="upload_text">
        <h6 class="upload_title_business">Document verification needed<br>to complete your order</h6>
<p class="info_text" style="text-align: center;">Our KYC partner requires additional information to verify your identity, Please provide one the following:
</p>
<br><br>
<p class="info_text">
    Acceptible froms of identification include:
    <br></p>
    <ul class="info_text">
    <li>Passport</li>
    <li>Liscense</li>
    <li>ID Card</li>
    <li><u>Note: Military IDs are NOT accepted</u></li>
</ul>
<p class="info_text">
All documents must be a color scan of U.S. government-issued identification.
</p>

<p class="info_text">
To prevent and minimize documents from being rejected, please follow<br>these <span @mouseover="designation_show_1 = true" class="more_info_text">guidelines <span class="designation_hover">?</span></span>
</p>
<p style="margin-left:1%" class="designation_text" :class="{designation_show: designation_show_1}" @mouseleave="designation_show_1 = false">

All documents must be a color scan of U.S. government-issued identification.
<br> <br>
Documents must be no larger then <i>10MB</i> in size.
<br> <br>
Documents must be in one of the following supported file types:

<ul >
<li>.jpg</li>
<li>.jpeg</li>
<li>.png</li>
<li>.pdf</li>
</ul>

<br> <br>
Reduce chance of rejection by ensuring:

<ul >
<li>All 4 Edges of the document should be visible</li>
<li>A dark/high contrast background should be used</li>
<li>At least 90% of the image should be the document</li>
<li>Should be at least 300dpi</li>
<li>Capture image from directly above the document</li>
<li>Make sure that the image is properly aligned, not rotated, tilted or skewed</li>
<li>No flash to reduce glare</li>
<li>No black and white documents</li>
<li>No expired IDs</li>
</ul>

</p>


</div>

<div ref="dropZoneRef_1" class="upload_container">
<img  class="upload_image" src="~assets/content/dashboard/file_upload.png">

<p  v-if="drop_success_1 == true && dropped_file_name_1 != ''" @click="replace_file(1)" class="drop_success">{{ dropped_file_name_1 }}</p>
<p  v-if="drop_success_1 == true && uploaded_file_1 != ''" @click="replace_file(1)" class="drop_success">{{ select_file_1 }}</p>
<p  class="show_drop_error" :class="{hide_it:!show_drop_error}">Filetype Not Supported</p>


<div v-if="drop_success_1 == true" class="input_wrap doc_wrap">
<select v-model="individual_verification_type" required class="select_black withholding_input">
    <option value="" disabled selected hidden></option>
    <option value="passport">Passport</option>
    <option value="license">License</option>
    <option value="idCard">ID Card</option>
</select>
<label class="label_black withholding_label">Document Type</label>
</div>




<div class="upload_button">
<div v-if="drop_success_1 == false">
<div class="files_open" @click="open_file_box_1.open">Choose file</div>
    </div>
    <div v-else>
        <div class="files_submit" @click="submit_file">Submit</div>
    </div>

    

</div>

</div>

</div>
</div>








<div v-else-if="investing_as == 'soleProprietorship'" class="form_container">




<div class="upload_text_business">
    <h6 class="upload_title_business">Document verification needed<br>to complete your order</h6>
<p class="info_text" style="text-align: center;">Our KYC partner requires additional information to verify your identity, Please provide one the following:</p>
<br><br>
<p class="info_text">
For your Sole Proprietorship personal identification, you will need to upload a copy of one of the following forms of identification:
<br></p>
<ul class="info_text">
<li>Passport</li>
<li>Liscense</li>
<li>ID Card</li>
<br>
<span @mouseover="designation_show_1 = true" class="more_info_text">More Info <span class="designation_hover">?</span></span>
</ul>
<p class="designation_text" :class="{designation_show: designation_show_1}" @mouseleave="designation_show_1 = false">
<u>US persons:</u> A color scanned photo of the owner's identifying document can be specified as documentType: license (state issued driver's license), or idCard (U.S. government-issued photo id card).<br><br>
Supported Document Examples:
<ul>
<li>Non-expired State Issued Driver’s License/Identification Card</li>
<li>Non-expired US Passport</li>
<li>Federal Employment Authorization Card</li>
<li>US Visa</li>
</ul>
Unsupported Document Examples:
<ul>
<li>Military IDs</li>
<li>Expired government-issued IDs</li>
</ul>
<br>
<u>Non-US persons:</u> A color scanned photo of the owner's identifying document can be specified as documentType: passport. Examples include:
<ul>
<li>Non-expired Foreign Passport Note: Foreign Passports are only accepted when the individual does not have an ITIN or SSN and the user must alternatively enter the Passport number.</li>
</ul>
</p>
<p class="info_text">
Valid business documents include:
</p>
<ul class="info_text">
<li>Fictitious Business Name Statement</li>
<li>Certificate of Assumed Name; Business License</li>
<li>Sales/Use Tax License</li>
<li>Registration of Trade Name</li>
<li>EIN documentation (IRS-issued SS4 confirmation letter)</li>
<br>
<span @mouseover="designation_show_2 = true" class="more_info_text">More Info <span class="designation_hover">?</span></span>
</ul>
<p class="designation_text" :class="{designation_show: designation_show_2}" @mouseleave="designation_show_2 = false">
Documents that are used to help identify a business are specified as documentType other. Note: A DBA document should be issued by the government and should include the DBA name along with the state registered business name. Business Identifying documents we recommend uploading can include the following:
<ul>
<li>Sole Proprietorship: Sole Proprietorships can be verified by uploading Business documents as well as Personal IDs. Personal IDs need to be specified as documentType idCard, license or passport depending on the type of the ID. Business documents need to be specified as documentType other. Acceptable documents include one or more of the following, as applicable to your sole proprietorship:
<ul>
  <li>Business documents (documentType other):
    <ul>
        <li>Fictitious Business Name Statement</li>
        <li>Certificate of Assumed Name; Business License</li>
        <li>Sales/Use Tax License</li>
        <li>Registration of Trade Name</li>
        <li>EIN documentation (IRS-issued SS4 confirmation letter)</li>
    </ul>
        Personal documents (documentType license, passport or idCard):
        <ul><li>Color copy of a valid government-issued photo ID (e.g., a driver’s license, passport, or state ID card).</li></ul>
  </li>
</ul>
</li>
</ul>
Note: Trusts should be created as Sole Proprietor accounts and will require signed trust documents that include the trust and username that are on file.
<br><br>
Other business documents may be acceptable on a case by case basis with Dwolla approval. These include any US government entity (federal, state, local) issued business formation or licensing exhibiting the name of the business enrolling with Dwolla, or; Any business formation documents exhibiting the name of the business entity in addition to being filed and stamped by a US government entity. Examples include:
<ul>
<li>Filed and stamped Articles of Organization or Incorporation</li>
<li>Sales/Use Tax License</li>
<li>Business License</li>
<li>Certificate of Good Standing
</li>
</ul>
</p>

<p class="info_text">
Valid DBA documents include:
</p>
<ul class="info_text">
<li>Fictitious Business Name Statement</li>
<li>Certificate of Assumed Name; Business License</li>
<br>
<span @mouseover="designation_show_3 = true" class="more_info_text">More Info <span class="designation_hover">?</span></span>
</ul>
<p class="designation_text" :class="{designation_show: designation_show_3}" @mouseleave="designation_show_3 = false">
This field is optional but we highly reccomend submitting this document if you have one. A DBA document should be issued by the government and should include the DBA name along with the state registered business name.
</p>
<br>
<p class="info_text">
To prevent and minimize documents from being rejected,<br>please follow these <span @mouseover="designation_show_4 = true" class="more_info_text">guidelines <span class="designation_hover">?</span></span>
</p>
<p class="designation_text" :class="{designation_show: designation_show_4}" @mouseleave="designation_show_4 = false">

All documents must be a color scan of U.S. government-issued identification.
<br> <br>
Documents must be no larger then <i>10MB</i> in size.
<br> <br>
Documents must be in one of the following supported file types:

<ul >
<li>.jpg</li>
<li>.jpeg</li>
<li>.png</li>
<li>.pdf</li>
</ul>

<br> <br>
Reduce chance of rejection by ensuring:

<ul >
<li>All 4 Edges of the document should be visible</li>
<li>A dark/high contrast background should be used</li>
<li>At least 90% of the image should be the document</li>
<li>Should be at least 300dpi</li>
<li>Capture image from directly above the document</li>
<li>Make sure that the image is properly aligned, not rotated, tilted or skewed</li>
<li>No flash to reduce glare</li>
<li>No black and white documents</li>
<li>No expired IDs</li>
</ul>

</p>

</div>


<div class="upload_box_solprop">
<!-- ------------------------------------ box 1 ------------------------------------ -->


<div class="upload_box_inner">

<div ref="dropZoneRef_1" class="upload_container">
<p>Personal Documents</p>
<p style="font-size:10px; margin-top:-15px; color:#000">.</p>
<img  class="upload_image_business" src="~assets/content/dashboard/file_upload.png">

<p  v-if="drop_success_1 == true && dropped_file_name_1 != ''" class="drop_success">{{ dropped_file_name_1 }}</p>
<p  v-if="drop_success_1 == true && uploaded_file_1 != ''" class="drop_success">{{ select_file_1 }}</p>
<p  class="show_drop_error" :class="{hide_it:!show_drop_error}">Filetype Not Supported</p>


<div v-if="drop_success_1 == true" class="input_wrap doc_wrap">
<select v-model="sole_prop_verification_type" required class="select_black withholding_input">
<option value="" disabled selected hidden></option>
<option value="passport">Passport</option>
<option value="license">License</option>
<option value="idCard">ID Card</option>
</select>
<label class="label_black withholding_label">Document Type</label>
</div>




<div class="upload_button">
<div v-if="drop_success_1 == false">
<div class="files_open" @click="open_file_box_1.open">Choose file</div>
</div>
<div v-else>
    <div class="files_replace" @click="replace_file(1)">Replace File</div>
</div>
</div></div></div>


<!-- ------------------------------------ box 2 ------------------------------------ -->


<div class="upload_box_inner">
<div ref="dropZoneRef_2" class="upload_container">
<p>Business Documents</p>
<p style="font-size:10px; margin-top:-15px; color:#000">.</p>
<img  class="upload_image_business" src="~assets/content/dashboard/file_upload.png">

<p  v-if="drop_success_2 == true && dropped_file_name_2 != ''" class="drop_success">{{ dropped_file_name_2 }}</p>
<p  v-if="drop_success_2 == true && uploaded_file_2 != ''" class="drop_success">{{ select_file_2 }}</p>
<p  class="show_drop_error" :class="{hide_it:!show_drop_error}">Filetype Not Supported</p>




<div class="upload_button">
<div v-if="drop_success_2 == false">
<div class="files_open" @click="open_file_box_2.open">Choose file</div>
</div>
<div v-else>
    <div class="files_replace" @click="replace_file(2)">Replace File</div>
</div>
</div></div></div>


<!-- ------------------------------------ box 3 ------------------------------------ -->


<div class="upload_box_inner">
<div ref="dropZoneRef_3" class="upload_container">
    <p>DBA Documents</p>
    <p style="font-size:10px; margin-top:-15px">(Optional but Reccomended)</p>
<img  class="upload_image_business" src="~assets/content/dashboard/file_upload.png">

<p  v-if="drop_success_3 == true && dropped_file_name_3 != ''" class="drop_success">{{ dropped_file_name_3 }}</p>
<p  v-if="drop_success_3 == true && uploaded_file_3 != ''" class="drop_success">{{ select_file_3 }}</p>
<p  class="show_drop_error" :class="{hide_it:!show_drop_error}">Filetype Not Supported</p>


<div class="upload_button">
<div v-if="drop_success_3 == false">
<div class="files_open" @click="open_file_box_3.open">Choose file</div>
</div>
<div v-else>
    <div class="files_replace" @click="replace_file(3)">Replace File</div>
</div>
</div></div></div>



</div>


    <div class="business_submit" @click="submit_file">Submit</div>



</div>




















<div v-else class="form_container">




    <div class="upload_text_business">
        <h6 class="upload_title_business">Document verification needed<br>to complete your order</h6>
<p class="info_text" style="text-align: center;">Our KYC partner requires additional information to verify your identity, Please provide one the following:</p>
<br><br>
    <p class="info_text">
    For both the controller and beneficial owner, you will need to upload a copy of one of the following forms of identification:
    <br></p>
    <ul class="info_text">
    <li>Passport</li>
    <li>Liscense</li>
    <li>ID Card</li>
    <br>
    <span @mouseover="designation_show_1 = true" class="more_info_text">More Info <span class="designation_hover">?</span></span>
</ul>
<p class="designation_text" :class="{designation_show: designation_show_1}" @mouseleave="designation_show_1 = false">
    <u>US persons:</u> A color scanned photo of the Controller or Beneficial Owner's identifying document can be specified as documentType: license (state issued driver's license), or idCard (U.S. government-issued photo id card).<br><br>
    Supported Document Examples:
    <ul>
    <li>Non-expired State Issued Driver’s License/Identification Card</li>
    <li>Non-expired US Passport</li>
    <li>Federal Employment Authorization Card</li>
    <li>US Visa</li>
</ul>
Unsupported Document Examples:
<ul>
    <li>Military IDs</li>
    <li>Expired government-issued IDs</li>
</ul>
<br>
<u>Non-US persons:</u> A color scanned photo of the Controller or Beneficial Owner's identifying document can be specified as documentType: passport. Examples include:
<ul>
    <li>Non-expired Foreign Passport Note: Foreign Passports are only accepted when the individual does not have an ITIN or SSN and the user must alternatively enter the Passport number.</li>
</ul>
</p>
<p class="info_text">
 Valid business documents include:
</p>
    <ul class="info_text">
    <li>Fictitious Business Name Statement</li>
    <li>Certificate of Assumed Name; Business License</li>
    <li>Sales/Use Tax License</li>
    <li>Registration of Trade Name</li>
    <li>EIN documentation (IRS-issued SS4 confirmation letter)</li>
    <br>
    <span @mouseover="designation_show_2 = true" class="more_info_text">More Info <span class="designation_hover">?</span></span>
</ul>
<p class="designation_text" :class="{designation_show: designation_show_2}" @mouseleave="designation_show_2 = false">
    Documents that are used to help identify a business are specified as documentType other. Note: A DBA document should be issued by the government and should include the DBA name along with the state registered business name. Business Identifying documents we recommend uploading can include the following:
    <ul>
    <li>Partnership, General Partnership: EIN Letter (IRS-issued SS4 confirmation letter).</li>
    <li>Limited Liability Corporation (LLC), Corporation: EIN Letter (IRS-issued SS4 confirmation letter).</li>
    <li>Sole Proprietorship: Sole Proprietorships can be verified by uploading Business documents as well as Personal IDs. Personal IDs need to be specified as documentType idCard, license or passport depending on the type of the ID. Business documents need to be specified as documentType other. Acceptable documents include one or more of the following, as applicable to your sole proprietorship:
    <ul>
      <li>Business documents (documentType other):
        <ul>
            <li>Fictitious Business Name Statement</li>
            <li>Certificate of Assumed Name; Business License</li>
            <li>Sales/Use Tax License</li>
            <li>Registration of Trade Name</li>
            <li>EIN documentation (IRS-issued SS4 confirmation letter)</li>
        </ul>
            Personal documents (documentType license, passport or idCard):
            <ul><li>Color copy of a valid government-issued photo ID (e.g., a driver’s license, passport, or state ID card).</li></ul>
      </li>
    </ul>
    </li>
</ul>
Note: Trusts should be created as Sole Proprietor accounts and will require signed trust documents that include the trust and username that are on file.
<br><br>
Other business documents may be acceptable on a case by case basis with Dwolla approval. These include any US government entity (federal, state, local) issued business formation or licensing exhibiting the name of the business enrolling with Dwolla, or; Any business formation documents exhibiting the name of the business entity in addition to being filed and stamped by a US government entity. Examples include:
<ul>
    <li>Filed and stamped Articles of Organization or Incorporation</li>
    <li>Sales/Use Tax License</li>
    <li>Business License</li>
    <li>Certificate of Good Standing
</li>
</ul>
</p>

<p class="info_text">
 Valid DBA documents include:
</p>
    <ul class="info_text">
    <li>Fictitious Business Name Statement</li>
    <li>Certificate of Assumed Name; Business License</li>
    <br>
    <span @mouseover="designation_show_3 = true" class="more_info_text">More Info <span class="designation_hover">?</span></span>
</ul>
<p class="designation_text" :class="{designation_show: designation_show_3}" @mouseleave="designation_show_3 = false">
    This field is optional but we highly reccomend submitting this document if you have one. A DBA document should be issued by the government and should include the DBA name along with the state registered business name.
</p>
<br>
<p class="info_text">
To prevent and minimize documents from being rejected,<br>please follow these <span @mouseover="designation_show_4 = true" class="more_info_text">guidelines <span class="designation_hover">?</span></span>
</p>
<p class="designation_text" :class="{designation_show: designation_show_4}" @mouseleave="designation_show_4 = false">

All documents must be a color scan of U.S. government-issued identification.
<br> <br>
Documents must be no larger then <i>10MB</i> in size.
<br> <br>
 Documents must be in one of the following supported file types:

    <ul >
    <li>.jpg</li>
    <li>.jpeg</li>
    <li>.png</li>
    <li>.pdf</li>
</ul>

<br> <br>
Reduce chance of rejection by ensuring:

    <ul >
    <li>All 4 Edges of the document should be visible</li>
    <li>A dark/high contrast background should be used</li>
    <li>At least 90% of the image should be the document</li>
    <li>Should be at least 300dpi</li>
    <li>Capture image from directly above the document</li>
    <li>Make sure that the image is properly aligned, not rotated, tilted or skewed</li>
    <li>No flash to reduce glare</li>
    <li>No black and white documents</li>
    <li>No expired IDs</li>
</ul>

</p>

</div>


<div class="upload_box_business">
<!-- ------------------------------------ box 1 ------------------------------------ -->


<div class="upload_box_inner">

<div ref="dropZoneRef_1" class="upload_container">
    <p>Controller Documents</p>
<img  class="upload_image_business" src="~assets/content/dashboard/file_upload.png">

<p  v-if="drop_success_1 == true && dropped_file_name_1 != ''" class="drop_success">{{ dropped_file_name_1 }}</p>
<p  v-if="drop_success_1 == true && uploaded_file_1 != ''" class="drop_success">{{ select_file_1 }}</p>
<p  class="show_drop_error" :class="{hide_it:!show_drop_error}">Filetype Not Supported</p>


<div v-if="drop_success_1 == true" class="input_wrap doc_wrap">
<select v-model="controller_verification_type" required class="select_black withholding_input">
    <option value="" disabled selected hidden></option>
    <option value="passport">Passport</option>
    <option value="license">License</option>
    <option value="idCard">ID Card</option>
</select>
<label class="label_black withholding_label">Document Type</label>
</div>




<div class="upload_button">
<div v-if="drop_success_1 == false">
<div class="files_open" @click="open_file_box_1.open">Choose file</div>
    </div>
    <div v-else>
        <div class="files_replace" @click="replace_file(1)">Replace File</div>
    </div>
</div></div></div>


<!-- ------------------------------------ box 2 ------------------------------------ -->


<div class="upload_box_inner">
<div ref="dropZoneRef_2" class="upload_container">
    <p>Owner Documents</p>
<img  class="upload_image_business" src="~assets/content/dashboard/file_upload.png">

<p  v-if="drop_success_2 == true && dropped_file_name_2 != ''" class="drop_success">{{ dropped_file_name_2 }}</p>
<p  v-if="drop_success_2 == true && uploaded_file_2 != ''" class="drop_success">{{ select_file_2 }}</p>
<p  class="show_drop_error" :class="{hide_it:!show_drop_error}">Filetype Not Supported</p>


<div v-if="drop_success_2 == true" class="input_wrap doc_wrap">
<select v-model="owner_verification_type" required class="select_black withholding_input">
    <option value="" disabled selected hidden></option>
    <option value="passport">Passport</option>
    <option value="license">License</option>
    <option value="idCard">ID Card</option>
</select>
<label class="label_black withholding_label">Document Type</label>
</div>




<div class="upload_button">
<div v-if="drop_success_2 == false">
<div class="files_open" @click="open_file_box_2.open">Choose file</div>
    </div>
    <div v-else>
        <div class="files_replace" @click="replace_file(2)">Replace File</div>
    </div>
</div></div></div>


<!-- ------------------------------------ box 3 ------------------------------------ -->


<div class="upload_box_inner">
<div ref="dropZoneRef_3" class="upload_container">
    <p>Business Documents</p>
    <p style="font-size:10px; margin-top:-15px; color:#000">.</p>
<img  class="upload_image_business" src="~assets/content/dashboard/file_upload.png">

<p  v-if="drop_success_3 == true && dropped_file_name_3 != ''" class="drop_success">{{ dropped_file_name_3 }}</p>
<p  v-if="drop_success_3 == true && uploaded_file_3 != ''" class="drop_success">{{ select_file_3 }}</p>
<p  class="show_drop_error" :class="{hide_it:!show_drop_error}">Filetype Not Supported</p>


<div class="upload_button">
<div v-if="drop_success_3 == false">
<div class="files_open" @click="open_file_box_3.open">Choose file</div>
    </div>
    <div v-else>
        <div class="files_replace" @click="replace_file(3)">Replace File</div>
    </div>
</div></div></div>


<!-- ------------------------------------ box 4 ------------------------------------ -->


<div class="upload_box_inner">
<div ref="dropZoneRef_4" class="upload_container">
    <p>DBA Documents</p>
    <p style="font-size:10px; margin-top:-15px">(Optional but Reccomended)</p>
<img  class="upload_image_business" src="~assets/content/dashboard/file_upload.png">

<p  v-if="drop_success_4 == true && dropped_file_name_4 != ''" class="drop_success">{{ dropped_file_name_4 }}</p>
<p  v-if="drop_success_4 == true && uploaded_file_4 != ''" class="drop_success">{{ select_file_4 }}</p>
<p  class="show_drop_error" :class="{hide_it:!show_drop_error}">Filetype Not Supported</p>



<div class="upload_button">
<div v-if="drop_success_4 == false">
<div class="files_open" @click="open_file_box_4.open">Choose file</div>
    </div>
    <div v-else>
        <div class="files_replace" @click="replace_file(4)">Replace File</div>
    </div>
</div></div></div>

<!-- ------------------------------------ box 4 ------------------------------------ -->




</div>




        <div class="business_submit" @click="submit_file">Submit</div>


    </div>




<!-- ------------------------------------------------------------ Modal Info ------------------------------------------------------------ -->
<!-- ------------------------------------------------------------ Modal Info ------------------------------------------------------------ -->


        </div>
    </div>
    
    </div>
    </template>
    
    
    
    
    
    <script setup>
    import { ref } from 'vue'
    import { onClickOutside, useElementVisibility } from '@vueuse/core'
    import { useFileDialog } from '@vueuse/core'
    import { useDropZone } from '@vueuse/core'




// onBeforeMount(() => { if (authCookieRefresh()) {get_investor_overview()} })

const config = useRuntimeConfig()
const cookie_options = {default:()=> '', watch:true, maxAge:1800}
const investor_ID = useCookie('investor_ID', cookie_options)
const investing_as = useCookie('investing_as')
const fund_ID = useCookie('fund_ID')
const documents_uploaded_successful = useCookie('documents_uploaded_successful', {watch:true, maxAge:1800})
const dwolla_customer_status = useCookie('dwolla_customer_status')
const dwolla_beneficial_owner_status = useCookie('dwolla_beneficial_owner_status')
const designation_show_1 = ref(false)
const designation_show_2 = ref(false)
const designation_show_3 = ref(false)
const designation_show_4 = ref(false)
const start_loader = ref(false);

const individual_verification_type = ref('')
const sole_prop_verification_type = ref('')
const controller_verification_type = ref('')
const owner_verification_type = ref('')
// const { files, open, reset } = useFileDialog()

const select_file_1 = ref('')
const dropped_file_name_1 = ref('')
const show_drop_error_1 = ref(false)
const drop_success_border_1 = ref("black")
const drop_success_1 = ref(false)
const uploaded_file_1 = ref(null)
const open_file_box_1 = useFileDialog()
const dropZoneRef_1 = ref()
useDropZone(dropZoneRef_1, onDrop_1) 

const select_file_2 = ref('')
const dropped_file_name_2 = ref('')
const show_drop_error_2 = ref(false)
const drop_success_border_2 = ref("black")
const drop_success_2 = ref(false)
const uploaded_file_2 = ref(null)
const open_file_box_2 = useFileDialog()
const dropZoneRef_2 = ref()
useDropZone(dropZoneRef_2, onDrop_2) 

const select_file_3 = ref('')
const dropped_file_name_3 = ref('')
const show_drop_error_3 = ref(false)
const drop_success_border_3 = ref("black")
const drop_success_3 = ref(false)
const uploaded_file_3 = ref(null)
const open_file_box_3 = useFileDialog()
const dropZoneRef_3 = ref()
useDropZone(dropZoneRef_3, onDrop_3) 

const select_file_4 = ref('')
const dropped_file_name_4 = ref('')
const show_drop_error_4 = ref(false)
const drop_success_border_4 = ref("black")
const drop_success_4 = ref(false)
const uploaded_file_4 = ref(null)
const open_file_box_4 = useFileDialog()
const dropZoneRef_4 = ref()
useDropZone(dropZoneRef_4, onDrop_4) 




watch(open_file_box_1.files, (newfiles) => {
    if (newfiles[0].type == "image/jpeg" || newfiles[0].type == "image/png" ||  newfiles[0].type == "application/pdf") {
        if(newfiles[0].size < 10000000) {
        uploaded_file_1.value = newfiles[0]
        select_file_1.value = newfiles[0].name
        drop_success_border_1.value = "green"
        drop_success_1.value = true
        } else {
        alert("Filesize must be less then 10MB")
        }
    } else {
        alert("Filetype Not Supported")
    }
})

watch(open_file_box_2.files, (newfiles) => {
    if (newfiles[0].type == "image/jpeg" || newfiles[0].type == "image/png" ||  newfiles[0].type == "application/pdf") {
        if(newfiles[0].size < 10000000) {
    uploaded_file_2.value = newfiles[0]
    select_file_2.value = newfiles[0].name
    drop_success_border_2.value = "green"
    drop_success_2.value = true
    } else {
            alert("Filesize must be less then 10MB")
            }
} else {
        alert("Filetype Not Supported")
    }
})

watch(open_file_box_3.files, (newfiles) => {
    if (newfiles[0].type == "image/jpeg" || newfiles[0].type == "image/png" ||  newfiles[0].type == "application/pdf") {
        if(newfiles[0].size < 10000000) {
    uploaded_file_3.value = newfiles[0]
    select_file_3.value = newfiles[0].name
    drop_success_border_3.value = "green"
    drop_success_3.value = true
    } else {
        alert("Filesize must be less then 10MB")
        }
} else {
        alert("Filetype Not Supported")
    }
})

watch(open_file_box_4.files, (newfiles) => {
    if (newfiles[0].type == "image/jpeg" || newfiles[0].type == "image/png" ||  newfiles[0].type == "application/pdf") {
        if(newfiles[0].size < 10000000) {
    uploaded_file_4.value = newfiles[0]
    select_file_4.value = newfiles[0].name
    drop_success_border_4.value = "green"
    drop_success_4.value = true
} else {
        alert("Filesize must be less then 10MB")
        }
} else {
        alert("Filetype Not Supported")
    }
})




function onDrop_1(drop_files) {
    if (drop_files[0].type == "image/jpeg" || drop_files[0].type == "image/png" ||  drop_files[0].type == "application/pdf") {
        if(drop_files[0].size < 10000000) {
    uploaded_file_1.value = drop_files[0]
    dropped_file_name_1.value = drop_files[0].name
    drop_success_border_1.value = "green"
    drop_success_1.value = true
    } else {
            alert("Filesize must be less then 10MB")
            }
} else {
        alert("Filetype Not Supported")
    }
}

function onDrop_2(drop_files) {
    if (drop_files[0].type == "image/jpeg" || drop_files[0].type == "image/png" ||  drop_files[0].type == "application/pdf") {
        if(drop_files[0].size < 10000000) {
    uploaded_file_2.value = drop_files[0]
    dropped_file_name_2.value = drop_files[0].name
    drop_success_border_2.value = "green"
    drop_success_2.value = true
    } else {
                alert("Filesize must be less then 10MB")
                }
} else {
        alert("Filetype Not Supported")
    }
}

function onDrop_3(drop_files) {
    if (drop_files[0].type == "image/jpeg" || drop_files[0].type == "image/png" ||  drop_files[0].type == "application/pdf") {
        if(drop_files[0].size < 10000000) {
    uploaded_file_3.value = drop_files[0]
    dropped_file_name_3.value = drop_files[0].name
    drop_success_border_3.value = "green"
    drop_success_3.value = true
    } else {
                alert("Filesize must be less then 10MB")
                }
} else {
        alert("Filetype Not Supported")
    }
}

function onDrop_4(drop_files) {
    if (drop_files[0].type == "image/jpeg" || drop_files[0].type == "image/png" ||  drop_files[0].type == "application/pdf") {
        if(drop_files[0].size < 10000000) {
    uploaded_file_4.value = drop_files[0]
    dropped_file_name_4.value = drop_files[0].name
    drop_success_border_4.value = "green"
    drop_success_4.value = true
    } else {
                alert("Filesize must be less then 10MB")
                }
} else {
        alert("Filetype Not Supported")
    }
}



function replace_file(num){
    if (num == 1){
        drop_success_1.value = false
        open_file_box_1.reset
    } else if (num == 2){
        drop_success_2.value = false
        open_file_box_2.reset
    } else if (num == 3){
        drop_success_3.value = false
        open_file_box_3.reset
    } else if (num == 4){
        drop_success_4.value = false
        open_file_box_4.reset
    }
}


sleep(1000).then(() => {
onClickOutside(designation_show_1, (event) => designation_show_1.value = false)
onClickOutside(designation_show_2, (event) => designation_show_2.value = false)
onClickOutside(designation_show_3, (event) => designation_show_3.value = false)
onClickOutside(designation_show_4, (event) => designation_show_4.value = false)
})


function submit_file() {

    if (investing_as.value == 'individual'){
    if (uploaded_file_1.value == null) {
        alert("Please Upload File")
        return
    }
    else if( individual_verification_type.value == ''){
        alert("Please Select A Document Type")
        return
    }
    } else if (investing_as.value == 'soleProprietorship'){
        if (uploaded_file_1.value == null || uploaded_file_2.value == null) {
        alert("Please Upload All Files")
        return
    } else if( sole_prop_verification_type.value == ''){
        alert("Please Select A Document Type")
        return
    }} else {
        if (uploaded_file_1.value == null || uploaded_file_2.value == null || uploaded_file_3.value == null) {
        alert("Please Upload All Files")
        return
    }else if( controller_verification_type.value == '' || owner_verification_type.value == ''){
        alert("Please Select A Document Type")
        return
    }}


    start_loader.value = true;
    const upload_data = new FormData()
    upload_data.append('file_1', uploaded_file_1.value)
    upload_data.append('file_2', uploaded_file_2.value)
    upload_data.append('file_3', uploaded_file_3.value)
    upload_data.append('file_4', uploaded_file_4.value)
    upload_data.append('investor_ID', investor_ID.value)
    upload_data.append('investing_as', investing_as.value)
    upload_data.append('individual_verification_type', individual_verification_type.value)
    upload_data.append('sole_prop_verification_type', sole_prop_verification_type.value)
    upload_data.append('controller_verification_type', controller_verification_type.value)
    upload_data.append('owner_verification_type', owner_verification_type.value)
    upload_data.append('fund_ID', fund_ID.value)
    

    fetch(`${config.flask_url}/api/dwolla_reverification/documents_needed/`, {
        method: 'POST',
    headers: {
        'Accept': 'application/json',
    },
        body: upload_data
    })
    .then((response) => response.json())
    .then((data) => {
        documents_uploaded_successful.value = true,
        dwolla_customer_status.value = data.dwolla_customer_status,
        dwolla_beneficial_owner_status.value = data.dwolla_beneficial_owner_status,
        start_loader.value = false;
        modal_leave()
        sleep(700).then(() => { window.location.reload(); });
    })
    .catch(error => {
          alert("Error")
        modal_leave()
        sleep(700).then(() => { window.location.reload(); });
        console.error('There was an error!', error);
        start_loader.value = false;
    });
}


















    // -------------------------------------------------- MODAL -------------------------------------------------- //
    
    const modal_exit_anim = ref(true)
    const modal_exit_display = ref(true)
    
    
    
    // sleep time expects milliseconds
    function sleep (time) {
      return new Promise((resolve) => setTimeout(resolve, time));
    }
    
    
    
    
    function modal_leave(){
        modal_exit_anim.value = true
        sleep(1100).then(() => {
        modal_exit_display.value = true
        });
    }
    
    const modal = ref(null)
    

    
    // open modal on load
    sleep(500).then(() => {      // Do something after the sleep!
        modal_exit_display.value = false
        sleep(100).then(() => {
        modal_exit_anim.value = false
        });
    });
    
    
    
    

    
    
    </script>
    
    
    
    
    <style scoped>
    
    
    .loader_container{
    position:fixed;
    top:0;
    left:0;
    height:100vh;
    width:100vw;
    background-color:rgba(25, 120, 237 , 0.125);
    z-index:100;
    backdrop-filter: blur(20px);
    transition:all 1s ease-in-out;
    display: flex;
    justify-content: center;
    align-items: center;
}

.info_text{
    color:#fff;
}



    .form_container{
        background-color: #000;
        border-radius:50px;
        padding-top:5%
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

.business_submit{
    padding: 10px;
    color:white;
    background-color:green;
    border:1px solid #fff;
    width:50%;
    margin-left:25%;
    border-radius:50px;
    text-align:center;
    height:20px;
    cursor:pointer;
    transition: all 0.5s ease;
    margin-top:5%;
    margin-bottom:12%
}

.business_submit:hover{
    background-color:#171717;
    transition: all 0.5s ease;
}

.files_replace{
    padding: 10px;
    color:white;
    background-color:#001b5f;
    border:1px solid #fff;
    width:200px;
    border-radius:50px;
    text-align:center;
    height:20px;
    cursor:pointer;
    transition: all 0.5s ease;
}

.files_replace:hover{
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


.upload_image_business{
    width:25%;
    margin-bottom:50px;
    background-color:#171717;
    padding:50px;
    border-radius:50px;
    border: 1px solid v-bind(drop_success_border);
    transition: background-color 2s ease, border .5s ease;
}

.upload_image_business:hover{
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
    margin-top:-10%
}

.upload_box_business{
    padding-bottom:10vh;
display: grid;
grid-template-columns:repeat(2, 1fr);
grid-template-rows: repeat(2, 1fr);
grid-column-gap: 10px;
grid-row-gap: 0%;
    margin-left:6%;
    margin-top:-10%
}

.upload_box_solprop{
    padding-bottom:10vh;
display: grid;
grid-template-columns:repeat(3, 1fr);
grid-template-rows: repeat(1, 1fr);
grid-column-gap: 10px;
grid-row-gap: 0%;
    margin-left:6%;
    margin-top:0%
}

.upload_text_business{
    width:70%;
    margin-left:15%
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
.upload_title_business{
    text-decoration: underline;
  text-decoration-color: red;
  text-underline-offset: 4px;
  text-decoration-thickness: 2px;
  text-decoration-skip-ink: none;
  text-align: center;
  white-space: nowrap;
}

.drop_success{
    text-decoration: underline;
  text-decoration-color: #3a6df0;
  text-underline-offset: 8px;
  font-size:15px;
  width:40%;
  word-wrap: break-word;
}

.more_info_text{
    text-decoration: underline;
  text-decoration-color: #3a6df0;
  text-underline-offset: 3px;
  text-decoration-thickness: 1px;
  cursor:pointer;
}

.designation_text{
    color:#000;
    width:60%;
    margin-left:-7%;
    margin-top:0%;
    opacity:0;
    position:absolute;
    background-color:#fff;
    z-index:5;
    padding:6%;
    border-radius:10px;
    border: 4px solid rgba(25, 120, 237, 0.7);
    mix-blend-mode: normal;
    display: inline-block;
    transition: all .35s ease-in-out;
    visibility: hidden;
    font-size:12px
}

.designation_show{
    top:25%;
    opacity:1;
    visibility: visible;
    transition: all .35s ease-in-out;
}


.designation_hover{
    font-size:13px;
    padding:2px 7px;
    border: 1px solid #3a6df0;
    color: rgba(255,255,255, 0.4);
    border-radius:100%;
    cursor:pointer;
    transition: all .35s ease-in-out;
    background-color: #000;
    text-decoration: underline;
    text-decoration-color: #000;
}

.more_info_text:hover .designation_hover{
    background-color:rgba(25, 120, 237, 0.3);
    color:#fff;
    transition: all .35s ease-in-out;
}


.show_drop_error{
    text-decoration: underline;
  text-decoration-color: red;
  text-underline-offset: 8px;
  font-size:15px
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



















    /* ------------------------------------ Modal ------------------------------------ */
        /* ------------------------------------ Modal ------------------------------------ */
            /* ------------------------------------ Modal ------------------------------------ */



    .modal_hide_anim{
        transition: all 1s ease-in-out !important;
        opacity: 0 !important;
    }
    
    .modal_bix_hide_anim{
        transition: all .6s ease-in-out !important;
        transform: scale(0) !important;
    }
    
    .modal_hide_disp{
        display:none !important;
    }
    
    
    
    
    
    
    
    .modal_container{
        width:100vw;
        height:100vh;
        background-color:rgba(255, 255, 255, 0.1);
        position:fixed;
        top:0;
        left:0;
        z-index:1;
        display:flex;
        justify-content:center;
        align-items:center;
        backdrop-filter: blur(10px);
        transition: all 1s ease-in-out;
        opacity: 1;
    
    }
    .modal_popup{
        width:85%;
        height:75vh;
        background-color:rgb(0, 0, 0);
        z-index:10;
        border-radius:20px;
        margin-top:20px;
        border: rgba(25, 120, 237, 0.499) solid 2px;
        transition: all 1s ease-in-out;
        overflow-x:scroll
    }

    .modal_popup::-webkit-scrollbar {
  width: 8px !important;
  border-radius: 10px !important;
}

.modal_popup::-webkit-scrollbar-thumb {
  background: rgba(0, 149, 255, 1) !important;
  border-radius: 10px !important;
}
    
    .modal_info{
        font-size:30px;
        font-weight:600;
        color:#fff;
        margin-left:10%;
        margin-top:10%;
        width:80%;
        text-align:center
    }
    
    .login_redirect{
        width:40%;
        height:50px;
        background-color:rgb(25, 120, 237) ;
        margin-left: 30%;
        margin-top:7%;
        border-radius:100px;
        border:#fff solid 0px;
        cursor:pointer;
        font-size:20px;
        color:#fff;
          box-shadow: 0px 7px 10px rgb(25, 120, 237, .3);
      transition: outline 12s ease 1s;
    }
    
    .login_redirect:hover{
      box-shadow: 0px 10px 15px rgb(25, 120, 237, .5);
      transform: translateY(-3px);
      outline: 3px solid rgba(19, 218, 218, 0.6);
      transition: outline 12s ease 1s;
    } 
    
    
    .modal_exit{
        margin-top:20px;
        margin-left:90%;
        cursor:pointer;
        z-index: 10;
        position: relative;
        width:50px;
        height:50px;
    }
    
    .modal_exit:hover .horizontal_line{
        transform: rotate(180deg);
        transition: all 0.2s ease-in-out;
    }
    
    .modal_exit:hover .vertical_line{
        transform: rotate(-90deg);
        transition: all 0.5s ease-in-out;
    }
    .horizontal_line{
        height:1px;
        width:30px;
        background-color:rgb(255, 255, 255);
        top:25px;
        left:10px;
        transform: rotate(45deg);
        z-index:1000;
        position: absolute;
    }
    
    .vertical_line{
        width:1px;
        height:30px;
        top:11px;
        left:25px;
        background-color:#fff;
        transform: rotate(45deg);
        position: absolute;
    }
    
    
    
    
    @media only screen and (min-width: 0px) and (max-width: 576px) {
    
        .modal_popup{
        width:350px;
        height:400px;
    }
    
    .modal_exit{
        margin-top:10px;
        margin-left:290px;
        width:40px;
        height:40px;
    }
    
    
    }
    
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
    
    
    
    </style>