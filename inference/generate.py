from mlx_lm import load, generate

model, tokenizer = load("mlx-community/Ministral-8B-Instruct-2410-4bit")

prompt = "Explain transformers simply"

response = generate(
    model,
    tokenizer,
    prompt=prompt,
    max_tokens=200,
    verbose=True
)

print(response)