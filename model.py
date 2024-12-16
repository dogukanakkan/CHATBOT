class ChatbotModel:
    def __init__(self):
        
        self.database = {
            "Merhaba": "Merhaba! Size nasıl yardımcı olabilirim?",
            "Nasılsın?": "Ben bir yapay zeka chatbot'um, hep iyiyim!",
            "Teşekkür ederim": "Rica ederim! Başka bir sorunuz var mı?",
        }
    
    def get_response(self, user_input):
        
        return self.database.get(user_input, "Üzgünüm, bunu anlayamadım.")