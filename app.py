import streamlit as st 

import edge_tts as ts

import asyncio as a 



st.title("convert text to sound")

text =st.text_area("Enter your text")

lang = st.selectbox("choose your languge", ["عربي","English"])

VOICES = {
    "عربي": {
        
        " زارية (امرأة - السعودية)": "ar-SA-ZariyahNeural",
        " جمال (رجل - مصر)":         "ar-EG-ShakirNeural",
        " سلمى (امرأة - مصر)":       "ar-EG-SalmaNeural",
    },
    "English": {
        " غاي (رجل - أمريكا)":       "en-US-GuyNeural",
        " جيني (امرأة - أمريكا)":    "en-US-JennyNeural",
        " رايان (رجل - بريطانيا)":   "en-GB-RyanNeural",
        " ليبرا (امرأة - بريطانيا)": "en-GB-LibbyNeural",
    }
}
 
voice_label = st.selectbox("Choose Voice", list(VOICES[lang].keys()))
voice_id = VOICES[lang][voice_label]

async def generate_audio(text, voice):
    communicate = ts.Communicate(text=text, voice=voice)

    audio_chunks = []

    async for chunk in communicate.stream():
        if chunk['type'] == "audio":
            audio_chunks.append(chunk["data"])

    return b"".join(audio_chunks)

if st.button("Convert"):
    if text:
        audio_bytes = a.run(generate_audio(text, voice_id))
        st.audio(audio_bytes, format="audio/mp3")
    else:
        st.warning("اكنب النص وبعدها هنفتحلك")