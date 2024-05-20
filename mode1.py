from landsites import Land
from data_structures import bst

class Mode1Navigator:
    """
    Student-TODO: short paragraph as per
    https://edstem.org/au/courses/14293/lessons/46720/slides/318306
    """

    def __init__(self, sites: list[Land], adventurers: int) -> None:
        """
        Student-TODO: Best/Worst Case
        """
        self.sites = sites
        self.adventurers = adventurers
        self.tree = bst.BinarySearchTree()

        for i in range(len(sites)):
            key = sites[i].get_guardians() / sites[i].get_gold()
            self.tree.__setitem__(key, sites[i])
        



    def select_sites(self) -> list[tuple[Land, int]]:
        """
        Student-TODO: Best/Worst Case
        """

        land_sites = []
        adventurer_num = self.adventurers
        iterator = bst.BSTInOrderIterator(self.tree.root)

        try:
            while True:
                node = next(iterator)
                site = node.item

                if site.get_gold() > 0 and site.get_guardians() > 0:
                    if site.get_guardians() > adventurer_num:
                        adventurer = adventurer_num
                        land_sites.append((site, adventurer))
                        break
                    else:
                        adventurer = min(adventurer_num, site.get_guardians())
                        land_sites.append((site, adventurer))
                        adventurer_num -= adventurer

                if adventurer_num <= 0:
                    break

        except StopIteration:
            pass

        return land_sites
            




        

    def select_sites_from_adventure_numbers(self, adventure_numbers: list[int]) -> list[float]:
        """
        Student-TODO: Best/Worst Case
        """

        gold_list = []

        for adventurer in adventure_numbers:
            total_gold = 0
            traversal = bst.BSTInOrderIterator(self.tree.root)

            try:
                while adventurer > 0:
                    node = next(traversal)
                    site = node.item

                    if site.get_gold() > 0 and site.get_guardians() > 0:
                        if adventurer >= site.get_guardians():
                            reward = min(site.get_gold(), (site.get_guardians() * site.get_gold()) / site.get_guardians())
                            total_gold += reward
                            adventurer -= site.get_guardians()
                        else:
                            reward = min((adventurer * site.get_gold()) / site.get_guardians(), site.get_gold())
                            total_gold += reward
                            adventurer = 0

            except StopIteration:
                pass 

            gold_list.append(total_gold)

        return gold_list

            

            


    def update_site(self, land: Land, new_reward: float, new_guardians: int) -> None:
        """
        Student-TODO: Best/Worst Case
        """
        
        self.tree.__delitem__(land.guardians / land.gold)
        land.gold = new_reward
        land.guardians = new_guardians
        self.tree.__setitem__(land.guardians / land.gold, land)





if __name__ == "__main__":
    print(min(1,3))