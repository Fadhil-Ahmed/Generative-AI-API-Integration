# 🧠 AI API Integration: BlackForest + Perplexity

This project demonstrates two separate API integrations:

- 🎨 **BlackForest AI**: Generate cartoon-style illustrations from detailed prompts.
- 🧾 **Perplexity AI**: Use a LLaMA-based chat model to answer questions conversationally.

---

## 📂 Project Files

```plaintext
.
├── blackforest_ai.py      # Generates an image from a descriptive prompt using BlackForest API
├── perplexity_ai.py       # Sends a user query to Perplexity AI and prints the response
├── README.md              # This documentation file
```

---

## 🖼️ 1. BlackForest AI: Image Generation

**Description:**  
Generate a cartoon-style image featuring a rat and a duck in front of Saint Basil’s Cathedral in Moscow using the `flux-pro-1.1` model.

### 🔧 Dependencies

- Python 3.8+
- `requests` library

Install with:

```bash
pip install requests
```

### 🔑 Environment Variables

Set your API keys in your environment:

```bash
export BLACK_FOREST-API-KEY="your_blackforest_post_key"
export BFL_API_KEY="your_blackforest_get_key"
```

### ▶️ Run

```bash
python blackforest_ai.py
```

Once the image is ready, the final image URL will be printed to the terminal.

---

## 💬 2. Perplexity AI: Chat Completion

**Description:**  
Ask a question and receive a response from the `llama-3.1-sonar-large-128k-chat` model hosted on Perplexity’s API.

### 🔧 Dependencies

- Python 3.8+
- `openai` package (used for compatibility)

Install with:

```bash
pip install openai
```

### 🔑 Environment Variables

```bash
export PREPLEXITY_API_KEY="your_perplexity_api_key"
```

### ▶️ Run

```bash
python perplexity_ai.py
```

This will print the response to the hardcoded question:

> "Who is Kenneth Kousen?"

---

## 📌 Notes

- Both scripts rely on environment variables for security — do **not** hardcode keys into your files.
- BlackForest uses a polling mechanism to check when the image is ready. You can adjust the delay between checks (`sleep(0.5)`) as needed.
- The OpenAI-compatible client in `perplexity_ai.py` is initialized with a custom `base_url`.

---

## 🧪 Testing Example Output

### 🖼️ BlackForest AI Image Output

Sample Prompt:

> "An illustration of a cartoon-style rat and duck, both as friendly characters, set in a colorful, animated version of Moscow..."

**Sample Output:** *(a URL will be printed when ready)*

### 💬 Perplexity AI Output

Sample Query:

> "Who is Kenneth Kousen?"

**Sample Output:**

> Kenneth Kousen is a Java Champion, author of multiple technical books, and a well-known educator in the Java and Spring ecosystem.

---

## 🙌 Credits

- 🔗 [BlackForest API](https://bfl.ml)
- 🔗 [Perplexity AI](https://www.perplexity.ai)
