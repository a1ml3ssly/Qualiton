import json
import base64


class CaptchaHandler:
    __author__ = "Nitzan Bachar"
    __version__ = "1.0.0"
    captcha_list = ['tatio', 'conse', 'ender', 'incid', 'uteni', 'aliqu', 'etdol', 'offic', 'eatna', 'dolor', 'tempo',
                    'irure',
                    'quisn', 'molly', 'culpa', 'itasx', 'eufug', 'sinto', 'ipsum', 'excep', 'paria', 'zaaze', 'commo',
                    'sitam',
                    'osrud', 'borum', 'deser', 'nulla', 'duist', 'essec', 'oiden', 'exerc', 'admin', 'labor', 'ullam',
                    'nonpr',
                    'sunti', 'venia', 'autez', 'caeca', 'elita', 'uptat', 'seddo', 'nisiu', 'lorem', 'cupid', 'magna',
                    'invol',
                    'estla', 'repre', 'adipi', 'eiusm', 'velit', 'exear', 'animi']
    captcha_dict = dict()

    def __init__(self):
        self.json_file_name = 'data.json'
        print(len(self.captcha_list))

    def generate_pictures_from_base64(self):
        with open(self.json_file_name) as json_file:
            data = json.load(json_file)
            index = 1
            for item in data:
                base64_code = item.split(",")
                print(base64_code[1])
                base64_img_bytes = base64_code[1].encode('utf-8')
                with open('images\\decoded_image' + str(index) + '.png', 'wb') as file_to_save:
                    decoded_image_data = base64.decodebytes(base64_img_bytes)
                    file_to_save.write(decoded_image_data)
                index += 1

    def combine_list_with_json(self):
        index = 0
        with open(self.json_file_name) as json_file:
            data = json.load(json_file)
            for item in data:
                data[item] = self.captcha_list[index]
                index += 1
        self.captcha_dict = data

    def print_dict(self):
        for item in self.captcha_dict:
            print(item)
            print(self.captcha_dict[item])
            print("----------")

    def save(self):
        a_file = open("../Utilities/finished_data.json", "w")
        json.dump(self.captcha_dict, a_file)
        a_file.close()


a = CaptchaHandler()
a.combine_list_with_json()
a.print_dict()
a.save()
