import streamlit as st
import random

st.set_page_config(page_title="大阪おばちゃんチャット", page_icon="🍬")
st.title("🍬 大阪のおばちゃんチャットボット")
st.write("嫌やったこと言うてみ？おばちゃんが元気づけたろ！")

# ネガティブワードの例
negative_words = ["疲れた", "嫌だ", "もう無理", "だめ", "しんどい", "つらい","辛い","やりたくない","逃げたい","死にたい","泣きそう","消えたい"]

# 大阪おばちゃんの慰め言葉
obachan_responses = [
    "あんた、そないに落ち込みな！人生塞翁が馬っちゅーしな",
    "まぁまぁ、しゃーないわ。そんな時もあるてほら、お茶でも飲みや！",
    "そんな時もあるわ。ウチがついとるさかい心配しな！",
    "あんまり気にせんと、別にあんただけが悪いんちゃうんやし。",
    "泣いたらスッキリするで！思いっきり泣きや〜",
    "よそはよそ、うちはうち！あんたはあんたでええねんで",
    "あんたご飯食べた？落ち込むんは食べてからにしぃや",
    "全部捨ててもええねんで。ゴミはぱーっと捨てなはれ",
    "誰やあんたのこといじめてんの！おばちゃんがネギでどついたるわ！",
]

# セッション履歴
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("あなたの疲れを一言でどうぞ", "")


if st.button("話しかける"):
    if user_input:
        st.session_state.chat_history.append(("あなた", user_input))

        if any(word in user_input for word in negative_words):
            response = random.choice(obachan_responses)
        else:
            response = "ぼちぼちやってるみたいやん。それはそれでええことや〜😊"

        st.session_state.chat_history.append(("おばちゃん", response))

# チャット履歴表示
for speaker, message in st.session_state.chat_history:
    st.markdown(f"**{speaker}**：{message}")