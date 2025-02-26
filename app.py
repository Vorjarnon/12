import streamlit as st
import time

# List of image paths (update these paths to your actual images)
image_paths = [
    "img/image1.jpg",
    "img/image2.jpg",
    "img/image3.jpg",
    "img/image5.jpg",
    "img/image6.jpg",
    "img/image7.jpg",
    "img/image8.jpg",
    "img/image9.jpg",
    "img/image10.jpg",
    "img/image11.jpg",
    "img/image12.jpg",
    "img/image13.jpg",
    "img/image14.jpg",
    "img/image15.jpg",
    "img/image16.jpg",
    "img/image17.jpg",
    "img/image18.jpg",
    "img/image19.jpg",
    "img/image20.jpg",
    "img/image21.jpg",
    "img/image22.jpg",
    "img/image23.png",
    "img/image24.jpg",
    "img/image25.png",
    "img/image26.jpg",
    "img/image27.jpg",
    "img/image28.jpg",
    "img/image29.jpg",
    "img/image30.jpg",
    "img/image31.jpg",
    "img/image32.jpg",
    "img/image33.jpg",
    "img/image34.jpg",
    "img/image35.jpg",
    "img/image36.jpg",
    "img/image37.jpg",
    "img/image38.jpg",
    "img/image39.jpg",
    "img/image40.jpg",
    "img/image41.jpg",
    "img/image42.jpg",
    "img/image43.jpg",
    "img/image44.jpg",
    "img/image45.jpg",
    "img/image46.jpg",
    "img/image47.jpg",
    "img/image48.jpg",
    "img/image49.jpg",
    "img/image50.jpg",
    "img/image51.jpg",
    "img/image52.jpg",
    "img/image53.jpg",
    "img/image54.jpg",
    "img/image55.jpg",
    "img/image56.jpg",
    "img/image57.jpg",
    "img/image58.jpg",
    "img/image59.jpg",
    "img/image60.jpg",
    "img/image61.jpg",
    "img/image62.jpg",
    "img/image63.jpg",
    "img/image64.jpg",
    "img/image65.jpg",
    "img/image66.jpg",
    "img/image67.jpg",
    "img/image68.jpg",
    "img/image69.jpg",
    "img/image70.jpg",
    "img/image71.jpg",
    "img/image72.jpg",
    "img/image73.jpg",
    "img/image74.jpg",
    "img/image75.jpg",
    "img/image76.jpg",
    "img/image77.jpg",
    "img/image78.jpg",
    "img/image79.jpg",
    "img/image80.jpg",
    "img/image81.jpg",
    "img/image82.jpg",
    "img/image83.jpg",
    "img/image84.jpg",
    "img/image85.jpg",
    "img/image86.jpg",
    "img/image87.jpg",
    "img/image88.jpg",
    "img/image89.jpg",
    "img/image90.jpg",
    "img/image91.jpg",
    "img/image92.jpg",
    "img/image93.jpg",
    "img/image94.jpg",
    "img/image95.jpg",
    "img/image96.jpg",
    "img/image97.jpg",
    "img/image98.jpg",
    "img/image99.jpg",
    "img/image100.jpg",
    "img/image101.jpg",
    "img/image102.jpg",
    "img/image103.jpg",
    "img/image104.jpg",
    "img/image105.jpg",
    "img/image106.jpg",
    "img/image107.jpg",
    "img/image108.jpg",
    "img/image109.jpg",
    "img/image110.jpg",
    "img/image111.jpg",
    "img/image112.jpg",
    "img/image113.jpg",
    "img/image114.jpg",
    "img/image115.jpg",
    "img/image116.jpg",
    "img/image117.jpg",
    "img/image118.jpg",
    "img/image119.jpg",
    "img/image120.jpg",
    "img/image121.jpg",
    "img/image122.jpg",
    "img/image123.jpg",
    "img/image124.jpg",
    "img/image125.jpg",
    "img/image126.jpg",
    "img/image127.jpg",
    "img/image128.jpg",
    "img/image129.jpg",
    "img/image130.jpg",
    "img/image131.jpg",
    "img/image132.jpg",
    "img/image133.jpg",
    "img/image134.jpg",
    "img/image135.jpg",
    "img/image136.jpg",
    "img/image137.jpg",
    "img/image138.jpg",
    "img/image139.jpg",
    "img/image140.jpg",
    "img/image141.jpg",
    "img/image142.jpg",
    "img/image143.jpg"
]

# Initialize session state for image index if not already done
if 'image_index' not in st.session_state:
    st.session_state.image_index = 0  # Default index

# Function to display the main content
def display_main_content():
    # Streamlit app title
    st.title("Happy 3rd Anniversary, Babie! 💖")

    # Love letter content
    love_letter = """
    Nakalipas na ng 1096 na araw simula nung naging tayo. Dami nating napagdaanan, dami nating napagusapan, nalaman sa isa't isa, napagtawanan, napagawayan, pagkatampuhan, at maraming-maraming-marami pa. Ang mga taon na to ay napakasaya at hinding-hindi ko makakalimutan hanggang sa pagtanda natin. Ako ay nagpapasalamat na nakilala kita, at napakasaya at tanging maipagmamalaki na ikaw ang aking tanging babie. Ang taong 2024 ay napakasama saatin, noh? Tipong yung mga araw na nagkita tayo nung huling taon, pag pinagsama-sama ay parang isa o dalawang buwan lang. Nakakamiss yung mga panahon na kada linggo nagkikita tayo, minsan nga dumadating pa sa punto na araw-araw na. Nakakamiss yun. Sana itong taon na to ay mas maging isang taon na hinding-hindi natin makakalimutan. Sana yung mga pinaggagagawa natin noon, mabalik natin sa taon na to. Ikaw ay aking pinasasalamatan dahil ikaw ang nagbunyag saakin na karapat-dapat kong maramdaman ang pagmamahal, at ibigay din ito saiyo. Sa mga taon na to, ngayong tayo ay tatlong taon na, ako ay may malakas na loob na sabihin na ang nararamdaman ko sa iyo ay kailanman ay di nagbago at lalong-lalo na sa mga darating na panahon at taon, ay hinding-hindi lalo magbabago. Subalit, marami man akong dapat ipasalamat, marami rin akong dapat hingan ng patawad sa'yo. Ako ay humihingi ng patawad sa mga panahon na di ko nakontrol ang sarili ko pag ako'y iritable. Pangako ko na iyon ay aking babaguhin. Ako rin ay humihingi ng tawad dahil di pa rin ako nakakapunta diyan sa inyo, sa Pangasinan. Pangako mahal, pagtapos neto lahat, makakapunta rin ako, ha? Antayin mo lang ako. Pero ako ay humihingi ng patawad don kasi alam kong matagal ka na ring nag aantay. Patawad dahil maraming beses kitang nabigo. Sa tatlong taon natin alam kong marami akong nagawang mga bagay na nakasakit sa'yo. Ako ay humihingi ng patawad sa lahat. Babie, mahal na mahal kita sobra. Kulang tong mga salita na 'to para mailahad sa'yo ang nararamdaman ko. Gusto kong magpasalamat kasi napakalaki ng pasensya mo saakin. Sa mga kagaguhan na ginagawa ko araw-araw, sa ugali kong 'to. Salamat sobra. Salamat dahil sa mga araw na walang-wala akong gana gumawa ng kung ano-ano, binibigyan mo ko ng lakas para gumalaw at magpursigi sa kung ano mang gagawin ko. Salamat dahil ikaw ang aking motivasyon para gawin ang lahat. Totoo talaga na kung wala ka, siguro walang-wala ako. Mahal na mahal kita, masabi ko lang uli. Mahal na mahal talaga kita. Isa sa mga magiging dasal ko para sa magiging 2025 natin ay maging mas maganda sana ang taon na to para saating dalawa. Pinagdarasal ko na mas marami pa tayong magawang mga alaala ngayon, at sana di magbago ang pagmamahal mo saakin. Inuulit ko, mahal na mahal kita. Salamat din pala sa mga naibigay mo sakin. Mga regalo, pagkain, at iba pa. Lahat yun ay nasaakin pa (Syempre yung pagkain hindi, diba? HAHAHA) at aalagaan ko nang maayos. Pag magkasama na tayo sa iisang bahay, dala-dala ko yun lahat hehe. Miss na kita. Miss na kita makasama uli, miss na kita kulitin, lahat eh. Kahit yung mga simpleng kain dates lang natin tas gala tas dessert. Nakakamiss sobra. Gusto ko na bumalik yun lahat baby. Gusto nalang kita makasama ulit. Wag mo ko sukuan, ha? I have made many mistakes, but I swear that I will fix them all. I promise to be a better man for you every day. Don't forget that I'll be your supporter, your support, and your shoulder to cry on. I'll always be here whenever you need me. I love you baby. Mahal na mahal kita. Hinding-hindi magbabago ang nararamdaman ko sa'yo. Kahit kelan pa yan si Shane lang mamahalin ko. My future Pharmacist hehe. Tignan mo lahat ng mga picture ha. Pinaghirapan ko yan AHAHAHA. Chineck ko code ko bali asa 142 images yan lahat. From video call days natin to latest picture natin (May tinanggal akong isa, pasend mo nalang siguro mamaya sa chat. Nahiya lang ako kaya tinanggal ko HAHAHA). Marami-rami rin kulang pero iuupdate ko naman yung mga pictures para sa mga susunod HAHAHAHA. I LOVE YOU MY BABYYYYYY Sana naenjoy mo to TvT
    """
    
    # Display the love letter
    st.write(love_letter)

    # Subheader for the image slideshow
    st.title("I love you to the moon and back. Always. 💖")

    # Add background music
    st.audio("loml.mp3", start_time=0)  # Update with your music file path
    st.write("Play music, then enjoy the slideshow hehe")
    st.write("**Naka autoplay pala tong slideshow kasi naka code na after mo pindutin yung START magpplay na siya 😭 Refresh mo nalang yung site babie tas after mo istart balik ka kagad hereeee**")

    # Automatic slideshow
    image_placeholder = st.empty()
    while True:
        for image_path in image_paths:
            image_placeholder.image(image_path)
            time.sleep(2)  # Change the duration as needed

# Starting screen
if st.button("START"):
    display_main_content()
else:
    # Add video to the starting screen
    st.video("143.mp4")
    st.subheader("*^^PRESS START^^*")