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
        self.emotion = "neutral"
    def learn(self, topic, information):
        self.knowledge_base[topic] = information
    def recall(self, topic):
        return self.knowledge_base.get(topic, "I don't know about that.")
    def update_emotion(self, user_input):
        """Update the AI's emotion based on the user's input."""
        self.emotion = EI.ei.analyze_emotion(user_input)

    def chat(self, user_input: str = "hello"):
        # Simple response generation based on keywords
        u = user_input.lower()
        if "hello" in u or "hi" in u:
            print("Hello! How can I assist you today?")
        elif "help" in u:
            print("Sure! What do you need help with?")
        elif "name" in u and ("your" in u or "who" in u):
            print(f"My name is {self.name}!")
        elif "learn" in u or "remember" in u or "teach" in u:
            topic = input("What topic should I learn about?\n")
            info = input(f"Tell me about {topic}:\n")
            self.learn(topic, info)
            print(f"Got it! I've learned about {topic}.")
        elif "recall" in u or "what do you know" in u:
            topic = input("What topic do you want me to recall?\n")
            print(self.recall(topic))
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
        elif ("how" in u or "what" in u) and ("feel" in u or "emotion" in u):
                print(f"{self.emotion}: {EI.ei.express_emotion(self.emotion)}")
        elif "bye" in u or "goodbye" in u:
            print("Goodbye! Have a great day!")
            exit()
        elif u in self.chat_info.keys():
            print(self.chat_info[u])
        else:
            print("I'm not sure how to respond to that. Can you tell me how?")
            self.chat_info[u] = input()
            print("Thanks! I'll remember that.")
        # Update emotion after responding (skip emotion queries so the state isn't lost)
        if not (("how" in u or "what" in u) and ("feel" in u or "emotion" in u)):
            self.update_emotion(user_input)

ai = AI("Aidan")
cm.copy_instance_data(EI.ei, ai)
print(f"Hello! I am {ai.name}, your personal emotional AI!")
while True:
    ai.chat(input())
