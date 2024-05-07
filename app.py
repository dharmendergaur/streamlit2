import streamlit as st
from streamlit_extras.app_logo import add_logo
import os
import json

st.image("https://cms-docdb.cern.ch/cgi-bin/PublicDocDB/RetrieveFile?docid=3045&filename=CMSlogo_color_label_1024_May2014.png&version=3", width=150)

st.title('CMS Trigger Subsystem Restart')


st.markdown("""
This GUI performs 
* **Choose subsystems from the sidebar**
* **Send Restart request using the "Send Restart Request" Button.**
""")

with st.sidebar:
  st.image("https://cms-docdb.cern.ch/cgi-bin/PublicDocDB/RetrieveFile?docid=3045&filename=CMSlogo_black_label_1024_May2014.png&version=3", width=150)

st.sidebar.header('User Input Features')
selected_year = st.sidebar.selectbox('Year', list(reversed(range(1950,2020))))

trigger_components = ['BCT','GMT','GTT']
selected_components = st.sidebar.multiselect('Calorimeter Trigger', trigger_components)

available_options = []
if 'BCT' in selected_components:
    # If 'BCT' is present, add ['GCT', 'GMT', 'GTT'] to available_options
    available_options.extend(['GCT'])

if 'GMT' in selected_components:
    # If 'BCT' is present, add ['GCT', 'GMT', 'GTT'] to available_options
    available_options.extend(['BMTF','OMTF','EMTF'])

if 'GTT' in selected_components:
    # If 'BCT' is present, add ['GCT', 'GMT', 'GTT'] to available_options
    available_options.extend(['GTT'])

# available_options = ['GCT','GMT','GTT']
selected_options = st.sidebar.multiselect('Subsystem', available_options)

restart_confirmed = False
msg=""
if selected_options:
    selected_options_string = '\n'.join([f"{i+1}. {item.capitalize()}" for i, item in enumerate(selected_options)])
    st.write("**Subsystems to be restarted:**", selected_options_string)
    # if st.button('Send the Restart request'):
    #     if st.button("Confirm Restart"):
    #         st.write(str(os.popen('./example.sh').read()))
    #         restart_confirmed = False
    #         msg="Restart"

    #     if st.button("Cancel"):
    #         restart_confirmed = False
    #         st.warning('Request cancelled')
    #         msg="Cancel"





# if st.button('Send the Restart request', type="primary"):
#     if st.button("Confirm Restart", type="secondary"):
#         st.write(str(os.popen('./example.sh').read()))
#         restart_confirmed = False
#         msg="Restart"

#     if st.button("Cancel", type="secondary"):
#         selected_options=[]
#         st.warning('Request cancelled')
#         msg="Cancel"



if st.button('Send the Restart request', type="primary"):
    st.write(str(os.popen('./example.sh').read()))


# if restart_confirmed:   
#     st.markdown(str(os.popen('./example.sh').read()))


st.write(msg)

        
    # restart_confirmed = st.checkbox('Are you sure you want to restart?')

    # if restart_confirmed:
    #     st.write('Request sent... Waiting for the response')
    
    # else:
    #     st.write('Request sent... Waiting for the response')
