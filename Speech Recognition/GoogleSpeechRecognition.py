# Playing around the Google Speech Recognition API

import speech_recognition as sr
import time
r = sr.Recognizer()

MICROSOFT_COGNITIVE_SERVICES_API_KEY = "c7f71b677a364f18aa96220bb1793316"
print(sr.Microphone.list_microphone_names())

'''
['Microsoft Sound Mapper - Input', 'Microphone Array (IDT High Defi', 'Microphone / Line In (IDT High ', 'Dock Mic (IDT High Definition A', 'Microsoft Sound Mapper - Output', 'Speakers / Headphones (IDT High', 'Independent (R.T.C.) Headphones', 'Primary Sound Capture Driver', 'Microphone Array (IDT High Definition Audio CODEC)', 'Microphone / Line In (IDT High Definition Audio CODEC)', 'Dock Mic (IDT High Definition Audio CODEC)', 'Primary Sound Driver', 'Speakers / Headphones (IDT High Definition Audio CODEC)', 'Independent (R.T.C.) 
Headphones (IDT High Definition Audio CODEC)', 'Speakers / Headphones (IDT High Definition Audio CODEC)', 'Independent (R.T.C.) Headphones (IDT High Definition Audio CODEC)', 'Microphone Array (IDT High Definition Audio CODEC)', 'Microphone / Line In (IDT High Definition Audio CODEC)', 'Dock Mic (IDT High Definition Audio CODEC)', 'Headphones (HpOut)', 'Microphone / Line In (MuxedIn)', 'Dock Mic (MuxedIn)', 'Rec. Playback (MuxedIn)', 'Speakers (Speaker/HP)', 'Microphone Array (MicIn2)']
'''

mic = sr.Microphone()  # Using the default system microphone

print("Please Say something !!")
with mic as source:
    r.adjust_for_ambient_noise(source) # To prevent noise or interference
    audio = r.listen(source)

# Requires Internet connection

try:
    start = time.time()
    print(f"[GOOGLE] You said : {r.recognize_google(audio)}")
    end = time.time()
    print(f"Time Elapsed - {(end - start)*1000} ms")
    print("="*50)

except Exception as e:
    print(f"Error : {e}")
# print(r.recognize_google_cloud(audio))

try:
    start = time.time()
    print(r.recognize_bing(audio, key = MICROSOFT_COGNITIVE_SERVICES_API_KEY))
    end = time.time()
    print(f"Time Elapsed - {(end - start)*1000} ms")
    print("="*50)


except Exception as e:
    print(f"Error : {e}")

# Does not Require internet connection (CMU Sphinx)

try:
    start = time.time()
    print(f"[CMU SPHINX] You said : {r.recognize_sphinx(audio)}")
    end = time.time()
    print(f"Time Elapsed - {(end - start)*1000} ms")
    print("="*50)

except Exception as e:
    print(f"Error : {e}")



