import os
import shutil

def move_wav_files(src_directory, target_directory):
    if not os.path.exists(target_directory):
        os.makedirs(target_directory)
        print(f"Created directory: {target_directory}")

    file_count = 0
    for root, dirs, files in os.walk(src_directory):
        for file in files:
            if file.endswith('.wav'):
                source_file = os.path.join(root, file)
                target_file = os.path.join(target_directory, file)
                
                # Check if file already exists in target directory
                original_target = target_file
                counter = 1
                while os.path.exists(target_file):
                    # Append a counter to the filename to avoid overwriting
                    base, ext = os.path.splitext(original_target)
                    target_file = f"{base}_{counter}{ext}"
                    counter += 1

                shutil.move(source_file, target_file)
                print(f"Moved {file} to {target_file}")
                file_count += 1

    print(f"Total files moved: {file_count}")

if __name__ == '__main__':
    base_dir = 'UBI_COMP_TRAINING_DATA'  # Update this path if necessary
    target_dir = os.path.join(base_dir, 'Total_dataset')
    move_wav_files(base_dir, target_dir)
