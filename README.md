\# 🚁 Drone Intelligence System – India



!\[CI](https://github.com/karthikreddy0-hash/drone-intelligence-system-india/actions/workflows/ci.yml/badge.svg)



An AI-powered backend system designed to assist with drone analytics, regulatory compliance (India), intelligent drone selection, and business ROI estimation.



This system integrates Retrieval-Augmented Generation (RAG), API-based calculations, and modular backend services.





\# 📌 Overview



The Drone Intelligence System provides:



\- 📜 Indian Drone Regulation compliance checks

\- 🤖 AI-powered drone recommendation system

\- ⏱ Flight time estimation calculator

\- 💰 Return on Investment (ROI) calculator

\- 📚 RAG-based document knowledge retrieval

\- 🧪 Automated testing with pytest

\- ⚙️ Continuous Integration using GitHub Actions







\# 🏗️ Architecture



The system follows a modular backend architecture:



User Request  

&nbsp;  ↓  

FastAPI Backend (`api/`)  

&nbsp;  ↓  

Business Logic Modules  

&nbsp;  ├── RAG Engine (`rag/`)  

&nbsp;  ├── MCP Tools (`mcp\_server/`)  

&nbsp;  └── Calculation Services  

&nbsp;  ↓  

Response Returned as JSON  







\# 📂 Project Structure



drone\_intelligence\_system\_india/

│

├── api/                     # FastAPI backend endpoints  

├── rag/                     # Retrieval-Augmented Generation system  

├── mcp\_server/              # MCP tools for drone analysis  

├── tests/                   # Unit tests using pytest  

├── data/                    # Raw \& processed \& synthetic data  

├── .github/workflows/       # CI pipeline configuration  

├── pytest.ini               # Pytest configuration  #unit test

├── requirements.txt         # Python dependencies  

└── README.md  







\# 🚀 Installation Guide



\## 1️⃣ Clone the Repository



git clone https://github.com/karthikreddy0-hash/drone-intelligence-system-india.git  

cd drone-intelligence-system-india  







\## 2️⃣ Create Virtual Environment



Windows:

python -m venv venv  

venv\\Scripts\\activate  



Mac/Linux:

python3 -m venv venv  

source venv/bin/activate  







\## 3️⃣ Install Dependencies



pip install -r requirements.txt  







\# ▶ Running the Application



If using FastAPI:



uvicorn api.main:app --reload  



Server will start at:



http://127.0.0.1:8000  



Swagger Documentation:



http://127.0.0.1:8000/docs  







\# 🧪 Running Tests



pytest  



Expected output:



5 passed  



All tests are automatically executed in GitHub Actions on every push and pull request.







\# 🔐 Environment Variables



Create a `.env` file (DO NOT COMMIT):



GOOGLE\_API\_KEY=your\_api\_key\_here  



The `.env` file is ignored via `.gitignore`.







\# ⚙️ Continuous Integration



CI pipeline runs automatically on:



\- Push to main branch  

\- Pull requests  



It performs:



\- Dependency installation  

\- Pytest execution  

\- Workflow validation  



Status badge is shown at top of this README.







\# 📊 Key Functional Modules



\## 1️⃣ Drone Selection Assistant

\- Accepts use case  

\- Accepts budget constraints  

\- Returns recommended models  



\## 2️⃣ Flight Time Calculator

Calculates estimated flight duration based on:

\- Battery capacity  

\- Payload weight  

\- Power consumption  



\## 3️⃣ ROI Calculator

Estimates:

\- Operational savings  

\- Investment recovery time  

\- Profit projections  



\## 4️⃣ Compliance Checker (India)

Validates drone category and operation rules under DGCA regulations.



---



\# 🛡 Security Measures



\- API keys stored via environment variables  

\- No hardcoded secrets  

\- GitHub secret scanning enabled  

\- Clean Git history  







\# 🧱 Technologies Used



\- Python 3.13  

\- FastAPI  

\- Pytest  

\- LangChain  

\- HuggingFace Embeddings  

\- GitHub Actions  

\- Docker (optional support)  







\# 📈 Future Improvements



\- Docker container optimization  

\- Deployment on cloud (Render / AWS)  

\- Streamlit frontend dashboard  

\- Database integration (PostgreSQL)  

\- Authentication layer  

\- Production logging \& monitoring  







\# 👨‍💻 Author



Karthik Reddy  

AI \& Backend Development  





