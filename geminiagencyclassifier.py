# Install web scraping, Google Sheets, and email libraries
# !pip install google-generativeai
# !pip install beautifulsoup4
# !pip install requests
# !pip install pandas
# !pip install gspread
# !pip install smtplib


import os

# Set your Gemini API key


import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        text = soup.get_text()
        text=text.replace("\n"," ")
        text=text.replace("|"," ")
        text=text.replace(",","")
        text=text.replace("   "," ")

        return text
    else:
        return None



import os
import google.generativeai as genai
from dotenv import load_dotenv

def classify_agency(content):
    """Classify the agency website using a Gemini fine-tuned model."""

    api_key=open('GEMINI_API_KEY').read()
    if not api_key:
        raise ValueError("GEMINI_API_KEY environment variable is not set.")

    genai.configure(api_key=api_key)  

    model_name = "gemini-1.5-flash"  

    formatted_prompt = f"""
    You are an AI designed to classify websites into agencies or non-agencies. 
    The website content is given below:
    ---
    {content}
    ---
    Based on the content:
    - Decide if it is an agency or not.
    - Provide the result in the following format:
    
    **Response Format:**
    APPROVE | Confidence: X/10 | Reason: [Explain why it was approved or rejected].
    
    **Example Responses:**
    - "APPROVE | Confidence: 9/10 | Reason: The website offers digital marketing and web development services."
    - "REJECT | Confidence: 8/10 | Reason: The website is an e-commerce store, not an agency."
    """

    model = genai.GenerativeModel(model_name)

    response = model.generate_content(formatted_prompt)

    return response.text 




import pandas as pd

results = []

def save_to_csv(url, decision, confidence, reason):
    """Save the result to a CSV file."""
    results.append({
        "Website": url,
        "Decision": decision,
        "Confidence Score": confidence,
        "Reason": reason
    })
    
    df = pd.DataFrame(results)
    df.to_csv("agency_results.csv", index=False)


import smtplib
from email.message import EmailMessage

def send_email(recipient, subject, body):
    """Send email notification."""
    # EMAIL = os.getenv("EMAIL_SENDER")
    # PASSWORD = os.getenv("EMAIL_PASSWORD")
    EMAIL=open('EMAIL_SENDER').read()
    PASSWORD=open('EMAIL_PASSWORD').read()

    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = EMAIL
    msg["To"] = recipient
    msg.set_content(body)


    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(EMAIL, PASSWORD)
        server.send_message(msg)
    print("mail sent")

def main(url,mail):
    print(f"Processing {url}...")
    
    content = scrape_website(url)
    
    if "Error" in content:
        print(f"Failed to fetch {url}")
        return
    # print(content)
    response = classify_agency(content)
    print('respomse',response)
    # Extract decision, confidence, and reason
    decision, confidence, reason = response.split("|")
    print("de", decision)
    decision = decision.strip()
    confidence = confidence.strip()
    reason = reason.strip()

    # Save results
    save_to_csv(url, decision, confidence, reason)

    # Send email
    t="APPROVE"
    # if t in decision:
    #     send_email(mail, "Welcome to CookieYes!", "You have been approved!")
    # else:
    #     send_email(mail, "Application Declined", "Unfortunately, you did not meet the requirements.")\

    if t in decision:
        subject = "Agency Approval Notification - CookieYes"
        body = f"""
        Hello,

        We are pleased to inform you that your website has been successfully classified as an agency!

        📝 **Reason:** {reason}

        If you have any questions or require further assistance, feel free to reply to this email.

        Best regards,  
        CookieYes Team  
        [Your Website or Contact Info]
        """
        send_email(mail, subject, body)
    else:
        subject = "Agency Classification Result - CookieYes"
        body = f"""
        Hello,

        After reviewing your website, we regret to inform you that it does not meet the criteria for agency classification.

        📝 **Reason:** {reason}

        If you believe this decision was made in error, feel free to contact us for a review.

        Best regards,  
        CookieYes Team  
        [Your Website or Contact Info]
        """
        send_email(mail, subject, body)


# Example URLs
urls = [
    "https://www.webfx.com/",
    "https://www.ogilvy.com/",
    "https://techcrunch.com/"
]
emal=[
    "21br14301@rit.ac.in",
    "divyeshashok004@gmail.com",
    "sreejithjnv1962@gmail.com"
]

for url in range(len(urls)):
    main(urls[url],emal[url])
