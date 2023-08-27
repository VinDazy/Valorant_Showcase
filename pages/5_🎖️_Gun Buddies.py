import streamlit as st
import requests


st.set_page_config(page_title="Valorant Gun Buddies ",layout="wide", page_icon="icons/val_icon2.png")
st.image("icons/background.png")
st.title("Valorant Gun Buddies")
hide_menu_style="""
<style>

footer {visibility: hidden;}
</style> 
"""
col1,col2,col3,col4,col5,col6=st.columns(6)

#! Gun buddies count : 366
result=requests.get(url="https://valorant-api.com/v1/buddies")
json_data=result.json()
buddy_count = 1
for buddy in json_data['data']:
    with st.spinner("Gathering Resources"):
        buddy_name = buddy['displayName']
        buddy_image = buddy['displayIcon']
        if buddy['isHiddenIfNotOwned']==True:
            availability=False
        else:
            availability=True
        if buddy_count <= 61:
            col1.image(buddy_image, caption=f"{buddy_name} \n",width=120)
            col1.write(f"Availability : {availability}")
            col1.markdown("---")
        elif buddy_count in range(62, 123):
            col2.image(buddy_image, caption=f"{buddy_name} \n",width=120)
            col2.write(f"Availability : {availability}")
            col2.markdown("---")
        elif buddy_count in range(123, 185):
            col3.image(buddy_image, caption=f"{buddy_name} \n",width=120)
            col3.write(f"Availability : {availability}")
            col3.markdown("---")
        elif buddy_count in range(185, 247):
            col4.image(buddy_image, caption=f"{buddy_name} \n",width=120)
            col4.write(f"Availability : {availability}")
            col4.markdown("---")
        elif buddy_count in range(247, 309):
            col5.image(buddy_image, caption=f"{buddy_name} \n",width=120)
            col5.write(f"Availability : {availability}")
            col5.markdown("---")
        elif buddy_count in range(309, 367):  # Corrected range here
            col6.image(buddy_image, caption=f"{buddy_name}\n",width=120)
            col6.write(f"Availability : {availability}")
            col6.markdown("---")
        else:
            # Handle any remaining buddies or cases not covered in the ranges
            pass
        
        buddy_count += 1
st.sidebar.info(f"Loading Gun Buddies : Done",icon="🎉")

