import os
import sys

def parse_filename(filename):
    parts = filename.split('-')
    # Decode the filename components
    modality = {'01': 'Audio_only', '02': 'Video_only', '03': 'Audio_only'}.get(parts[0], 'Unknown_modality')
    vocal_channel = {'01': 'Speech', '02': 'Song'}.get(parts[1], 'Unknown_channel')
    emotion = {
        '01': 'Neutral', '02': 'Calm', '03': 'Happy', '04': 'Sad',
        '05': 'Angry', '06': 'Fearful', '07': 'Disgust', '08': 'Surprised'
    }.get(parts[2], 'Unknown_emotion')
    intensity = {'01': 'Normal_intensity', '02': 'Strong_intensity'}.get(parts[3], 'Unknown_intensity')
    statement = {'01': 'Kids_talking', '02': 'Dogs_sitting'}.get(parts[4], 'Unknown_statement')
    repetition = 'First_repetition' if parts[5] == '01' else 'Second_repetition'
    actor_id = f"Actor_id_{parts[6].split('.')[0]}"  # Remove file extension for actor ID
    return modality, vocal_channel, emotion, intensity, statement, repetition, actor_id

def rename_and_categorize_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.wav') and '-' in file:
                modality, vocal_channel, emotion, intensity, statement, repetition, actor_id = parse_filename(file)
                
                # Check if the modality is audio-only; if not, delete the file
                if modality != 'Audio_only':
                    os.remove(os.path.join(root, file))
                    print(f"Deleted {file} due to incompatible modality ({modality}).")
                    continue
                
                # Determine emotion category
                category = 'non_negative' if emotion in ['Neutral', 'Calm', 'Happy', 'Surprised'] else 'negative'
                
                # Create new filename
                new_filename = f"{category}.{modality}-{vocal_channel}-{emotion}-{intensity}-{statement}-{repetition}-{actor_id}.wav"
                original_path = os.path.join(root, file)
                new_path = os.path.join(root, new_filename)
                
                # Move and rename the file
                if not os.path.exists(new_path):
                    os.rename(original_path, new_path)
                    print(f"Renamed and moved {file} to {new_filename}")
                else:
                    print(f"File {new_filename} already exists. Skipping.")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python RAVDESS_rename_files.py <base_directory>")
        sys.exit(1)
    
    base_directory = sys.argv[1]
    rename_and_categorize_files(base_directory)
