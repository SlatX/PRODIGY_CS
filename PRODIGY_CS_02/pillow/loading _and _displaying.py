from PIL import Image
import numpy as np
import random
import string

def generate_random_name():
    # Choose 5 random letters from the alphabet
    letters = string.ascii_lowercase  # You can use string.ascii_uppercase for uppercase letters
    random_name = ''.join(random.choice(letters) for _ in range(5))
    return random_name

def encrypt_image(image_path, key):
    
    try:
        # Load image
        with Image.open(image_path) as im:
            image_array = np.array(im)

        # Encrypt: Add the key value to each pixel and ensure it stays within [0, 255]
        encrypted_array = (image_array + key) 
        encrypted_array = np.where(encrypted_array > 255, encrypted_array - 255, encrypted_array)
        encrypted_image = Image.fromarray(encrypted_array.astype('uint8'))
        return encrypted_image
    
    except Exception as e:
        print(f"An error occurred during encryption: {e}")

        return e

def decrypt_image(encrypted_image, key):
    try:
        # Decrypt: Subtract the key value from each pixel and ensure it stays within [0, 255]
        encrypted_array = np.array(encrypted_image)
        decrypted_array = (encrypted_array - key) 
        decrypted_array = np.where(decrypted_array < 0, decrypted_array + 255, decrypted_array)
        decrypted_image = Image.fromarray(decrypted_array.astype('uint8'))
        
        return decrypted_image
    
    except Exception as e:
        print(f"An error occurred during decryption: {e}")
        return None

if __name__ == "__main__":
    def runscript (image_path, key):
        # Encrypt the image
        try:
            encrypted_image = encrypt_image(image_path, key)
            if encrypted_image:
                encrypted_image.save(f"./saved-images/en_{generate_random_name()}.png")
                
        except Exception as e :
            print(f"this is the error{str(e)}")
            raise e
        # Decrypt the image
        if encrypted_image:  # Check if encryption was successful
            decrypted_image = decrypt_image(encrypted_image, key)
            if decrypted_image:
                decrypted_image.save(f"./saved-images/de_{generate_random_name()}.png")
            

runscript("./images/ape.jpg", 60) 
runscript("./images/design.png", 70)

