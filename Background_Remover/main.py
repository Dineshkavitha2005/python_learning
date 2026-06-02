import streamlit as st
from rembg import remove
from PIL import Image

def removebg(img):
    im = Image.open(img).convert("RGBA")
    return remove(im)



def main():
    st.title("Background Remover App")
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        st.image(uploaded_file, caption="Uploaded Image")


        st.write("Processing...")
        try:
            result = removebg(uploaded_file)
            st.success("Done")
            st.image(result, caption="Result")
        except Exception as e:
            st.error(f"Background removal failed: {e}")



main()

