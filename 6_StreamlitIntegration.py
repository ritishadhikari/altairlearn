import streamlit as st
import numpy as np
import pandas as pd
import altair as alt
from vega_datasets import data


cars=data.cars()
cols=['#4B0082','yellow','#FFC0CB']

sp1=alt\
.Chart(
    data=cars,
    width=800,
    height=700
    )\
.mark_point()\
.encode(
    x=alt.X(shorthand="Miles_per_Gallon"),
    y=alt.Y(shorthand="Horsepower"),
    color=alt.Color(
        shorthand="Origin",
        scale=alt.Scale(
            scheme="accent"
        )
    ),
    tooltip=[
        alt.Tooltip(shorthand="Miles_per_Gallon"),
        alt.Tooltip(shorthand="Horsepower"),
        alt.Tooltip(shorthand="Origin")
    ]
)

st.header(body="Altair Representation")
st.altair_chart(altair_chart=sp1)
