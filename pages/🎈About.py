#importing library
import streamlit as sl

page_bg_img = f"""
<style>
.st-emotion-cache-bm2z3a {{
    background-image: url("https://images.unsplash.com/photo-1441974231531-c6227db76b6e?q=80&w=2071&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D");
    background-size: cover;
}}

.st-emotion-cache-h4xjwg {{
    background-color: rgba(0, 0, 0, 0);
}}

.st-emotion-cache-qcpnpn {{
    background-color: rgba(0, 0, 0, 0.6);
}}
</style>
"""
sl.markdown(page_bg_img, unsafe_allow_html=True)

#tab title and page title
#sl.set_page_config(page_title="Instructions")

with ((sl.container(border=True))):
    sl.title("About")
    sl.markdown("It has a total of three pages:")
    sl.markdown("- Home - All of the main content lies here")
    sl.markdown("- About - Quick facts about the project")
    sl.markdown("- Instructions - Simple instructions to use the app.")
    sl.markdown("This project also has a responsive design, adapting to any screen size")

    sl.title("Documentation")
    sl.markdown("This project uses Streamlit to cast the website and deploy it through the Streamlit Community Cloud.")
    sl.markdown("- Design Documentation: https://docs.streamlit.io/")
    sl.markdown("- Streamlit Community Cloud Deployment Documentation: https://docs.streamlit.io/deploy/streamlit-community-cloud")
    sl.write("")
    sl.write("")


