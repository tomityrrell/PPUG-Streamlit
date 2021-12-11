# import streamlit, dependencies
from pytesseract import image_to_data, Output
from PIL import Image, ImageDraw
import streamlit as st

# upload images
image_upload = st.file_uploader("Choose an image", type=["png", "jpg"])
image_placeholder = st.empty()

# visualize images
if image_upload:
    image = Image.open(image_upload)
    image_placeholder.image(image)

    # Apply pytesseract
    if st.button("Activate the tesseract!!"):
        image_data = image_to_data(image, config="--psm 6", output_type=Output.DATAFRAME)
        image_data = image_data[image_data.conf > 90].reset_index(drop=True)

        # inspect dataframe results
        st.write(image_data)

        # annotate image
        annotated_image = ImageDraw.Draw(image)
        for (_, word) in image_data.iterrows():
            annotated_image.rectangle([word.left,
                                       word.top,
                                       word.left + word.width,
                                       word.top + word.height], outline="red", width=2)

        # view new image!
        image_placeholder.image(image)
