import random, data, EI, cm

class AI:
    def __init__(self, name):
        self.knowledge_base = {
            "editoplit": {
                "jokes": [],
                "chat-info": {}
            }
        }
        self.emotions = data.feelings
        self.name = name
        self.jokes = self.knowledge_base["editoplit"]["jokes"]
        self.chat_info = self.knowledge_base["editoplit"]["chat-info"]
        self.jcount = 0
    def learn(self, topic, information):
        self.knowledge_base[topic] = information
    def recall(self, topic):
        return self.knowledge_base.get(topic, "I don't know about that.")
    def chat(self, user_input: str = "hello"):
        # Simple response generation based on keywords
        u = user_input.lower()
        if "hello" in u or "hi" in u:
            print("Hello! How can I assist you today?")
        elif "help" in u:
            print("Sure! What do you need help with?")
        elif "joke" in u:
            if "i" in u:
                j1 = input("Tell it to me.\n").lower()
                if "knock knock" in j1:
                    self.jokes.append(["Knock Knock."])
                    self.jokes[self.jcount].append("Who's there?")
                    self.jokes[self.jcount].append(input("Who's there?\n"))
                    self.jokes[self.jcount].append(input(self.jokes[self.jcount][2] + " who?\n"))
                    self.jcount += 1
            else:
                if self.jokes == []:
                    print("Sorry, but I don't know any jokes.\n Please tell me some.")
                else:
                    joke = random.choice(self.jokes)
                    if joke[0] == "Knock Knock.":
                        print(joke[0])
                        input(joke[1] + "\n")
                        print(joke[2])
                        input(joke[2] + " who?\n")
                        print(joke[3])
        elif "how" in u and ("feel" in u or "emotion" in u):
            for emotion, response in self.emotions.items():
                print(f"  {emotion}: {response}")
        elif "bye" in u or "goodbye" in u:
            print("Goodbye! Have a great day!")
        else:
            print("I'm not sure how to respond to that. Can you try again?")

ai = AI("Aidan")
cm.copy_instance_data(EI.ei, ai)
while True:
    ai.chat(input())
