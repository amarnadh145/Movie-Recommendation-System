## Abstract
MOVIE RECOMMENDER SYSTEM is a machine learning application. Today the amount
of information in the internet growth very rapidly and people need some instruments to find and
access appropriate information. One of such tools is the recommender system. Movie recommender
system aims to recommend movies that users may be interested in.
In our project, we have developed a content-based movie recommender system by creating
different attributes elicited from user preference. We have improved the existing content
based recommender system by adding some new attributes like cast, crew, user_id, genre,
rating and user past experience. We have also developed the popularity-based recommender
system which recommends the movies that are in trend and are most popular among the users
based on their rating and vote count.
Our main vision is to develop a project to recommend the books to users based on his/her
interest by using content based recommender system.

## Requirements
1.Streamlit Framework
2.Pickle
3.Count vectorizer
4.Cosine Similarity

## Build
Run the code of model.txt file in a notebook to build the model which gives pickle files named 'movies.pkl',popularity.pkl',similarity.pkl' after training.

## Execution
Place all the pickle files and the app.py filr in a editor. Run the command `streamlit run app.py` in editor, browser will automatically opens and asks for the input.

## Checking for results
Give inputs to the model of your wish and click `Show recommendations` button to get the desired recommendations
