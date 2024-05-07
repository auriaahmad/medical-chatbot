# End-to-end-Medical-Chatbot-using-Llama2

# How to run?
### STEPS:

Clone the repository

```bash
Project repo: https://github.com/
```

### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n mchatbot python=3.8 -y
```

```bash
conda activate mchatbot
```

### STEP 02- install the requirements
```bash
pip install -r requirements.
```


### Create a `.env` file in the root directory and add your Pinecone credentials as follows:

```ini
PINECONE_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```


### Download the quantize model from the link provided in model folder & keep the model in the model directory:

```ini
## Download the Llama 2 Model:

llama-2-7b-chat.ggmlv3.q4_0.bin


## From the following link:
https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/tree/main
```

```bash
# run the following command
python store_index.py
```

```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up localhost:
```


### Techstack Used:

- Python 
- LangChain
- Flask
- Meta Llama2
- Pinecone

### Packages Used:

- ctransformers == 0.2.5
- sentence-transformers == 2.2.2
- pinecone-client == 3.2.2
- langchain == 0.1.9 
- langchain_pinecone ==  0.1.0
- flask == 3.0.3
- pypdf == 4.2.0
- python-dotenv == 1.0.1


### Command to Check Version of Packages:

```bash
# run the following command
pip show <package-name>
```