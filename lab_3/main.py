import argparse
from file_utils import *
from asymmetric_crypto import generate_keys
from symmetric_crypto import encrypt_data, decrypt_data

def main():
    try:
        print("Starting application...")

        parser = argparse.ArgumentParser()
        parser.add_argument("mode", choices=["generation", "encryption", "decryption"], help="Operation mode: generation / encryption / decryption")
        parser.add_argument("-c", "--config", default="settings.json", help="Path to configuration JSON file")
        
        args = parser.parse_args()
        config = load_config(args.config)

        print(f"Running in {args.mode} mode.")

        match args.mode:
            case "generation":
                generate_keys(config)
            case "encryption":
                key = load_binary(config["symmetric_key"])
                text = load_text_file(config["initial_file"])
                encrypted_data = encrypt_data(key, text)
                save_binary(config["encrypted_file"], encrypted_data)
            case "decryption":
                key = load_binary(config["symmetric_key"])
                encrypted_data = load_binary(config["encrypted_file"])
                decrypted_text = decrypt_data(key, encrypted_data)
                save_text_file(config["decrypted_file"], decrypted_text)

        print("Operation completed successfully.")
    
    except Exception as e:
        raise RuntimeError(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
