<template>
    

    <div class="input_wrap">
            <select  v-model="value" required class="select_black">
                <option value="" disabled selected hidden></option>
            <option value="9ed3f669-7d6f-11e3-b545-5404a6144203">Food Retail and Service</option>
          <option value="9ed41d89-7d6f-11e3-beff-5404a6144203">Manufacturing</option>
          <option value="9ed35a3b-7d6f-11e3-83c8-5404a6144203">Business to Business</option>
          <option value="9ed4449e-7d6f-11e3-a32d-5404a6144203">Services</option>
          <option value="9ed3a866-7d6f-11e3-a0ce-5404a6144203">Entertainment and Media</option>
          <option value="9ed41d75-7d6f-11e3-b151-5404a6144203">Home and Garden</option>
          <option value="9ed35a29-7d6f-11e3-930b-5404a6144203">Baby</option>
          <option value="9ed492c6-7d6f-11e3-80f4-5404a6144203">Travel</option>
          <option value="9ed38152-7d6f-11e3-9042-5404a6144203">Clothing, Accessories, and Shoes</option>
          <option value="9ed3f686-7d6f-11e3-af6e-5404a6144203">Health and Personal Care</option>
          <option value="9ed35a2e-7d6f-11e3-a5cf-5404a6144203">Beauty and fragrances</option>
          <option value="9ed3a846-7d6f-11e3-8a79-5404a6144203">Computers, Accessories, and Services</option>
          <option value="9ed44496-7d6f-11e3-865d-5404a6144203">Retail</option>
          <option value="9ed492bc-7d6f-11e3-9a1b-5404a6144203">Toys and Hobbies</option>
          <option value="9ed4448d-7d6f-11e3-aab2-5404a6144203">Pets and Animals</option>
          <option value="9ed3a854-7d6f-11e3-a193-5404a6144203">Education</option>
          <option value="9ed248ae-7d6f-11e3-ba6e-5404a6144203">Arts, Crafts, and Collectibles</option>
          <option value="9ed3cf5f-7d6f-11e3-8af8-5404a6144203">Financial Services and Products</option>
          <option value="9ed3f67d-7d6f-11e3-bf40-5404a6144203">Government</option>
          <option value="9ed4b9bc-7d6f-11e3-9133-5404a6144203">Vehicle Sales</option>
          <option value="9ed44486-7d6f-11e3-89f8-5404a6144203">Nonprofit</option>
          <option value="9ed4b9c6-7d6f-11e3-a156-5404a6144203">Vehicle Service and Accessories</option>
          <option value="9ed3a85b-7d6f-11e3-8995-5404a6144203">Electronics and Telecom</option>
          <option value="9ed35a32-7d6f-11e3-9830-5404a6144203">Books and Magazines</option>
          <option value="9ed44492-7d6f-11e3-98d1-5404a6144203">Religion and Spirituality (for profit)</option>
          <option value="9ed492ac-7d6f-11e3-a2d2-5404a6144203">Sports and Outdoors</option>
          <option value="9ed3f677-7d6f-11e3-96a2-5404a6144203">Gifts and flowers</option>
            </select>
                <label class="label_black">Industry Classification</label>
        </div>






</template>




<script setup>


const props = defineProps(['industry_classification'])
const emit = defineEmits(['update:industry_classification'])

const value = computed({
  get() {
    return props.industry_classification
  },
  set(value) {
    emit('update:industry_classification', value)
  }
})

</script>



