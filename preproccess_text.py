from nltk.corpus import stopwords
import redditcleaner
import re


#Removing stop words
pattern = re.compile(r'\b(' + r'|'.join(stopwords.words('english')) + r')\b\s*')
df_mid['subm_text_processed'] = df_mid['Body'].map(lambda x: re.sub(pattern, '', x))
df_pre['subm_text_processed'] = df_pre['Body'].map(lambda x: re.sub(pattern, '', x))
df_ctrl['subm_text_processed'] = df_ctrl['Body'].map(lambda x: re.sub(pattern, '', x))

#redditclean
df_mid['subm_text_processed'] = df_mid['subm_text_processed'].map(redditcleaner.clean)
df_pre['subm_text_processed'] = df_pre['subm_text_processed'].map(redditcleaner.clean)
df_ctrl['subm_text_processed'] = df_ctrl['subm_text_processed'].map(redditcleaner.clean)

#Removing x200b
df_mid['subm_text_processed'] = df_mid['subm_text_processed'].map(lambda x: re.sub('x200b', '', x))
df_pre['subm_text_processed'] = df_pre['subm_text_processed'].map(lambda x: re.sub('x200b', '', x))
df_ctrl['subm_text_processed'] = df_ctrl['subm_text_processed'].map(lambda x: re.sub('x200b', '', x))


#Removing url links
df_mid['subm_text_processed'] = df_mid['subm_text_processed'].map(lambda x: re.sub('(https?:\/\/)(\s)*(www\.)?(\s)*((\w|\s)+\.)*([\w\-\s]+\/)*([\w\-]+)((\?)?[\w\s]*=\s*[\w\%&]*)*', '', x))
df_pre['subm_text_processed'] = df_pre['subm_text_processed'].map(lambda x: re.sub('(https?:\/\/)(\s)*(www\.)?(\s)*((\w|\s)+\.)*([\w\-\s]+\/)*([\w\-]+)((\?)?[\w\s]*=\s*[\w\%&]*)*', '', x))
df_ctrl['subm_text_processed'] = df_ctrl['subm_text_processed'].map(lambda x: re.sub('(https?:\/\/)(\s)*(www\.)?(\s)*((\w|\s)+\.)*([\w\-\s]+\/)*([\w\-]+)((\?)?[\w\s]*=\s*[\w\%&]*)*', '', x))

#Removing ampersands
df_mid['subm_text_processed'] = df_mid['subm_text_processed'].map(lambda x: re.sub('amp', '', x))
df_pre['subm_text_processed'] = df_pre['subm_text_processed'].map(lambda x: re.sub('amp', '', x))
df_ctrl['subm_text_processed'] = df_ctrl['subm_text_processed'].map(lambda x: re.sub('amp', '', x))

#Removing nan
df_mid['subm_text_processed'] = df_mid['subm_text_processed'].map(lambda x: re.sub('nan', '', x))
df_pre['subm_text_processed'] = df_pre['subm_text_processed'].map(lambda x: re.sub('nan', '', x))
df_ctrl['subm_text_processed'] = df_ctrl['subm_text_processed'].map(lambda x: re.sub('nan', '', x))

#Removing new line tabs
df_mid['subm_text_processed'] = df_mid['subm_text_processed'].map(lambda x: re.sub('[\n]', '', x))
df_pre['subm_text_processed'] = df_pre['subm_text_processed'].map(lambda x: re.sub('[\n]', '', x))
df_ctrl['subm_text_processed'] = df_ctrl['subm_text_processed'].map(lambda x: re.sub('[\n]', '', x))

# Remove punctuation
df_mid['subm_text_processed'] = df_mid['subm_text_processed'].map(lambda x: re.sub('[,\.*!?]', '', x))
df_pre['subm_text_processed'] = df_pre['subm_text_processed'].map(lambda x: re.sub('[,\.*!?]', '', x))
df_ctrl['subm_text_processed'] = df_ctrl['subm_text_processed'].map(lambda x: re.sub('[,\.*!?]', '', x))

# Convert the titles to lowercase
df_mid['subm_text_processed'] = df_mid['subm_text_processed'].map(lambda x: x.lower())
df_pre['subm_text_processed'] = df_pre['subm_text_processed'].map(lambda x: x.lower())
df_ctrl['subm_text_processed'] = df_ctrl['subm_text_processed'].map(lambda x: x.lower())
