import streamlit as st

st.title("材質判定アプリ")

z = st.number_input("重量 (g)", min_value=0.0, step=0.1)
y = st.number_input("浮力 (g)", min_value=0.0, step=0.1)

if st.button("判定する"):
    if y == 0:
        st.error("水中での増加分 y を入力してください")
    else:
        density = z / y

        if density <= 3:
            material = "アルミ"
        elif density < 9:
            material = "鉄"
        elif density < 11.3:
            material = "鉛"
        elif density < 14:
            material = "樹脂タングステン"
        else:
            material = "タングステン"

        st.write(f"密度：{density:.2f} g/cm³")
        st.success(f"判定：{material}")
