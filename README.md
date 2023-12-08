# youtube-comments - Project Description

## Final Project Proposal
Gabriel Andres Soto, Sam Cohen, Daniel Cardenas Sanchez
PPOL 5203

### Introduction and Research Question
With the advent of the internet and the increase in Smartphone usage across the world, the speed at which individuals can now obtain information and news has never been faster. This interconnectedness comes with problems, however. The spread of misinformation, political extremism, and polarization are just a few consequential examples. This phenomenon provides researchers with a looking glass into public sentiment regarding certain issues, which can often be found in some of the darkest places on the web– Youtube’s comments sections. 

Our research will attempt to answer the following research question: do individuals react differently to different types of shocking news on Youtube?  Will those comments be mostly “positive” (i.e. concerned, empathetic, well-intentioned) if the news is more serious? Will they be mostly negative (ill-intentioned, bullying, insulting)? We will also consider the following when writing our report and carrying out our analysis:

### Navigating this repository
This repository has been divided into 3 primary folders for our research:
- Code
- Data
- Output

#### Code
This folder contains the Python files that were used in our analysis:
- "Data Science 1 Final Project - Data Analysis" contains the summary statistics, hypothesis testing, and data visualizations for this project. Data was imported, wrangled, and analyzed in this file.
- "Data Science 1 Final Project - Sentiment" was used to generate the sentiment analysis of Youtube comments necessary for our research.
- "_data_gathering" contains the code for using the Youtube API to retrieve comment and video data in the first place.
- "yt_videos_comments" is the file that houses the functions necessary to carry out retrieving comment and video data using the Youtube API 
The folder titled "Old" contains previous versions of the files above.

#### Data
This folder houses all of the raw extracted data from the Youtube API. Specifically, it contains the comment and video data for Taylor Swift dating Travis Kelce for pop news, video data for the Menendez scandal for scandalous news, and Uvalde shooting video data for horrific news. Please note that comment data for both scandalous and horrific news has been put in the "Output" folder-- the comment data and sentiment analysis were carried out both in the same file for these. 

### Output
This folder contains the comment sentiment analysis for all news categories. Some categories (e.g. Uvalde) have multiple sentiment analysis files. These files were concatenated with each other in the "Data Science 1 Final Project - Data Analysis" file when data analysis was being carried out. 

Along with the sentiment analysis output, this folder contains a literature review which outlines previous research carried out on reactions to shocking news, sentiment analysis, and the combination of both. 



