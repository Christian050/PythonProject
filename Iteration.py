import random



class CoolEmoticonGenerator(object):
    """Docstring for CoolEmoticonGenerator"""
    strings = "!@#$^&*_=+?/,.:;"
    grouped_strings = [("(",")"), ("<", ">"), ("([","]"),("{","}")]

    def create_emoticon(self, grp: object) -> object:   # Actual method that creates the emoticon"""
        face_strings_list = [random.choice(self .strings)for _ in range(3)]
        face_strings = "".join(face_strings_list)
        emoticon = (grp[0], face_strings, grp[1])
        emoticon = "".join(emoticon)
        return emoticon


    def __iter__(self):
     #returns the self object to be accessed by the for loop
     return self

    def __next__(self):         # Returns the next emoticon indefinitely"""
        grp = random.choice(self.grouped_strings)
        return self.create_emoticon(grp)






from Main import CoolEmoticonGenerator
g = CoolEmoticonGenerator()
print([next(g) for _ in range(5)])

# iterator with the while loop

guests = {"Luffy","Zorro","Sanji","Ike","Chika","Solomon","Issa","Amarachi","Oromesele","Shola","Nana","Afosa","Rudolph","Philip","Benedict","Moses","Sam"}
            # same as guest.__iter__()
guest_iterator = iter(guests)
while True:
             try:
                 # same as guest__iterator.__next__()
                 guest = next(guest_iterator)
                 print(guest)
             except StopIteration as e: break
