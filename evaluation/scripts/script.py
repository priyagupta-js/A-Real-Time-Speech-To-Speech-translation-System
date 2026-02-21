import os
import shutil
import pandas as pd

def extract_language_subset(language_folder, output_folder, num_samples=150):
    tsv_path = os.path.join(language_folder, "test.tsv")
    clips_path = os.path.join(language_folder, "clips")

    df = pd.read_csv(tsv_path, sep="\t")

    os.makedirs(output_folder, exist_ok=True)

    for idx, row in df.head(num_samples).iterrows():
        audio_file = row["path"]
        sentence = row["sentence"]

        src_audio = os.path.join(clips_path, audio_file)
        dst_audio = os.path.join(output_folder, f"{idx}.mp3")

        if os.path.exists(src_audio):
            shutil.copy(src_audio, dst_audio)

            with open(dst_audio.replace(".mp3", ".txt"), "w", encoding="utf-8") as f:
                f.write(sentence)

    print(f"Done extracting {num_samples} samples for {output_folder}")

# -------- MODIFY THESE PATHS -------- #

project_root = r"C:\Users\DELL\Desktop\A-Real-Time-Speech-To-Speech-Translation-System"

english_folder = os.path.join(project_root, "dataset", "english_audio_files")
hindi_folder = os.path.join(project_root, "dataset", "hindi_audio_files")
tamil_folder = os.path.join(project_root, "dataset", "tamil_audio_files")

extract_language_subset(english_folder,
                        os.path.join(project_root, "evaluation", "speech", "english_clean"))

extract_language_subset(hindi_folder,
                        os.path.join(project_root, "evaluation", "speech", "hindi_clean"))

extract_language_subset(tamil_folder,
                        os.path.join(project_root, "evaluation", "speech", "tamil_clean"))
