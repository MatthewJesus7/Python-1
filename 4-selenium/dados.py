import json

# Definindo uma classe para representar um Card
class Card:
    def __init__(self, link, title, price, totalPrice, background_image):
        self.link = link
        self.title = title
        self.price = price
        self.totalPrice = totalPrice
        self.background_image = background_image

    def to_dict(self):
        # Converte o objeto Card para um dicionário para facilitar a exportação para JSON
        return {
            "link": self.link,
            "title": self.title,
            "price": self.price,
            "totalPrice": self.totalPrice,
            "background_image": self.background_image
        }

# Criando uma lista de cards
cards = [
    Card("link", "titulo", "12x R$93,94", 999.99, "image1.jpg"),
]

# Convertendo os cards para uma lista de dicionários
cards_data = [card.to_dict() for card in cards]

# Convertendo a lista de dicionários para JSON
cards_json = json.dumps(cards_data, ensure_ascii=False, indent=4)

# Exibe o JSON
# print(cards_json)