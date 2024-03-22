#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : codenamewei
# Created Date: 2024-03-23
# Updated Date: 2024-03-23
# version ='1.0'
# ---------------------------------------------------------------------------
import streamlit as st
import requests
import time

is_server_up_key = "is_server_up"
server_url = "http://sample-app-backend:8000/" #"http://localhost:8000/"


def config():

    if is_server_up_key not in st.session_state:

        with st.spinner('Check if server is up'):
            #artificial slowing down to check if server is up
            time.sleep(1)

        response = requests.get(server_url + "status")

        st.session_state[is_server_up_key] = True if response.ok else False



if __name__ == "__main__":


    st.title("Sample App")
        
    config()

    if st.session_state[is_server_up_key] == True:
        st.caption(':white_check_mark: Connected to Server')
    
    st.image("public/banner.png", use_column_width = True)

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Raise 404 Error", type = "primary", use_container_width = True):

            response = requests.get(server_url + "items")

            if response.ok:

                st.info("No error raised")

            elif response.status_code == 404:

                st.switch_page("pages/404.py")       

                #st.error("Oops! 404 Not Found Error has been raised.")

    with col2: 
        if st.button("Raise 500 Error", type = "primary", use_container_width = True):

            response = requests.get(server_url + "logs")

            if response.ok:

                st.info("No error raised")

            elif response.status_code == 500:

                st.switch_page("pages/500.py")       
                #st.error("Sorry. 500 Internal Server Error has been raised. Please try again later.")