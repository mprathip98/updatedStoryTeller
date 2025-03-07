#importing library
import streamlit as sl

page_bg_img = f"""
<style>
.st-emotion-cache-bm2z3a {{
    background-image: url("https://cms-artifacts.artlist.io/content/motion-array/1745347/Mountain_Bright_Autumn_Forest_high_resolution_preview_1745347.jpg?Expires=2036329896747&Key-Pair-Id=K2ZDLYDZI2R1DF&Signature=to~NvTcwVobd8enJBhvKln5V74E8Atbo6DW0Uu01AGG~dKyeYc9Z344sMDNsJywyrFwF~CDdt~-BJjjE9Ndxv0si~vkFOKx1am7Jumz8kFMCJG1wQDXPFJzrImkVgNgLIFUW82F~yZCG3A46OZzp307RsPd1dKX1PBh1TaRIsZz4UwMM2qPrFFvNiC~-owXjrCUCJ91vyHYxRS6kZipD4vVkfs16swASe7OchJyVPP4YuKRmza48LwzacMT8Y5V-BdlJwOtBweWNbSOV3RY1laOGPQ1lgz4M1LTV~nxfcd3QSZLJNiRGNi0U-Mvc2Y7eYqXQa-S12lL~UV4hRHTl5w__");
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


