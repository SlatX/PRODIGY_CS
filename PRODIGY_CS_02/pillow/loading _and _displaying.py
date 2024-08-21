from PIL import Image
import numpy as np

def encrypt_image(image_path, key):
    
    try:
        # Load image
        with Image.open(image_path) as im:
            image_array = np.array(im)
        
        # Encrypt: Add the key value to each pixel and ensure it stays within [0, 255]
        encrypted_array = (image_array + key) % 255
        
        #encrypted_array = np.where(encrypted_array > 255, encrypted_array * 256, encrypted_array)
        encrypted_image = Image.fromarray(encrypted_array.astype('uint8'))
        return encrypted_image
    
    except Exception as e:
        print(f"An error occurred during encryption: {e}")

        return e

def decrypt_image(encrypted_image, key):
    try:
        # Decrypt: Subtract the key value from each pixel and ensure it stays within [0, 255]
        encrypted_array = np.array(encrypted_image)
        print(encrypted_array)
        decrypted_array = (encrypted_array - key) % 255
        print(decrypted_array)
        decrypted_image = Image.fromarray(decrypted_array.astype('uint8'))
        
        return decrypted_image
    
    except Exception as e:
        print(f"An error occurred during decryption: {e}")
        return None

if __name__ == "__main__":
    image_path = "./images/design.png"
    key = 50  # Example key

    # Encrypt the image
    try:
        encrypted_image = encrypt_image(image_path, key)
        print("this is the first step")
        if encrypted_image:
            encrypted_image.save("./saved-images/encrypted_ape.png")
            print("Image encrypted and saved as 'encrypted_ape.png'.")
    except Exception as e :
        print(f"this is the error{str(e)}")
        raise e
    # Decrypt the image
    if encrypted_image:  # Check if encryption was successful
        decrypted_image = decrypt_image(encrypted_image, key)
        if decrypted_image:
            decrypted_image.save("./saved-images/decrypted_ape.png")
            print("Image decrypted and saved as 'decrypted_ape.png'.") 
