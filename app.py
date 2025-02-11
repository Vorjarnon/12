import streamlit as st

# Function to display the main content
def display_main_content():
    # Streamlit app title
    st.title("To Charmagne Gyle Z. Corpuz,")

    # Love letter content
    love_letter = """
    Ito ay isang letra na nakatuon sa aking minamahal. Para sa aking kasintahan, aking prinsesa, aking reyna, aking babie.

    Nakalipas na ng 1096 na araw simula nung tayo ay naging opisyal. Dami nating napagdaanan, dami nating napagusapan, nalaman sa isa't isa, napagtawanan, napagawayan, pagkatampuhan, at maraming-maraming-marami pa. Ang mga taon na to ay napakasaya at hinding-hindi ko makakalimutan hanggang sa pagtanda natin. Ako ay nagpapasalamat na nakilala kita, at napakasaya at tanging maipagmamalaki na ikaw ang aking tanging babie. Ang taong 2024 ay napakasama saatin, noh? Tipong yung mga araw na nagkita tayo nung huling taon, pag pinagsama-sama ay parang isa o dalawang buwan lang. Nakakamiss yung mga panahon na kada linggo nagkikita tayo, minsan nga dumadating pa sa punto na araw-araw na. Nakakamiss yun. Sana itong taon na to ay mas maging isang taon na hinding-hindi natin makakalimutan. Sana yung mga pinaggagagawa natin noon, mabalik natin sa taon na to. Ikaw ay aking pinasasalamatan dahil ikaw ang nagbunyag saakin na karapat-dapat kong maramdaman ang pagmamahal, at ibigay din ito saiyo. Sa mga taon na to, ngayong tayo ay tatlong taon na, ako ay may malakas na loob na sabihin na ang nararamdaman ko sa iyo ay kailanman ay di nagbago at lalong-lalo na sa mga darating na panahon at taon, ay hinding-hindi lalo magbabago. Subalit, marami man akong dapat ipasalamat, marami rin akong dapat hingan ng patawad sa'yo. Ako ay humihingi ng patawad sa mga panahon na di ko nakontrol ang sarili ko pag ako'y iritable. Pangako ko na iyon ay aking babaguhin. Ako rin ay humihingi ng tawad dahil di pa rin ako nakakapunta diyan sa inyo, sa Pangasinan. Pangako mahal, pagtapos neto lahat, makakapunta rin ako, ha? Antayin mo lang ako. Pero ako ay humihingi ng patawad don kasi alam kong matagal ka na ring nag aantay. Patawad dahil maraming beses kitang nabigo. Sa tatlong taon natin alam kong marami akong nagawang mga bagay na nakasakit sa'yo. Ako ay humihingi ng patawad sa lahat. Babie, mahal na mahal kita sobra. Kulang tong mga salita na 'to para mailahad sa'yo ang nararamdaman ko. 
    """

    # Display the love letter
    st.write(love_letter)

    # Subheader for the image slideshow
    st.header("I love you to the moon and back, always. 💖")
    st.title("Happy 3rd Anniversary!")

    # List of image paths (update these paths to your actual images)
    image_paths = [...]  # Keep your list of image paths here

    # Slider to select the current image
    image_index = st.slider("", 0, len(image_paths) - 1)
    st.image(image_paths[image_index])

# Starting screen
if st.button("Start"):
    display_main_content()
else:
    st.title("Welcome to the Love Letter App")
    st.write("Press the button below to start reading the love letter.")