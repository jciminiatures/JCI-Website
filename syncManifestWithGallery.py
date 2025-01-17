import os
import json

gallery_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images", "gallery")

with open("manifest.json","r") as f:
    old_manifest = json.loads(f.read())["gallery"]

with open("manifest.json","w") as f:
    files = os.listdir(gallery_path)

    # MACOS bypass
    try:
        files.remove(".DS_Store")
    except:
        pass

    f.write(json.dumps({"gallery": files}))
    
    print("[OK]: Finished syncing manifest to gallery.")
    
    removed = [file for file in old_manifest if file not in files]
    added = [file for file in files if file not in old_manifest]
    print("[CHANGES]:")
    for i in added: print(f"  + {i}")
    for i in removed: print(f"  - {i}")