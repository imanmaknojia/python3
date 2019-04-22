  
import speech_recognition as sr 
  

r = sr.Recognizer() 
    
with sr.Microphone() as source: 
    
    print ("Say Something")
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source,timeout=3,phrase_time_limit=3) 
          
    try: 
        text = r.recognize_google(audio) 
        print ("you said: ") + text 
      
    
      
    except sr.UnknownValueError: 
        print("Google Speech Recognition could not understand audio") 
      
    except sr.RequestError as e: 
        print("Could not request results from Google  Speech Recognition service; {0}".format(e))
                                 