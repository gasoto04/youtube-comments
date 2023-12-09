# Code
For our project we have used three different processes: data collection/gathering, the data sentiment analysis and the data visualization. For ease of code, we have divided these processes into 3 different Jupyter Notebooks. For more information about the notebooks, we suggest following the supplied link to our github repository.

For our data gathering section we  download the video's metadata and comments from the 3 categories of analysis. Using the Youtube API, facilitated through a *.py* file adjacent to this one, it gets the information on two dataframes: one with the video information, and the other with the comments information. For each video/comment the days since the event happened is on a column. All the information is stored in .csv to later be processed on sentiment analysis. 
This file that contains the main structure for data collection is _data_gathering.ipynb and the functions that extract detailed data from the videos is yt_videos_comments.py

The main functions used for our data gathering were:
* *get_videos_after_ndays(api_key, query, start_date, n_days)*: This function gets the videos from the query through the Youtube API from the start date to 14 days, which is the n we have established.
* *get_comments_all_videos(api_key, df_videos, get_replies=False)*: This function gets the comments from the videos, where the date are the date the video was published to 14 days. This is to get the most engaged comments after video publication.
We have used the pd.to_csv function to export csv files of the comments to later be used as inputs for our sentiment analysis. 
For each category we have the following outputs on csv:

#### Video data csv files
- Swift_pop_videodata.csv
- Uvalde_horrific_videodata.csv
- Ukraine_horrific_videodata.csv
- menendez_scandal_videodata.csv
#### Comments data csv files
- Swift_pop_comments.csv
- Uvalde_horrific_comments.csv
- Ukraine_horrific_comments.csv
- menendez_scandal_comments.csv

Second, we did the data sentiment analysis with a DistilBert based machine learning model included in the Hugging Face website. Our model used is the *distilbert-base-multilingual-cased-sentiments-student*, its a zero-shot classification bert based model, that every score it gives, its a  probability of that comment analyzed to be neutral, positive or negative. 
For every category we have used the output from the previous sections to create dataframes to do the sentiment analysis to each one of them using the pd.read_csv() function. The sentiment analysis is located in the Data Science 1 Final Project - Sentiment file. Our main function used for the sentiment analysis is the following:
* *get_sentiment_score(sentiment_list, target_label)*: This function is used to extract the score out of the sentiment column that has a list of the probabilities score per sentiment. 
sentiment_analyzer = pipeline("sentiment-analysis", model="lxyuan/distilbert-base-multilingual-cased-sentiments-student", return_all_scores=True)
* *get_sentiment_score(sentiment_list, target_label)*: We have instantiated our analyzer with the model, so we can run the sentiment_analyzer on our categories.  
* *truncate_text(text)*: This function is being used to truncate the text column to 512 tokens, for the limit we are facing with the model.
Our outputs are csv files that have 3 extra columns to our dataframe, adding a ‘negative’, ‘positive’ and ‘neutral’ probabilities score for each comment. It is worth noting that for bigger datasets (Ukraine and Uvalde) the outputs had to be splitted in several files due to processing time. 

Lastly, the data visualization was done first, reading the csv files of comments csvs and the video data csv this way we have the metadata attached to our analysis. It is important to note that for our dataframes, we have created a column called comment_score, where we are counting the amount of likes +1 a comment has, so to run a regression and see the relationship between the amount of likes and the probability score of a particular sentiment. Plus, we are also creating positive, negative and neutral dummy columns that will help us classify a comment by its probability score greater than 0.7. Below, we have detailed the results obtained from the data processing and how we graphed, made and summarize the data. Data visualizations were created using the *Plotnine* Python package. 
