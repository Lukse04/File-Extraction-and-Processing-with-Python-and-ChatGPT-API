# File Extraction, Processing, and ChatGPT Integration with GitHub ZIP Download

This project downloads a ZIP file from GitHub, extracts its contents, and sends them to the ChatGPT API using Python.

## Requirements

1. Python 3 must be installed on your VPS server (tested with Ubuntu 22.04).
2. OpenAI API key (can be obtained [here](https://beta.openai.com/signup/)).
3. The ZIP file should be hosted on GitHub, and its download link should be provided.

## Installation Steps

### 1. Update the server and install Python
Run the following commands to update the system and install Python:

```bash
sudo apt update
sudo apt install python3 python3-pip
```

### 2. Create a virtual environment (optional but recommended)
Use a virtual environment to isolate dependencies:

```bash
sudo apt install python3-venv
python3 -m venv myenv
source myenv/bin/activate
```

### 3. Project file structure
Make sure your file structure looks like this:

```
/project-directory
    ├── script.py         # Main script
```

### 4. Install dependencies

Install the required Python packages:

```bash
pip install openai requests zipfile tqdm
```

### 5. Add your ChatGPT API key

Open the `script.py` file and locate the following line:

```python
openai.api_key = 'YOUR_API_KEY'
```

Replace `'YOUR_API_KEY'` with your actual OpenAI API key, which you can get [here](https://beta.openai.com/signup/).

### 6. Add your GitHub ZIP file URL

Find the line in `script.py` where the ZIP URL is defined:

```python
zip_url = 'https://github.com/your-repo/your-archive.zip'
```

Replace the `'your-repo/your-archive.zip'` part with the actual URL of the ZIP file you want to download from GitHub.

### 7. Running the script

Navigate to the directory where the script is located:

```bash
cd /project-directory
```

Run `script.py`:

```bash
python3 script.py
```

The script will download the ZIP file from GitHub, extract it, process all files, and send their content to the ChatGPT API in batches, ensuring that no message exceeds 4000 characters.

## How it works

1. The script downloads the ZIP file from GitHub.
2. It extracts the ZIP file.
3. It reads the content of each file.
4. The file content is collected into a message until the 4000-character limit is reached.
5. If the limit is reached, the message is sent to the ChatGPT API, and a new one is started.
6. This process repeats until all files are processed.

## Contact

If you have any questions or need assistance, feel free to contact me at: your@email.com.
