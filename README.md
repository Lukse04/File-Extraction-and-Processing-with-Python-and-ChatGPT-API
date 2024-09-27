# File Extraction and Processing with Python and ChatGPT API

This project is designed to extract files from a ZIP archive, process them, and send their content to the ChatGPT API using Python.

## Requirements

1. Python 3 must be installed on the VPS server (tested with Ubuntu 22.04).
2. OpenAI API key (can be obtained [here](https://beta.openai.com/signup/)).
3. The ZIP file should be placed in the same directory as `script.py`.

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
Upload the ZIP file you want to process and make sure the file structure looks like this:

```
/project-directory
    ├── script.py         # Main script
    ├── file.zip          # ZIP file to be processed by the script
```

### 4. Install dependencies

Install the required Python packages:

```bash
pip install openai zipfile tqdm
```

### 5. Add your ChatGPT API key

Open the `script.py` file and locate the following line:

```python
openai.api_key = 'YOUR_API_KEY'
```

Replace `'YOUR_API_KEY'` with your actual OpenAI API key, which you can get [here](https://beta.openai.com/signup/).

### 6. Running the script

Navigate to the directory where the script is located:

```bash
cd /project-directory
```

Run `script.py`:

```bash
python3 script.py
```

The script will extract the ZIP file, process all files, and send their content to the ChatGPT API in batches, ensuring that no message exceeds 4000 characters.

## How it works

1. The script extracts the ZIP file.
2. It reads the content of each file.
3. The file content is collected into a message until the 4000-character limit is reached.
4. If the limit is reached, the message is sent to the ChatGPT API, and a new one is started.
5. This process repeats until all files are processed.

## Contact

If you have any questions or need assistance, feel free to contact me at: :D .
