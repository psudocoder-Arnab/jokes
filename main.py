import pyjokes as PJ
import pyttsx3

joke_maker = PJ.get_joke()


def joke():
    print(joke_maker)
    engine = pyttsx3.init()
    engine.say(joke_maker)
    engine.runAndWait()
    engine.stop()


joke()
