from dataclasses import dataclass

@dataclass()
class Product:

    # atributos
    id: int
    name: str
    price: float
    stock: int

    # aumentar qtd itens estoque
    def increase_stock(self, stock_to_add: int):
        self.check_positive_number(stock_to_add)
        self.stock: int = self.stock + stock_to_add

    # diminuir qtd itens estoque
    def decrease_stock(self, stock_to_reduce: int):
        self.check_positive_number(stock_to_reduce) 
        new_stock = self.stock - stock_to_reduce
        self.check_negative_stock(new_stock)
        self.stock = self.stock - stock_to_reduce

    def check_positive_number(self, value):
        if value <= 0:
            raise Exception("Number must be positive")
        
    # valida pq n pode ser negativo o estoque
    def check_negative_stock(self, value):
        if value < 0:
            raise Exception("Stock must be greater than or equal to 0")