import streamlit as st 
import pandas as pd
import numpy as np 

print(pd.__version__)
print(np.__version__)

st.title('Streamlit 超入門')

"""
```python
import streamlit as st 
import numpy as np
import pandas as pd 

st.title('Streamlit 超入門')

df=pd.DataFrame({
    '1列目':[1,2,3,4],
    '2列目':[10,20,30,40]
})
st.DataFrame(df.style.highlight_max(axis=0))
```
"""

st.write('DataFrame')
df=pd.DataFrame({
    '1列目':[1,2,3,4],
    '2列目':[10,20,30,40]
})

def highlight_ner_row(x):
    color = ""
    if x.entity != "O":
        color = "background-color: skyblue;"
    return [color for _ in x]

#df = df.style.apply(highlight_ner_row,axis=1)
#df.style.highlight_max(axis=0)
#st.write(df)
#st.dataframe(df)
st.table(df)

"""
```python
df=pd.DataFrame(
     np.random.rand(20,3),
     columns=['a','b','c']
 )
st.line_chart(df)
st.area_chart(df)
st.bar_chart(df)
```
"""

df=pd.DataFrame(
     np.random.rand(20,3),
     columns=['a','b','c']
 )
st.line_chart(df)
st.area_chart(df)
st.bar_chart(df)

"""
```python
from PIL import Image

img = Image.open('sample.jpg')
st.image(img,caption='サンプル画像',use_column_width=True)
```
"""

from PIL import Image

if st.checkbox('Show Image'):
    img = Image.open('sample.jpg')
    st.image(img,caption='サンプル画像',use_column_width=True)
    

st.sidebar.write('<span style="color:red;background:pink">Configuration： Theme</span>',unsafe_allow_html=True)
st.sidebar.slider(label='Slider')
st.sidebar.selectbox(label='Choose Your Favourite', options=['Snowpeak', 'Rakuten', 'Toyota Motors'])

