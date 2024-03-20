# Thyroid Disease Detection

Thyroid disease is a very common problem in India, more than one crore people are suffering with the disease every year. Thyroid disorder can speed up or slow down the metabolism of the body.

The main objective of this project is to predict if a person is having any of the following with the help of Machine Learning.

Letters in the dataset correspond to following abnormalities :

		Letter	Diagnosis
		------	---------

	hyperthyroid conditions:

		A	hyperthyroid
		B	T3 toxic
		C	toxic goitre
		D	secondary toxic

	hypothyroid conditions:

		E	hypothyroid
		F	primary hypothyroid
		G	compensated hypothyroid
		H	secondary hypothyroid

	binding protein:

		I	increased binding protein
		J	decreased binding protein

	general health:

		K	concurrent non-thyroidal illness

	replacement therapy:

		L	consistent with replacement therapy
		M	underreplaced
		N	overreplaced

	antithyroid treatment:

		O	antithyroid drugs
		P	I131 treatment
		Q	surgery

	miscellaneous:

		R	discordant assay results
		S	elevated TBG
		T	elevated thyroid hormones
Classification algorithms such as Random Forest, Decision Tree and KNN Model have been trained on the thyroid dataset, UCI Machine Learning repository. After hyperparameter tuning Decision Tree model has performed well with better accuracy. Application has deployed on Azure with the help of flask framework.

# Webpage Link

Azure: https://thyroid-disease-detection1.azurewebsites.net


# Technical Aspects

- Python 3.9 and more
- Important Libraries: sklearn, pandas, numpy, matplotlib & seaborn
- Front-end: HTML, CSS 
- Back-end: Flask framework
- IDE: Jupyter Notebook, Pycharm & VSCode 
- Deployment: Azure

# How to run this app 

Code is written in Python 3.9 and more. If you don't have python installed on your system, click here https://www.python.org/downloads/ to install.

- Create virtual environment - conda create -n venv python=3.9
- Activate the environment - conda activate venv
- Install the packages - pip install -r requirements.txt
- Run the app - python run app.py

# Workflow

## Data Collection

Thyroid Disease Data Set from UCI Machine Learning Repository.

Link:https://archive.ics.uci.edu/ml/datasets/thyroid+disease

## Data Pre-processing

- Missing values handling by Simple imputation (KNN Imputer)
- Outliers detection and removal by boxplot and percentile methods
- Categorical features handling by ordinal encoding and label encoding
- Feature scaling done by Standard Scalar method
- Imbalanced dataset handled by SMOTE
- Drop unnecessary columns

## Model Creation and Evaluation

- Various classification algorithms like Random Forest, XGBoost, KNN etc tested.
- Random Forest, XGBoost and KNN were all performed well. XGBoost was chosen for the final model training and testing.
- Hyper parameter tuning was performed using RandomizedSearchCV
- Model performance evaluated based on accuracy, confusion matrix, classification report.


## Model Deployment
The final model is deployed on Azure using Flask framework.


## User Interface

<img width="824" alt="Screenshot 2024-03-16 at 9 15 53 AM" src="https://github.com/Nayanajagadeesh/Thyroid_disease_detection/assets/138456413/5cc69e1a-015c-4167-b909-9d39a9cfae39">
<img width="824" alt="Screenshot 2024-03-16 at 9 16 28 AM" src="https://github.com/Nayanajagadeesh/Thyroid_disease_detection/assets/138456413/eb3fd4d2-18c5-4195-8258-12460acf279b">


<img width="1429" alt="Screenshot 2024-03-15 at 11 55 36 PM" src="https://github.com/Nayanajagadeesh/Thyroid_disease_detection/assets/138456413/9ded190a-1496-4ac7-ba6b-62750ffc4be3">


## Project Documents

- HLD: https://github.com/Nayanajagadeesh/Thyroid_disease_detection/blob/main/Documents/TDD_HLD_V1.0.pdf

- LLD: https://github.com/Nayanajagadeesh/Thyroid_disease_detection/blob/main/Documents/TDD_LLD_V1.0.pdf

- Architecture: https://github.com/Nayanajagadeesh/Thyroid_disease_detection/blob/main/Documents/TDD_Architecture_V1.0.pdf

- Wireframe: https://github.com/Nayanajagadeesh/Thyroid_disease_detection/blob/main/Documents/TDD_Wireframe_V1.0.pdf

- Detailed Project Report: https://github.com/Nayanajagadeesh/Thyroid_disease_detection/blob/main/Documents/TDD_DPR.pdf

