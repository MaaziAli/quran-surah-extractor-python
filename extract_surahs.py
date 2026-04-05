import json

SELECTED_SURAHS = [36, 55, 56, 67, 32, 112, 113, 114, 108, 103, 18, 62, 76]


INPUT_FILE = "quran_full.txt"
OUTPUT_FILE = "output/selected_surahs.json"

surahs = {}

with open(INPUT_FILE, "r", encoding="utf-8") as f:
    for line in f:
        parts = line.strip().split("|")

        if len(parts) != 3:
            continue

        surah_num = int(parts[0])
        ayah_num = int(parts[1])
        text = parts[2]

        if surah_num not in SELECTED_SURAHS:
            continue

        if surah_num not in surahs:
            surahs[surah_num] = {
                "surah": surah_num,
                "ayahs": []
            }

        surahs[surah_num]["ayahs"].append({
            "number": ayah_num,
            "text": text,
            "clean_text": text
        })

result = list(surahs.values())

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(result, f, ensure_ascii=False, indent=2)

print("✅ Done! JSON created successfully.")