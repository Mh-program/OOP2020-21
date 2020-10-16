# course: Object-oriented programming, year 2, semester 1
# academic year: 2020-21
# author: B. Schoen-Phelan
# date: Oct 2020
# purpose: Lab 4

class WordCloud:

    # initialises everything
    # everything gets kicked off here
    def __init__(self):
        self.my_dict = self.create_dict()
        # you might like to run the following line only
        # if there wasn't a problem creating the dictionary
        self.create_html(self.my_dict)

    # this function creates the actual html file
    # takes a dictionary as an argument
    # it helps to multiply the key/occurance of word number with 10
    # in order to get a decent size output in the html
    def create_html(self, the_dict):
        fo = open("output.html", "w")
        fo.write('<!DOCTYPE html>\
            <html>\
            <head lang="en">\
            <meta charset="UTF-8">\
            <title>Tag Cloud Generator</title>\
            </head>\
            <body>\
            <div style="text-align: center; vertical-align: middle; font-family: arial; color: white; background-color:black; border:1px solid black">')

        fo.write('<span style="font-size: 20px"> HELLO </span>')
        fo.write('<span style= "font-size: 10px"> fathers those </span ')
        fo.write('<span style= "font-size: 15px"> conceived </span')
        fo.write('<span style= "font-size: 10px"> bought all battlefield portion met </span')
        fo.write('<span style= "font-size: 15px"> rather </span')
        fo.write('<span style="font-size: 25px"> dedicated </span>')
        fo.write('<span style="font-size: 10px"> forget endure consecrate </span>')
        fo.write('<span style="font-size: 15px"> devotion </span>')
        fo.write('<span style="font-size: 10px"> score whether poor forth </span>')
        fo.write('<span style="font-size: 15px"> us </span>')
        fo.write('<span style="font-size: 5px"> nobly </span>')
        fo.write('<span style="font-size: 10px"> be </span>')
        fo.write('<span style="font-size: 5px"> liberty </span>')
        fo.write('<span style="font-size: 25px"> a </span>')
        fo.write('<span style="font-size: 5px"> proper god </span>')
        fo.write('<span style="font-size: 10px"> is </span>')
        fo.write('<span style="font-size: 8px"> living </span>')
        fo.write('<span style="font-size: 10px"> honored unfinished </span>')
        fo.write('<span style="font-size: 12px"> from </span>')
        fo.write('<span style="font-size: 8px"> with</span>')
        fo.write('<span style="font-size: 10px"> not </span>')
        fo.write('<span style="font-size: 30px"> here </span>')
        fo.write('<span style="font-size: 10px"> sense or </span>')
        fo.write('<span style="font-size: 30px"> and </span>')


        fo.write('</div>\
            </body>\
            </html>')

        fo.close()

        file = open("gettisburg.txt", "r")
        for line in file:
            word = line.split()
            print(word)
        file.close()

    # creates the dictionary containing the word itself
    # and how often it occurs in a sentence
    # makes a call to add_to_dict where the dictionary
    # is actually populated
    # returns a dictionary
    def create_dict(self):
        my_dict = {
            "1": "fathers",
            "2": "battlefield",
            "3": "dedicated",
            "5": "conceived",
            "6": "honored",
            "7": "living",
            "8": "god",
        }

        print(my_dict)

        b = my_dict.get("2")
        print(b)

        if "1" in my_dict:
            print("yes")

        for word in my_dict:
            print(word)

        print(len(my_dict))


        return my_dict

    # helper function that is called from
    # create_dict
    # receives a word and a dictionary
    # does the counting of the key we are at and adds 1
    # if this word already exists. Otherwise sets the
    # word occurance counter to 1
    # returns a dictionary
    def add_to_dict(self, word, the_dict):


        return the_dict


wc = WordCloud()
