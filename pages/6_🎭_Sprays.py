import streamlit as st 
import requests 
st.set_page_config(page_title="Valorant Sprays ",layout="wide", page_icon="icons/val_icon2.png")
st.image("icons/background.png")
st.title("Valorant Sprays")

def main():

    result = requests.get(url="https://valorant-api.com/v1/sprays")
    json_data = result.json()
    sprays = json_data['data']
    sprays_per_page = 50
    num_pages = (len(sprays) + sprays_per_page - 1) // sprays_per_page
    page = st.sidebar.number_input("Page", min_value=1, max_value=num_pages, value=1)
    start_idx = (page - 1) * sprays_per_page
    end_idx = min(start_idx + sprays_per_page, len(sprays))
    cols = st.columns(4)
    for spray in sprays[start_idx:end_idx]:
        name = spray['displayName']
        full_transparent_icon = spray['fullTransparentIcon']
        display_icon = spray['displayIcon']
        availability = '🚫' if spray['hideIfNotOwned'] else '✔️'
        col_index = (sprays.index(spray) - start_idx) % 4
        with cols[col_index]:
            if full_transparent_icon is not None:
                st.image(full_transparent_icon, caption=name, width=120)
                st.write(f"Available : {availability}")
            else:
                st.image(display_icon, caption=name, width=120)
                st.write(f"Available : {availability}")
            st.markdown("---")
if __name__ == "__main__":
    main()

    
