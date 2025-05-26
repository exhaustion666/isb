import argparse
from file_utils import load_config
from asymmetric_crypto import generate_keys
from hybrid_crypto_core import encrypt_data, decrypt_data


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
                encrypt_data(config)
            case "decryption":
                decrypt_data(config)

        print("Operation completed successfully.")
    
    except Exception as e:
        raise RuntimeError(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
