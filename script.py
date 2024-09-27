import zipfile
import os
import openai

# OpenAI API key
openai.api_key = 'YOUR_API_KEY'

# Maximum number of characters per message
MAX_CHAR_LIMIT = 4000  # Set the character limit to reserve space for structure

def send_message_to_chatgpt(content):
    # Send a request to the ChatGPT API
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=content,
        max_tokens=100  # Adjust based on your needs
    )
    print(f"ChatGPT response:\n{response.choices[0].text.strip()}\n")
    print("="*40)  # Separator for messages


# Extract the ZIP file
with zipfile.ZipFile('file.zip', 'r') as zip_ref:
    zip_ref.extractall('temp')

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
