import streamlit as st

# Streamlit app title
st.title("To Charmagne Gyle Z. Corpuz, Happy 3rd Anniversary!")

# Love letter content
love_letter = """
This is a letter dedicated to the woman I love. My significant other, my princess, my queen, my babie.

It's been 1096 days. It's one helluva ride. To be honest, I'll always say these words to you. The fact that I am very thankful to have met you, and the fact that I am very happy have you as my one and only babie. 2024 has been rough for the two of us, rough in a way that the days we met personally can be easily counted. I really, really miss the days that we can see each other in every week that passes. I hope this year will be the return of that, babie. I have you to thank for telling me that I deserve to feel, let alone express love. In these years, let me tell you, I'm confident.. VERY confident to say that what I feel for you hasn't changed. And it sure as hell will never change.

"""

# Display the love letter
st.write(love_letter)

# Subheader for the image slideshow
st.subheader("I love you to the moon and back, always.")

# List of image paths (update these paths to your actual images)
image_paths = [
    "image1.jpg",
    "image2.jpg",
    "image3.jpg"
]

# Slider to select the current image
image_index = st.slider("", 0, len(image_paths) - 1)
st.image(image_paths[image_index])