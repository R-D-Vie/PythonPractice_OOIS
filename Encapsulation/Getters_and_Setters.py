class Phone:
  def __init__(self, model, storage, megapixels):
    self._model = model
    self._storage = storage
    self._megapixels = megapixels
    
  def get_model(self):
    return self._model

  def get_storage(self):
    return self._storage

  def get_megapixels(self):
    return self._megapixels
  
  def set_model(self, new_model):
    self._model = new_model
  
  def set_storage(self, new_storage):
    self._storage = new_storage

  def set_storage(self, new_megapixels):
    self._megapixels = new_megapixels


 
my_phone = Phone("iPhone", 256, 12)
print(my_phone.get_model())
my_phone.set_model("Galaxy S20")
print(my_phone.get_model())