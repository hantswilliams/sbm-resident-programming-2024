import streamlit as st 

st.title('500 Places CDC, 2023')
st.subheader('Chronic Disease Prevention and Health Promotion at the Censsu Tract Level')
st.image('https://datadrivendetroit.org/wp-content/uploads/2022/04/US-Census-Spine_D3_No-Title.jpg')
st.write('Data Source: https://data.cdc.gov/500-Cities-Places/PLACES-Local-Data-for-Better-Health-Census-Tract-D/cwsq-ngmh/about_data')
st.markdown('---')
st.markdown('## Census Track FIPS')
st.markdown('A census tract FIPS code is an 11-digit number that uniquely identifies each census tract in the United States.It is a concatentation of - reading from left to right - the 2-digit state code, the 3-digit county code, and the 6-digit tract code.')
st.write('https://www.fcc.gov/general/form-477-census-tract-information')

## Get shape files/line files from https://www.census.gov/cgi-bin/geo/shapefiles/index.php
## will likely want to match 2020-2021 




