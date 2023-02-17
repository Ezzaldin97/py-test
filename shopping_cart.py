from typing import List, Dict

class ShoppingCart:
    def __init__(self, max_size:int) -> None:
        self.items:List[str] = []
        self.max_size = max_size
    
    def add(self, item:str):
        if self.size() == self.max_size:
            raise OverflowError("Can not Add More items to Cart..")
        self.items.append(item)
    
    def size(self) -> int:
        return len(self.items)
    
    def get_items(self) -> List[str]:
        return self.items
    
    def get_total_price(self, price_map:Dict[str, float]):
        total = 0
        for item in self.items:
            total+=price_map.get(item)
        return total