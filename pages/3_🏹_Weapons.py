import streamlit as st
import requests
st.set_page_config(layout="wide", page_icon="icons/val_icon2.png")
st.image("icons/upp.png")
st.title("Valorant Weapons Information")
sidebar=st.sidebar
result = requests.get(url="https://valorant-api.com/v1/weapons")
json_data = result.json()
col1,col2,col3=st.columns(3)



index=1
for weapon in json_data['data'] :
    weaponName=weapon['displayName']
    weapon_image=weapon['displayIcon']
    if index<=6:
        col1.image(weapon_image,weaponName)
    elif index in range(7,13):
        col2.image(weapon_image,weaponName)
    elif index in range(12,19):
        col3.image(weapon_image,weaponName)
    index+=1
    
