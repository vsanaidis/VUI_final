import requests
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionGetJoke(Action):
    def name(self) -> str:
        return "action_tell_joke" #the name of the action to be called

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict) -> list:
        # sents a get request to the api to get the joke
        response = requests.get("https://official-joke-api.appspot.com/random_joke")
        # if the code is 200 (successfull) it returns the joke as assigned
        if response.status_code == 200:
            joke_data = response.json()
            joke = f"{joke_data['setup']} ... {joke_data['punchline']}"
        # if the code is not successfull...
        else:
            joke = "Oops! I couldn't fetch a joke right now."
        #sends the message back to the user by rasa's dispatcher
        dispatcher.utter_message(text=joke)
        return []
