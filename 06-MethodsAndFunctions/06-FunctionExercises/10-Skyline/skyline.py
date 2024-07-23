def myfunc(input_str):
    output_str = ''

    for (index, character) in enumerate(input_str):
        if index % 2 == 0:
            output_str += character.upper()
        else:
            output_str += character.lower()

    return output_str

print(myfunc('Anthropomorphism'))