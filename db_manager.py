import psycopg2
import models
import inspect

class Engine(object):
    def __init__(self, dbname=None, host=None, user=None, password=None):
        self.dbname = dbname
        self.host = host
        self.user = user
        self.password = password

    def connect(self):
        try:
            self.conn = psycopg2.connect(dbname=self.dbname,
                    user=self.user, host=self.host, password=self.password)
            self.cur = self.conn.cursor()
        except:
            raise Exception('Failure to connect!')

    def make_tables(self):
        """
        Try to create a list of dicts of all the objects in models.py
        to be iterated through in the next step
        """
        try:
            model_list = [m for m in inspect.getmembers(models, inspect.isclass) if m[1].__module__ == 'models']
            def create_model_dict_list(model_list):
                model_dict_list = list()
                for x, y in model_list:
                    all_props = vars(y)
                    prop_dict = dict()
                    for key in all_props.keys():
                        if not key.startswith('__'):
                            prop_dict[key] = all_props[key]
                    model_dict_list.append({'name': x, 'obj': y, 'properties': prop_dict})
                return model_dict_list
            self.models = create_model_dict_list(model_list)
        except:
            raise Exception('No models.py!')
