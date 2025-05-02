
# 🔐 Simple Password Generator

A simple Python script to generate random passwords, customizable via command-line arguments.

## 📦 Features

- Generates a random password
- Customizable length
- Optional inclusion of:
  - Digits (`0-9`)
  - Symbols (`!@#...`)
  - Uppercase letters (`A-Z`)
- By default, the password includes only lowercase letters (`a-z`)

## 🚀 Usage

```bash
python password_generator.py [OPTIONS]
```

### ✅ Available Options

| Short Flag | Long Flag     | Description                                   |
|------------|---------------|-----------------------------------------------|
| `-l`       | `--length`    | Password length (default: 12)                 |
| `-d`       | `--digits`    | Include digits                                |
| `-s`       | `--symbols`   | Include symbols                               |
| `-u`       | `--uppercase` | Include uppercase letters                     |

### 🧪 Examples

- Generate a 16-character password with only lowercase letters:
  ```bash
  python password_generator.py -l 16
  ```

- Generate a 20-character password with digits and symbols:
  ```bash
  python password_generator.py -l 20 -d -s
  ```

- Generate an 8-character password with all options enabled:
  ```bash
  python password_generator.py -l 8 -d -s -u
  ```

## ⚠️ Notes

- If no character sets are selected (which shouldn't happen due to defaults), the script will print an error and exit.
- Password generation is fully random, so results may vary with each run.

## 🛠 Dependencies

No external dependencies. The script uses only Python's standard library.

## 📄 License

This project is open-source. Feel free to use it for educational or personal purposes.
