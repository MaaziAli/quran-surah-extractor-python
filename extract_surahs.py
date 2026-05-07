import json

SELECTED_SURAHS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114]


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