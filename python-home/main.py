class BookDto:
  class BookRequestDto:
    def __init__(self, title, price):
      self.title = title
      self.price = price
      
  class BookResponse:
    def __init__(self, message, data):
      self.message = message
      self.data = data
      
    
request = BookDto.BookRequestDto(title="Test", price=12000)
response = BookDto.BookResponse(message="Success", data={"book": "Test Book"})

print(request)
print(response)

clear