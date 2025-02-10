import streamlit as st

# Streamlit app title
st.title("To Charmagne Gyle Z. Corpuz, Happy 3rd Anniversary!")

# Love letter content
love_letter = """
Ito ay isang letra na nakatuon sa aking minamahal. Sa aking kasintahan, aking prinsesa, aking reyna, aking babie.

Nakalipas na ng 1096 na araw simula nung tayo ay naging opisyal. Dami nating napagdaanan, dami nating napagusapan, nalaman sa isa't isa, at marami pa. Ang mga taon na to ay napakasaya at hinding-hindi ko makakalimutan hanggang sa pagtanda natin. Ako ay nagpapasalamat na nakilala kita, at napakasaya at tanging maipagmamalaki na ikaw ang aking tanging babie. Ang taong 2024 ay napakasama saatin, noh? Tipong yung mga araw na nagkita tayo nung huling taon, pag pinagsama-sama ay parang isa o dalawang buwan lang. Nakakamiss yung mga panahon na kada linggo nagkikita tayo, minsan nga dumadating pa sa punto na araw-araw na. Nakakamiss yun. Sana itong taon na to ay mas maging isang taon na hinding-hindi natin makakalimutan. Sana yung mga pinaggagagawa natin noon, mabalik natin sa taon na to. Ikaw ay aking pinasasalamatan dahil ikaw ang nagbunyag saakin na karapat-dapat kong maramdaman ang pagmamahal, at ibigay din ito saiyo. Sa mga taon na to, ngayong tayo ay tatlong taon na, ako ay may malakas na loob na sabihin na ang nararamdaman ko sa iyo ay kailanman ay di nagbago at lalong-lalo na sa mga darating na panahon at taon, ay hinding-hindi lalo magbabago. Subalit, marami man akong dapat ipasalamat, marami rin akong dapat hingan ng patawad sa'yo.
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