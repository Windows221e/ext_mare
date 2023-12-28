import os
import json
from PIL import Image


#returns the extension name from input
def v_en(extension_name):
    return extension_name.strip()



#path handler
def v_ip(icon_path):
    icon_path = icon_path.strip()
    if os.path.isfile(icon_path):
        return icon_path
    else:
        raise ValueError("Invalid icon path. Provide a valid file path.")


#manifest json file structure
def c_m_f(ext_folder, ext_name, ic_format):
    manifest_content = {
        "manifest_version": 2,
        "name": ext_name,
        "version": "1.0",
        "description": "Your extension description here",
        "browser_action": {
            "default_icon": f"icon.{ic_format}",
            "default_popup": "popup.html"
        },
    }
    manifest_path = os.path.join(ext_folder, "manifest.json")
    with open(manifest_path, "w") as manifest_file:
        json.dump(manifest_content, manifest_file, indent=2)


#create the popup html file
def c_p_f(ext_folder):
    popup_content = "<html><body><h1>My First Extension!</h1></body></html>"
    popup_path = os.path.join(ext_folder, "popup.html")
    with open(popup_path, "w") as popup_file:
        popup_file.write(popup_content)


#resize
def r_a_s_i(icon_path, ext_folder, ic_format):
    icon = Image.open(icon_path)
    icon_resized = icon.resize((48, 48), Image.ANTIALIAS)
    icon_resized.save(os.path.join(ext_folder, f"icon.{ic_format}"))


#create path
def c_e_f(ext_name, icon_path, ic_format):
    try:
        ext_name = v_en(ext_name)
        icon_path = v_ip(icon_path)
        ext_folder = os.path.join(os.getcwd(), ext_name)
        os.makedirs(ext_folder)
        c_m_f(ext_folder, ext_name, ic_format)
        c_p_f(ext_folder)
        r_a_s_i(icon_path, ext_folder, ic_format)

        print(f"Extension '{ext_name}' created successfully.")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__": #inputs
    ext_name = input("Enter the extension name: ")
    icon_path = input("Enter the path to the icon image (png, jpg, jpeg, webp): ")
    ic_format = icon_path.split(".")[-1].lower()

    if ic_format not in ["png", "jpg", "jpeg", "webp"]: #error handler
        print("Invalid icon format. Supported formats: png, jpg, jpeg, webp.")
    else:
        c_e_f(ext_name, icon_path, ic_format)
        
        

