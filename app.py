from supabase import create_client, Client
import os
from dotenv import load_dotenv
import streamlit as st
import pandas as pd
from json import loads
from io import StringIO

load_dotenv()

supabase_url = st.secrets['SUPABASE_CLIENT_URL']
supabase_key = st.secrets['SUPABASE_CLIENT_KEY']

st.set_page_config(
   page_title="Dashboard Sakernas",
   page_icon="🧊"
)

# Create supabase client
supabase: Client = create_client(supabase_url, supabase_key)

# Create Title Element
st.title('Dashboard Sakernas Agustus 2024 Pendataan Kota Lubuk Linggau')

# Get data from database
response = (
    supabase.table("streamlit")
    .select('*').single().execute()
).model_dump_json()

# Create dataframe
json = StringIO(loads(response)['data']['data'])
df = pd.read_json(json)

st.header("Tabulasi Progres")
st.dataframe(df, hide_index=True)