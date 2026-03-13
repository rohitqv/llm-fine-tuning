import subprocess
import sys

command = [
    sys.executable, "-m", "mlx_lm", "lora",
    "--model", "mlx-community/Ministral-8B-Instruct-2410-4bit",
    "--data", "datasets/processed",
    "--train",
    "--batch-size", "2",
    "--iters", "600",
    "--learning-rate", "1e-4",
    "--adapter-path", "models/finetuned/my-adapter"
]

print("Running command:", " ".join(command))
subprocess.run(command)