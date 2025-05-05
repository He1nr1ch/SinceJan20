import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title("Displaying a Matplotlib Plot with Streamlit")

# Generate some sample data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create the Matplotlib plot
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_title("Sine Wave")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")

# Display the Matplotlib plot in the Streamlit app
st.pyplot(fig)

st.write("You can also add text and other elements to your Streamlit app.")