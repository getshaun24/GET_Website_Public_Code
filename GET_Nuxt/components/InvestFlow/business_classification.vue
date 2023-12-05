<template>
    
    <div class="input_wrap">
      
            <select v-model="value" required class="select_white">
              <option value="" disabled selected hidden></option>

              <option v-if="no_industry_selected" value="" >Please Select An industry First</option>


          <option v-if="food_retail_and_service" value="9ed3f671-7d6f-11e3-803c-5404a6144203">Gourmet Foods</option>
          <option v-if="food_retail_and_service" value="9ed3f66c-7d6f-11e3-86ae-5404a6144203">Distilleries</option>
          <option v-if="food_retail_and_service" value="9ed3f66a-7d6f-11e3-8acd-5404a6144203">Breweries</option>
          <option v-if="food_retail_and_service" value="9ed3f66d-7d6f-11e3-9101-5404a6144203">Alcoholic Beverage Drinking Places</option>
          <option v-if="food_retail_and_service" value="9ed3f66e-7d6f-11e3-9480-5404a6144203">Beer, Wine, and Liquor Store</option>
          <option v-if="food_retail_and_service" value="9ed3f66b-7d6f-11e3-95ac-5404a6144203">Wineries</option>
          <option v-if="food_retail_and_service" value="9ed3f674-7d6f-11e3-9619-5404a6144203">Tobacco</option>
          <option v-if="food_retail_and_service" value="9ed3f673-7d6f-11e3-adb1-5404a6144203">Restaurant</option>
          <option v-if="food_retail_and_service" value="9ed3f676-7d6f-11e3-af8e-5404a6144203">Supplement Store</option>
          <option v-if="food_retail_and_service" value="9ed3f675-7d6f-11e3-afad-5404a6144203">Pharmacy and Drugstore</option>
          <option v-if="food_retail_and_service" value="9ed3f670-7d6f-11e3-b1ce-5404a6144203">Coffee and Tea</option>
          <option v-if="food_retail_and_service" value="9ed3f66f-7d6f-11e3-b1df-5404a6144203">Catering Services</option>
          <option v-if="food_retail_and_service" value="9ed3f672-7d6f-11e3-b67a-5404a6144203">Specialty and Miscellaneous Food Store</option>
          <option v-if="manufacturing" value="9ed41d96-7d6f-11e3-804a-5404a6144203">Nonmetallic Mineral Product Manufacturing</option>
          <option v-if="manufacturing" value="9ed44484-7d6f-11e3-8b25-5404a6144203">Furniture and Related Product Manufacturing</option>
          <option v-if="manufacturing" value="9ed41d95-7d6f-11e3-8b36-5404a6144203">Plastics and Rubber Products Manufacturing</option>
          <option v-if="manufacturing" value="9ed41d94-7d6f-11e3-8dc3-5404a6144203">Chemical Manufacturing</option>
          <option v-if="manufacturing" value="9ed41d97-7d6f-11e3-92aa-5404a6144203">Primary Metal Manufacturing</option>
          <option v-if="manufacturing" value="9ed44483-7d6f-11e3-95ce-5404a6144203">Transportation Equipment Manufacturing</option>
          <option v-if="manufacturing" value="9ed41d8f-7d6f-11e3-9762-5404a6144203">Leather and Allied Product Manufacturing</option>
          <option v-if="manufacturing" value="9ed41d8d-7d6f-11e3-9a24-5404a6144203">Textile Product Mills</option>
          <option v-if="manufacturing" value="9ed41d92-7d6f-11e3-a0ad-5404a6144203">Printing and Related Support Activities</option>
          <option v-if="manufacturing" value="9ed44485-7d6f-11e3-a2bc-5404a6144203">Miscellaneous Manufacturing</option>
          <option v-if="manufacturing" value="9ed41d8a-7d6f-11e3-a5dc-5404a6144203">Food Manufacturing</option>
          <option v-if="manufacturing" value="9ed41d98-7d6f-11e3-a88a-5404a6144203">Fabricated Metal Product Manufacturing</option>
          <option v-if="manufacturing" value="9ed41d90-7d6f-11e3-a8f0-5404a6144203">Wood product manufacturing</option>
          <option v-if="manufacturing" value="9ed44481-7d6f-11e3-aa45-5404a6144203">Computer and Electronic Product Manufacturing</option>
          <option v-if="manufacturing" value="9ed41d91-7d6f-11e3-b262-5404a6144203">Paper Manufacturing</option>
          <option v-if="manufacturing" value="9ed44480-7d6f-11e3-b289-5404a6144203">Machinery Manufacturing</option>
          <option v-if="manufacturing" value="9ed41d8e-7d6f-11e3-b45c-5404a6144203">Apparel Manufacturing</option>
          <option v-if="manufacturing" value="9ed41d93-7d6f-11e3-b677-5404a6144203">Petroleum and Coal Products Manufacturing</option>
          <option v-if="manufacturing" value="9ed41d8b-7d6f-11e3-b721-5404a6144203">Beverage and Tobacco Product Manufacturing</option>
          <option v-if="manufacturing" value="9ed44482-7d6f-11e3-babe-5404a6144203">Electrical Equipment, Appliance, and Component Manufacturing</option>
          <option v-if="manufacturing" value="9ed41d8c-7d6f-11e3-bce3-5404a6144203">Textile Mills</option>
          <option v-if="b_2_b" value="9ed38132-7d6f-11e3-815d-5404a6144203">Agriculture - Animal Production and Aquaculture</option>
          <option v-if="b_2_b" value="9ed38131-7d6f-11e3-828e-5404a6144203">Agriculture - Fruit, Vegetable, and Crop Production</option>
          <option v-if="b_2_b" value="9ed3813c-7d6f-11e3-82cc-5404a6144203">Consulting Services</option>
          <option v-if="b_2_b" value="9ed38134-7d6f-11e3-8529-5404a6144203">Agriculture - fishing, hunting, and trapping</option>
          <option v-if="b_2_b" value="9ed38138-7d6f-11e3-862a-5404a6144203">Construction - residential building</option>
          <option v-if="b_2_b" value="9ed3813e-7d6f-11e3-86eb-5404a6144203">Consumer goods rental</option>
          <option v-if="b_2_b" value="9ed3813f-7d6f-11e3-8840-5404a6144203">Commercial and industrial goods rental</option>
          <option v-if="b_2_b" value="9ed38146-7d6f-11e3-89d6-5404a6144203">Marketing</option>
          <option v-if="b_2_b" value="9ed3814a-7d6f-11e3-8c10-5404a6144203">Publishing</option>
          <option v-if="b_2_b" value="9ed3814d-7d6f-11e3-8eb5-5404a6144203">Shipping and packing</option>
          <option v-if="b_2_b" value="9ed3814e-7d6f-11e3-9087-5404a6144203">Stenographic and secretarial support services</option>
          <option v-if="b_2_b" value="9ed38147-7d6f-11e3-94f8-5404a6144203">Multi-level marketing</option>
          <option v-if="b_2_b" value="9ed38148-7d6f-11e3-9820-5404a6144203">Office and commercial furniture</option>
          <option v-if="b_2_b" value="9ed38133-7d6f-11e3-9892-5404a6144203">Agriculture - forestry and logging</option>
          <option v-if="b_2_b" value="9ed3814b-7d6f-11e3-9ed9-5404a6144203">Printing</option>
          <option v-if="b_2_b" value="9ed38145-7d6f-11e3-a442-5404a6144203">Mailing lists</option>
          <option v-if="b_2_b" value="9ed38144-7d6f-11e3-a4f3-5404a6144203">Industrial and manufacturing supplies</option>
          <option v-if="b_2_b" value="9ed38141-7d6f-11e3-a5d2-5404a6144203">Commercial and industrial goods repair and maintenance</option>
          <option v-if="b_2_b" value="9ed3814c-7d6f-11e3-a77b-5404a6144203">Quick copy and reproduction services</option>
          <option v-if="b_2_b" value="9ed38137-7d6f-11e3-a92b-5404a6144203">Commercial photography, art, and graphics</option>
          <option v-if="b_2_b" value="9ed38135-7d6f-11e3-a9f8-5404a6144203">Architectural, engineering, and surveying services</option>
          <option v-if="services_other" value="9ed46baf-7d6f-11e3-816d-5404a6144203">Online dating</option>
          <option v-if="services_other" value="9ed492a7-7d6f-11e3-8278-5404a6144203">Vision care</option>
          <option v-if="services_other" value="9ed46b98-7d6f-11e3-8308-5404a6144203">Consumer goods rental</option>
          <option v-if="services_other" value="9ed46bac-7d6f-11e3-83b7-5404a6144203">Printing</option>
          <option v-if="services_other" value="9ed444a1-7d6f-11e3-858e-5404a6144203">All other personal services</option>
          <option v-if="services_other" value="9ed444a5-7d6f-11e3-85d6-5404a6144203">Cleaning and maintenance</option>
          <option v-if="services_other" value="9ed46bb2-7d6f-11e3-861c-5404a6144203">Investigation and security services</option>
          <option v-if="services_other" value="9ed444a8-7d6f-11e3-87fd-5404a6144203">Computer network services</option>
          <option v-if="services_other" value="9ed492a5-7d6f-11e3-8d8f-5404a6144203">Telecommunication services</option>
          <option v-if="services_other" value="9ed46b97-7d6f-11e3-8dd7-5404a6144203">Entertainment</option>
          <option v-if="services_other" value="9ed492a3-7d6f-11e3-8f04-5404a6144203">Swimming pool services</option>
          <option v-if="services_other" value="9ed444a0-7d6f-11e3-8fb1-5404a6144203">Warehouse clubs and supercenters</option>
          <option v-if="services_other" value="9ed46bb5-7d6f-11e3-9631-5404a6144203">Real estate agent</option>
          <option v-if="services_other" value="9ed46b9f-7d6f-11e3-96b0-5404a6144203">Health and beauty spas</option>
          <option v-if="services_other" value="9ed46b91-7d6f-11e3-9704-5404a6144203">Consulting services</option>
          <option v-if="services_other" value="9ed46b95-7d6f-11e3-970b-5404a6144203">eCommerce services</option>
          <option v-if="services_other" value="9ed492a8-7d6f-11e3-9894-5404a6144203">Watch, clock, and jewelry repair</option>
          <option v-if="services_other" value="9ed492ab-7d6f-11e3-9907-5404a6144203">Real estate - other</option>
          <option v-if="services_other" value="9ed46bae-7d6f-11e3-9966-5404a6144203">Storage</option>
          <option v-if="services_other" value="9ed46ba9-7d6f-11e3-9b47-5404a6144203">Medical care</option>
          <option v-if="services_other" value="9ed492a1-7d6f-11e3-9ccf-5404a6144203">Services not elsewhere classified</option>
          <option v-if="services_other" value="9ed46ba1-7d6f-11e3-9d1b-5404a6144203">Importing and exporting</option>
          <option v-if="services_other" value="9ed444a4-7d6f-11e3-9dc4-5404a6144203">Child care services</option>
          <option v-if="services_other" value="9ed46ba3-7d6f-11e3-9efe-5404a6144203">Insurance - auto and home</option>
          <option v-if="services_other" value="9ed46b92-7d6f-11e3-9f08-5404a6144203">Counseling services</option>
          <option v-if="services_other" value="9ed46b9e-7d6f-11e3-9fec-5404a6144203">Graphic and commercial design</option>
          <option v-if="services_other" value="9ed46bad-7d6f-11e3-a006-5404a6144203">Moving</option>
          <option v-if="services_other" value="9ed46b9a-7d6f-11e3-a11b-5404a6144203">Event and wedding planning</option>
          <option v-if="services_other" value="9ed46b96-7d6f-11e3-a2ee-5404a6144203">Electronic repair and maintenance</option>
          <option v-if="services_other" value="9ed46bb3-7d6f-11e3-a347-5404a6144203">Quick copy and reproduction services</option>
          <option v-if="services_other" value="9ed46bb0-7d6f-11e3-a35d-5404a6144203">Photofinishing</option>
          <option v-if="services_other" value="9ed46bb4-7d6f-11e3-a3c3-5404a6144203">Radio, television, and stereo repair</option>
          <option v-if="services_other" value="9ed46bab-7d6f-11e3-a401-5404a6144203">Publishing</option>
          <option v-if="services_other" value="9ed46ba8-7d6f-11e3-a726-5404a6144203">Lottery and contests</option>
          <option v-if="services_other" value="9ed492aa-7d6f-11e3-aca1-5404a6144203">Research and development</option>
          <option v-if="services_other" value="9ed46bb1-7d6f-11e3-acac-5404a6144203">Photographic studios - portraits</option>
          <option v-if="services_other" value="9ed444a6-7d6f-11e3-ad1c-5404a6144203">Commercial photography, art, and graphics</option>
          <option v-if="services_other" value="9ed46b9c-7d6f-11e3-ad21-5404a6144203">Construction - residential building</option>
          <option v-if="services_other" value="9ed46baa-7d6f-11e3-ad74-5404a6144203">Membership clubs and organizations</option>
          <option v-if="services_other" value="9ed46b94-7d6f-11e3-ad88-5404a6144203">Dental care</option>
          <option v-if="services_other" value="9ed46ba6-7d6f-11e3-ae95-5404a6144203">Legal services and attorneys</option>
          <option v-if="services_other" value="9ed492a9-7d6f-11e3-af4b-5404a6144203">Mining</option>
          <option v-if="services_other" value="9ed46ba5-7d6f-11e3-b01c-5404a6144203">Landscaping and horticultural</option>
          <option v-if="services_other" value="9ed46ba2-7d6f-11e3-b242-5404a6144203">Information retrieval services</option>
          <option v-if="services_other" value="9ed46ba4-7d6f-11e3-b31e-5404a6144203">Insurance - life and annuity</option>
          <option v-if="services_other" value="9ed46b9b-7d6f-11e3-b391-5404a6144203">Gambling</option>
          <option v-if="services_other" value="9ed46b93-7d6f-11e3-b3b9-5404a6144203">Courier services</option>
          <option v-if="services_other" value="9ed492a4-7d6f-11e3-b3dc-5404a6144203">Tailors and alterations</option>
          <option v-if="services_other" value="9ed444a7-7d6f-11e3-b42d-5404a6144203">Computer and data processing services</option>
          <option v-if="services_other" value="9ed46b9d-7d6f-11e3-b5da-5404a6144203">Construction - nonresidential building</option>
          <option v-if="services_other" value="9ed46ba0-7d6f-11e3-b775-5404a6144203">IDs, licenses, and passports</option>
          <option v-if="services_other" value="9ed444a3-7d6f-11e3-b785-5404a6144203">Carpentry</option>
          <option v-if="services_other" value="9ed46ba7-7d6f-11e3-b85c-5404a6144203">Local delivery service</option>
          <option v-if="services_other" value="9ed4449f-7d6f-11e3-b867-5404a6144203">Advertising and public relations</option>
          <option v-if="services_other" value="9ed46bb7-7d6f-11e3-b950-5404a6144203">Reupholstery and furniture repair</option>
          <option v-if="services_other" value="9ed46bb6-7d6f-11e3-b9b2-5404a6144203">Rental property management</option>
          <option v-if="services_other" value="9ed444a2-7d6f-11e3-ba23-5404a6144203">Career services</option>
          <option v-if="services_other" value="9ed492a6-7d6f-11e3-bbd2-5404a6144203">Utilities</option>
          <option v-if="services_other" value="9ed46b99-7d6f-11e3-be4c-5404a6144203">Commercial and industrial goods rental</option>
          <option v-if="services_other" value="9ed492a2-7d6f-11e3-bfb3-5404a6144203">Shipping and packing</option>
          <option v-if="entertainment_and_media" value="9ed3cf58-7d6f-11e3-81a4-5404a6144203">Toys and games</option>
          <option v-if="entertainment_and_media" value="9ed3cf50-7d6f-11e3-8ae8-5404a6144203">Music</option>
          <option v-if="entertainment_and_media" value="9ed3cf5c-7d6f-11e3-8d0e-5404a6144203">Gambling</option>
          <option v-if="entertainment_and_media" value="9ed3cf53-7d6f-11e3-8ee9-5404a6144203">Cable, satellite, and other pay TV and radio broadcasting</option>
          <option v-if="entertainment_and_media" value="9ed3cf59-7d6f-11e3-9158-5404a6144203">Slot machines</option>
          <option v-if="entertainment_and_media" value="9ed3cf57-7d6f-11e3-921d-5404a6144203">Theater tickets</option>
          <option v-if="entertainment_and_media" value="9ed3cf4f-7d6f-11e3-97ea-5404a6144203">Motion picture and video</option>
          <option v-if="entertainment_and_media" value="9ed3cf5a-7d6f-11e3-9a99-5404a6144203">Digital content</option>
          <option v-if="entertainment_and_media" value="9ed3cf5b-7d6f-11e3-a368-5404a6144203">Entertainers</option>
          <option v-if="entertainment_and_media" value="9ed3a867-7d6f-11e3-a6e4-5404a6144203">Memorabilia</option>
          <option v-if="entertainment_and_media" value="9ed3cf52-7d6f-11e3-b0da-5404a6144203">Music store - CDs, cassettes and albums</option>
          <option v-if="entertainment_and_media" value="9ed3cf5d-7d6f-11e3-b35e-5404a6144203">Online gaming</option>
          <option v-if="entertainment_and_media" value="9ed3cf55-7d6f-11e3-b43c-5404a6144203">Adult digital content</option>
          <option v-if="entertainment_and_media" value="9ed3cf51-7d6f-11e3-b49f-5404a6144203">Movie store - DVDs, videotapes</option>
          <option v-if="entertainment_and_media" value="9ed3cf5e-7d6f-11e3-b9d5-5404a6144203">Video games and systems</option>
          <option v-if="entertainment_and_media" value="9ed3cf56-7d6f-11e3-ba87-5404a6144203">Concert tickets</option>
          <option v-if="entertainment_and_media" value="9ed3cf54-7d6f-11e3-bf23-5404a6144203">Cable and other subscription programming</option>
          <option v-if="home_and_garden" value="9ed41d76-7d6f-11e3-81ef-5404a6144203">Antiques</option>
          <option v-if="home_and_garden" value="9ed41d80-7d6f-11e3-857a-5404a6144203">Glass, paint, and wallpaper</option>
          <option v-if="home_and_garden" value="9ed41d77-7d6f-11e3-8cda-5404a6144203">Appliances</option>
          <option v-if="home_and_garden" value="9ed41d7c-7d6f-11e3-8fb6-5404a6144203">Exterminating and disinfecting services</option>
          <option v-if="home_and_garden" value="9ed41d7b-7d6f-11e3-9534-5404a6144203">Drapery, window covering, and upholstery</option>
          <option v-if="home_and_garden" value="9ed41d81-7d6f-11e3-9904-5404a6144203">Hardware and tools</option>
          <option v-if="home_and_garden" value="9ed41d86-7d6f-11e3-9e98-5404a6144203">Rugs and carpets</option>
          <option v-if="home_and_garden" value="9ed41d7e-7d6f-11e3-a3fc-5404a6144203">Furniture</option>
          <option v-if="home_and_garden" value="9ed41d7a-7d6f-11e3-ae21-5404a6144203">Construction material</option>
          <option v-if="home_and_garden" value="9ed41d7f-7d6f-11e3-b918-5404a6144203">Lawn and garden equipment and supplies</option>
          <option v-if="home_and_garden" value="9ed41d84-7d6f-11e3-bc20-5404a6144203">Home furnishings store</option>
          <option v-if="home_and_garden" value="9ed41d78-7d6f-11e3-bd3f-5404a6144203">Art dealers and galleries</option>
          <option v-if="baby" value="9ed35a2d-7d6f-11e3-8284-5404a6144203">Safety and health</option>
          <option v-if="baby" value="9ed35a2b-7d6f-11e3-942f-5404a6144203">Furniture</option>
          <option v-if="baby" value="9ed35a2a-7d6f-11e3-b976-5404a6144203">Children's and baby's clothing</option>
          <option v-if="travel" value="9ed4b9b8-7d6f-11e3-8329-5404a6144203">Tours</option>
          <option v-if="travel" value="9ed4b9b0-7d6f-11e3-8f2f-5404a6144203">Bus line</option>
          <option v-if="travel" value="9ed492c7-7d6f-11e3-8fc5-5404a6144203">Airline</option>
          <option v-if="travel" value="9ed4b9b5-7d6f-11e3-9031-5404a6144203">Sporting and recreation camps</option>
          <option v-if="travel" value="9ed4b9b1-7d6f-11e3-9ce7-5404a6144203">Cruises</option>
          <option v-if="travel" value="9ed4b9b2-7d6f-11e3-a1d5-5404a6144203">Lodging and accommodations</option>
          <option v-if="travel" value="9ed4b9b7-7d6f-11e3-a615-5404a6144203">Timeshares</option>
          <option v-if="travel" value="9ed4b9b3-7d6f-11e3-aea7-5404a6144203">Luggage and leather goods</option>
          <option v-if="travel" value="9ed4b9bb-7d6f-11e3-af9f-5404a6144203">Travel agency</option>
          <option v-if="travel" value="9ed4b9b6-7d6f-11e3-b843-5404a6144203">Taxicabs and limousines</option>
          <option v-if="travel" value="9ed492c8-7d6f-11e3-ba44-5404a6144203">Auto rental</option>
          <option v-if="travel" value="9ed4b9ba-7d6f-11e3-bbf4-5404a6144203">Transportation services - other</option>
          <option v-if="travel" value="9ed4b9b4-7d6f-11e3-bcfd-5404a6144203">Recreational services</option>
          <option v-if="travel" value="9ed4b9b9-7d6f-11e3-bf00-5404a6144203">Trailer parks and campgrounds</option>
          <option v-if="clothing_accessories_shoes" value="9ed38155-7d6f-11e3-83c3-5404a6144203">Women's clothing</option>
          <option v-if="clothing_accessories_shoes" value="9ed3a841-7d6f-11e3-954f-5404a6144203">Military and civil service uniforms</option>
          <option v-if="clothing_accessories_shoes" value="9ed38153-7d6f-11e3-97e3-5404a6144203">Children's and baby's clothing</option>
          <option v-if="clothing_accessories_shoes" value="9ed38154-7d6f-11e3-9b0d-5404a6144203">Men's clothing</option>
          <option v-if="clothing_accessories_shoes" value="9ed3a844-7d6f-11e3-9d68-5404a6144203">Wholesale - precious stones and metals</option>
          <option v-if="clothing_accessories_shoes" value="9ed3a840-7d6f-11e3-a314-5404a6144203">Shoes</option>
          <option v-if="clothing_accessories_shoes" value="9ed3a845-7d6f-11e3-b307-5404a6144203">Fashion jewelry</option>
          <option v-if="clothing_accessories_shoes" value="9ed3a842-7d6f-11e3-bba3-5404a6144203">Accessories</option>
          <option v-if="clothing_accessories_shoes" value="9ed3a843-7d6f-11e3-bbb4-5404a6144203">Retail - fine jewelry and watches</option>
          <option v-if="health_personal_care" value="9ed41d70-7d6f-11e3-851b-5404a6144203">Dental care</option>
          <option v-if="health_personal_care" value="9ed41d74-7d6f-11e3-8b34-5404a6144203">Vitamins and supplements</option>
          <option v-if="health_personal_care" value="9ed41d73-7d6f-11e3-963f-5404a6144203">Vision care</option>
          <option v-if="health_personal_care" value="9ed3f687-7d6f-11e3-a1ac-5404a6144203">Pharmacy and drugstore</option>
          <option v-if="health_personal_care" value="9ed41d71-7d6f-11e3-abed-5404a6144203">Medical care</option>
          <option v-if="health_personal_care" value="9ed41d72-7d6f-11e3-b770-5404a6144203">Medical equipment and supplies</option>
          <option v-if="beauty_fragrances" value="9ed35a2f-7d6f-11e3-8593-5404a6144203">Bath and body</option>
          <option v-if="beauty_fragrances" value="9ed35a30-7d6f-11e3-b9d5-5404a6144203">Fragrances and perfumes</option>
          <option v-if="beauty_fragrances" value="9ed35a31-7d6f-11e3-bf68-5404a6144203">Makeup and cosmetics</option>
          <option v-if="computers_accessories_services" value="9ed3a84b-7d6f-11e3-8661-5404a6144203">Maintenance and repair services</option>
          <option v-if="computers_accessories_services" value="9ed3a84e-7d6f-11e3-87df-5404a6144203">Online gaming</option>
          <option v-if="computers_accessories_services" value="9ed3a851-7d6f-11e3-92a4-5404a6144203">Software</option>
          <option v-if="computers_accessories_services" value="9ed3a84c-7d6f-11e3-9a6e-5404a6144203">Monitors and projectors</option>
          <option v-if="computers_accessories_services" value="9ed3a84d-7d6f-11e3-9eca-5404a6144203">Networking</option>
          <option v-if="computers_accessories_services" value="9ed3a853-7d6f-11e3-a35d-5404a6144203">Web hosting and design</option>
          <option v-if="computers_accessories_services" value="9ed3a852-7d6f-11e3-aba3-5404a6144203">Training services</option>
          <option v-if="computers_accessories_services" value="9ed3a850-7d6f-11e3-ad7d-5404a6144203">Peripherals</option>
          <option v-if="computers_accessories_services" value="9ed3a848-7d6f-11e3-af5a-5404a6144203">Desktops, laptops, and notebooks</option>
          <option v-if="computers_accessories_services" value="9ed3a84f-7d6f-11e3-b1a4-5404a6144203">Parts and accessories</option>
          <option v-if="computers_accessories_services" value="9ed3a84a-7d6f-11e3-b682-5404a6144203">eCommerce services</option>
          <option v-if="computers_accessories_services" value="9ed3a847-7d6f-11e3-b813-5404a6144203">Computer and data processing services</option>
          <option v-if="retail" value="9ed44498-7d6f-11e3-87b4-5404a6144203">Department store</option>
          <option v-if="retail" value="9ed4449d-7d6f-11e3-9238-5404a6144203">Variety store</option>
          <option v-if="retail" value="9ed4449c-7d6f-11e3-9843-5404a6144203">Used and secondhand store</option>
          <option v-if="retail" value="9ed4449a-7d6f-11e3-a380-5404a6144203">Miscellaneous store retailer</option>
          <option v-if="retail" value="9ed44499-7d6f-11e3-aa99-5404a6144203">Discount store</option>
          <option v-if="toys_hobbies" value="9ed492bf-7d6f-11e3-87d7-5404a6144203">Hobby, toy, and game shops</option>
          <option v-if="toys_hobbies" value="9ed492c3-7d6f-11e3-96a8-5404a6144203">Stationery, printing, and writing paper</option>
          <option v-if="toys_hobbies" value="9ed492c4-7d6f-11e3-9f0c-5404a6144203">Vintage and collectibles</option>
          <option v-if="toys_hobbies" value="9ed492c5-7d6f-11e3-9fe5-5404a6144203">Video games and systems</option>
          <option v-if="toys_hobbies" value="9ed492bd-7d6f-11e3-ab0a-5404a6144203">Arts and crafts</option>
          <option v-if="toys_hobbies" value="9ed492c0-7d6f-11e3-b1b2-5404a6144203">Memorabilia</option>
          <option v-if="toys_hobbies" value="9ed492c2-7d6f-11e3-b58e-5404a6144203">Stamp and coin</option>
          <option v-if="toys_hobbies" value="9ed492c1-7d6f-11e3-b5a1-5404a6144203">Music store - instruments and sheet music</option>
          <option v-if="toys_hobbies" value="9ed492be-7d6f-11e3-bf01-5404a6144203">Camera and photographic supplies</option>
          <option v-if="pets_animals" value="9ed4448f-7d6f-11e3-8817-5404a6144203">Pet shops, pet food, and supplies</option>
          <option v-if="pets_animals" value="9ed44491-7d6f-11e3-a152-5404a6144203">Veterinary services</option>
          <option v-if="pets_animals" value="9ed4448e-7d6f-11e3-b343-5404a6144203">Medication and supplements</option>
          <option v-if="pets_animals" value="9ed44490-7d6f-11e3-bfda-5404a6144203">Specialty and rare pets</option>
          <option v-if="education" value="9ed3a85a-7d6f-11e3-889a-5404a6144203">Vocational and trade schools</option>
          <option v-if="education" value="9ed3a855-7d6f-11e3-8d29-5404a6144203">Business and secretarial schools</option>
          <option v-if="education" value="9ed3a856-7d6f-11e3-962b-5404a6144203">Child care services</option>
          <option v-if="education" value="9ed3a858-7d6f-11e3-9d57-5404a6144203">Dance halls, studios, and school</option>
          <option v-if="education" value="9ed3a857-7d6f-11e3-b6c2-5404a6144203">Colleges and universities</option>
          <option v-if="education" value="9ed3a859-7d6f-11e3-bcbb-5404a6144203">Elementary and secondary schools</option>
          <option v-if="arts_crafts_collectibles" value="9ed35a26-7d6f-11e3-890f-5404a6144203">Stamp and coin</option>
          <option v-if="arts_crafts_collectibles" value="9ed35a22-7d6f-11e3-9b52-5404a6144203">Digital art</option>
          <option v-if="arts_crafts_collectibles" value="9ed35a25-7d6f-11e3-a03c-5404a6144203">Sewing, needlework, and fabrics</option>
          <option v-if="arts_crafts_collectibles" value="9ed35a21-7d6f-11e3-a35c-5404a6144203">Camera and photographic supplies</option>
          <option v-if="arts_crafts_collectibles" value="9ed35a1e-7d6f-11e3-a517-5404a6144203">Antiques</option>
          <option v-if="arts_crafts_collectibles" value="9ed35a27-7d6f-11e3-aa1b-5404a6144203">Stationery, printing and writing paper</option>
          <option v-if="arts_crafts_collectibles" value="9ed35a20-7d6f-11e3-ac6a-5404a6144203">Art dealers and galleries</option>
          <option v-if="arts_crafts_collectibles" value="9ed35a23-7d6f-11e3-b222-5404a6144203">Memorabilia</option>
          <option v-if="arts_crafts_collectibles" value="9ed35a24-7d6f-11e3-b2a3-5404a6144203">Music store - instruments and sheet music</option>
          <option v-if="arts_crafts_collectibles" value="9ed35a1f-7d6f-11e3-ba72-5404a6144203">Art and craft supplies</option>
          <option v-if="arts_crafts_collectibles" value="9ed35a28-7d6f-11e3-bdec-5404a6144203">Vintage and collectibles</option>
          <option v-if="financial_services_products" value="9ed3f663-7d6f-11e3-8a12-5404a6144203">Prepaid and stored value cards</option>
          <option v-if="financial_services_products" value="9ed3cf68-7d6f-11e3-8abb-5404a6144203">Credit union</option>
          <option v-if="financial_services_products" value="9ed3f667-7d6f-11e3-996b-5404a6144203">Security brokers and dealers</option>
          <option v-if="financial_services_products" value="9ed3f665-7d6f-11e3-99f4-5404a6144203">Remittance</option>
          <option v-if="financial_services_products" value="9ed3f666-7d6f-11e3-9a8d-5404a6144203">Rental property management</option>
          <option v-if="financial_services_products" value="9ed3cf69-7d6f-11e3-9dfb-5404a6144203">Investment banking and securities dealing</option>
          <option v-if="financial_services_products" value="9ed3f664-7d6f-11e3-9eaa-5404a6144203">Real estate agent</option>
          <option v-if="financial_services_products" value="9ed3cf6b-7d6f-11e3-a38f-5404a6144203">Sales financing</option>
          <option v-if="financial_services_products" value="9ed3cf67-7d6f-11e3-a43e-5404a6144203">Debt counseling service</option>
          <option v-if="financial_services_products" value="9ed3cf61-7d6f-11e3-a622-5404a6144203">Collection agency</option>
          <option v-if="financial_services_products" value="9ed3cf65-7d6f-11e3-a76a-5404a6144203">Securities and commodity exchanges</option>
          <option v-if="financial_services_products" value="9ed3cf6e-7d6f-11e3-a77e-5404a6144203">Financial and investment advice</option>
          <option v-if="financial_services_products" value="9ed3cf60-7d6f-11e3-a80d-5404a6144203">Accounting</option>
          <option v-if="financial_services_products" value="9ed3cf6a-7d6f-11e3-a898-5404a6144203">Escrow</option>
          <option v-if="financial_services_products" value="9ed3cf75-7d6f-11e3-aa5a-5404a6144203">Mortgage brokers and dealers</option>
          <option v-if="financial_services_products" value="9ed3cf74-7d6f-11e3-ac83-5404a6144203">Financial transactions processing, reserve, and clearinghouse activities</option>
          <option v-if="financial_services_products" value="9ed3f662-7d6f-11e3-ad1d-5404a6144203">Paycheck lender and cash advance</option>
          <option v-if="financial_services_products" value="9ed3cf70-7d6f-11e3-afb0-5404a6144203">Insurance - life and annuity</option>
          <option v-if="financial_services_products" value="9ed3cf73-7d6f-11e3-b045-5404a6144203">Other activities related to credit intermediation</option>
          <option v-if="financial_services_products" value="9ed3f661-7d6f-11e3-b15e-5404a6144203">Online gaming currency</option>
          <option v-if="financial_services_products" value="9ed3cf62-7d6f-11e3-b2cd-5404a6144203">Commodity contracts dealing</option>
          <option v-if="financial_services_products" value="9ed3cf64-7d6f-11e3-b326-5404a6144203">Commodity contracts brokerage</option>
          <option v-if="financial_services_products" value="9ed3cf72-7d6f-11e3-b387-5404a6144203">Other investment pools and funds</option>
          <option v-if="financial_services_products" value="9ed3cf63-7d6f-11e3-b50c-5404a6144203">Miscellaneous financial investment activities</option>
          <option v-if="financial_services_products" value="9ed3f668-7d6f-11e3-b821-5404a6144203">Wire transfer and money order</option>
          <option v-if="financial_services_products" value="9ed3cf6c-7d6f-11e3-ba14-5404a6144203">Consumer lending</option>
          <option v-if="financial_services_products" value="9ed3cf66-7d6f-11e3-bc6c-5404a6144203">Credit bureaus</option>
          <option v-if="financial_services_products" value="9ed3cf6f-7d6f-11e3-bc97-5404a6144203">Insurance - auto and home</option>
          <option v-if="financial_services_products" value="9ed3cf6d-7d6f-11e3-bd75-5404a6144203">Offices of other holding companies</option>
          <option v-if="financial_services_products" value="9ed3cf71-7d6f-11e3-bf7b-5404a6144203">Other financial investment activities</option>
          <option v-if="government" value="9ed3f683-7d6f-11e3-8a57-5404a6144203">Administration of economic programs</option>
          <option v-if="government" value="9ed3f682-7d6f-11e3-925c-5404a6144203">Administration of housing programs, urban planning, and community development</option>
          <option v-if="government" value="9ed3f680-7d6f-11e3-945b-5404a6144203">Administration of human resource programs</option>
          <option v-if="government" value="9ed3f681-7d6f-11e3-99ff-5404a6144203">Administration and environmental quality programs</option>
          <option v-if="government" value="9ed3f67f-7d6f-11e3-a83d-5404a6144203">Justice, public order, and safety activities</option>
          <option v-if="government" value="9ed3f67e-7d6f-11e3-b5c9-5404a6144203">Executive, legislative, and other general government support</option>
          <option v-if="government" value="9ed3f684-7d6f-11e3-b716-5404a6144203">Space research and technology</option>
          <option v-if="government" value="9ed3f685-7d6f-11e3-ba5b-5404a6144203">National security and international affairs</option>
          <option v-if="vehicle_sales" value="9ed4b9c5-7d6f-11e3-8b92-5404a6144203">Vintage and collectibles</option>
          <option v-if="vehicle_sales" value="9ed4b9c0-7d6f-11e3-9035-5404a6144203">Boat dealer</option>
          <option v-if="vehicle_sales" value="9ed4b9c2-7d6f-11e3-9147-5404a6144203">Motorcycle dealer</option>
          <option v-if="vehicle_sales" value="9ed4b9c4-7d6f-11e3-97b9-5404a6144203">Recreational vehicle dealer</option>
          <option v-if="vehicle_sales" value="9ed4b9c1-7d6f-11e3-99a2-5404a6144203">Mobile home dealer</option>
          <option v-if="vehicle_sales" value="9ed4b9be-7d6f-11e3-a3eb-5404a6144203">Auto dealer - used only</option>
          <option v-if="vehicle_sales" value="9ed4b9bf-7d6f-11e3-ad02-5404a6144203">Aviation</option>
          <option v-if="vehicle_sales" value="9ed4b9c3-7d6f-11e3-ba27-5404a6144203">Recreational and utility trailer dealer</option>
          <option v-if="vehicle_sales" value="9ed4b9bd-7d6f-11e3-bb61-5404a6144203">Auto dealer - new and used</option>
          <option v-if="nonprofit" value="9ed4448c-7d6f-11e3-8ce5-5404a6144203">Educational</option>
          <option v-if="nonprofit" value="9ed44487-7d6f-11e3-9419-5404a6144203">Charity</option>
          <option v-if="nonprofit" value="9ed44488-7d6f-11e3-9872-5404a6144203">Political</option>
          <option v-if="nonprofit" value="9ed44489-7d6f-11e3-a09e-5404a6144203">Religious</option>
          <option v-if="nonprofit" value="9ed4448a-7d6f-11e3-a496-5404a6144203">Other</option>
          <option v-if="nonprofit" value="9ed4448b-7d6f-11e3-be19-5404a6144203">Personal</option>
          <option v-if="vehicle_service_accessories" value="9ed4b9c9-7d6f-11e3-8d35-5404a6144203">Audio and video</option>
          <option v-if="vehicle_service_accessories" value="9ed4b9d2-7d6f-11e3-90bc-5404a6144203">Towing service</option>
          <option v-if="vehicle_service_accessories" value="9ed4b9cc-7d6f-11e3-940b-5404a6144203">Auto service</option>
          <option v-if="vehicle_service_accessories" value="9ed4b9ce-7d6f-11e3-95d6-5404a6144203">Boat rental and leases</option>
          <option v-if="vehicle_service_accessories" value="9ed4b9d1-7d6f-11e3-9894-5404a6144203">Tools and equipment</option>
          <option v-if="vehicle_service_accessories" value="9ed4b9cf-7d6f-11e3-a74e-5404a6144203">Car wash</option>
          <option v-if="vehicle_service_accessories" value="9ed4b9d0-7d6f-11e3-a967-5404a6144203">Motorhome and recreational vehicle rental</option>
          <option v-if="vehicle_service_accessories" value="9ed4b9d3-7d6f-11e3-ad63-5404a6144203">Truck and utility trailer rental</option>
          <option v-if="vehicle_service_accessories" value="9ed4b9d4-7d6f-11e3-aeef-5404a6144203">Parts, supplies, and accessories</option>
          <option v-if="vehicle_service_accessories" value="9ed4b9ca-7d6f-11e3-af09-5404a6144203">Auto body repair and paint</option>
          <option v-if="vehicle_service_accessories" value="9ed4b9cd-7d6f-11e3-b533-5404a6144203">Automotive tire supply and service</option>
          <option v-if="vehicle_service_accessories" value="9ed4b9cb-7d6f-11e3-b5bb-5404a6144203">Auto rental</option>
          <option v-if="electronics_telecom" value="9ed3a85f-7d6f-11e3-8e3b-5404a6144203">General electronic accessories</option>
          <option v-if="electronics_telecom" value="9ed3a85e-7d6f-11e3-9379-5404a6144203">Cell phones, PDAs, and pagers</option>
          <option v-if="electronics_telecom" value="9ed3a85d-7d6f-11e3-9b4f-5404a6144203">Car audio and electronics</option>
          <option v-if="electronics_telecom" value="9ed3a863-7d6f-11e3-9f20-5404a6144203">Telecommunication equipment and sales</option>
          <option v-if="electronics_telecom" value="9ed3a865-7d6f-11e3-a3d0-5404a6144203">Telephone cards</option>
          <option v-if="electronics_telecom" value="9ed3a861-7d6f-11e3-a572-5404a6144203">Home electronics</option>
          <option v-if="electronics_telecom" value="9ed3a85c-7d6f-11e3-af39-5404a6144203">Cameras, camcorders and equipment</option>
          <option v-if="electronics_telecom" value="9ed3a862-7d6f-11e3-b65b-5404a6144203">Investigation and security services</option>
          <option v-if="electronics_telecom" value="9ed3a864-7d6f-11e3-bcd4-5404a6144203">Telecommunication services</option>
          <option v-if="electronics_telecom" value="9ed3a860-7d6f-11e3-befb-5404a6144203">Home audio</option>
          <option v-if="books_magazines" value="9ed35a3a-7d6f-11e3-9579-5404a6144203">Rare and used books</option>
          <option v-if="books_magazines" value="9ed35a39-7d6f-11e3-96ad-5404a6144203">Printing</option>
          <option v-if="books_magazines" value="9ed35a37-7d6f-11e3-a05d-5404a6144203">Magazines</option>
          <option v-if="books_magazines" value="9ed35a38-7d6f-11e3-a24f-5404a6144203">Publishing</option>
          <option v-if="books_magazines" value="9ed35a35-7d6f-11e3-a469-5404a6144203">Book store</option>
          <option v-if="books_magazines" value="9ed35a33-7d6f-11e3-ba85-5404a6144203">Audio books</option>
          <option v-if="religion_spirituality" value="9ed44493-7d6f-11e3-9b4f-5404a6144203">Membership services</option>
          <option v-if="religion_spirituality" value="9ed44495-7d6f-11e3-b2f6-5404a6144203">Services not elsewhere classified</option>
          <option v-if="sports_outdoors" value="9ed492b1-7d6f-11e3-a276-5404a6144203">Dance halls, studios, and schools</option>
          <option v-if="sports_outdoors" value="9ed492b9-7d6f-11e3-a5ed-5404a6144203">Other sporting goods</option>
          <option v-if="sports_outdoors" value="9ed492ba-7d6f-11e3-ab20-5404a6144203">Firearms, knives, and martial arts weapons</option>
          <option v-if="sports_outdoors" value="9ed492bb-7d6f-11e3-b634-5404a6144203">Swimming pools and spas</option>
          <option v-if="sports_outdoors" value="9ed492b3-7d6f-11e3-bbca-5404a6144203">Fan gear and memorabilia</option>
          <option v-if="gifts_flowers" value="9ed3f679-7d6f-11e3-a884-5404a6144203">Gift, card, novelty, and souvenir shops</option>
          <option v-if="gifts_flowers" value="9ed3f67b-7d6f-11e3-aead-5404a6144203">Nursery plants and flowers</option>
          <option v-if="gifts_flowers" value="9ed3f67c-7d6f-11e3-b1fb-5404a6144203">Party supplies</option>
          <option v-if="gifts_flowers" value="9ed3f678-7d6f-11e3-b609-5404a6144203">Florist</option>
          <option v-if="gifts_flowers" value="9ed3f67a-7d6f-11e3-bb5b-5404a6144203">Gourmet foods</option>
      
            </select>
                <label class="label_white">Business Classification</label>
        </div>





</template>






<script setup>


const props = defineProps(['business_classification', 'industry_class'])
const emit = defineEmits(['update:business_classification'])

const value = computed({
  get() {
    return props.business_classification
  },
  set(value) {
    emit('update:business_classification', value)
  }
})


const industry_classification = ref(computed(() => props.industry_class))


watch(industry_classification, (newX) => {
  no_industry_selected.value = false
  update_for_industry()
})


const no_industry_selected = ref(true)

const food_retail_and_service = ref(false)
const manufacturing = ref(false)
const b_2_b = ref(false)
const services_other = ref(false)
const entertainment_and_media = ref(false)
const home_and_garden = ref(false)
const baby = ref(false)
const travel = ref(false)
const clothing_accessories_shoes = ref(false)
const health_personal_care = ref(false)
const beauty_fragrances = ref(false)
const computers_accessories_services = ref(false)
const retail = ref(false)
const toys_hobbies = ref(false)
const pets_animals = ref(false)
const education = ref(false)
const arts_crafts_collectibles = ref(false)
const financial_services_products = ref(false)
const government = ref(false)
const vehicle_sales = ref(false)
const nonprofit = ref(false)
const vehicle_service_accessories = ref(false)
const electronics_telecom = ref(false)
const books_magazines = ref(false)
const religion_spirituality = ref(false)
const sports_outdoors = ref(false)
const gifts_flowers = ref(false)



function update_for_industry(){

if (industry_classification.value == "9ed3f669-7d6f-11e3-b545-5404a6144203") {food_retail_and_service.value = true}

else if (industry_classification.value == "9ed41d89-7d6f-11e3-beff-5404a6144203") {manufacturing.value = true;}

else if (industry_classification.value == "9ed41d89-7d6f-11e3-beff-5404a6144203") {manufacturing.value = true;}

else if (industry_classification.value == "9ed35a3b-7d6f-11e3-83c8-5404a6144203") {b_2_b.value = true;}

else if (industry_classification.value == "9ed4449e-7d6f-11e3-a32d-5404a6144203") {services_other.value = true;}

else if (industry_classification.value == "9ed3a866-7d6f-11e3-a0ce-5404a6144203") {entertainment_and_media.value = true;}

else if (industry_classification.value == "9ed41d75-7d6f-11e3-b151-5404a6144203") {home_and_garden.value = true;}

else if (industry_classification.value == "9ed35a29-7d6f-11e3-930b-5404a6144203") {baby.value = true;}

else if (industry_classification.value == "9ed492c6-7d6f-11e3-80f4-5404a6144203") {travel.value = true;}

else if (industry_classification.value == "9ed38152-7d6f-11e3-9042-5404a6144203") {clothing_accessories_shoes.value = true;}

else if (industry_classification.value == "9ed3f686-7d6f-11e3-af6e-5404a6144203") {health_personal_care.value = true;}

else if (industry_classification.value == "9ed35a2e-7d6f-11e3-a5cf-5404a6144203") {beauty_fragrances.value = true;}

else if (industry_classification.value == "9ed3a846-7d6f-11e3-8a79-5404a6144203") {computers_accessories_services.value = true;}

else if (industry_classification.value == "9ed44496-7d6f-11e3-865d-5404a6144203") {retail.value = true;}

else if (industry_classification.value == "9ed492bc-7d6f-11e3-9a1b-5404a6144203") {toys_hobbies.value = true;}

else if (industry_classification.value == "9ed4448d-7d6f-11e3-aab2-5404a6144203") {pets_animals.value = true;}

else if (industry_classification.value == "9ed3a854-7d6f-11e3-a193-5404a6144203") {education.value = true;}

else if (industry_classification.value == "9ed248ae-7d6f-11e3-ba6e-5404a6144203") {arts_crafts_collectibles.value = true;}

else if (industry_classification.value == "9ed3cf5f-7d6f-11e3-8af8-5404a6144203") {financial_services_products.value = true;}

else if (industry_classification.value == "9ed3f67d-7d6f-11e3-bf40-5404a6144203") {government.value = true;}

else if (industry_classification.value == "9ed4b9bc-7d6f-11e3-9133-5404a6144203") {vehicle_sales.value = true;}

else if (industry_classification.value == "9ed44486-7d6f-11e3-89f8-5404a6144203") {nonprofit.value = true;}

else if (industry_classification.value == "9ed4b9c6-7d6f-11e3-a156-5404a6144203") {vehicle_service_accessories.value = true;}

else if (industry_classification.value == "9ed3a85b-7d6f-11e3-8995-5404a6144203") {electronics_telecom.value = true;}

else if (industry_classification.value == "9ed35a32-7d6f-11e3-9830-5404a6144203") {books_magazines.value = true;}

else if (industry_classification.value == "9ed44492-7d6f-11e3-98d1-5404a6144203") {religion_spirituality.value = true;}

else if (industry_classification.value == "9ed492ac-7d6f-11e3-a2d2-5404a6144203") {sports_outdoors.value = true;}

else if (industry_classification.value == "9ed3f677-7d6f-11e3-96a2-5404a6144203") {gifts_flowers.value = true;}




}




















</script>


