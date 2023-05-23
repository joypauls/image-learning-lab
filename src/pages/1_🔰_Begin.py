import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

from image import Image

image = Image()
image.read("./static/test.jpg")


st.set_page_config(page_title="Begin", page_icon="🔰")

# st.markdown("# Plotting Demo")
# st.sidebar.header("Plotting Demo")
st.header("Everytime you point your phone camera and take a picture, you are collecting data.")

import os
st.write(os.getcwd())
# st.write(os.())

st.image(image.data)

st.image(image.to_grayscale())

x, y = np.meshgrid(range(0, 20), range(0, 20))
z = image.to_grayscale()[615:635,950:970]

# Convert this grid to columnar data expected by Altair
source = pd.DataFrame({'x': x.ravel(),
                     'y': y.ravel(),
                     'z': z.ravel()})

st.altair_chart(
alt.Chart(source).mark_rect().encode(
    x='x:O',
    y='y:O',
    color='z:Q'
)
)

# st.image(image.to_grayscale()[615:635,950:970])

# progress_bar = st.sidebar.progress(0)
# status_text = st.sidebar.empty()
# last_rows = np.random.randn(1, 1)
# chart = st.line_chart(last_rows)

# for i in range(1, 101):
#     new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
#     status_text.text("%i%% Complete" % i)
#     chart.add_rows(new_rows)
#     progress_bar.progress(i)
#     last_rows = new_rows
#     time.sleep(0.05)

# progress_bar.empty()

# # Streamlit widgets automatically run the script from top to bottom. Since
# # this button is not connected to any other logic, it just causes a plain
# # rerun.
# st.button("Re-run")