from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


cv= CountVectorizer(max_features=5000,stop_words='english')

def word2vector(df):
    new_df=df
    vectors=cv.fit_transform(new_df['Tags']).toarray()
    similarity=cosine_similarity(vectors)
    return similarity


def recommend(movie,df,similarity):
    new_df=df
    movie_index=new_df[new_df['title']==movie].index[0]
    distances=similarity[movie_index]
    movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    L=[]
    for i in movies_list:
        L.append(new_df.iloc[i[0]].title)
    return L






