## Natural Language Processing To Analyze Abuse and Domestic Violence Subreddits During COVID-19

#### Author: Amie Kong

## Subreddit Data Download & Extraction:
> pushshift.py

Datasets were extracted using the Pushshift API  (pushshift.io) from 4 different subreddits (r/abuse, r/domesticViolence, r/ptsd, r/CSEducation) during different time frames: pre-pandemic (November 1, 2018 to November 1, 2019), mid-pandemic (January 15, 2020 to May 1, 2020), and a control time frame to compare the quantity of submissions before and during the pandemic (January 15, 2019 to May 1, 2019). Another dataset was created as a separate experimental group: (r/covid) in a shortened time frame of January 15, 2020 to April 1, 2020 to account for the influx of post submissions and it made it easier to handle the data. Only posts including a title and a body were included to exclude posts with just images. The datasets were then saved as CSV files and distinguished by the different time frames and subreddit. The number of submissions for each dataset range from 792 to 8682 due to the popularity of certain subreddit groups (e.g. r/ptsd and r/home) that possess more posts overall. Dropping and querying of the datasets was necessary to normalize the data into the following columns: Post Id, Title, Body, Author, Publish Date, and Total No. of Comments. Using the NLTK and redditclean package, the “Body” column text of each submission post was further cleaned and preprocessed by removing English stop-words, punctuation, and url links.

## NLP Analysis and LDA Topic Modeling On Multiple Subreddits:

Each notebook under the /experiments directory includes experiments for Linguistic Inquiry & Word Count (LIWC) Feature Analysis, VADER Sentiment Analysis, and Latent Dirichlet Allocation Topic Modeling.

1. Abuse Subreddit Feature Analysis and LDA Topic Modeling.ipynb
2. CS Education Subreddit Feature Analysis and LDA Topic Modeling.ipynb
3. Domestic Violence Subreddit Feature Analysis and LDA Topic Modeling.ipynb
4. PTSD Subreddit Feature Analysis and LDA Topic Modeling.ipynb

> reddit_data/
>> directory includes .csv files for subreddit data sets that were extracted using pushshift.py code

### Subreddit Analysis Using LIWC Feature Extraction

Linguistic Inquiry Word Count (LIWC) features from the body of each subreddit was extracted to perform an analysis on the dominant traits present in each subreddit (Pennebaker). 92 features were extracted using the LIWC software which includes the general LIWC features such as word count, analytic, cloud, tone, pronoun, as well as other features that detect other scenarios such as anger, sad, social (all LIWC features extracted in the following order):

> 'WC', 'Analytic', 'Clout', 'Authentic', 'Tone', 'WPS', 'Sixltr', 'Dic',
       'function', 'pronoun', 'ppron', 'i', 'we', 'you', 'shehe', 'they',
       'ipron', 'article', 'prep', 'auxverb', 'adverb', 'conj', 'negate',
       'verb', 'adj', 'compare', 'interrog', 'number', 'quant', 'affect',
       'posemo', 'negemo', 'anx', 'anger', 'sad', 'social', 'family', 'friend',
       'female', 'male', 'cogproc', 'insight', 'cause', 'discrep', 'tentat',
       'certain', 'differ', 'percept', 'see', 'hear', 'feel', 'bio', 'body',
       'health', 'sexual', 'ingest', 'drives', 'affiliation', 'achieve',
       'power', 'reward', 'risk', 'focuspast', 'focuspresent', 'focusfuture',
       'relativ', 'motion', 'space', 'time', 'work', 'leisure', 'home',
       'money', 'relig', 'death', 'informal', 'swear', 'netspeak', 'assent',
       'nonflu', 'filler', 'AllPunc', 'Period', 'Comma', 'Colon', 'SemiC',
       'QMark', 'Exclam', 'Dash', 'Quote', 'Apostro', 'Parenth', 'OtherP'

The psychological processes summed by the 9 subprocesses (affective, social, cognitive, perceptual, biological, informal language, and drives), were extracted from each subreddit to study the general psychological processes used in posts, as well as for comparison before and during the pandemic. 

A change in the psychological processes categories of cognitive processes and relativity existed for the CS Education subreddit, which is the control group of this study. During the pandemic, the frequency of words that fall under the cognitive processes category increased by 4% and relativity increased by 2%. It also has a higher portion of language classified under “drives” (summed up by categories: achievement, power, and reward scores); therefore, we can deduce that this subreddit group primarily includes posts that relate to drive. As for the other control dataset of the PTSD subreddit, all areas of psychological processes remain consistent before and during the pandemic with the top two processes that generalize the PTSD subreddit being cognitive processes (e.g. insight, causation, discrepancy, tentative, certainty) and relativity (e.g. motion and space).

<img src="https://github.com/amiekong/nlp-reddit-analysis/blob/master/images/abuse_liwc_mid.png" width="500" height="350">

<img src="https://github.com/amiekong/nlp-reddit-analysis/blob/master/images/abuse_liwc_pre.png" width="500" height="350">

For the abuse subreddit, the top processes that generalize this data set are social, cognitive, and relativity; however, no change in frequency distribution of the categories was detected in pre-pandemic vs the mid-pandemic dataset. Similarly, the top processes that generalize the domestic violence subreddits are social, cognitive, and relativity, with no change detected in the frequency distribution of the psychological processes in the pre-pandemic vs the mid-pandemic dataset.

### Extracting VADER Features for Sentiment Analysis

Valence Aware Dictionary and Sentiment Reasoner (VADER) is a “a lexicon and rule-based sentiment analysis tool that is specifically attuned to sentiments expressed in social media.” It measures the strength and direction of sentiment across an entire text and the algorithm adjusts for negations and booster words, returning the proportion of the text that is negative, positive, neutral, and a combined score. VADER scores were extracted for each subreddit by importing SentimentAnalyzer from the NLTK package. The polarity scores were concatenated onto the data frame and an analysis on the compound scores were done to examine the positive, neutral, and negative posts of each subreddit.

<img src="https://github.com/amiekong/nlp-reddit-analysis/blob/master/images/vader_results.png" width="300" height="900">


### Latent Dirichlet Allocation Topic Modeling on Subreddits

A probabilistic modeling approach of topic modeling, LDA (Latent Dirichlet Allocation), was performed on each data set to detect the top underlying topics and if there exists any noticeable changes for each subreddit prepandemic vs midpandemic [1].

LDA was used to detect any topic changes in the extracted pre-pandemic subreddit submissions vs the mid-pandemic subreddit submissions. A bag-of-words corpus was created, which was used to create an LDA model and 5 topics were created. Models were also generated multiple times with different numbers of words for each topic to address the consistency of topics. Using the scikit package, a manually chosen LDA model with 5 topics was then applied to the r/abuse subreddit to assess the distribution of topics, allowing for comparison between the distribution of subreddit submissions pre-pandemic vs mid-pandemic. Furthermore, the gensim package was installed to generate the interactive pyLDAvis visualization maps.





### Project Report:
"Kong_Amie_Project_Report.pdf"
