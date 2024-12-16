import pyttsx3
from pydub import AudioSegment
import os
import random

def initialize_tts_engine():
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    for voice in voices:
        if 'italian' in voice.name.lower():
            engine.setProperty('voice', voice.id)
            break
    return engine

def synthesize_speech(text, output_path, engine):
    engine.save_to_file(text, output_path)
    engine.runAndWait()

def apply_transformations(audio, speed_prob=0.7, pitch_prob=0.7, volume_prob=0.5, random_cut_prob=0.3):
    if random.random() < speed_prob:
        speed_factor = random.uniform(0.8, 1.2)  
        audio = audio._spawn(audio.raw_data, overrides={"frame_rate": int(audio.frame_rate * speed_factor)})
        audio = audio.set_frame_rate(16000)  
        print(f" - Modificata velocità: {speed_factor:.2f}")
    
    if random.random() < pitch_prob:
        semitones = random.uniform(-5, 5) 
        new_frame_rate = int(audio.frame_rate * (2 ** (semitones / 12.0)))
        audio = audio._spawn(audio.raw_data, overrides={"frame_rate": new_frame_rate})
        audio = audio.set_frame_rate(16000)  
        print(f" - Modificato pitch di {semitones:.2f} semitoni")
    
    if random.random() < volume_prob:
        volume_change = random.uniform(-10, 5) 
        audio = audio + volume_change
        print(f" - Modificato volume: {volume_change:.2f} dB")
    
    if random.random() < random_cut_prob:
        start_cut = random.randint(0, int(len(audio) * 0.2))  
        end_cut = random.randint(int(len(audio) * 0.8), len(audio))  
        audio = audio[start_cut:end_cut]
        print(f" - Tagliato audio: da {start_cut} ms a {end_cut} ms")
    
    return audio

def generate_audio(text, output_folder, engine, num_repeats=1, 
                   speed_prob=0.7, pitch_prob=0.7, volume_prob=0.5, random_cut_prob=0.3):
    os.makedirs(output_folder, exist_ok=True)  
    for i in range(num_repeats):
        temp_filename = os.path.join(output_folder, f"temp_{text}_{i+1}.wav")
        final_filename = os.path.join(output_folder, f"{text}_{i+1}.wav")
        
        synthesize_speech(text, temp_filename, engine)
        
        audio = AudioSegment.from_file(temp_filename)
        audio = apply_transformations(audio, speed_prob, pitch_prob, volume_prob, random_cut_prob)
        
        audio.export(final_filename, format="wav")
        os.remove(temp_filename)  
        print(f"Salvato: {final_filename}")

def generate_silence(output_folder, num_repeats=10, duration=1):
    os.makedirs(output_folder, exist_ok=True)  
    for i in range(num_repeats):
        silence = AudioSegment.silent(duration=duration * 1000)  
        filename = os.path.join(output_folder, f"silenzio_{i+1}.wav")
        silence.export(filename, format="wav")
        print(f"Generato file di silenzio: {filename}")

commands = ["destra", "sinistra", "su", "giù"]
output_folder = "test2Output"

# Inizializza il motore TTS
tts_engine = initialize_tts_engine()

# Genera i comandi
for command in commands:
    generate_audio(
        text=command,
        output_folder=output_folder,
        engine=tts_engine,
        num_repeats=3,
        speed_prob=0.7,  
        pitch_prob=0.3,  
        volume_prob=0.5,
        random_cut_prob=0.3  
    )

