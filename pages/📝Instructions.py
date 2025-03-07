#importing library
import streamlit as sl

page_bg_img = f"""
<style>
.st-emotion-cache-bm2z3a {{
    background-image: url("https://interactivestory.streamlit.app/~/+/media/00b21288c6e019acb0dd9ce88dfd5e15d0e489279c6e33a337097e8d.jpg");
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
    sl.title("Instructions")
    sl.markdown("")
    sl.markdown("- The intro slide presents the **opening text**. Click the **continue button** to navigate to the next slide at your own pace.")
    sl.markdown("- The user is occasionally presented with two choices. Click on the either of the **two choices** to continue.")
    sl.markdown("- Click the **stop button** to quit and restart.")
    sl.markdown("- Click the **restart button**, which appears at the end, to reset and to navigate back to the inital slide.")
    sl.subheader("")
