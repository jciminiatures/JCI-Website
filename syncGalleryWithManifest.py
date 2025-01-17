import os
import json

gallery_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images", "gallery")

with open("manifest.json","r") as f:
    manifest = json.loads(f.read())
    files = os.listdir(gallery_path)

    # MACOS bypass
    try:
        files.remove(".DS_Store")
    except:
        pass

    for file in files:
        if file not in manifest["gallery"]:
            os.remove(os.path.join(gallery_path, file))
    
    for file in manifest["gallery"]:
        if file not in files:
            print(f"[ERROR]: File in manifest but not in gallery:{file}")

    print("[OK]: Finished syncing gallery to manifest.")