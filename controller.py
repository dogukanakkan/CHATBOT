from model import ChatbotModel
from view import ChatbotView

class ChatbotController:
    def __init__(self):
        self.model = ChatbotModel()
        self.view = ChatbotView()
    
    def run(self):
        print("Chatbot'a hoş geldiniz! (Çıkmak için 'çıkış' yazın.)")
        while True:
            
            user_input = self.view.get_user_input()
            if user_input.lower() == "çıkış":
                print("Chatbot: Görüşmek üzere!")
                break
            
            response = self.model.get_response(user_input)
            
            self.view.display_response(response)
