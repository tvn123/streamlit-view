import streamlit as st
view = [100,150,30]
st.write("# Youtube view")
st.write("## raw")
view
st.write("## raw")
st.bar_chart(view)
import pandas as pd
sview = pd.Series(view)
sview