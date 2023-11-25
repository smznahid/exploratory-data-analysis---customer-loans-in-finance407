# EDA on the loan portfolio for a large financial institution.
---
## Introduction:
 This is a project assigned to me by AiCore as part of my Data Analytics Bootcamp, during this project I have been tasked with performing an in depth analysis on a koan portfolio of a mock company using different statistical and data visualisation techniques to find insights, patterns, anomalies and relationships found within the loan data.

---

## Technology/framework used:
- python 3.12.0
- pip
- VSCode
- CLI
- miniconda


### Python libraries used:
- matplotlib 3.5.1
- missingno 0.5.2
- numpy 1.21.3
- pandas 1.4.2
- plotly 5.18.0
- PyYAML 6.0.1
- scipy 1.7.1
- seaborn 0.13.0
- SQLAlchemy 1.4.35



---
## Usage:
Create a `credentials.yaml` file in the following format
```yaml
RDS_HOST: # RDS host url.
RDS_PASSWORD: # RDS password
RDS_USER: # RDS username
RDS_DATABASE: # database name
RDS_PORT: # port
```
after creating your credentials file direct yourself to the src folder using
```bash
cd path/to/src
```
then create and activate a new conda environment by using:
```bash
conda create -n [name of environment]
```
```bash
conda activate [name of environment]
```
then install pip
```bash
conda install pip -y 
```
after installing pip run:
```bash
pip install -r requirements.txt
```
then open the notebook and run the cells.

---
## File Structure:
```
├── src
│   ├── modules
│   │   ├── db_utils.py
│   │   ├── get_information.py
│   │   ├── plotter.py
│   │   ├── transform_data.py
│   ├── .gitignore
│   ├── README.md
│   ├── analysis.ipynb
│   ├── credentials.yaml # after creating your own.
│   ├── requirements.txt
└──
```


---
## Roadmap:

1. [x] Finish implementing ```db_utils.py``` to correctly connect and extract data from the database in the cloud.
1. [x] Familiarise myself with the data using `get_information.py`.
1. [x] Clean and transform the data using `transform_data.py`
1. [x] Find insights from within the data and correctly visualise them using `plotter.py`.
