import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import time


# progress bar

st.write('Progress bar')
'Start !!!'
latest_iteration =st.empty()
bar=st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration:{i+1}')
    bar.progress(i+1)
    time.sleep(0.1)
    
'Done !!!'

st.title("Title2")
st.write("Data Frame")
df=pd.DataFrame({
    "1st column": [1,2,3],
    "2nd column": [10,20,20],
})

st.write(df)

st.dataframe(df,width=250,height=200)
st.dataframe(df.style.highlight_max(axis=0),width=250,height=200)
st.table(df.style.highlight_max(axis=0))

"""
# 章
## 節
### 項
    
```python
import streamlit as st
import pandas as pd
import numpy as np
```   
"""


df2=pd.DataFrame(
    np.random.rand(10,3),
    columns=['a','b','c']
)
st.write(df2)

st.line_chart(df2)
st.area_chart(df2)
st.bar_chart(df2)



df3=pd.DataFrame(
    np.random.rand(10,2)/[50,50]+[35.69,139.70],    #新宿の緯度と経度
    columns=['lat','lon']
)

st.map(df3)

st.write("Display Image")
img=Image.open(r'C:\Users\ikyo1\Documents\Udemy\爆速で5つのPython Webアプリを開発\photo.png')

if st.checkbox('Show Image'):
    st.image(img, caption='sample',use_column_width=True)
    
opt=st.selectbox(
    '好きな数字は？',
    list(range(1,11))
)

'好きな数字は',opt,'です。'

st.write('Interactive widgets')
text=st.text_input(
    'Favorite hobby？'
)

'Favorite hobby is',text,'.'

condition=st.slider('your condition?',0,100,50)


'Condition is',condition,'.'

# sideber
st.sidebar.write('Input for Main')
text2=st.sidebar.text_input('Favorite hobby？',key='text2')
condition2=st.sidebar.slider('your condition?',0,100,50,key='condition2')
'Favorite hobby is',text2,'.'
'Condition is',condition2,'.'


# 2 column
st.write('2 column')
#left_col, right_col=st.beta_columns(2)
left_col, right_col=st.columns(2)
button_left=left_col.button('Add the botton to right colmun')

if button_left:
    right_col.write('Right colmun')
    
    

# expander
expander=st.expander('問い合わせ')
expander.write('問い合わせ内容')
expander.write('問い合わせ内容')
expander.write('問い合わせ内容')

expander1=st.expander('問い合わせ1')
expander1.write('問い合わせ1の回答')
expander2=st.expander('問い合わせ2')
expander2.write('問い合わせ2の回答')
expander3=st.expander('問い合わせ3')
expander3.write('問い合わせ3の回答')