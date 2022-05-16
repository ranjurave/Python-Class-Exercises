class Date:
    def __init__(self, date):
        self.date = date

    def get_date(self):
        return self.date

    @staticmethod
    def convert_date(date):
        return date.replace("/","-")

d1 = Date('17/05/2022')
print(d1.convert_date(d1.date))
print(d1.get_date())