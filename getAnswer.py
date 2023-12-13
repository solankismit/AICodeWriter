from bardapi import Bard
import os
str = "Hello world"
str.__contains__
#Replace XXXX with the values you get from __Secure-1PSID 
os.environ['_BARD_API_KEY']="Wgg9nXs8vdqDukBDp7C2ParXPNVd7ERFt5FSjsufXP3pi4_30sDSICpGrBmDD46CDErP2g."
def getOutput(input_text):
    # Code to get Answer from Google Bard
    ans = Bard().get_answer(input_text)['content']
    return ans 

# Preprocess the input text
def preprocess(input_text):
    input_text = input_text[:input_text.lower().find("study")] + input_text[input_text.lower().find("study")+5:] if input_text.lower().__contains__("study") else input_text
    input_text = input_text[:input_text.lower().find("describe")] + input_text[input_text.lower().find("describe")+8:] if input_text.lower().__contains__("describe") else input_text
    input_text = input_text[:input_text.lower().find("explain")] + input_text[input_text.lower().find("explain")+7:] if input_text.lower().__contains__("explain") else input_text
    input_text = input_text[:input_text.lower().find("write")] + input_text[input_text.lower().find("write")+17:] if input_text.lower().__contains__("write") else input_text
    input_text = input_text[:input_text.lower().find("description")] + input_text[input_text.lower().find("description")+19:] if input_text.lower().__contains__("description") else input_text
    input_text = input_text[:input_text.lower().find("the")] + input_text[input_text.lower().find("the")+21:] if input_text.lower().__contains__("the") else input_text
    input_text = input_text.replace("and", "")
    input_text = input_text.replace("or", "")
    input_text = input_text.replace("of", "")
    input_text = input_text.replace(",", "")
    # input_text = input_text.replace(" ", "")
    input_text = input_text[:input_text.lower().find("implement")] + input_text[input_text.lower().find("implement")+9:] if input_text.lower().__contains__("implement") else input_text
    input_text = input_text[:input_text.lower().find("write a program")] + input_text[input_text.lower().find("write a program")+16:] if input_text.lower().__contains__("write a program") else input_text
    input_text = input_text[:input_text.lower().find("write a code")] + input_text[input_text.lower().find("write a code")+13:] if input_text.lower().__contains__("write a code") else input_text
    return input_text

def getCode(input_text):
    input_text = preprocess(input_text)
    # set your input text
    ans = getOutput("Write a code for "+input_text+" in python")
    code = ans[ans.find("```")+9:ans.find("```", ans.find("```")+9)]
    return code

def isCode(input_text):
    if input_text.lower().__contains__("implement") or input_text.lower().__contains__("write a program") or input_text.lower().__contains__("write a code"):
        return True
    return False

def isDescription(input_text):
    if input_text.lower().__contains__("study"):
        return True
    return False

def getDescription(input_text):
    input_text = preprocess(input_text)
    temp = input_text
        # Write a proper query so we get perfect answer add to Write description
    input_text = "Tell me about "+input_text +" in detail for my Learning Journal. Do not Write that extra things like \"This is a very good question\" or \"I am very happy to answer this question\". Just write the answer."
    print("INPUT TEXT: "+input_text)    

    # set your input text
    ans = getOutput(input_text)
    # IF ans contains less than 4 new line then rerun the funtion
    if ans.count("\n") < 3:
        input_text = temp
        ans = getDescription(input_text)
    # Remove the first line
    ans = ans[ans.find("\n")+1:]
    
    print(ans)
    return ans
