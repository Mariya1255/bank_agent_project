Bank Agent Mini Project

Overview
Ye project ek simple Bank Agent banata hai jo users ke bank-related queries ko samajhta hai aur unka jawab deta hai. 
Is project mein input aur output guardrails implement kiye gaye hain taake sirf valid aur bank-related sawalat process hon. 
Isme kam az kam do agents hain — ek guardrail agent jo input validate karta hai aur ek main bank agent jo tools ke zariye balance check karta hai.

Features
  . Input Guardrails: User inputs ko validate karta hai, sirf bank-related sawalat allow karta hai.
  . Output Guardrails: Responses ko control karta hai taake sirf relevant jawab milein.
  . Multiple Agents:
     . Guardrail Agent: Input ko filter karta hai.
     . Bank Agent: User ke sawalon ka jawab deta hai.
 . Context: User ka context (name aur pin) securely handle karta hai.
 . Tools: Ek tool implement kiya gaya hai jo account balance provide karta hai.

 Folder Structure
 08_bank_agent_project/
│
├── agents/
│   ├── base_agent.py
│   ├── bank_main_agent.py
│   ├── guardrail_agent.py
│
├── tools/
│   └── balance_tool.py
│
├── models/
│   └── account_model.py
│
├── bank_agent.py
├── .env
├── requirements.txt
└── README.md

Setup Instructions
1. Python 3.8+ install karein.
2. Virtual environment banayein aur activate karein:
  python -m venv .venv
  .venv\Scripts\activate   # Windows
  source .venv/bin/activate  # macOS/Linux

3. Dependencies install karein:
   pip install -r requirements.txt

4. .env file banayein aur apna OpenAI API key add karein:   
    OPENAI_API_KEY=your_openai_api_key_here

5. Project run karein:
   python bank_agent.py
   
How It Works
. User bank_agent.py ko run karta hai.
. Input Bank Agent ko diya jata hai, jo pehle input guardrail se check hota hai.
. Agar input valid hai, to Bank Agent tool se balance check karta hai.
. Response console pe print hota hai.

Example Input/Output

 Input:
 What is the balance of account 30943883

 Output:
 The balance of account 30943883 is $1,000,000

 Notes
 . Yeh project demonstration ke liye hai, real banking systems mein security aur privacy measures zaroori hain.
 . Project ko apni zarurat ke mutabiq customize kiya ja sakta hai.
 
