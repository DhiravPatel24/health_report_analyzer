from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Now you can access the variables
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
MODEL = os.getenv("MODEL")
