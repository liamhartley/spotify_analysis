# Spotify Analysis

## Contents
0. [Introduction](#introduction)
1. [Installation](#installation) 
2. [Usage](#usage)
3. [Project Architecture](#projectarchitecture)
4. [Future Improvements](#futureimprovements)
    1. [Calculation Improvements](#calculationimprovements)
    2. [Platform Imrpovements](#platformimprovements)
    3. [Code Quality Improvements](#codequalityimprovements)
5. [How to Contribute](#howtocontribute)

<a name="introduction"></a>
## Introduction 

Welcome to Spotify Analysis. 
Enjoy learning more about the music you listen to and your personal listening habits.


<a name="installation"></a>
## Installation 

#### Pre-Requisites
[Python](https://www.python.org/downloads/), [Terraform](https://www.terraform.io/downloads.html) and [Spotipy](https://spotipy.readthedocs.io/en/2.13.0/).


<a name="usage"></a>
## Usage 
Run the scripts with a dictionary of your faovurite artists or playlists to gather data about them and save it locally or in S3.

<a name="projectarchitecture"></a>
## Project Architecture 

<img src="https://github.com/liamhartley/spotify_analysis/blob/master/spotify_analysis.drawio.png" width="500px">

The Terraform scripts build:
- A lambda function with the analysis code
- A cloudwatch alarm to run that function weekly
- All relevant IAM policies / roles

This will generate a datalake of Spotify data locally or in S3.

<a name="futureimprovements"></a>
## Future Improvements

Any 'TODO' tags in the project.

<a name="calculationimprovements"></a>
##### Calculation Improvements

<a name="platformimprovements"></a>
##### Platform Improvements
- Improve UX
- Upload as a package

<a name="codequalityimprovements"></a>
##### Code Quality Imrpovements

<a name="howtocontribute"></a>
## How to Contribute 
Make a branch and raise a PR
