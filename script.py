import zipfile
import os
import requests
import openai

# OpenAI API key
openai.api_key = 'YOUR_API_KEY'

# URL of the ZIP file on GitHub
zip_url = 'https://github.com/your-repo/your-archive.zip'

# Maximum number of characters per message
MAX_CHAR_LIMIT = 4000  # Set the character limit to reserve space for structure

def download_zip(url, save_path):
    """Download ZIP file from a URL and save it locally."""
    print("Downloading ZIP file...")
    response = requests.get(url)
    with open(save_path, 'wb') as file:
        file.write(response.content)
    print("Download complete.")

def send_message_to_chatgpt(content):
    """Send content to ChatGPT API."""
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=content,
        max_tokens=100  # Adjust based on your needs
    )
    print(f"ChatGPT response:\n{response.choices[0].text.strip()}\n")
    print("="*40)  # Separator for messages

# Step 1: Download the ZIP file from GitHub
zip_file_path = 'downloaded_archive.zip'
download_zip(zip_url, zip_file_path)

# Step 2: Extract the ZIP file
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall('temp')

# Step 3: Read and process files
collected_message = ""  # Collect content for a single message
for foldername, subfolders, filenames in os.walk('temp'):
    for filename in filenames:
        file_path = os.path.join(foldername, filename)
        
        with open(file_path, 'r') as file:
            content = file.read()
            file_info = f"File Name: {filename}\nContent:\n{content}\n\n"

            # If adding this file's content exceeds the limit, send the current message and start a new one
            if len(collected_message) + len(file_info) > MAX_CHAR_LIMIT:
                send_message_to_chatgpt(collected_message)  # Send the message to ChatGPT
                collected_message = ""  # Start a new message
            
            # Add file info to the current message
            collected_message += file_info

# Send the last message if there is any remaining content
if collected_message:
    send_message_to_chatgpt(collected_message)
