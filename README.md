# 🚀 Agency Website Classifier  

This project classifies websites into **agencies** or **non-agencies** using **Google Gemini AI**. It scrapes website content, analyzes it with Gemini, and sends email notifications based on the classification.

## 🌟 Features  
- ✅ **Scrapes website content** using **BeautifulSoup**  
- 🤖 **Classifies websites** using **Google Gemini AI**  
- 📊 **Saves results** to a CSV file  
- 📧 **Sends email notifications** based on classification  

---

## 📥 Installation  

### 1️⃣ Clone the repository  
```sh
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

### 2️⃣ Install dependencies
```sh
pip install -r requirements.txt
```
### 3️⃣ Set up environment variables
Create a .env file and add the following:

```sh
GEMINI_API_KEY=your-gemini-api-key
EMAIL_SENDER=your-email@gmail.com
EMAIL_PASSWORD=your-app-password
```

Alternatively, create separate files for each key:

```sh
echo "your-gemini-api-key" > GEMINI_API_KEY
echo "your-email@gmail.com" > EMAIL_SENDER
echo "your-app-password" > EMAIL_PASSWORD
```

### 🛠️ Usage

Run the script with:

```sh
python main.py
```

✅ What It Does:
1️⃣ Scrapes the websites listed in the urls array.
2️⃣ Classifies them as agencies or non-agencies.
3️⃣ Saves results in agency_results.csv.
4️⃣ Sends email notifications to the respective recipients.

### 📊 Example Classification Results

Website	Decision	Confidence	Reason
webfx.com	APPROVE	9/10	Offers marketing and development services
ogilvy.com	APPROVE	9/10	A well-known marketing agency
techcrunch.com	REJECT	8/10	A news website, not an agency

### 🔧 Troubleshooting

⚠️ Emails Going to Spam?
Use a professional SMTP service like SendGrid or Mailgun.

Update email content to avoid spam trigger words.

### 🔗 Contributors
Divyesh Ashok
