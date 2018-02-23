class Router:

  def __init__(self, controller):
    self.controller = controller
    self.running = True

  def run(self):
    print "Welcome to my PYTHON APP"
    while (self.running):
      self.display_menu()
      choice = raw_input(">> ")
      self.choice_action(int(choice))
      print "-------------------------"
    print "Bye !"

  def shut_down(self):
    self.running = False

  def display_menu(self):
    print "What's your choice ?"
    print "1. Display all your recipes"
    print "2. Add a recipe"
    print "0. Exit"
    print "----------------------------"

  def choice_action(self, action):
    if (action == 1):
      self.controller.list()
    elif (action == 2):
      self.controller.create()
    elif (action == 0):
      self.shut_down()
