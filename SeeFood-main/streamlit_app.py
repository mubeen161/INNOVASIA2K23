import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
from inference import infer
import time



st.set_page_config(page_icon="", page_title="Scanner")

st.markdown("<h1 style='text-align: center; color: brown;'>Recipe Generator</h1>", unsafe_allow_html=True)

st.markdown("<h4 style='text-align: center; color: brown;'>Trained to recognize 85 types of Indian Food ,data link<a href = 'https://www.kaggle.com/datasets/iamsouravbanerjee/indian-food-images-dataset'></a> </h4>", unsafe_allow_html=True)


col1, col2, col3 = st.columns([1,18,1])


img = 0

def load_image(img):
    im = Image.open(img)
    image = np.array(im)
    return image



uploadFile = st.file_uploader(label="Upload image", type=['jpg', 'png','jpeg'])



with col2:



    if uploadFile is not None:


        img = load_image(uploadFile)


        with st.spinner('Wait for it...'):

            list_of_predictions,list_of_prep_times,list_of_regions,list_of_ingredients,pred_prob = infer(uploadFile)
            st.image(img)
            time.sleep(1)





        list_of_predictions = [i.replace('_',' ') for i in list_of_predictions]

        #st.write('The most likely foods are as follows 👇')
        
        st.markdown("<p style='text-align: center; color: white;'>The most likely foods are as follows 👇.</p>", unsafe_allow_html=True)

        if pred_prob[0] > 0.0:
            
            
            st.markdown("""
  #### <p style="color:white">* This is {} . It takes {} minutes to prepare. The cuisine is based in {} India. The ingredients are {} .</p>  
""".format(list_of_predictions[0],list_of_prep_times[0],list_of_regions[0],list_of_ingredients[0]),  unsafe_allow_html=True)
            

#             st.write('* This is ', list_of_predictions[0],". It takes ",list_of_prep_times[0],' minutes to prepare.',' The cuisine is based in  ',list_of_regions[0], ' India.', 'The main ingredients are ',list_of_ingredients[0] ,' .')

        if pred_prob[1] > 0 :
            st.markdown("""
  #### <p style="color:white">* This is {} . It takes {} minutes to prepare. The cuisine is based in {} India. The ingredients are {} .</p>  
""".format(list_of_predictions[1],list_of_prep_times[1],list_of_regions[1],list_of_ingredients[1]),  unsafe_allow_html=True)

#             st.write('* This is ',list_of_predictions[1],". It takes ",list_of_prep_times[1],' minutes to prepare.',' The cuisine is based in  ',list_of_regions[1], ' India.','The main ingredients are ',list_of_ingredients[1] ,' .')

        if pred_prob[2] > 0:
        
            st.markdown("""
  #### <p style="color:white">* This is {} . It takes {} minutes to prepare. The cuisine is based in {} India. The ingredients are {} .</p>
""".format(list_of_predictions[2],list_of_prep_times[2],list_of_regions[2],list_of_ingredients[2]),  unsafe_allow_html=True)

#             st.write('* This is ',list_of_predictions[2],". It takes ",list_of_prep_times[2],' minutes to prepare.',' The cuisine is based in  ',list_of_regions[2], ' India.','The main ingredients are ',list_of_ingredients[2] ,' .')

        if pred_prob[3] > 0:
        
            st.markdown("""
  #### <p style="color:white">* This is {} . It takes {} minutes to prepare. The cuisine is based in {} India. The ingredients are {} .</p>
""".format(list_of_predictions[3],list_of_prep_times[3],list_of_regions[3],list_of_ingredients[3]),  unsafe_allow_html=True)

#             st.write('* This is ',list_of_predictions[3],". It takes ",list_of_prep_times[3],' minutes to prepare.',' The cuisine is based in  ',list_of_regions[3], ' India.','The main ingredients are ',list_of_ingredients[3] ,' .')

        if pred_prob[4] > 0:
        
            st.markdown("""
  #### <p style="color:white">* This is {} . It takes {} minutes to prepare. The cuisine is based in {} India. The ingredients are {} .</p>  
""".format(list_of_predictions[4],list_of_prep_times[4],list_of_regions[4],list_of_ingredients[4]),  unsafe_allow_html=True)
        
        

#             st.write('* This is ',list_of_predictions[4],". It takes ",list_of_prep_times[4],' minutes to prepare.',' The cuisine is based in  ',list_of_regions[4], ' India.','The main ingredients are ',list_of_ingredients[4] ,' .')







        #st.write("Image Uploaded Successfully")
        st.markdown("<p style='text-align: center; color: white;'>Image Uploaded Successfully</p>", unsafe_allow_html=True)
    else:
        #st.write("Make sure you image is in JPG/PNG Format.")
        
        st.markdown("<p style='text-align: center; color: white;'>Make sure you image is in JPG/PNG Format.</p>", unsafe_allow_html=True)
        

















# df = pd.DataFrame(
#     np.ones((5000,2)) / [50, 50] + [12.97, 77.59],
#     columns=['lat', 'lon'])

# st.pydeck_chart(pdk.Deck(
#      map_style=None,
#      initial_view_state=pdk.ViewState(
#          latitude=12.97,
#          longitude=77.59,
#          zoom=5,
#          pitch=50,
#      ),
#      layers=[
#          # pdk.Layer(
#          #    'HexagonLayer',
#          #    data=df,
#          #    get_position='[lon, lat]',
#          #    radius=0,
#          #    elevation_scale=10,
#          #    elevation_range=[0, 1000],
#          #    pickable=True,
#          #    extruded=True,
#          # ),
#          pdk.Layer(
#              'ScatterplotLayer',
#              data=df,
#              get_position='[lon, lat]',
#              get_color='[100, 150, 0, 1]',
#              get_radius=50000,

#          ),
#      ],
#  ))
