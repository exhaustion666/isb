import argparse
from file_utils import load_config
from key_manager import generate_keys
from hybrid_crypto_core import encrypt_data, decrypt_data


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", choices=["generation", "encryption", "decryption"],
                        help="Режим работы: generation / encryption / decryption")
    parser.add_argument("-c", "--config", default="settings.json", help="Путь к конфигурационному JSON файлу")

    args = parser.parse_args()
    config = load_config(args.config)

    match args.mode:
        case "generation":
            generate_keys(config)
        case "encryption":
            encrypt_data(config)
        case "decryption":
            decrypt_data(config)


if __name__ == "__main__":
    main()
