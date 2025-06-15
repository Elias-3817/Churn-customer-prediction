# Customer Churn Prediction
Predicting customer churn to drive retention strategy and reduce business losses.



## 🚀 Project Overview
Customer churn is a silent killer of revenue. In this project, we:


-Analyzed a real-world telco dataset

-Engineered meaningful features

-Built and tuned classification models

-Optimized for recall using cost-sensitive analysis

-Saved the best model for deployment

-Our final model enables targeted retention campaigns, minimizing churn at scale.



##📂 Repository Structure
graphql
Copy
Edit
├── data/                          # Cleaned CSV files (train/val/test sets)
├── models/                        # Saved model + threshold pickles
├── notebooks/
│   ├── 01_problem_statement_and_goals.ipynb
│   ├── 02_data_understanding_and_cleaning.ipynb
│   ├── 03_eda_hypothesis_driven.ipynb
│   ├── 04_feature_engineering_and_preprocessing.ipynb
│   └── 05_model_building_evaluation_cost_analysis.ipynb
├── .gitignore
└── README.md                      # This file


##🛠️ Tech Stack
Python (Pandas, NumPy, Scikit-learn, XGBoost, Matplotlib, Seaborn)
Jupyter Notebooks
Git + GitHub



###📊 Final Model: Tuned XGBoost
max_depth = 3, n_estimators = 100, scale_pos_weight = 3

Threshold = 0.65

Precision: 0.55

Recall: 0.61

F1 Score: 0.58

Accuracy: 76%

Why XGBoost? Best tradeoff between recall (catching churners) and limiting false positives.



##💸 Cost-Sensitive Strategy
We estimated financial impact using:

Churn cost: $70/month lost revenue

Outreach cost: $10/retention attempt

Target churn reduction: from 25% → 20%

We selected a threshold that maximizes business savings, not just metrics.



##✅ Highlights
🧼 Cleaned and validated all key variables

🔍 Hypothesis-driven EDA

🔁 Cross-validation with recall scoring

🧠 Feature importance analysis

🧪 Multiple models tested (Logistic, RF, XGB)

💾 Model + threshold saved to .pkl for deployment

📦 Deployment-Ready
Both the trained model and its threshold are saved in models/:

xgb_churn_model.pkl

churn_threshold.pkl



###📈 Next Steps (Optional)
Add a Streamlit dashboard or FastAPI endpoint

Connect to a customer DB for live scoring

Automate monthly churn reports

Explore SHAP values for model interpretability



👤 Author
Elias
Aspiring Data Analyst / Machine Learning Engineer
GitHub | LinkedIn




