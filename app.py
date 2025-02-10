import streamlit as st

# Streamlit app title
st.title("Happy 3 Years!")

# Love letter content
love_letter = """
To Charmagne Gyle Z. Corpuz,

Happy 3rd Anniversary!

I love you to the moon and back, always.
"""

# Display the love letter
st.write(love_letter)

# Subheader for the image slideshow
st.subheader("Memorable Moments")

# List of image paths (update these paths to your actual images)
image_paths = [
    "image1.jpg",
    "image2.jpg",
    "image3.jpg"
]

# Slider to select the current image
image_index = st.slider("Select an image index", 0, len(image_paths) - 1)
st.image(image_paths[image_index], caption=f"Image {image_index + 1}", width=700)