'''
Author:Shubham Sharma
Date:15-04-2021
Purpose:Search Engine
'''

def matchingWords(sentence1,sentence2):
    words1=sentence1.strip().split(" ")
    words2=sentence2.strip().split(" ")
    score=0

    for word1 in words1:
        for word2 in words2:
            if word1.lower()==word2.lower():

                score+=1
    return score

if __name__=="__main__":
    sentences=["Youtube Python Videos","Coding in Python","GeeksofGeeks for python",
               "Mathematics for Machine Learning"]
    query=input("Please Enter the String you want to Search\n")
    scores=[matchingWords(query,sentence) for sentence in sentences]

    sortedSentScore=[sentScore for sentScore  in sorted(
        zip(scores,sentences),reverse=True) if sentScore[0]!=0]
    print(f"{len(sortedSentScore)} results found!")
    for score,item in sortedSentScore:
        print(f" \"{item}\": with a score of {score}")

