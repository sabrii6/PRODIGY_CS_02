from PIL import Image
import numpy as np

def encrypt_image(image_path, output_path, key):
    try:
        # Load the image
        image = Image.open(image_path)
        pixels = np.array(image)

        # Encrypt the image by applying a basic mathematical operation to each pixel
        encrypted_pixels = (pixels + key) % 256

        # Create and save the encrypted image
        encrypted_image = Image.fromarray(encrypted_pixels.astype('uint8'))
        encrypted_image.save(output_path)
        
        print(f"Encryption completed. Encrypted image saved as '{output_path}'")

    except Exception as e:
        print(f"Error occurred during encryption: {str(e)}")

def decrypt_image(encrypted_image_path, output_path, key):
    try:
        # Load the encrypted image
        encrypted_image = Image.open(encrypted_image_path)
        encrypted_pixels = np.array(encrypted_image)

        # Decrypt the image by reversing the encryption operation
        decrypted_pixels = (encrypted_pixels - key) % 256

        # Create and save the decrypted image
        decrypted_image = Image.fromarray(decrypted_pixels.astype('uint8'))
        decrypted_image.save(output_path)
        
        print(f"Decryption completed. Decrypted image saved as '{output_path}'")

    except Exception as e:
        print(f"Error occurred during decryption: {str(e)}")

# Example usage
def main():
    try:
        # Ask user for image file path
        input_image_path = input("Enter the input image file path: ").strip()

        # Ask user for encryption key
        key = int(input("Enter the encryption key (an integer): "))

        # Define output file paths
        encrypted_image_path = 'encrypted_image.png'
        decrypted_image_path = 'decrypted_image.png'

        # Encrypt the image
        encrypt_image(input_image_path, encrypted_image_path, key)

        # Decrypt the image
        decrypt_image(encrypted_image_path, decrypted_image_path, key)

    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
