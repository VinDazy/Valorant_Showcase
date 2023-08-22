import streamlit as st
import requests
from bs4 import BeautifulSoup
import re 
import time
import os 





st.set_page_config(page_title="Valorant Maps ",layout="wide", page_icon="icons/val_icon2.png")
st.image("icons/background.png")
st.title("Valorant Maps")
hide_menu_style="""
<style>

footer {visibility: hidden;}
</style> 
"""

sidebar=st.sidebar
result = requests.get(url="https://valorant-api.com/v1/maps")
json_data = result.json()
maps=[]
death_match_maps=[]
training_map=[]
for mapp in json_data['data']:
    map_name=mapp['displayName']
    if mapp['coordinates']==None:
        death_match_maps.append(mapp['displayName'])
    elif mapp['uuid']=='ee613ee9-28b7-4beb-9666-08db13bb2244':
        training_map.append(mapp['displayName'])
    else:
        maps.append(map_name)


def scrape_image(country):
    try:

        url=f'https://www.countryflags.com/{country}-flag-image/'
        result=requests.get(url=url).text
        soup=BeautifulSoup(result,'lxml')
        image_url=soup.find('div',class_='col-12 col-md-5 text-center d-flex align-items-center justify-content-center').find('img')['src']
        return(image_url)
    except:
        st.error(f'No flag found for "{country}" ')
def get_agent_icon(agent_name):
    result = requests.get(url="https://valorant-api.com/v1/agents")
    json_data = result.json()
    for agent in json_data['data']:
        if (agent["displayName"]==agent_name):
            icon=agent['displayIconSmall']
            return icon







    







#sidebar : two forms , first form for map type (standard, team deathmatch,training), second form for to display which map specifically 
with sidebar:
    sidebar.header("Search Map information")
    input_form=sidebar.form(key="map_input")
    input_form.image("icons/val_icon1.png")
    map_name=input_form.selectbox("Map name",options=maps)
    search=input_form.form_submit_button("Search Map information")
    result=requests.get(url=f"https://valorant.fandom.com/wiki/{map_name}").text
    soup = BeautifulSoup(result, 'lxml')
    #LOCATION + LOCATION IMAGE + ADDED DATE
    information=soup.find("section",class_="pi-item pi-group pi-border-color pi-collapse pi-collapse-open")
    map_location=information.find('div',class_='pi-data-value pi-font').text
    country=map_location.split(", ")[-2]
    if country=="USA":
        country="United-States"
    elif country=="Atlantic Ocean":
        country="No Country"
    image=scrape_image(country=country)
    #location_image=information.find('div',class_='pi-data-value pi-font').find('img')['src']
    added_div = soup.find('div', {'data-source': 'added'})
    added_date = added_div.find('div', {'class': 'pi-data-value pi-font'}).text.strip()
    descriptions_strings=soup.find_all('div',style="font-size:1.1em; padding-left: 0.6em; padding-top:1em; padding-bottom:1em; padding-right: 1em;")
    description_list=[]
    for description in descriptions_strings:
        text=description.find('i').get_text()
        text = re.sub(r'https://.*?\.mp3', '', text)
        description_list.append(text)
    #map theme + agent audio
    audio_list=[]
    map_sound=soup.find_all('span',class_='audio-button')
    for sound in map_sound:
        audio_element=sound.find('audio')
        if audio_element:
            source=audio_element['src']
            audio_list.append(source)

if search :
    if map_name=='':
        st.warning("Please enter a valid Map name")
    elif map_name not in maps:
        st.error("No such Map found! ")
    else:
        with st.spinner("Gathering Resources"):
            time.sleep(0.9)
            sidebar.info(f"Displaying {map_name} information",icon="🎉")
        pic,description,additional=st.columns(3)
        for mapp in json_data['data']:
            if mapp['displayName']==map_name:
                map_image=mapp["splash"]
                map_illustration=mapp['displayIcon']
                map_coordinates=mapp['coordinates']
                with pic:
                    pic.subheader("Map illustration")
                    pic.image(image=map_image,caption=map_name)
                    pic.markdown("---")
                    pic.image(image=map_illustration,caption=f"{map_name} Mini map")
                with description:
                    description.subheader(f"Map Description")
                    description.write('- '+description_list[1])
                    description.markdown("---")
                    #description.subheader(f"Map Details")
                    date,location=description.columns(2)
                    with date:
                        date.subheader(f"Release Date " )
                        date.write(added_date)
                    with location:
                        location.subheader(f" Location ")
                        location.write(map_location)
                        location.markdown("---")
                        if image is not None:
                            location.subheader("Inspiration country")
                            location.image(image=image,caption=country)
                    with additional:
                        additional.subheader("Map Theme")
                        path_1=f'audio\wav-audio\{map_name}\{map_name}_Theme.mp3.wav'
                        additional.audio(path_1,format='audio/wav')
                        additional.markdown("---")
                        if len(audio_list)==2:
                            path_2=f"C:\\Users\\ebdel\\Desktop\\Valorant\\audio\\wav-audio\\{map_name}"
                            additional.subheader("Agent Audio")
                            files_in_directory = os.listdir(path_2)
                            filtered_files = [file for file in files_in_directory if not file.startswith(f"{map_name}")]
                            filtered_paths = [os.path.join(path_2, file) for file in filtered_files]
                            additional.audio(filtered_paths[0],format='audio/wav')
                            terms = files_in_directory[1].split("MatchStart")
                            agent_name = terms[0]
                            additional.write(f'-   {agent_name} Match Start on {map_name}')
                        else:
                            additional.write("Oran McEneff, speaking to Rúben Pontes about his home world")
                        pic,info=additional.columns(2)
                        
                        with pic:
                            if map_name !='Pearl':
                                pic.image(get_agent_icon(agent_name),caption=agent_name,width=90)
                            else:
                                pic.image('icons\Oran_McEneff.webp',caption="Oran McEneff")
                        with info :
                            info.write(description_list[0])
                            
                        



   


                        

