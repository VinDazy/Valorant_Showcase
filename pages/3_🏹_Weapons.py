import streamlit as st
import requests
st.set_page_config(layout="wide", page_icon="icons/val_icon2.png")
st.image("icons/upp.png")
st.title("Valorant Weapons Information")
sidebar = st.sidebar
result = requests.get(url="https://valorant-api.com/v1/weapons")
json_data = result.json()
melee,sidearms,smg,shotguns,heavy_weapons,assault_rifles,sniper_rifles=st.columns(7)
melee.subheader("Melee")
heavy_weapons.subheader("Heavy Weapons")
assault_rifles.subheader("Assault Rifles")
sniper_rifles.subheader("Sniper Rifles")
shotguns.subheader("Shotguns")
sidearms.subheader("Sidearms")
smg.subheader("SMGs")



weaponCategories = []
for weapon in json_data['data']:
    weaponName = weapon['displayName']
    weapon_image = weapon['displayIcon']
    if weapon['shopData'] == None:
        weapon_price = '0'
        weapon_category = "Melee"
        weaponCategories.append(weapon_category)
    else:
        weapon_price = weapon['shopData']['cost']
        weapon_category = weapon['shopData']['categoryText']
        if weapon_category not in weaponCategories:
            weaponCategories.append(weapon_category)

    if weapon_category == "Melee":
        melee.image(weapon_image, weaponName+' : ' +
                    str(weapon_price)+' 💲')
        
    
    elif weapon_category == 'Sidearms':
        sidearms.image(weapon_image, weaponName+' : ' +
                       str(weapon_price)+' 💲')
        sidearms.markdown("---")
    
    
    elif weapon_category == "SMGs":
        smg.image(weapon_image, weaponName+' : ' +
                  str(weapon_price)+' 💲')
        smg.markdown("---")


    elif weapon_category == "Shotguns":
        shotguns.image(weapon_image, weaponName+' : ' +
                       str(weapon_price)+' 💲')
        shotguns.markdown("---")



    
    elif weapon_category == 'Heavy Weapons':
        heavy_weapons.image(weapon_image, weaponName+' : ' +
                            str(weapon_price)+' 💲')
        heavy_weapons.markdown("---")



    elif (weapon_category == 'Assault Rifles'):
        assault_rifles.image(weapon_image, weaponName +
                             ' : '+str(weapon_price)+' 💲')
        assault_rifles.markdown("---")


    elif weapon_category == "Sniper Rifles":
        sniper_rifles.image(weapon_image, weaponName+' : ' +
                            str(weapon_price)+' 💲')
        sniper_rifles.markdown("---")

