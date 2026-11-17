import urllib.request
import os
import ssl
import certifi

def download_files():
    # Create SSL context using certifi
    ssl_context = ssl.create_default_context(cafile=certifi.where())
    
    # URLs for the model files

    files = {
        'yolov4-tiny.weights': 'https://github.com/AlexeyAB/darknet/releases/download darknet_yolo_v4_pre/yolov4-tiny.weights',
        'yolov4-tiny.cfg': 'https://raw.githubusercontent.com/AlexeyAB/darknet/master/cfg/yolov4-tiny.cfg',
        'coco.names': 'https://raw.githubusercontent.com/AlexeyAB/darknet/master/data/coco.names'
    }

    
    print("Downloading required model files...")
    
    for filename, url in files.items():
        if not os.path.exists(filename):
            print(f"Downloading {filename}...")
            try:
                # Create a request with headers
                req = urllib.request.Request(
                    url,
                    headers={'User-Agent': 'Mozilla/5.0'}
                )
                
                # Download the file
                with urllib.request.urlopen(req, context=ssl_context) as response:
                    with open(filename, 'wb') as f:
                        f.write(response.read())
                        
                print(f"Successfully downloaded {filename}")
                
                # Verify file exists and has size > 0
                if os.path.exists(filename) and os.path.getsize(filename) > 0:
                    print(f"Verified {filename}")
                else:
                    print(f"Error: {filename} is empty or missing")
                    return False
                    
            except Exception as e:
                print(f"Error downloading {filename}: {str(e)}")
                return False
        else:
            print(f"{filename} already exists")
            
            # Verify existing file
            if os.path.getsize(filename) == 0:
                print(f"Error: {filename} exists but is empty. Deleting and retrying...")
                os.remove(filename)
                return download_files()
    
    print("All files downloaded successfully!")
    return True

if __name__ == "__main__":
    # First install certifi if not present
    try:
        import certifi
    except ImportError:
        print("Installing certifi...")
        import subprocess
        subprocess.check_call(['pip', 'install', 'certifi'])
        import certifi
    
    success = download_files()
    
    if success:
        print("\nVerifying files...")
        all_files_present = all(os.path.exists(f) and os.path.getsize(f) > 0 for f in [
            'yolov4-tiny.weights',
            'yolov4-tiny.cfg',
            'coco.names'
        ])
        
        if all_files_present:
            print("All files are present and valid!")
        else:
            print("Some files are missing or invalid. Please run the script again.")
    else:
        print("Download failed. Please try again.") 