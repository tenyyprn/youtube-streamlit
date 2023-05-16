import streamlit as st
import time

st.title('Streamlit超入門')

st.write('プレグレスバーの表示')
'start!!'
latest_iteration = st.empty()
bar = st.progress(0)

#バーとプログレスで進化させている。
#time.sleepが重要1からのカウントを時間制御できる。


for i in range(100):
    latest_iteration.text(f'Iteration{i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)
    
'Done!!!!!'



# df = pd.DataFrame({
#     '1列目': [1, 2, 3, 4],
#     '2列目': [10, 20, 30, 40]
# })

#st.table(df.style.highlight_max(axis=0))
#dataflame やtable,等、表を表示させるやり方を学ぶ
#streamlit.jsonでjsonを表示させることもできる。

#マジックコマンド
#章
## 節
###項    
###streamlit.関数を学ぶ
    
# df = pd.DataFrame(
    # np.random.rand(20,3),
    # columns=['a','b','c']
# )
# st.table(df.style.highlight_max(axis=0))
#グラフ表示、st.line_chart
#面グラフ　st.area_chart
#棒グラフ　st.bar_chart

# st.bar_chart(df)
# df

# df = pd.DataFrame(
#     np.random.rand(100, 2,)/[50, 50] +[35.69, 139.70],
    
#     #緯度と経度の百か所の位置をデータで用意されているものを読む
    
#     columns=['lat','lon']
# )

# #st.map(df) 新宿付近の経度緯度を足して、ランダムに生成されている緯度経度データ情報を
# #地図上でプロット、マッピングできる。apiのリファレンスで確認可能。

# st.map(df)

#イメージを表示させる。

# st.write('Display Image')

# # img = Image.open('sample.jpg')
# # st.image(img, caption='vessel', use_column_width=True)

# #音楽等も表示させることができる。

# #チェックボックス
# if st.checkbox('Show Image'):
#         img = Image.open('sample.jpg')
#         st.image(img, caption='vessel', use_column_width=True)

# #セレクトボックスで指定、optionに入る。

# option = st.selectbox(
#     'あなたが好きな数字を教えてください',
#     list(range(1, 11))
    
# ) 

# 'あなたの好きな数字は、', option, 'です。' 

# # st.sidebar.write('Intaractive Widgets')

# text = st.text_input('あなたの趣味を教えてください')
# 'あなたの趣味：', text, 'です。'

#スライダーによる動的変化
#最小値、最大値、デフォルト値を示す。
#api referenceで確認できる。

# condition = st.slider('あなたの今の調子は？', 0, 100, 50)
# 'コンディション:', condition

#サイドバーに表示可能。
#サイドバーにウィジェットを置き、右側に表示させる。

# text = st.sidebar.text_input('あなたの趣味を教えてください')
# condition = st.sidebar.slider('あなたの今の調子は？', 0, 100, 50)

# 'あなたの趣味：', text
# 'コンディション：', condition

#２つのカラムを追加。左のボタンを推すと、右カラムに文字を表示。
left_column, right_colums = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_colums.write('ここは右カラム')
    
expander1 = st.expander('問い合わせ')
expander1.write('問い合わせ1の回答')
expander2 = st.expander('問い合わせ')
expander2.write('問い合わせ２の回答')
expander3 = st.expander('問い合わせ')
expander3.write('問い合わせ３の回答')