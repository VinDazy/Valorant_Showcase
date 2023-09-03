import streamlit as st
import requests
st.set_page_config(layout="wide", page_icon="icons/val_icon2.png")
st.image("icons/background.png")
st.title("Valorant Agents Information")
sidebar=st.sidebar

result = requests.get(url="https://valorant-api.com/v1/agents")
json_data = result.json()
agentNames=[]
for agent in json_data['data'] :
    agentName=agent['displayName']
    if (agentName=="Sova") and (agent['isPlayableCharacter']==False):
        continue
    #! skipping the duplicate sova chatacter
    agentNames.append(agentName)


with sidebar:
    sidebar.header("Search agent information")
    input_form=sidebar.form(key="input")
    input_form.image("icons/val_icon1.png")
    Agent_name=input_form.selectbox("Agent name",options=agentNames)
    search=input_form.form_submit_button("Search agent information")
#Agent information  
#    fullportrait, description, backgroundimage, role, role_description, abilities, voiceline   
if search:
    if Agent_name=='': 
        st.warning("Please enter a valid Agent name")

    elif Agent_name not in agentNames:
        st.error('No such Agent found!')
    else :
        pic,description,additional=st.columns(3)
        for agent in json_data['data']:
            if agent['displayName']==Agent_name: 
                if Agent_name=='Sova' and (agent['isPlayableCharacter']==False):
                    continue
                
                image=agent['fullPortrait']
                biography=agent['description']
                ability_images=[]
                ability_names=[]
                ability_description=[]

                agent_role=agent['role']['displayName']
                role_description=agent['role']['description']
                role_img=agent['role']['displayIcon']
                voiceline=agent['voiceLine']['mediaList'][0]["wave"]
                agent_tags=agent['characterTags']
                agent_background_image=agent['background']


                for ability in agent['abilities']:
                    ability_names.append(ability['displayName'])
                    ability_images.append(ability['displayIcon'])
                    ability_description.append(ability['description'])
                with pic:
                    pic.subheader(f"{Agent_name} Portrait")
                    pic.image(image,caption=f"{Agent_name}",use_column_width=True)

                with description:
                    description.subheader(f"{Agent_name} Description")
                    description.write(biography)
                    description.markdown("---")
                    description.subheader(f"{Agent_name} Abilities")
                    ab1,ab2,ab3,ult=description.columns(4)
                    with ab1:
                        ab1.image(image=ability_images[0],caption=ability_names[0])
                    with ab2:
                        ab2.image(image=ability_images[1],caption=ability_names[1])
                    with ab3:
                        ab3.image(image=ability_images[2],caption=ability_names[2])
                    with ult :
                        ult.image(image=ability_images[3],caption=ability_names[3])
                    description.markdown("---")
                    if agent_tags is not None:
                        description.subheader(f"{Agent_name} Tags")
                        for tag in agent_tags:
                            description.markdown('- '+tag.capitalize())
                with additional:
                    
                    additional.subheader(f"{Agent_name} Voiceline")
                    additional.audio(voiceline,format="audio/wav")
                    placeholder=additional.empty()
                    placeholder.text("\n")
                    additional.markdown("---")
                    tags,role=additional.columns(2)
                    tags.subheader(f"{Agent_name} Art")
                    tags.image(agent_background_image)
                    role.subheader(f"{Agent_name} Role")
                    role.image(role_img,caption=agent_role)
                    role.write(role_description)


                    






             