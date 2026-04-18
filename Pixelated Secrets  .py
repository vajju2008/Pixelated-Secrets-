from PIL import Image

FILE_NAME = "classified.png"

print("Initiating Forensic Analysis...\n")

try: 
    img = Image.open(FILE_NAME)
    
    print("--- METADATA EXTRACTION ---")
    # FIX: Matched the print variables to the loop variables
    for key, value in img.info.items():  
        print(f"Key: {key} | Value: {value}")
        
    print("\n--- LSB EXTRACTION ---")
    pixels = img.load()
    extracted_binary = ""
    
    # FIX: Changed arrSize to the correct Pillow attribute: size
    wd, ht = img.size
    
    # FIX: Swapped to standard x/y naming for easier reading
    for y in range(ht):
        for x in range(wd):
            # FIX: Renamed 'v' to 'g' for standard RGB naming
            r, g, b = pixels[x, y][:3] 
            extracted_binary += str(b % 2) 

    real_flag = "" 
    
    for s in range(0, len(extracted_binary), 8):
        byte_chunk = extracted_binary[s:s+8]
        
        if byte_chunk == "00000000":
            break
            
        if len(byte_chunk) == 8:
            real_flag += chr(int(byte_chunk, 2))
            
    print(f"REAL FLAG RECOVERED: {real_flag}")

except FileNotFoundError:
    print(f"Error: {FILE_NAME} not found.")