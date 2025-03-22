import os

def rename_images(folder_path, start_number=1):
    print(f"Renaming images in folder: {folder_path}")
    # Get a sorted list of all image filenames in the folder
    image_files = sorted([f for f in os.listdir(folder_path) if f.startswith("frames_")])
    
    # Start renaming from the specified start_number
    for idx, filename in enumerate(image_files, start=start_number):
        # Create the new filename (padded with zeros, e.g., frames_0001)
        new_filename = f"frames_{idx:04}.jpg"  # Assuming the file extension is .jpg, change if different
        
        # Get the full paths for renaming
        old_file = os.path.join(folder_path, filename)
        new_file = os.path.join(folder_path, new_filename)
        
        # Rename the file
        os.rename(old_file, new_file)
        print(f"Renamed {old_file} to {new_file}")

# Example usage
rename_images('./logo', start_number=548) 