def hello(lastname:str,middlename:str,firstname:str="World")->None:
    """This is Discription of hello() method
    """
    print(f'Hello {firstname} {middlename} {lastname}!')


# def hello(name="World"):
#     print(f'Hello {name}!')

#hello()

#positional args
#hello("Saxena","K","Piyush")

#keyword args

#hello(middlename="K",lastname="Saxena")

#Args parameter
# *args Arguments


def hello(*args):
    for i in range(len(args)):
        print(f'index {i} is having values as {args[i]}')
#hello()
#hello("Piyush")
#hello("Piyush","Saxena")
#hello("Piyush","K","Saxena")

#Keyword parameters
# **kwargs Arguments

def hello(**kwargs):
    for i, key in enumerate(kwargs):
        print(f'{i} index has key as "{key}" and value as "{kwargs[key]}"')

hello(firstname="Piyush",lastname="Saxena")