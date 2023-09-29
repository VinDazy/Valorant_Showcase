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
def main():

    result = requests.get(url="https://valorant-api.com/v1/buddies")
    json_data = result.json()
    buddies = json_data['data']

    num_columns = 6
    cols = st.columns(num_columns)

    sprays_per_page = 50
    num_pages = (len(buddies) + sprays_per_page - 1) // sprays_per_page

    page = st.sidebar.number_input("Page", min_value=1, max_value=num_pages, value=1)

    start_idx = (page - 1) * sprays_per_page
    end_idx = min(start_idx + sprays_per_page, len(buddies))

    for buddy_count, buddy in enumerate(buddies[start_idx:end_idx], start=start_idx + 1):
        buddy_name = buddy['displayName']
        buddy_image = buddy['displayIcon']
        is_hidden_if_not_owned = buddy['isHiddenIfNotOwned']

        availability = '🚫' if is_hidden_if_not_owned else '✔️'

        col_index = buddy_count % num_columns  # Calculate the current column index (0 to num_columns - 1)

        with cols[col_index]:
            st.write(buddy_name)
            if buddy_image is not None:
                st.image(buddy_image, caption=buddy_name, width=120)
                st.write(f"Available: {availability}")
            else:
                st.write("Image not available")

            st.markdown("---")



