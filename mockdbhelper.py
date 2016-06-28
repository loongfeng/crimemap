class MockDBHelper:
  def connect(self,database="crimemap"):
    pass
  def get_all_inputs(self):
    return []
  def add_input(self,data):
    pass
  def clear_all(self):
    pass
  def add_crime(self,category,date,latitude,longtitude,description):
    pass
  def get_all_crimes(self):
    return [{'latitude':-33.301304,
    'longitude':26.523355,
    'date':"2016-05-23",
    'category':'mugging',
    'description':"mock description"
    }]
