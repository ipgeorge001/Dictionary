import steamlit as st



Hausa_dictionary = {
    "hello": "sannu",
    "thank you": "na gode",
    "water": "ruwa",
    "house": "gida",
    "food": "abinci",
    "come": "zo",
    "go": "je",
    "good": "mai kyau",
    "book": "littafi",
    "money": "kudi",
    "father": "uba",
    "mother": "uwa",
    "child": "yaro",
    "market": "kasuwa",
    "road": "hanya",
    "friend": "aboki",
    "sun": "rana",
    "moon": "wata",
    "star": "tauraro",
    "day": "rana"
}

yoruba_dictionary = {
    "hello": "ẹ̀ kaasan",
    "good morning": "ẹ̀ kaárọ̀",
    "thank you": "ẹ jẹ́jú",
    "please": "jọ̀wọ́",
    "yes": "bẹ́ẹ̀ni",
    "no": "rárá",
    "water": "omi",
    "sun": "òòrùn",
    "moon": "òṣùpá",
    "house": "ilé",
    "food": "oúnjẹ",
    "man": "ọkùnrin",
    "woman": "obìnrin",
    "child": "ọmọ",
    "love": "ìfẹ́",
    "friend": "ọ̀rẹ́",
    "come": "wá",
    "go": "lọ",
    "book": "ìwé",
    "money": "owó"
}

igala_dictionary = {
    "hello": "kóo",
    "how are you": "chí là?",
    "i am fine": "mé jé gá", 
    "thank you": "àhì",
    "welcome": "gbàwó",
    "person": "ónú",
    "man": "ókùnrin",
    "woman": "ónògbá",
    "child": "ómí",
    "father": "àbà",
    "eat": "jé",
    "drink": "myí",
    "come": "wá",
    "go": "lo",
    "sleep": "wó",
    "water": "ómí",
    "house": "ulé",
    "food": "òúnjé",
    "hand": "òwó",
    "money": "óchí"
}

st.title("Translator")

lang_data = {
    "hausa": Hausa_dictionary,
    "yoruba": yoruba_dictionary,
    "igala": igala_dictionary,
    
}

choice = st.selectbox("Select Language", ["hausa", "yoruba", "igala",])

english_word = st.text_input("Enter the English word to translate:").strip().lower()

if st.button("Translate"):
    if choice in lang_data:
        selected_dictionary = lang_data[choice]
        
        if english_word in selected_dictionary:
            translation = selected_dictionary[english_word]
            st.success(f"**English:** {english_word.capitalize()}")
            st.success(f"**{choice.capitalize()}:** {translation}")
        else:
            st.error(f"Sorry, the word '{english_word}' is not in the {choice.capitalize()} vocabulary.")
            st.write(f"Please try: {', '.join(selected_dictionary.keys())}")