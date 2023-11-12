from transformers import pipeline
import webbrowser
import random

#user interacts with prototype chatbot

def isHappyOrSad(s):
    output = classifier(s)
    #print(output)
    if output[0]['label'] == 'NEGATIVE':
        return 'sad'
    elif output[0]['label'] == 'POSITIVE':
        return 'happy'
    return 'neutral'

if __name__ == "__main__":
    #transcriber = pipeline("text-generation")
    #in the future, we could generate responses to user inputs instead to having fixed responses from the flowchart

    classifier = pipeline("sentiment-analysis")

    responses = []
    
    responses.append(input("Hi! How are you feeling today? "))
    if isHappyOrSad(responses[-1]) == 'sad':
        responses.append(input("Oh no! What's going on? "))
        if isHappyOrSad(responses[-1]) == 'sad':
            responses.append(input((random.choice(["I'm sorry to hear that, I can't even imagine what that is like. ", "Thank you for opening up to me, it takes a lot of strength to do that. "]) + "Please elaborate on how you're feeling. ")).lower())
            if isHappyOrSad(responses[-1]) == 'happy' or (isHappyOrSad(responses[-1]) == 'sad' and "don't" in responses[-1] and ("know" in responses[-1] or "understand" in responses[-1])):
                seeTherapist = input("Would you like to see a therapist by any chance (y/n)? ").lower()
                if seeTherapist == "y":
                    webbrowser.open("https://www.google.com/search?q=therapist+near+me&rlz=1C1VIQF_enUS1037US1037&oq=therapis&gs_lcrp=EgZjaHJvbWUqBwgBEAAYjwIyBggAEEUYOTIHCAEQABiPAjIHCAIQABiPAjIHCAMQABiPAjIGCAQQRRg80gEIMzI3NWowajGoAgCwAgA&sourceid=chrome&ie=UTF-8")
                elif seeTherapist == "n":
                    print("I hope you feel better soon! Hang in there!")
            else:
                seeDepResources = input("Would you like to see some resources for depression (y/n)? ").lower()
                if seeDepResources == "y":
                    webbrowser.open("https://www.oprahdaily.com/life/health/a27507222/how-to-stop-being-sad")
                elif seeDepResources == "n":
                    print("I hope you feel better soon! Hang in there!")
    else:
        print("Congrats! Here's some cute cat videos to celebrate")
        webbrowser.open("https://youtu.be/hY7m5jjJ9mM?si=Awzgx8UdJSAJfHBm&t=13")

            


"""
How does a bastard, orphan, son of a whore
and a scotsman, dropped in the middle of a forggotten spot
in the carrieanbean imporbverished and something in squaler
grow up to be a hero and a scholar?

The ten dollar founding father without a father
got a lot farther by working a lot harder
by bein ggg a lot smarter a self-sstarter
by fourteen, they placed him in charge of a trading charter

adn every dday while slaves were being carted away
acrross the waves he struggled and kept his gaurd up
inside he was longing for womthing to vee a part of
a broher was ready to stesal bartor and borrow

then a hurrican came, decistation rained
my man saw his futture drip, dripping down the drain
put a pencil to he temple connected it to his gbrain
then hse wrote his first restrain, a testament to his pain

then the birds? started to come out saying this kid is insanem, man,
took a book collection just to send him to the mainlsand
something something something dont' forget from where you came
cause the worlds gonna know ur name, what's ur name man?

aledczxander hamilton
my name is alexander hamilront
theres a milliton thigsn i haven't done
buy just u wait, just u waittt

when he waas ten his father split, full of it
debt ridden, mother sidk half dead
soething thick air thick
and alex got better but his mother went quick

moved in with his cousin, the cousin commited suiceide
left him nothing with pride, nothing new insedie
wa  voice saying 'alex u gotta fend for urself
he started drinking and reading every book thats on the shelf

there was nothign left to do for something less astute
he woul'eve been dead of destite, nothing new
he started working, working for his late fathers landlord
drinking sugear can and all th ethigns he cna't afford

saving for a afutre somehting
iforgot the part
for a new land
in new york u can be a new man
in new york u can be a new man
in new york u can be a new man
in new york u can be a new man
ju st u wait
alexadner hamilton
just u waitttttt
what's ur name man
alexander hamilton


"""