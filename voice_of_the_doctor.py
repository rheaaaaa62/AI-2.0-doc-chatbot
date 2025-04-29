

# if you dont use pipenv uncomment the following:
# from dotenv import load_dotenv
# load_dotenv()

#Step1a: Setup Text to Speech–TTS–model with gTTS
import os
from gtts import gTTS

def text_to_speech_with_gtts_old(input_text, output_filepath):
    language="en"

    audioobj= gTTS(
        text=input_text,
        lang=language,
        slow=False
    )
    audioobj.save(output_filepath)


input_text="Hi this is Ai with Hassan!"
text_to_speech_with_gtts_old(input_text=input_text, output_filepath="gtts_testing.mp3")



#Step2: Use Model for Text output to Voice

import platform
import subprocess
from gtts import gTTS
from playsound import playsound
import platform
import subprocess
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play

def text_to_speech_with_gtts(input_text, output_filepath="final.mp3"):
    language = "en"

    # Generate speech
    audioobj = gTTS(text=input_text, lang=language, slow=False)
    audioobj.save(output_filepath)

    # Convert MP3 to WAV
    wav_filepath = output_filepath.replace(".mp3", ".wav")
    sound = AudioSegment.from_mp3(output_filepath)
    sound.export(wav_filepath, format="wav")

    # Play WAV file
    play(AudioSegment.from_wav(wav_filepath))

# Test the function
input_text = "Hi, this is AI Doctor VoiceBot, testing audio playback!"
text_to_speech_with_gtts(input_text=input_text)
'''
def text_to_speech_with_gtts(input_text, output_filepath="gtts_testing_autoplay.mp3"):
    language = "en"

    # Generate speech
    audioobj = gTTS(text=input_text, lang=language, slow=False)
    audioobj.save(output_filepath)

    os_name = platform.system()
    try:
        if os_name == "Windows":  # ✅ Use playsound for MP3 playback
            playsound(output_filepath)
        elif os_name == "Darwin":  # macOS
            subprocess.run(['afplay', output_filepath])
        elif os_name == "Linux":  # Linux
            subprocess.run(['mpg123', output_filepath])  # Use mpg123 for MP3 playback
        else:
            raise OSError("Unsupported operating system")
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")

# Test the function
# input_text = "Hi, this is AI Doctor VoiceBot, autoplay testing!"
#text_to_speech_with_gtts(input_text=input_text)'''



'''def text_to_speech_with_elevenlabs(input_text, output_filepath):
    client=ElevenLabs(api_key=ELEVENLABS_API_KEY)
    audio=client.generate(
        text= input_text,
        voice= "Aria",
        output_format= "mp3_22050_32",
        model= "eleven_turbo_v2"
    )
    elevenlabs.save(audio, output_filepath)
    os_name = platform.system()
    try:
        if os_name == "Darwin":  # macOS
            subprocess.run(['afplay', output_filepath])
        elif os_name == "Windows":  # Windows
            subprocess.run(['powershell', '-c', f'(New-Object Media.SoundPlayer "{output_filepath}").PlaySync();'])
        elif os_name == "Linux":  # Linux
            subprocess.run(['aplay', output_filepath])  # Alternative: use 'mpg123' or 'ffplay'
        else:
            raise OSError("Unsupported operating system")
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")

text_to_speech_with_gtts(input_text, output_filepath="elevenlabs_testing_autoplay.mp3")'''

