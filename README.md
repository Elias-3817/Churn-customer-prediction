
# 📊 Customer Churn Prediction

Predict and prevent customer churn to drive retention strategies and protect revenue.

---

## 🚀 Project Overview

Churn is a silent revenue killer. In this end‑to‑end project, we:

- **Cleaned & Explored** a real‑world telecom dataset (EDA, hypothesis testing, null handling, )
- **Feature engineered** (Label encoding,Standardised numerical features)
- **Tuned & Compared** three classifiers: Logistic Regression, Random Forest, XGBoost
- **Optimized Threshold** for Recall ≥ 75% using cost‑sensitive analysis (FN = $70, FP = $10, TP benefit = $70)
- **Validated Performance** with 5‑fold CV and hold‑out test set
- **Simulated Business Impact**: projected \$58K–\$101K monthly in net savings

Our final model enables surgical retention campaigns by flagging the highest‑risk customers.

---

## 📂 Repository Structure

```
├── data/                                # Cleaned train/val/test CSVs
├── models/                              # Saved Random Forest model + threshold
├── notebooks/                           # Step-by-step analysis notebooks
│   ├── 01_problem_and_goals.ipynb
│   ├── 02_data_cleaning_and_eda.ipynb
│   ├── 03_feature_engineering.ipynb
│   ├── 04_model_comparison_and_tuning.ipynb
│   └── 05_evaluation_and_cost_analysis.ipynb
├── deployment_script.py                 # Load model & predict function (In progress)
├── Dashboard/                          # Final model dashboard 
├── requirements.txt                     # Python dependencies
|── README.md                            # Project overview (this file)


---

## 🛠️ Tech Stack

- **Language & Libraries**: Python, Pandas, NumPy, scikit-learn, XGBoost, Matplotlib, Seaborn
- **Feature Engineering**: Label Encoding, One‑Hot Encoding, Scaling (StandardScaler)
- **Modeling**: Logistic Regression, Random Forest, XGBoost
- **Evaluation**: Precision, Recall, F1‑Score, Confusion Matrix, Cross‑Validation
- **Business Analysis**: Cost‑Critical Threshold Tuning, ROI Simulation
- **Environment & Tools**: Jupyter Notebooks, Power BI (dashboard), Git & GitHub
---

## 📈 Final Model: Random Forest (Business‑Optimized)

| Metric                       | Value   |
|------------------------------|--------:|
| **Model**                    | Random Forest (n_estimators=100, max_depth=5)  |
| **Threshold**                | 0.503   |
| **Precision (Churn)**        | 0.564   |
| **Recall (Churn)**           | 0.751   |
| **F1‑Score (Churn)**         | 0.640   |
| **Accuracy**                 | 0.78    |
| **Projected Monthly Savings**| \$58,104 (conservative) / \$101,110 (full scale)|

> We selected this configuration to maximize net savings while maintaining strong churn detection.

---

## 💡 Key Business Insights

- **High‑risk segments**: Short tenure, electronic check payers, fiber internet users
- **Action levers**: Incentivize auto‑pay, premium support for fiber users, targeted offers for new customers
- **Impact**: Data‑driven interventions can **double** the savings compared to blanket churn reduction targets

---

## 🌐 Deployment Ready (still in progress)

- **Model** and **threshold** saved in `models/`:
  - `rf_churn_model.pkl`
  - `rf_threshold.pkl`
- **Deployment Script**: `deployment_script.py` provides a `predict_churn()` function for new customer data 
---

## 📊 Next Steps

- **Productionize** with Streamlit or FastAPI endpoint
- **Connect** to live customer database for automated scoring
- **Monitor & Retrain** quarterly to adapt to behavior shifts
- **Interpretability**: integrate SHAP values for stakeholder transparency

---

## 👤 Author

**Elias Gichuru**  
 Data Analyst | Machine Learning Engineer  
[GitHub Profile](https://github.com/Elias-3817)  
[LinkedIn Profile](https://www.linkedin.com/in/elias-gichuru-56a2a3250/)  
