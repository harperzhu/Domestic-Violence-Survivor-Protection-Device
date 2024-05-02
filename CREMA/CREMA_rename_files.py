import os
import sys

def rename_files(directory):
    negative_emotions = {'ANG', 'DIS', 'FEA', 'SAD'}
    non_negative_emotions = {'HAP', 'NEU'}

    # Process each file in the directory
    for filename in os.listdir(directory):
        if filename.endswith(".wav"):  # Ensure we're only processing .wav files
            parts = filename.split('_')
            if len(parts) < 4 or filename.startswith("negative.") or filename.startswith("non_negative."):
                print(f"Skipping already processed or unexpected format file: {filename}")
                continue
            
            emotion_code = parts[2].upper()  # Emotion code is expected to be the third part
            dataset_initials = "IEO"  # Assuming DatasetInitials is static as "IEO"

            # Determine if the emotion is negative, non-negative, or neither
            if emotion_code in negative_emotions:
                prefix = "negative."
            elif emotion_code in non_negative_emotions:
                prefix = "non_negative."
            else:
                prefix = ""  # No prefix if the emotion is not recognized

            newname = f"{prefix}{dataset_initials}_{filename}"
            original_path = os.path.join(directory, filename)
            new_path = os.path.join(directory, newname)

            if not os.path.exists(new_path):
                os.rename(original_path, new_path)
                print(f"Renamed {filename} to {newname}")
            else:
                print(f"Error: Target name {newname} already exists, not renaming {filename}")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python CREMA_rename_files.py <directory>")
        sys.exit(1)
    
    directory = sys.argv[1]
    if not os.path.isdir(directory):
        print(f"Error: {directory} is not a valid directory")
        sys.exit(1)
    
    rename_files(directory)
