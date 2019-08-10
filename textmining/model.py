from konlpy.tag import Okt
from nltk.tokenize import word_tokenize
import re
import nltk
import pandas as pd
from nltk import FreqDist
from wordcloud import WordCloud
import matplotlib.pyplot as plt

class SamsungReport:
    def __init__(self):
        self.okt=Okt()


    def read_file(self):

        self.okt.pos('삼성전자 글로벌센터 전자사업부',stem=True)
        filename='./data/kr-Report_2018.txt'
        with open(filename,'r',encoding='utf-8') as f:
            texts=f.read()
        return texts

    @staticmethod
    def extract_hangeul(texts):
        temp=texts.replace('\n',' ')
        tokenizer=re.compile(r'[^ ㄱ-힣]+')
        temp=tokenizer.sub('',temp)
        return temp

    @staticmethod
    def change_token(texts):
        tokens = word_tokenize(texts)
        print(tokens[:7])
        return tokens

    def extract_noun(self):
        #삼성전자의 스마트폰은 - >삼성전자 스마트폰
        noun_tokens=[]
        tokens=self.change_token(self.extract_hangeul(self.read_file()))
        for token in tokens:
            token_pos=self.okt.pos(token)
            temp=[txt_tag[0] for txt_tag in token_pos if txt_tag[1]=='Noun']
            if len(''.join(temp))>1:
                noun_tokens.append(''.join(temp))

        texts=''.join(noun_tokens)
        print('------------')
        print(texts[:300])
    @staticmethod
    def download():
        nltk.download()


    @staticmethod
    def read_stopword():
        stopfile='./data/stopwords.txt'
        with open(stopfile,'r',encoding='utf-8') as f:
            stopwords=f.read()
        stopwords = stopwords.split(' ')
        print('-------제거할 단어-------')
        print(stopwords[:10])
        return stopwords


    def remove_stopword(self):
        texts = self.extract_noun()
        tokens = self.change_token(texts)
        # print('------- 1 명사 -------')
        # print(texts[:30])
        stopwords = self.read_stopword()
        # print('------- 2 스톱 -------')
        # print(stopwords[:30])
        # print('------- 3 필터 -------')
        texts = [text for text in tokens
                 if text not in stopwords]
        # print(texts[:30])
        return texts

    def find_freq(self):
        texts=self.remove_stopword()
        freqtxt=pd.Series(dict(FreqDist(texts))).sort_values(ascending=False)
        print(freqtxt[:30])
        return freqtxt

    def draw_wordcloud(self):
        texts=self.remove_stopword()
        wcloud=WordCloud('./data/D2Coding.ttf',relative_scaling=0.2,background_color='white').generate(' '.join(texts))


        plt.figure(figsize=(12,12))
        plt.imshow(wcloud,interpolation='bilinear')
        plt.axis('off')
        plt.show()








