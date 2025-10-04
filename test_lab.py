def type_convert(value):
    import string
    list_str_value = list(value)
    print(list_str_value)
    n_alphanumeric = 0
    n_valuecount = 0
    list_english_alphabet_string_lowercase = list(string.ascii_lowercase)
    if type(value)==string:
        while True:
            print([i for i in list_str_value])
            if list_english_alphabet_string_lowercase not in list_str_value:
                break
            if n_alphanumeric==26:
                n_alphanumeric = 0
            if list_str_value[n_valuecount] == list_english_alphabet_string_lowercase[n_alphanumeric]:
                list_str_value.remove(list_str_value[n_valuecount])
            print(list_str_value[n_valuecount]) 
            n_valuecount += 1
            n_alphanumeric += 1
    return ','.join(list_str_value)

my_value = '5u'
type_convert(my_value)
