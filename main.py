#test 

# we want to test this program for the first time, we need to have
# the winning condiditon, so that we may track our progress

class Bank:
  def __init__(self, name, code):
    self.name = name
    self._code = code
  def display_bank(self):
    print(f"Bank Name: {self.name}")
    print(f"Bank Code: {self._code}")

class CentralBank:
  def __init__(self):
    self.banks = [Bank]
    self.codes = [str]
  def add_bank(self, bank: Bank):
    if bank._code in self.codes:
      print(f"Bank with code {bank._code} already exists.")
    else:
      self.banks.append(bank)
      self.codes.append(bank._code)
  def display_all_banks(self):
    print('=============[]=============')
    for bank in self.banks:
      bank.display_bank()
      print('----------------------------')
    print('============================')


    

if __name__ == '__main__':
  bi = CentralBank()
  bi.add_bank(Bank('Bank Rakyat Indonesia', 'BRI'))
  bi.add_bank(Bank('Bank Mandiri', 'BMRI'))
  bi.add_bank(Bank('Bank Central Asia', 'BCA'))
  bi.display_all_banks()
  
  # print('test')



