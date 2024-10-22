import os
import pandas as pd
import openai

def get_openai_api_key():
    api_key = os.environ.get('OPENAI_API_KEY')
    openai.api_key =  api_key      

# Function to read all text files
def read_text_files(folder_path):
    transcript_df = pd.DataFrame(columns=['customer_text','agent_text', 'transcript_file'])  
    agent_text = []    
    customer_text = []
    transcript_file = []

    # Loop through all files in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):  # Check if the file is a text file
            file_path = os.path.join(folder_path, filename)
            
            with open(file_path, 'r', encoding='utf-8') as file:
                transcripts = file.readlines()  # Read the entire file content
                customer_conversation = ""
                agent_conversation = ""

                for line in transcripts:
                    if line.startswith('Member:'):
                        # Extract the part after 'Member: ' for clean text
                        if customer_conversation == "":
                            customer_conversation += line.replace('Member:', '').strip()
                        else:
                            customer_conversation += ' ' + line.replace('Member:', '').strip()
                    else:
                        index = line.find(':')
                        if agent_conversation == "" and index >= 0 :
                            agent_conversation = line[index+1:].strip()
                        else:
                            agent_conversation += ' ' + line[index+1:].strip()                          
                
                customer_text.append(customer_conversation)
                agent_text.append(agent_conversation)
                transcript_file.append(filename)
    transcript_data = {
        'customer_text':customer_text,
        'agent_text':agent_text,
        'transcript_file': transcript_file
    }
    transcript_df = pd.DataFrame(data=transcript_data)

    return transcript_df

def analyze_sentiment(text):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", 
            "content": "You are a helpful assistant and text analyser that classifies customer sentiments."},
            {"role": "user", 
            "content": f"Analyze the sentiment of the following text, don't provide any justification, and respond strictly with only 'Positive', 'Negative', or 'Neutral':\n\n{text}"}
        ]
    )
    return response['choices'][0]['message']['content'].strip()

def determine_outcome(text):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", 
            "content": "You are a helpful assistant and text analyser that determines the outcome of customer calls."},
            {"role": "user", 
            "content": f"Based on the following text, determine if the issue is resolved or if a follow-up action is needed. Dont provide justification, Respond with 'Issue Resolved' or 'Follow-up Needed':\n\n{text}"}
        ]
    )
    return response['choices'][0]['message']['content'].strip()


