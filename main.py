import requests
from bs4 import BeautifulSoup

# func which get dict and sort it by values
def sortDict(dic):
    sorted_dict = {}
    for w in sorted(dic, key=dic.get,):
       sorted_dict[w] = dic[w]
    return sorted_dict

# func which get dict and sort it reverse by values
def sortReverseDict(dic):
    sorted_dict = {}
    for w in sorted(dic, key=dic.get, reverse=True):
       sorted_dict[w] = dic[w]
    return sorted_dict

# function which get single url and return words list without characters and numbers
def getURLAndReturnWordsList(url):
    res = requests.get(url)
    html_page = res.content
    soup = BeautifulSoup(html_page, 'html.parser')
    content = ''
    for each_text in soup.find_all(text=True):
        content = content + each_text
    words = content.lower().split()
    clean_list = []
    for word in words:
        symbols = "!@#$%^&*()_-+={[}]|\;:\"<>?/., "
        for i in range(len(symbols)):
            word = word.replace(symbols[i], '')
        if len(word) > 1 and word.isalpha():
            if not word.isnumeric():
                clean_list.append(word)
    return clean_list

# func which get list and put their name and freq in dict, for example: {"word": 2,...}
def checkCommonByDict(list):
    dictOfCommonWords = {}
    #run on the list and put each word in dict and his frequency,
    # if it exist - inc the frequency, else frequency = 1.
    for word in list:
        if word in dictOfCommonWords:
            dictOfCommonWords[word] += 1
        else:
            dictOfCommonWords[word] = 1
    return sortReverseDict(dictOfCommonWords)

# func which get dict with words and freq, it return The ten most common words and their length
def dictToOrderNewDictByLength(dic):
    LengthDict = {}
    for word in list(dic)[0:10]:
            LengthDict[word] = len(word)
    return LengthDict


if __name__ == '__main__':
    urlsString = input("Please insert a urls with space,\n for example: url1 url2 url3\n")
    listOfUrl = urlsString.split(' ')
    worldsAllURLsList = []
    for url in listOfUrl:
        worldsAllURLsList.extend(getURLAndReturnWordsList(url))
    dictOfAllTheURLs = checkCommonByDict(worldsAllURLsList)
    print(dictOfAllTheURLs)

    dictOfAllTheURLs = dictToOrderNewDictByLength(dictOfAllTheURLs)
    dictOfAllTheURLs = sortReverseDict(dictOfAllTheURLs)

    for word, length in sortDict(dictToOrderNewDictByLength(dictOfAllTheURLs)).items():
        print('Length ' + str(length) + ': ' + word)

