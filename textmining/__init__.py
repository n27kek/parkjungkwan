from textmining.model import SamsungReport

if __name__=="__main__":
    sam = SamsungReport()

   # print(sam.read_stopword())
   # sam.download()
    print(sam.find_freq())
    print(sam.draw_wordcloud())




