import streamlit as st

st.title('st.experimental_get_query_params')

with st.expander('About this app'):
  st.write("`st.experimental_get_query_params` allows the retrieval of query parameters directly from the URL of the user's browser.")

# 1. Instructions
st.header('1. Instructions')
st.markdown('''
In the above URL bar of your internet browser, append the following:
`?firstname=Jack&surname=Beanstalk`
after the base URL `http://share.streamlit.io/dataprofessor/st.experimental_get_query_params/`
such that it becomes
`http://share.streamlit.io/dataprofessor/st.experimental_get_query_params/?firstname=Jack&surname=Beanstalk`
''')

# store dict in a variable
params = st.experimental_get_query_params()

# 2. Contents of st.experimental_get_query_params
st.header('2. Contents of st.experimental_get_query_params')
st.write(params)

st.header('Display items from dict:')
st.write(params.items())

# 3. Retrieving and displaying information from the URL
st.header('3. Retrieving and displaying information from the URL')

if params:
    firstname = params['firstname'][0]
    surname = params['surname'][0]
    st.write(f'Hello **{firstname} {surname}**, how are you?')
else:
    st.write("Please pass parameters in the URL")
