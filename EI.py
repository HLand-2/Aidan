class EI:
    def __init__(self):
        self.emotions = {
            'happy': "I'm feeling great! 😊",
            'sad': "I'm feeling down. 😢",
            'angry': "I'm quite upset right now. 😠",
            'anxious': "I'm feeling a bit anxious. 😟",
            'neutral': "I'm okay, just here to listen. 🙂"
        }

        self.positive_words = ['happy', 'great', 'good', 'awesome', 'love', 'like', 'wonderful', 'amazing', 'thanks', 'thank', 'please', 'friend', 'fun', 'glad', 'enjoy']
        self.negative_words = ['sad', 'bad', 'hate', 'angry', 'upset', 'terrible', 'horrible', 'awful', 'worst', 'annoying', 'stupid', 'mean', 'boring']
        self.anxious_words = ['worried', 'anxious', 'nervous', 'scared', 'afraid', 'stress', 'panic', 'fear', 'concern']

    def express_emotion(self, emotion_key):
        return self.emotions.get(emotion_key, "I'm not sure how to express that emotion.")

    def analyze_emotion(self, text):
        """Analyze the emotion of a text input and return an emotion key."""
        words = text.lower().split()
        pos = sum(1 for w in self.positive_words if w in words)
        neg = sum(1 for w in self.negative_words if w in words)
        anx = sum(1 for w in self.anxious_words if w in words)
        if anx > 0:
            return 'anxious'
        elif neg > pos:
            if any(w in words for w in ['angry', 'hate', 'upset', 'annoying', 'stupid', 'mean']):
                return 'angry'
            return 'sad'
        elif pos > neg:
            return 'happy'
        return 'neutral'

ei = EI()
