import os
import json
from google import genai
import requests

# --- Configuration ---
INPUT_FILE = "input.txt"
OUTPUT_FILE = "content_output.json"
# The Vercel Hook URL will be injected from GitHub Secrets at runtime
VERCEL_HOOK_URL = os.environ.get("VERCEL_DEPLOY_HOOK")

# Get the API Key from the environment variables (set in GitHub Secrets)
# IMPORTANT: This needs the GEMINI_API_KEY environment variable to be set!
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

def generate_content_with_gemini():
    # 1. Read the raw input text
    with open(INPUT_FILE, "r") as f:
        raw_text = f.read()

    # 2. Define the prompt and desired output structure
    prompt = (
        f"You are a professional content editor for a README file. Take the following raw text and "
        f"rewrite it into a compelling, professional project summary. "
        f"The output MUST be a single, valid JSON object with two keys: 'title' (a catchy headline) and 'summary' (a detailed paragraph summary). "
        f"The original text is: \"{raw_text}\""
    )

    try:
        # 3. Call the Gemini API
        print("🤖 Calling Gemini API...")
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt
        )

        # 4. Extract and validate the JSON output
        # LLMs often wrap JSON in ```json...```, so we clean it up
        json_text = response.text.strip().lstrip('`json').rstrip('`').strip()
        processed_data = json.loads(json_text)

        # 5. Save the final JSON to the output file
        with open(OUTPUT_FILE, "w") as f:
            json.dump(processed_data, f, indent=2)

        print(f"✅ Success! Content saved to {OUTPUT_FILE}")
        return True

    except Exception as e:
        print(f"❌ An error occurred during AI processing: {e}")
        # Create a placeholder error file so the Vercel site doesn't crash
        with open(OUTPUT_FILE, "w") as f:
             json.dump({"title": "Error: AI Processing Failed", "summary": f"Could not process content. Error: {str(e)}"}, f, indent=2)
        return False

def trigger_vercel_deploy():
    """Triggers a rebuild of the Vercel frontend site using the Deploy Hook."""
    if not VERCEL_HOOK_URL:
        print("⚠️ VERCEL_DEPLOY_HOOK environment variable not set. Skipping deployment trigger.")
        return

    print("🚀 Triggering Vercel Deployment Hook...")
    # Sending a POST request to the Vercel Deploy Hook URL
    response = requests.post(VERCEL_HOOK_URL) 
    
    if response.status_code == 201 or response.status_code == 200:
        print("✅ Vercel deploy hook triggered successfully.")
    else:
        print(f"❌ Failed to trigger Vercel deploy hook. Status: {response.status_code}. Response: {response.text}")

if __name__ == "__main__":
    if generate_content_with_gemini():
        # The Vercel trigger is now done by the GitHub Action workflow itself, 
        # not the Python script, for cleaner separation and error handling.
        pass # trigger_vercel_deploy()
