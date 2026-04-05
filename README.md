📖 Quran Surah Extractor (Python)

This project provides a Python script to extract selected Surahs from the Tanzil Quran text file and convert them into a structured JSON format.

🚀 Features

- Extract specific Surahs (customizable)
- Supports Uthmani script (with full marks)
- Generates clean JSON for mobile apps (Flutter ready)
- Includes optional clean text (for simplified reading mode)
- Lightweight and fast

📂 Input Format

The script expects a text file ("quran_full.txt") in this format:

surah_number|ayah_number|text

Example:

1|1|بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ

⚙️ How to Use

1. Download Quran text from Tanzil.net (Uthmani format)
2. Rename file to:

quran_full.txt

3. Run the script:

python extract_surahs.py

4. Output will be generated:

output/selected_surahs.json

🧠 Customize Surahs

Edit this line in script:

SELECTED_SURAHS = [36, 55, 56, 67]

📱 Use Case

- Flutter Islamic apps
- Quran reading apps
- Offline Surah access
- Azkar + Surah integration

⚠️ License & Attribution

Quran text is sourced from:
👉 https://tanzil.net

Please ensure proper attribution when using in applications.

🤝 Contributions

Feel free to improve or extend this script!
