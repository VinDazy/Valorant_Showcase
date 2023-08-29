import streamlit as st
import requests
st.set_page_config(layout="wide", page_icon="icons/val_icon2.png")
st.image("icons/background.png")
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
    info=[]
    firerate={}
    wallpenetration={}
    reloadtime={}
    equiptime={}
    magazinesize={}
    price={}
    if weapon['weaponStats'] is not None:
        firerate['Fire Rate']=weapon['weaponStats']['fireRate']
        magazinesize['Magazine Size']=weapon['weaponStats']['magazineSize']
        equiptime['Equip Time']=weapon['weaponStats']['equipTimeSeconds']
        reloadtime['Reload Time']=weapon['weaponStats']['reloadTimeSeconds']
        wallpenetration['Wall Penetration']=weapon['weaponStats']['wallPenetration'].split("::")[1]
        info.append(wallpenetration)
        info.append(firerate)
        info.append(magazinesize)
        info.append(equiptime)
        info.append(reloadtime)
    if weapon['shopData'] == None:
        weapon_price = '0'
        price['Price']=weapon_price
        weapon_category = "Melee"
        weaponCategories.append(weapon_category)
        info.append(price)
    else:
        weapon_price = weapon['shopData']['cost']
        price['Price']=weapon_price
        info.append(price)
        weapon_category = weapon['shopData']['categoryText']
        if weapon_category not in weaponCategories:
            weaponCategories.append(weapon_category)
    info[0],info[-1]=info[-1],info[0]

    if weapon_category == "Melee":
        melee.image(weapon_image, weaponName)
        
        
    
    elif weapon_category == 'Sidearms':
        sidearms.image(weapon_image, weaponName)
        expander=sidearms.expander("More info")
        for item in info:
            for key, value in item.items():
                expander.write(f"{key} : {value}")

        sidearms.markdown("---")
        

    
    
    elif weapon_category == "SMGs":
        smg.image(weapon_image, weaponName)
        expander=smg.expander("More info")
        for item in info:
            for key, value in item.items():
                expander.write(f"{key} : {value}")


        smg.markdown("---")


    elif weapon_category == "Shotguns":
        shotguns.image(weapon_image, weaponName)
        expander=shotguns.expander("More info")
        for item in info:
            for key, value in item.items():
                expander.write(f"{key} : {value}")


        shotguns.markdown("---")



    
    elif weapon_category == 'Heavy Weapons':
        heavy_weapons.image(weapon_image, weaponName)
        expander=heavy_weapons.expander("More info")
        for item in info:
            for key, value in item.items():
                expander.write(f"{key} : {value}")

        heavy_weapons.markdown("---")



    elif (weapon_category == 'Assault Rifles'):
        assault_rifles.image(weapon_image, weaponName)
        expander=assault_rifles.expander("More info")
        for item in info:
            for key, value in item.items():
                expander.write(f"{key} : {value}")
        assault_rifles.markdown("---")


    elif weapon_category == "Sniper Rifles":
        sniper_rifles.image(weapon_image, weaponName)
        expander=sniper_rifles.expander("More info")
        for item in info:
            for key, value in item.items():
                expander.write(f"{key} : {value}")
        sniper_rifles.markdown("---")

