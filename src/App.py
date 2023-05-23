import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

# from pages.begin import BeginPage


st.set_page_config(
    page_title="Image Learning Lab",
    page_icon="📸",
)


# PAGES = ["Begin", "Space", "About"]


st.title("Image Learning Lab 📸")
st.divider()


# sidebar

# selected_page = st.sidebar.selectbox("Choose Page", PAGES)
# st.write("Current Page:", selected_page)
# st.sidebar.divider()

# Handle current "page" selected by user
# if selected_page == "Begin":
#     BeginPage.render()
# elif selected_page == "About":
#     st.header("About")
#     st.write("This is the about page")
# else:
#     st.write("This shouldn't happen")




















# st.sidebar.subheader("Initial Conditions")

# x_initial = st.sidebar.slider(
#     "Starting x (Rabbits)",
#     0, 100, 10
# )

# y_initial = st.sidebar.slider(
#     "Starting y (Foxes)",
#     0, 100, 5
# )

# st.sidebar.subheader("Parameters")

# time_range = st.sidebar.slider(
#     "Time Range",
#     0, 100, (0, 20)
# )

# alpha = st.sidebar.slider(
#     "alpha",
#     0.0, 10.0, 1.5
# )

# beta = st.sidebar.slider(
#     "beta",
#     0.0, 10.0, 1.0
# )

# gamma = st.sidebar.slider(
#     "gamma",
#     0.0, 10.0, 3.0
# )

# delta = st.sidebar.slider(
#     "delta",
#     0.0, 10.0, 1.0
# )

# st.text(str([alpha, beta, delta, gamma]))


# # simulation_df = simulate(time_range, [x_initial, y_initial], alpha, beta, gamma, delta)
# # simulation_alt_df = pd.melt(simulation_df, id_vars=["t"], value_vars=["x", "y"], var_name="label", value_name="value")
# # time_chart = alt.Chart(simulation_alt_df).mark_line().encode(
# #     x=alt.X("t", axis=alt.Axis(title="time")),
# #     y=alt.Y("value", axis=alt.Axis(title="population")),
# #     color="label",
# #     # strokeDash="label",
# # )
# st.header("Time Dynamics")
# # st.altair_chart(time_chart, use_container_width=True)


# # phase_chart = alt.Chart(simulation_df).mark_point().encode(
# #     x=alt.X("x", axis=alt.Axis(title="rabbits")),
# #     y=alt.Y("y", axis=alt.Axis(title="foxes")),
# #     # color="label",
# #     # strokeDash="label",
# #     order="t"
# # )
# st.header("Phase Dynamics")
# # st.altair_chart(phase_chart, use_container_width=True)


# # add_slider = st.sidebar.slider(
# #     'Select a range of values',
# #     0.0, 100.0, (25.0, 75.0)
# # )

# # if st.checkbox('Show raw data'):
# #     st.subheader('Raw data')
# #     st.write(data)

# # st.subheader('Number of pickups by hour')
# # hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
# # st.bar_chart(hist_values)

# # # Some number in the range 0-23
# # hour_to_filter = st.slider('hour', 0, 23, 17)
# # filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

# # st.subheader('Map of all pickups at %s:00' % hour_to_filter)
# # st.map(filtered_data)
