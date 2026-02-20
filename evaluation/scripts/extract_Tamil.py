import os
from datasets import load_dataset
import soundfile as sf
from tqdm import tqdm

# Output folder
output_dir = "../speech/tamil_clean"
os.makedirs(output_dir, exist_ok=True)

# Load Tamil dataset in streaming mode
dataset = load_dataset(
    "mozilla-foundation/common_voice_17_0",
    "ta",
    split="validated",
    streaming=True
)

max_samples = 150
count = 0

for sample in tqdm(dataset):
    if count >= max_samples:
        break

    audio = sample["audio"]
    text = sample["sentence"]

    file_path = os.path.join(output_dir, f"tamil_{count}.wav")

    # Save audio
    sf.write(file_path, audio["array"], audio["sampling_rate"])

    # Save transcript
    with open(file_path.replace(".wav", ".txt"), "w", encoding="utf-8") as f:
        f.write(text)

    count += 1

print("Done extracting Tamil samples!")
