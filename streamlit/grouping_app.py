# -*- coding: utf-8 -*-

import streamlit as st
import numpy as np
import pandas as pd
import statistics as stc

def csv():
    st.title("CSVファイルのクラス分け")

    #ファイルのアップロード
    uploaded_file = st.file_uploader("ファイルのアップロード", type='csv')

    #ファイルがアップロードされたら実行される処理
    if uploaded_file is not None:
        #ファイルによってはエンコードでエラーを吐く可能性あり
        df = pd.read_csv(uploaded_file, encoding="utf-8")
        df["クラス"] = ""

        st.markdown("### original CSV file")
        st.write(df)
        #フルサイズ表示
        if st.button("全て表示する", key="button01"):
            # st.tableでフルサイズ表示
            st.table(df)

        def devive(keyword, number):

            #status_text = st.empty()
            #progress_bar = st.progress(0)
            #i = 0
            List = []

            # リストに成績を入れていく
            for Column in range(len(df)):
                if keyword == df.iloc[Column, 0][2:4]:
                    List.insert(Column, df.iloc[Column, 1])

            # クラス分けする処理
            for Check in range(len(df)):
                # ２クラスに分ける場合の処理
                if df.iloc[Check, 0][2:4] == keyword and number == 2:
                    median = stc.median(List)
                    if df.iloc[Check, 1] <= median:
                        df.iloc[Check, 2] = "b"
                    elif df.iloc[Check, 0][2:4] == keyword:
                        df.iloc[Check, 2] = "a"

                # ３クラスに分ける場合の処理
                if df.iloc[Check, 0][2:4] == keyword and number == 3:
                    percentile = np.percentile(List, 33)
                    if df.iloc[Check, 1] < percentile:
                        df.iloc[Check, 2] = "c"
                    elif df.iloc[Check, 0][2:4] == keyword and Check < len(List) / 3:
                        df.iloc[Check, 2] = "a"
                    elif df.iloc[Check, 0][2:4] == keyword:
                        df.iloc[Check, 2] = "b"

                # 実行状況
                #status_text.text(f'Progress: {i}%')
                #progress_bar.progress(i)
                #i += 1

        # クラス分けしたい学科の学籍番号と何クラスに分けるかを入力して上の関数を実行する
        devive("A1", 3)
        devive("A2", 2)
        devive("A3", 2)
        devive("A4", 3)
        devive("A5", 2)
        devive("A6", 2)
        devive("B1", 3)
        devive("B2", 3)
        devive("B3", 3)
        devive("C1", 3)
        devive("C3", 2)
        devive("31", 3)
        devive("32", 3)

        st.sidebar.text('Done!')
        st.balloons()
        
        st.markdown("---")
        st.success("クラス分け完了")
        st.write(df)

        #フルサイズ表示
        if st.button("全て表示する", key="button02"):
            # st.tableでフルサイズ表示
            st.table(df)

        #ダウンロード
        st.download_button(
            label="Download data as CSV",
            data=df.to_csv(),
            file_name='out.csv',
            key="output01"
        )

        #ダウンロード
        st.sidebar.download_button(
            label="Download data as CSV",
            data=df.to_csv(),
            file_name='out.csv',
            key="output02"
        )

#サイドバー管理
menu_list = ["csv"]
sidebar = st.sidebar.selectbox(("Menu"), menu_list)

if sidebar == "csv":
    csv()