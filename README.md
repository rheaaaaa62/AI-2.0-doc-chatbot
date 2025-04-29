# Medical Chatbot with MultiModal LLM

AI Doctor 2.0 is an AI-powered multimodal medical chatbot that processes vision and voice inputs to assist in healthcare queries. It integrates speech-to-text, text-to-speech, and image-based analysis using LLMs to enable seamless doctor-patient interactions. The chatbot can transcribe speech, analyze medical images, and generate voice responses, making it useful for telemedicine and patient support.


Phase 1 – Setup the brain of the Doctor (Multimodal LLM)
● Setup GROQ API key
● Convert image to required format
● Setup Multimodal LLM 

Phase 2–Setup voice of the patient
● Setup Audio recorder (ffmpeg & portaudio)
● Setup Speech to text–STT–model for transcription

Phase 3–Setup voice of the Doctor
● Setup Text to Speech–TTS–model (gTTS & ElevenLabs)
● Use Model for Text output to Voice

Phase 4–Setup UI for the VoiceBot
● VoiceBot UI with Gradio

TOOLS AND TECHNOLOGIES USED:

● Groq for AI Inference
● OpenAI Whisper (Best open source model for Transcription)
● Llama 3 Vision (Open source by Meta)
● gTTS & ElevenLabs (Speech to Text)
● Gradio for UI
● Python
● VS Code

