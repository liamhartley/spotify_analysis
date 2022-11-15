# Basic ETL Pipeline

<img src="https://github.com/liamhartley/spotify_analysis/blob/master/pipeline_template_assessment/etl_simple.drawio.png" width="500px">

## Contents
0. [Introduction](#introduction)
1. [Installation](#installation) 
2. [Usage](#usage)
3. [Project Architecture](#projectarchitecture)

<a name="introduction"></a>
## Introduction
This basic ETL project highlights how you may be assessed in your Data Engineering Interviews.


<a name="installation"></a>
## Pre-Requisites
[Python](https://www.python.org/downloads/)


<a name="usage"></a>
## Usage 
Fill in the blanks across the extract, transform and load (ETL) scripts in order to load the transformed data to a remote or local location.

<a name="projectarchitecture"></a>
## Project Architecture
- main.py: this file controls the ETL process 
- extract.py: this file extracts the raw data from its location
- transform.py: this file transforms the raw DataFrame into a new DataFrame
- load.py: this file loads the final DataFrame to a remote or a local location

Advanced ETL architecture:

<img src="https://github.com/liamhartley/spotify_analysis/blob/master/pipeline_template_assessment/etl_advanced.drawio.png" width="500px">

The above diagram shows better ETL architecture than the previous diagram as the processes are able to run independently of one another.

Challenge yourself to create a project adhering to the advanced architecture!

<a name="examplequestions"></a>
## Example Questions

Technical Questions:
- How does the data move between separate components? What networking features are required for this?
- How is your code deployed? Is it via a CICD pipeline?
- What would you change if you were to re-design this solution?
- What performance considerations did you have when you were designing this solution?

Business Questions:
- What are the business requirements for this product?
- How do you know that you're delivering high-quality data to your customers? (e.g. data quality checks)
- How do you prevent any downtime during maintenance?
