class QuerySelectBuilder:
    def __init__(self):
        self.select: list[str] = []
        self.source: str = ""
        self.joins: list[str] = []
        self.where: list[str] = []
    
    def __str__(self):
        if not self.select:
            return None
        if not self.source:
            return None
        ret = f"SELECT {', '.join(self.select)}"
        ret += f"\nFROM {self.source}\n"
        ret += '\n'.join(self.joins)
        ret += f"\nWHERE {' '.join(self.where)}\n"
            
        return ret
        
    def addSelect(self, table_name, *cols):
        for col in cols:
            self.select.append(f"{table_name}.{col}")
        if not self.source:
            self.source = table_name
            
    def addJoin(self, tab1, col1, tab2, col2):
        self.joins.append(f"JOIN {tab1} ON {tab1}{col1} == {tab2}{col2}")
        if not self.source:
            self.source = tab2
    
    def addWhere(self, condition, operator=""):
        self.where.append(f"{operator} {condition}")

if __name__ == '__main__':
    q = QuerySelectBuilder()
    q.addSelect("table1", "col1", "col2", "col3")
    q.addSelect("table2", "col1", "col2", "col3")
    q.addJoin("table1", "col2", "table2", "col2")
    q.addWhere("table1.col1 >= 0")
    q.addWhere("table1.col3 < 0", "AND")
    print(q)

            
        
