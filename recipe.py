class Recipe:
  def __init__(self, infos):
    self.name = infos["name"]
    self.content = infos["content"]

  def get_id(self, id):
    self.id = id
