from src.main import read_text_files, analyze_sentiment, determine_outcome, get_openai_api_key, save_test_data

# Folder containing text files (Update with your folder path)
folder_path = "transcripts"

get_openai_api_key()

# Read all text files and get paragraphs as records
transcript_df = read_text_files(folder_path)

# Apply the sentiment analysis function to each customer conversation
transcript_df['sentiment'] = transcript_df['customer_text'].apply(analyze_sentiment)

# Apply the outcome analysis function to each customer conversation
transcript_df['outcome'] = transcript_df['customer_text'].apply(determine_outcome)

# Save the DataFrame to a CSV file
transcript_df.to_csv('customer_conversations_analysis.csv', index=False)

#Save the Test Dataframe to a CSV file
save_test_data(transcript_df)
