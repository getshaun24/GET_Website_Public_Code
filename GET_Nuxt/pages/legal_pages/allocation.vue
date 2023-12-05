<template>
    
    <Header/>
    
        <GSAPScrollSmoother>
    
<h5 class="page_title" data-speed="0.6" data-lag="0.2">Allocation Policy</h5>


<div class="main_text">

<p>
GET Resources Group LLC (“GET”) operates an investment Holding Company (the “Holdings”) on which eligible investors (“Holdings Investors”) may browse investment opportunities and complete investments in private placement transactions indirectly through GET and its affiliates (“GET Holdings”). The private placement transactions that are available are primarily in pre-IPO securities of private companies.
<br><br>
GET has two subsidiary affiliates:
     1. GET Resources Group LLC, the Manager and;
     2. GET Resources Holdings LLC, the Holding company.
     <br><br>
GET Holdings invests in private companies and or privately held securities, some of which are pre-IPO securities of private companies.
<br><br>
GET and its affiliates believe that opportunities must be allocated in a fair and equitable manner with no individual, group, or client being favored or disfavored over other individuals, groups, or clients. At the same time, GET’s allocation policy must take into account the nature of the private, pre-IPO investment opportunities and the practicality of adopting and implementing any particular allocation methodology. Due to constraints on the number of investors under various exemptions under applicable law other capacity constraints that may relate to specific investment opportunities, and other factors, pro rata allocations to investors are often infeasible.
<br><br>
To (i) ensure the fair and equitable allocation of investment opportunities GET has established the following allocation policies relating to investment opportunities available in GET Holdings in which a Manager makes an investment commitment.
<br><br>
<ul>
     <li> Certain employees of GET participate in preparing and/or reviewing email distributions regarding Platform Opportunities (the “Investor Email”), and otherwise will have knowledge of opportunities before such information is given to investors. In addition, one or more of those GET employees are, or in the future will be, members of the investment committee. To avoid any conflicts of interest related to such prior knowledge, and given the anticipated difficulties of implementing a pro rata allocation methodology for pre-IPO securities, GET will generally allocate all investment opportunities to the fullest extent possible on a first-come, first-served rotational basis based on the order in which a commitment to an opportunity was made. An Investor that is closed out of a particular opportunity to invest in a security will be rotated in to the next allocable opportunity in that investment. In evaluating which investor is allocated a particular opportunity at a given time, GET may also take into account such factors as historical investments, fairness to other investors, the interests and investment objectives of a particular investor, available investment capacity, proposed investment size, whether an investor has transacted previously with GET, and other timing considerations with respect to the particular investment (such as the ability to close on any particular investment within a given time frame) (“Additional Factors”).</li>
     <br><br>
     <li> If an opportunity does not close on the entire contemplated amount, allocations to investors in that transaction shall be made to interested investors on a first-come, first-served rotational basis based on the order in which a commitment to an investment opportunity was made.</li>
     <br><br>
     <li> GET shall not commit to an investment in order for such an opportunity to achieve a required minimum in order to proceed.
        <br>&nbsp;&nbsp; ⦾ Where GET has committed to an investment within the final 3 days of its being open, GET’s managers or investment committee or similar authority must explain in writing its basis for making the investment or otherwise demonstrate that the commitment was not made for the purpose of achieving a commitment minimum.</li>
         <br><br>
     <li> If multiple GET Investors with the same investment strategy, or overlapping investment strategies, seek to invest in individual opportunities not part of GET Holdings:
        <br> &nbsp;&nbsp; ⦾ Multiple investments may be accepted in the requested investment size for each GET Holding company if the total available size permits.
        <br> &nbsp;&nbsp; ⦾ If the available size is less than the total requested investment size for all GET Holdings seeking an investment, the investment shall be allocated to each GET Holding company based on the allocational and criteria-based methodology set forth above in good faith, including the Additional Factors.
        <br>&nbsp;&nbsp; ⦾ In making allocations, the investment committee shall not allocate between the availability of carried interest, performance relative to an applicable high-water mark should one exist, or the presence or absence of any affiliated investors, or the relative size of affiliated investments in the Holding company.</li>
         <br><br>
     <li> Investors shall be treated equally and consistently with each other. As stated above, all Investment Opportunities shall be allocated on an allocational basis to GET Holdings and individual investors, i.e., based on the order in which a commitment was made. Such allocation priority is consistent with the priority allocated to individual investors.
        <br> &nbsp;&nbsp; ⦾ A Discretionary Fund that commits to an oversubscribed individual investment opportunity shall be treated like any other investor with respect to a wait list, unallocated or partially allocated demand, or other similar procedure, including any opportunities to subscribe to a subsequent fund prior to the Investor Email.
        </li>
        <br><br>
     <li> Investments with a waitlist, or which are expected to be oversubscribed, may be allocated to Investors in an order determined by the date of their completed reservation, generally on a first-come, first-served rotational basis, subject to the Additional Factors (described above).</li>
     <br><br>
     <li> Deviation from these Allocation Policies, on a case-by-case basis, is permitted. However, any such deviation must be fair and equitable and documented in writing (including the methodology actually used).</li>
     <br><br>
     <li> These Allocation Policies shall be disclosed prominently (i) on GET’s website, (ii) in the offering documents of each investment opportunity, and (iii) the offering documents of each Holding Company.</li>
     <br><br>
     <li> With respect to Discretionary Funds that have closed prior to the adoption of these Allocation Policies and whose investment periods have not yet expired, a written notification of these Allocation Policies shall be provided to all investors in such situations.</li>
     <br><br>
    </ul>
* Eligibility, as it applies to Platform Investors and Discretionary Fund Investors means, at a minimum, meeting the criteria necessary to be deemed an “accredited investor” as defined in Regulation D under the Securities Act of 1933, as amended, as well as such other eligibility criteria imposed by GET or its affiliates with respect to investment in GET Holdings or individual investment. Those criteria may include additional eligibility criteria related to “qualified purchasers”, “qualified clients” or other categories of investors under applicable securities laws, as applicable to a particular investment opportunity. Eligibility shall also include any applicable know-your-customer, anti-money-laundering, investment suitability or other requirements applied by GET or its affiliates in its sole discretion.
</p>


</div>








<Footer/>
        </GSAPScrollSmoother>
    

</template>

<script setup>

const title_move = ref('100%');


onMounted(() => {
title_move.value = '35%';
})

</script>


<style scoped>

.page_title{
    background-color:#fff;
    background-image: url('~/assets/content/careers/careers_2.jpg');
    padding:25px;
    width:65%;
    margin-left:v-bind(title_move);
    text-align: center;
    border-top-left-radius: 10px;
    border-bottom-left-radius: 10px;
    z-index:10000;
    color: #fff;
    filter: drop-shadow(5px 3px 5px #ffffff21);
    transition: margin-left 1.75s ease 1.5s;
}

.main_text{
    width:80%;
    margin-left:10%;
    margin-bottom:10%;
    margin-top:30%
}

.section_title{
    font-size:35px
}

.section_subtitle{
    text-decoration: underline;
    text-underline-offset: 5px;
    text-decoration-thickness: 1px;
    text-decoration-color: #1978ed;
}

</style>