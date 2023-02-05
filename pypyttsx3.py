#vào url xem cách cài giọng nói tiếng việt "https://www.youtube.com/watch?v=qVMHoCtjLag"
import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty("voices")
vi_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_viVN_An"
engine.setProperty("voice",vi_voice_id)
engine.say("xin chào các bạn")
engine.runAndWait()
print("hello")