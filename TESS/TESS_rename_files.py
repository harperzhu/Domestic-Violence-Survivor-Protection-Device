import os
import sys

def rename_files(base_directory):
    # Map of folder names to their new prefix based on emotion
    emotion_mapping = {
        'angry': 'negative',
        'disgust': 'negative',
        'fear': 'negative',
        'sad': 'negative',
        'happy': 'non_negative',
        'pleasant_surprise': 'non_negative',
        'neutral': 'non_negative'
    }

    # Traverse through each directory and subdirectory
    for root, dirs, files in os.walk(base_directory):
        for file in files:
            if file.endswith(".wav"):
                # Determine the current emotion from the directory name
                current_emotion = root.split(os.path.sep)[-1].split('_')[-1]
                if current_emotion in emotion_mapping:
                    prefix = emotion_mapping[current_emotion]
                    dataset_initials = "TESS"
                    new_filename = f"{prefix}.{dataset_initials}_{file}"
                    original_path = os.path.join(root, file)
                    new_path = os.path.join(root, new_filename)
                    
                    # Rename the file
                    os.rename(original_path, new_path)
                    print(f"Renamed {file} to {new_filename}")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python TESS_rename_files.py <base_directory>")
        sys.exit(1)
    
    base_directory = sys.argv[1]
    if not os.path.isdir(base_directory):
        print(f"Error: {base_directory} is not a valid directory")
        sys.exit(1)
    
    rename_files(base_directory)
