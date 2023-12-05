<template>
    

    <client-only>
      
      <ve-progress 
      :progress="50" 
      empty-color="rgb(25, 120, 237, 0.8)" 
      :thickness="13" 
      :empty-thickness="5"
      :loading="true"
      :size="300"
      line-mode="in 10"
      line-position="out 10"
      :loader="{ color: 'rgb(25, 120, 237)', lineMode: 'in 10', opacity: 1, duration: 1300 }" 
      animation="reverse 700 400"
      :gap="20"
      dot="10 blue"
      />


    </client-only>

    
</template>


<script setup>

// const gradient1 = {
//       radial: true,
//       colors: [
//         {
//           color: "#3260FC",
//           offset: "50",
//           opacity: "1",
//         },
//         {
//           color: "#3260FC",
//           offset: "70",
//           opacity: "0.15",
//         },
//         {
//           color: "#3260FC",
//           offset: "70",
//           opacity: "0.2",
//         },
//         {
//           color: "#3260FC",
//           offset: "90",
//           opacity: ".8",
//         },
//         {
//           color: "#3260FC",
//           offset: "60",
//           opacity: "0",
//         },
//         {
//           color: "#3260FC",
//           offset: "20",
//           opacity: "0.05",
//         },
//       ],
//     }
    
    </script>