import streamlit as st

# Set the page config to include a title and an icon
st.set_page_config(page_title="Day and Night Mode Toggle", page_icon="🌞")

# Define styles for day and night modes
def apply_styles(background_color, text_color):
    st.markdown(
        f"""
        <style>
        .reportview-container {{
            background-color: {background_color};
            color: {text_color};
        }}
        .sidebar .sidebar-content {{
            background-color: {background_color};
            color: {text_color};
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Create a radio button to toggle between day and night mode
mode = st.radio("Select Mode:", ("Day", "Night"))

# Apply the selected style
if mode == "Day":
    apply_styles("#ffffff", "#000000")
else:
    apply_styles("#000000", "#ffffff")

# Add some content to demonstrate the mode change
st.write(f"The current mode is {mode}.")
st.write("Here is some sample content to showcase the style changes.")

# Add more content to visualize the effect
st.write("Some more text to show how the colors adapt to the selected mode.")
st.button("Sample Button")