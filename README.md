### Predicting diabetes


This dataset originally comes from the National Institute of Diabetes and Digestive and Kidney Diseases. The goal is to predict, based on diagnostic measures, whether or not a patient has diabetes.

#### Step 1: Loaded the dataset

Loaded the processed dataset from the previous project (split into training and test samples and analyzed with EDA).

#### Step 2: Built a boosting

One way to optimize and improve the results is to generate a boosting so that there is the necessary variety to enrich the prediction. I trained it and analyzed its results. I modified the hyperparameters that define the model with different values and analyzed their impact on the final accuracy and plot the conclusions.

#### Step 3 Analyzed and compared model results

Compared this Boosting model vs the previous ones (Regularized Regression and Decision Tree models), analyzed their predictions, the class with the highest prediction accuracy and the one with the lowest. Choosing the best performing model

#### CONCLUSIONS:

### **Key Findings**  

- **Best Test Performance (Generalization)**  
  - **Previous XGBoost Model**:  
    - **Test Accuracy**: **78.57%** (highest among all models).  
    - **Test F1-Score (Weighted Avg)**: **0.7853** (best balance of precision & recall).  
  - **Followed by**:  
    - Optimized Random Forest (**77.27%** accuracy).  
    - XGBClassifier (**76.62%** accuracy).  
    - Optimized Decision Tree (**71.43%** accuracy).  

- **Overfitting Control**  
  - The **Previous XGBoost Model** shows moderate overfitting (**4.98% gap** between train/test accuracy), which is better than:  
    - Optimized Random Forest (**6.77% gap**).  
    - XGBClassifier (**1.88% gap**, but lower test performance).  
  - This suggests the XGBoost model generalizes well to unseen diabetes patient data without memorizing noise.  

- **Alignment with Diabetes Prediction Challenges**  
  - The NIDDK dataset is **imbalanced** (more non-diabetic cases), making **F1-score** a critical metric.  
  - The **Previous XGBoost Model** outperforms others in **weighted F1-score**, meaning it better handles class imbalance.  
  - XGBoost’s built-in **regularization (L1/L2)** and **boosting mechanism** (sequential error correction) make it robust for medical data where **false negatives** (missed diabetes cases) are costly.  

---

### **Potential next steps for Deployment**  

- **Using the Previous XGBoost Model** for diabetes risk prediction, as it provides the best trade-off between **accuracy, recall** (identifying true diabetic cases), and **overfitting control**.  

- **Future improvements could include**:  
  - **Hyperparameter tuning** (e.g., adjusting `scale_pos_weight` to further mitigate class imbalance).  
  - **Feature importance analysis** (to identify key diabetes indicators like glucose levels, BMI, etc., as seen in the [`explore.ipynb` notebook](https://github.com/dianamonroe/Boosting_Algorithms/blob/main/src/explore.ipynb)).  
