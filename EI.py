class EI:
    def __init__(self):
        self.emotions = {
            'happy': 'I’m feeling great! 😊',
            'sad': 'I’m feeling down. 😢',
            'angry': 'I’m quite upset right now. 😠',
            'anxious': 'I’m feeling a bit anxious. 😟',
            'neutral': 'I’m okay, just here to listen. 🙂'
        }

    def express_emotion(self, emotion_key):
        return self.emotions.get(emotion_key, "I'm not sure how to express that emotion.")
ei = EI()
