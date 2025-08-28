# --- IMPORTANT: Before running, make sure you've installed gTTS, pydub, and FFmpeg! ---

import os
from gtts import gTTS
from pydub import AudioSegment

# --- PART 1: Your Document Text & Settings ---

# 1. PASTE YOUR ENTIRE DOCUMENT TEXT HERE!
#    This variable will hold all the pattern explanations you provided.
document_text = ""

# 2. What you want the final MP3 audio file to be named
output_mp3_filename = "my_document_audio.mp3"

# --- PART 2: Function to do the work ---

def text_to_audio_file(text_content, audio_output_filename, chunk_size=3000):
    """
    Converts a long string of text into an MP3 audio file.
    Splits long text into chunks to avoid TTS service limits and combines them.
    """
    print(f"Starting text-to-speech conversion for: {audio_output_filename}")
    temp_audio_files = []
    
    # Split text into manageable chunks. Prioritize natural breaks like paragraphs and sentences.
    paragraphs = text_content.split('\n\n') 
    final_chunks = []
    current_chunk_sentences = []
    current_chunk_len = 0
    
    for para in paragraphs:
        split_sentences_in_para = [s.strip() for s in para.split('.') if s.strip()]
        
        for sentence in split_sentences_in_para:
            if current_chunk_len + len(sentence) + 2 <= chunk_size: # +2 for potential space and period
                current_chunk_sentences.append(sentence)
                current_chunk_len += len(sentence) + 2
            else:
                if current_chunk_sentences:
                    final_chunks.append(". ".join(current_chunk_sentences) + ".")
                current_chunk_sentences = [sentence]
                current_chunk_len = len(sentence) + 2
        
        if current_chunk_sentences:
            final_chunks.append(". ".join(current_chunk_sentences) + ".")
            current_chunk_sentences = []
            current_chunk_len = 0

    if not final_chunks and text_content.strip(): # Fallback for very short texts or no natural breaks
        final_chunks = [text_content[i:i + chunk_size] for i in range(0, len(text_content), chunk_size)]


    if not final_chunks:
        print("No text found or processed to convert to audio. Cannot generate audio.")
        return None

    for i, chunk in enumerate(final_chunks):
        if not chunk.strip(): # Skip empty chunks
            continue
        try:
            tts = gTTS(text=chunk, lang='en') # 'en' for English
            temp_file = f"temp_chunk_{i}.mp3"
            tts.save(temp_file)
            temp_audio_files.append(temp_file)
            print(f"  Generated audio for chunk {i+1}/{len(final_chunks)}")
        except Exception as e:
            print(f"ERROR: Could not generate audio for chunk {i+1}. Problem: {e}")
            print(f"  Problematic chunk text (first 100 chars): '{chunk[:100]}...'")
            print("  This might be due to a network issue, a very long word, or an unsupported character.")

    if not temp_audio_files:
        print("No audio chunks were successfully generated. Cannot create main audio file.")
        return None

    # Combine all temporary audio files into one
    combined_audio = AudioSegment.empty()
    for temp_file in temp_audio_files:
        try:
            audio_segment = AudioSegment.from_mp3(temp_file)
            combined_audio += audio_segment
            os.remove(temp_file) # Clean up the temporary MP3 file
        except Exception as e:
            print(f"ERROR: Could not combine audio file '{temp_file}'. Problem: {e}. This part might be missing from the final audio.")

    if not combined_audio.duration_seconds > 0:
        print("Combined audio is empty or too short. Audio file not created.")
        return None

    combined_audio.export(audio_output_filename, format="mp3")
    print(f"SUCCESS! Full audio file created: {audio_output_filename}")
    return audio_output_filename

# --- PART 3: Run the Program ---
if __name__ == "__main__":
    print("--- Starting Document to MP3 Conversion ---")
    print("Please ensure your 'document_text' variable is correctly set in the code!")

    # Convert text to audio
    generated_audio_file = text_to_audio_file(document_text, output_mp3_filename)

    if not generated_audio_file:
        print("Audio generation failed. No MP3 file was created.")

    print("\n--- Process Finished ---")