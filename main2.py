#インタラクティブ（双方向）なウィジェット
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('Streamlit超入門')

st.write('Display Image')

#checkボックス
if st.checkbox('Show Image'):
        img = Image.open('sample.jpg')
        st.image(img, caption='vessel', use_column_width=True)
        
        