import streamlit as st
from bokeh.plotting import figure, show
import numpy as np

N = 100
x = np.linspace(0, 4*np.pi, N)
y = np.sin(x)

p = figure(title="simple sine wave example", height=350, width=600)
p.line(x, y, color="navy", line_width=3)

st.bokeh_chart(p, use_container_width=True)
