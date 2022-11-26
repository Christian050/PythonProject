import pyttsx3 as tts

voice = tts.init()
female_voice = voice.getProperty('voices')
voice.setProperty('rate', 150)
voice.setProperty('voice', female_voice[1].id)

intro = 'Hello. Welcome to the FBN bank chat bot'
voice.say(intro)
voice.runAndWait()

response = input().capitalize()
if response == 'Hi':
    assistant_response = 'What can i do for you?'
    voice.say(assistant_response)
    voice.runAndWait()
    response2 = input()
    if response2 == 'Account Creation':
        assistant_response2 = 'Would you like me to direct you to the nearest branch?'
        voice.say(assistant_response2)
        voice.runAndWait()
        response3 = input("Yes/No\n").capitalize()
        if response3 == "Yes":
            assistant_response3 = 'Whats your location?'
            voice.say(assistant_response3)
            voice.runAndWait()
            response4 = input().capitalize()
            if response4 == 'Accra':
                assistant_response4 = 'The nearest branch is on ring road adjacent to the MTN Office'
                voice.say(assistant_response4)
                voice.runAndWait()
            else:
                assistant_response5 = 'Sorry the are no branches where you reside'
                voice.say(assistant_response5)
                voice.runAndWait()
        if response3 == 'No':
            assistant_response6 = 'Okay, download the FBN Bank app on google playstore or the apple app store' \
                                  'or open the FBN Bank webpage to create an account'
            voice.say(assistant_response6)
            voice.runAndWait()
assistant_done = 'Are you satisfied with the responses?'
voice.say(assistant_done)
voice.runAndWait()
response_done = input('Yes/No\n').capitalize()
if response_done == 'Yes':
    assistant_done2 = 'Thank you for using FBN Bank chat bot. Goodbye'
    voice.say(assistant_done2)
    voice.runAndWait()
    voice.stop()
else:
    assistant_done3 = 'Please visit the nearest FBN branch or click this link to direct you to the FBN bank website.' \
                      ' Goodbye'
    voice.say(assistant_done3)
    voice.runAndWait()
    voice.stop()
    link = 'https://www.fbnbankghana.com'
    print(link)
