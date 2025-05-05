# 🧠 Client Segmentation & Profitability Analysis (ML + Power BI)

This project focuses on customer segmentation and profitability analysis using RFM (Recency, Frequency, Monetary) modeling, K-means clustering, and churn prediction. It combines machine learning with business intelligence to help companies understand customer behavior and make data-driven decisions.

## 📌 Key Features

- 🔍 RFM Analysis to identify customer value and loyalty  
- 📊 K-Means Clustering for segmenting customers based on behavior  
- 🧠 Churn Prediction Model using Random Forest Classifier  
- 📈 Interactive Power BI Dashboard for insights & decision-making  
- 📁 Organized Python workflow with output files and visualizations  

## 🚀 Tech Stack

- **Languages:** Python (Pandas, Scikit-learn, Matplotlib)  
- **Tools:** Power BI, Jupyter/VS Code  
- **ML Techniques:** RFM Scoring, K-Means Clustering, Random Forest  

## 📂 Folder Structure

```
client_segmentation_project/
│
├── data/                # Input CSV files (Fact.csv, Customer.csv, Date.csv)
├── output/              # RFM scores and churn prediction results
├── visuals/             # Elbow plot, charts
├── dashboard/           # Power BI .pbix file
├── rfm_analysis.py      # Main Python script
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

## 🛠️ How to Run Locally

```bash
# Clone the repository
git clone https://github.com/kaustubha-07/Client-Segmentation-Profitability-Analysis.git
cd Client-Segmentation-Profitability-Analysis

# Set up virtual environment
python -m venv venv
venv\Scripts\activate  # For Windows
# source venv/bin/activate  # For macOS/Linux

# Install dependencies
pip install -r requirements.txt

# Run the main analysis script
python rfm_analysis.py
```

## 📊 Power BI Dashboard

The dashboard visualizes:
- RFM clusters
- Customer segment distribution
- Churn probabilities
- Business recommendations

File location: `/dashboard/client_segmentation.pbix`

## 📈 Results

- Segmented customers into behavior-based clusters
- Churn prediction model trained with accuracy score
- Visual insights for strategic marketing and retention

## 👤 Author

**Kaustubh**  
[LinkedIn](https://www.linkedin.com/in/kaustubha-07) • [GitHub](https://github.com/kaustubha-07)

---

⭐ Feel free to fork this repo, contribute ideas, or use it for your own data-driven business analysis!
