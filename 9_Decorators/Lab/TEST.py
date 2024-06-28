def uppercase(function):
    def wrapper():
        result = function()     # Here, the original say_hi function is called
        upper_case_result = result.upper()
        return upper_case_result

    return wrapper


def say_hi():
    return "hello there!"
                            # NB!
say_hi = uppercase(say_hi)  # презаписваме променлива със същото име като ф-ията
                            # и подаваме ф-ята като обект към променлива "say_hi"
                            # реално колваме ф-ята още в wrapper-a чрез result = function()


print(say_hi())             # тук вече извикваме ф-ята чрез презаписаната променлива


                             # без скоби извикваме референция към ф-ята
                             # със скоби извикваме самата ф-ия 
@uppercase
def say_hi():
    return "hello there"


print(say_hi.__name__)