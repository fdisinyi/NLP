from stop_words import get_stop_words
import re
import nltk
from matplotlib import pyplot as plt
import seaborn as sns
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import pandas as pd
top_200 = 200
data=pd.read_csv('review.csv',encoding='latin-1')
lower_data = data['Review'].str.lower().str.cat(sep=' ')
# removes punctuation,numbers
data_list = re.sub('[^A-Za-z]+', ' ', lower_data)

#remove the stopwords
stop_words = list(get_stop_words('en'))         
nltk_words = list(stopwords.words('english'))   
stop_words.extend(nltk_words)

word_tokens = word_tokenize(data_list)
#filtered_sentence = [w for w in word_tokens if not w in stop_words]
filtered_sentence = []
for word in word_tokens:
    if word not in stop_words:
        filtered_sentence.append(word)

#remove stopwords based on Custom stopwords
stopwordlist = ['movie', 'film','one','really']
finalList=[]
for j in filtered_sentence:
    if j not in stopwordlist:
        finalList.append(j)
        
       
# Remove characters which have length less than 2  
without_single_chr = [word for word in finalList if len(word) > 2]

# Remove numbers
cleaned_data_title = [word for word in without_single_chr if not word.isnumeric()]        

# Calculate frequency distribution
word_dist = nltk.FreqDist(cleaned_data_title)
result = pd.DataFrame(word_dist.most_common(top_200), columns=['Word', 'Frequency'])
plt.figure(figsize=(10,10))
sns.set_style("whitegrid")
ax = sns.barplot(x="Word",y="Frequency", data=result.head(10))