import streamlit as st 
import requests 
st.set_page_config(page_title="Valorant Agents ",layout="wide", page_icon="icons/val_icon2.png")
st.image("icons/upp.png")
st.title("Valorant Agents")
result = requests.get(url="https://valorant-api.com/v1/agents")
json_data = result.json()



##MainMenu {visibility: hidden;} : ADD this to hide_menu_style to hide the hamburger menu
hide_menu_style="""
<style>

footer {visibility: hidden;}
</style> 
"""

col1,col2,col3=st.columns(3)









agentNames=[]
agent_count=1
for agent in json_data['data']:
        agent_name=agent['displayName']
        if (agent_name=='Sova') and (agent['isPlayableCharacter']==False):
            #! Skip this iteration because the API provided two sova's , to filter the right one, we use IsPlayableCharacter==True
            continue
        image=agent['fullPortrait']
        if agent_count <=7:
                col1.image(image,caption=agent_name)
        elif agent_count in range(8,15):
                col2.image(image,caption=agent_name)
        elif agent_count in range(16,23):
                col3.image(image,caption=agent_name)
        else:
              #! this needs to be updated when more agents are added
              #! it needs to stay consistent with the layout , for now agents are added to the first column 
              col1.image(image,caption=agent_name)
        agentNames.append(agent_name)
        agent_count+=1






              





