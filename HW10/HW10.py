class Flower:
    def __init__(self, type_flower, life_time, cost):
        self.type_flower = type_flower
        self.life_time = life_time
        self.cost = cost
    def info(self):
        return print (f"{self.type_flower}, "
                      f"{self.life_time} days, {self.cost}$.")
class Bouquet:
    def __init__(self, flowers_in_bouquet):
        self.flowers_in_bouquet = flowers_in_bouquet
        flowers_type = [i.type_flower for i in self.flowers_in_bouquet]
        print(f"Bouquet with: {', '.join(flowers_type)}")
    def life_time_flower(self):
        flowers_list = [i.life_time for i in self.flowers_in_bouquet]
        wilting_period = sum(flowers_list) // len(flowers_list)
        print(f"The bouquet will fade in {wilting_period} days")
        return wilting_period

    def sort(self):
        sort = [i.cost for i in self.flowers_in_bouquet]
        sort_cost = sorted(sort)
        print(f"Sorted Flowers by price in a bouque: "
              f"{str(sort_cost).strip('[]')}")

    def chek_flower(self, find_flower):
        if find_flower in flowers:
            print(f"Yes! {find_flower.type_flower} in bouquet!")
        else:
            print("No! Go away!")


rose_flower = Flower("rose", 8, 1)
rose_flower.info()
chamomie_flower = Flower("chamomile", 4, 7)
chamomie_flower.info()
tulip_flower = Flower("tulip", 7, 2)
tulip_flower.info()

flowers = [rose_flower, rose_flower, chamomie_flower]

bouquet = Bouquet(flowers)

bouquet.life_time_flower()
bouquet.sort()
bouquet.chek_flower(rose_flower)