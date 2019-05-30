## Project 3 - Reddit Post Predictor

General Assembly DSI CC7 Project 3<br>
Anne Kerr - SF

## Problem Statement
The challenge for this project is to build a model that compares text from two or more Reddit subposts and correctly classify them. Data is not provided, so another component to this project is to collect data from Reddit. 

**Business context:** <br>To set a business context I decided to assume Reddit hired us to do a test the value of machine learning applied to natural language processing. They want to improve their ability to perform analysis of text posted to their site. Social media and tech companies are increasingly being called upon to be responsible for the content on their site. E.g., they may be asked to prevent hate speech that spreads violence, identify threats, etc. They are considering forming a team of data scientists to work on this problem, and as a proof-of-concept, have asked us to see if we could develop a model that correctly identifies a post as belonging to a specific subreddit discussion thread.

**Plan**<br>In response to that challenge, this project specifically attempts to answer the question:<br>
***Given a post is from one of the these four subreddits, correctly classify whether or not a post came from the r/travel thread.***
-  r/travel     <=== Target
-  r/Fitness
-  r/wine
-  r/gardening

## Overview of approach

I began by reading data from four different subreddits related to subjects that interest me. I wasn't sure at the start what I would find and which of the four I would use for the model or which would be the target. What I found was that even though I attempted to capture 1000 unique, non-empty posts for each, after dropping duplicates I was left with far fewer.  Travel had the most - with just over 800 posts. The other three combined had just over 1000, so I decided to make r/travel my target, and the other three collectively the alternate, ie., 'not travel.'

Before modeling I looked at the most common words contained in each set to get a sense for the language within. Did they look likely to be predictive? If not I might have revised my approach, but they did seem to be predictive, and I concluded I had enough data to move forward. Some cleaning and pre-processig was necessary prior to modeling. The data had a lot of punction and formatting characters, so I used a regular expression tokenizer to to create a new data element with only the word tokens. It was this element that I passed to the modeling process.

I started the modeling process by defining a series of tests using pipelines and gridsearch to try a variety of machine learning techniques, looking for the best model. Once that was found, I used that model to make predictions and analyze the results. 

Through the process I was able to produce a model that performed remakably well. This is perhaps not too surprising, given that the language in the four chosen threads does have  very distinct words that make classification relatively easy. As a proof-of-concept it does illustrate the value of using machine learning for analyzing and classifyig text. The final recommendation is that Reddit does create a data science team to continue this work.

## Overview of the Data
The requests.get method of the Reddit API returns a set of data elements related to 25 posts at a time. This can be called in a loop to gather all or as many posts as desired for a particular URL, up to a max of 1000. (The URL indicates the subreddit of interest.) Many data elements are returned per post. For this project I need only the text of the post itself, and the name of the subreddit. The process for gathering data is time consuming, so I decided to save a few other key fields that may be of interest. I did not end up using them for the project, but they are in the dataset, which I saved for potential future use. The fields I saved are defined in the table below. 


|Data Element|Description|
|-------|----------|
| subreddit | Name of the subreddit, e.g., 'travel', 'fitness', gardening, 'wine' |
| id | Unique identier of post |
| selftext| The text of the post. Not all posts have text. Some are only images or videos. For this project only post with text were collected.  |
| title | Post Title |
| author | Reddit ID of author |
| created | Date the post was created |
| ups | Number of up votes the post has recevied |
| ups | Number of up votes the post has recevied |
| downs | Number of down votes the post has receivd |


### This project contains the following folders:

| Folder  | Contents                                                              |
|---------|-----------------------------------------------------------------------|
| root    | README project overview for GitHub                                    |
| \code   | Jupyter notebooks and python code                                     |
| \data   | Dataset saved from reddit and interim files used for downstream steps |
| \images | Graphs and charts in jpg format, pfd of final presentation            |



### Summary of conclusion and next steps
The model successfully classifies r/travel, and not r/travel, with a 96% of the time!!! This is not surprising, though. These topics have very distinguishing words. It may have been much harder with more similar threads. It DOES do a good job of illustrating the classification techniques and the modeling process. Recommendation: DO HIRE DATA SCIENTISTS!!!!