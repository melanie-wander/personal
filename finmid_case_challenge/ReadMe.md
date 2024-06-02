# Setup & Requirements
*Requirements* 
* Visual Studio code or similiar coding interface
* Docker 
* Python 3.9+
* All other packages needed can be installe by uncommenting the #pip.... at the beginning of the files


*Setup*
Make sure Docker is running, the navigate [docker-compose](./input-data/docker-compose.yaml) 
Then run in terminal the code below:
```shell
docker compose up
```

This will start a fresh postgres instance with all the data available.
You can connect to it on localhost:5432 with login `postgres` and password `finmid`

For all juypter and python scripts a db_connection.py exists to pull the credentials and run the sql within the scripts. 

# Report Generation
When run the report the first time either ensure you have the below packages or simple uncomment (remove #) from the beginning of the script. 
Note: ideally you would only have a data not created in this docker you can just connect via credential via the db_connection.py

* Run `client_monthly-report.py` 
* You will be promoted to  give an input 'all' or a date in the format YYYY-MM-01 
    * an error will promote you to reenter if you provide the wrong format
* a csv file will be saved in the same file location as the .py script is saved. 
    * If all it will be labeled  `client_monthly_report.csv`
    * Else `client_monthly_report_YYYY-MM-01.csv`

Future improvements, this is a realistic problem we seen in creating financial reports and invoices. The python can be updated to pull a particular client and generate a report for them. If this is only used for reporting, then it would be better to connect to the data warehouse through a visualization tool  and  have filters added for the users ease. 

# Bank Export versus Transactional data. 
This investigation can be found in the  `EDA_of_Datasets.ipynb` under the markdown `Investigate Bank Report and Transactions`; however if I were to provide updates to stakeholders I would not just show them could but just a summary of my findings and next step forward as you can see below. 

#### Summary of Findings
The Bank report is missing 12 entries dates/currency from 2022, while the companies transactions is missing 18 entries. 
* Jan 2024 is completely missing from the Company's stack
* From the timeline, we can hypothesis that full bank integration for payments was not started until late 2022 as this is when we see the amount of bank export start to increase, this does also align with the use from the clients as well. after bank ramp up we also see a connection between client ramp up in spending


#### Next Actions
* Document in the pipelines that bank transactions did not fully go through the bank until X date (assuming the hypothesis was validated with the business)
* Future proof against discrepancies, import bank amount, % taken , revenue
    * This will make it easier not only for QA for for an easier central table to review growth and financial predictions. 
    * We can also ad a test to the pipelines to check large date discrepancies. 


# Basket Size investigation
Again all pip will be at the top of the script for ease of funtion; however I would not present in this format to non-technical Stakeholders. 
The notebooek is `line_items_investigation.ipynb`

As such, I have put together a short powerpoint of the finding around basket size and customer baskets over time.  Labeled `finmid_basket_size`
