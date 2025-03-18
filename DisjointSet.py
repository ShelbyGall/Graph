# %%
class DisjointSet:

    def __init__(self, items: list):
        self.parent = dict(zip(items,items))
        self.size = dict(zip(items, [1] * len(items)))

    def find(self, item):
        root = self.parent[item]
        if self.parent[root] != root:
            self.parent[item] = self.find(root)
            return self.parent[item]
        
        return root
    
    # TODO: rewrite union for the UnionBySize optmization using the size field
    def union(self, item1, item2):
        par1 = self.find(item1)
        par2 = self.find(item2)

        self.parent[par1] = par2
#%%



# %%
