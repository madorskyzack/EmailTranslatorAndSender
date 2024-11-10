#python user prompted email sender with translator using app passwords (to bypass two factor authentication) by Zachary Madorsky
#contains code to from CodeWithTomi on YouTube
#created 11/3/24
#updated 11/5/24 added translator 
#updated 11/9/24 added comments and imported to GitHub 

from email.message import EmailMessage #for creating and sending the email
from googletrans import Translator #for translating
import ssl #to set up a secure SSL context 
import smtplib #to send emails
import re #for checking if email and app password formats are valid

#functions----------------------------------

def translateMessage(text, choice):
    translator = Translator() #translator object from google

    #Add more languages by searching up Google Translate's API
    if choice == "s":
        language = 'es'  # Spanish
    elif choice == "r":
        language = 'ru'  # Russian
    elif choice == "f":
        language = 'fr'  # French
    elif choice == "c":
        language = 'zh-CN'  # Chinese
    elif choice == "t":
        language = 'tl'  # Tagalog

    translation = translator.translate(text, dest=language)

    translation2 = translation.text #remove the .text
    return translation2

def isEmailValid(email): #checks if a user inputted email is a valid email
    emailFormat = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$' #expression for email format (x@y.z)
    
    if re.match(emailFormat, email): #check if email_regex matches the pattern of an email
        return True
    else:
        return False

def isAppPassValid(appPass): #checks if an app password is in a valid format
    appPassFormat = r'^[a-z]{4} [a-z]{4} [a-z]{4} [a-z]{4}$' #expression for app password format

    if re.match(appPassFormat, appPass): 
        return True
    else:
        return False
    
def isLanguageValid(userInput):
    if userInput in ('s', 'r', 'f', 'c', 't'): #check if user inputted a valid character
        return True
    else:
        return False
    
#main program--------------------------------

email_sender = input('Enter the sender email (ex. "example@gmail.com"): ')
while (isEmailValid(email_sender) == False): 
        email_sender = input('Invalid format. Enter the sender email (ex. "example@gmail.com"): ')
  
email_password = input('Enter the app password of the sender email (ex: "abcd efgh ijkl mnop"): ')
while (isAppPassValid(email_password) == False):
     email_password = input('Invalid format. Enter the app password of the sender email (ex: "abcd efgh ijkl mnop"): ')
#two more options of obtaining the app password:
#1. import password from another file (ex: "from senderAppPassword import password") 
#2. define the app password locally (ex: "email_password = (sender app pasword)")
email_receiver = input('Enter the receiver email (ex. "example@gmail.com"): ')
while (isEmailValid(email_receiver) == False):
        email_receiver = input('Invalid format. Enter the receiver email (ex. "example@gmail.com"): ')

subject = input('Enter the subject of the email: ')
body = input('Enter the body: ')

#translator-----------------------------------

translateIn = input('Would you like to translate the email into another language? (y/Y for Yes): ')
while(translateIn not in ['y', 'Y', 'n', 'N']):
    translateIn = input('Invalid input. Would you like to translate the email into another language? (y/Y for Yes, n/N for No): ')
if (translateIn == 'y' or translateIn == 'Y'):
     langIn = input('What language would you like to translate to? (s for Spanish, r for Russian, f for French, c for Chinese, t for Tagalog): ')
     while(isLanguageValid(langIn) == False):
         langIn = input('Invalid input. What language would you like to translate to? (s for Spanish, r for Russian, f for French, c for Chinese, t for Tagalog): ')
     
     #set the language output for the final output (last lines)
     if (langIn == 's'):
        finalLang = 'Spanish'
     elif(langIn == 'r'):
        finalLang = 'Russian'
     elif(langIn == 'f'):
        finalLang = 'French'
     elif (langIn == 'c'):
        finalLang = 'Chinese'
     elif (langIn == 't'):
        finalLang = 'Tagalog'

     #translate messages
     subjectTranslated = translateMessage(subject, langIn)
     bodyTranslated = translateMessage(body, langIn)

#email sender---------------------------------

try:
    print("Sending email...")
    em = EmailMessage() #create instance of email
    em['From'] = email_sender
    em['To'] = email_receiver

    if (translateIn == 'y' or translateIn == 'Y'):
        em['subject'] = subjectTranslated
        em.set_content(bodyTranslated + "\n\nOriginal subject: " + subject + "\n\nOriginal body: " + body + "\n\n(Translated from English to " + finalLang + ")")
    else:
        em['subject'] = subject
        em.set_content(body)

    context  = ssl.create_default_context() 
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp: #connect to Gmail
        smtp.login(email_sender, email_password) 
        smtp.sendmail(email_sender, email_receiver, em.as_string())


    if (translateIn == 'y' or translateIn == 'Y'):
        print ("Email sent from " + email_sender + " to " + email_receiver + " translated from English to " + finalLang + "!")
    else:
        print ("Email sent from " + email_sender + " to " + email_receiver + "!")
except: #in case the user enters the wrong email/password
    print("The email or app password is incorrect and the email failed to send.")
