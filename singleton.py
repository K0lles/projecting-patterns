class SingletonBase(type):
    _instances ={}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class DataBase(metaclass=SingletonBase):
    def __init__(self):
        self.table_amount = 0

    def create_table(self):
        self.table_amount += 1

    def delete_table(self):
        if self.table_amount > 0:
            self.table_amount -= 1
        else:
            raise ValueError("There is no connections")


if __name__ == "__main__":
    database1 = DataBase()
    database2 = DataBase()
    database1.create_table()
    database1.create_table()
    database2.delete_table()
    print(database1.table_amount)
    print(database2.table_amount)
