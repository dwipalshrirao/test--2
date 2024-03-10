input_dict = {"abc":{"def":{"ghi":{"jkl":{"mno":{"pqr":{"stu":{"vwx":{"yz":"you are finally here !!!"}}}}}}}}}

output = {}
def recursive_func(input_d, values_of=None):

    for key, value in input_d.items():
        if not isinstance(value, dict):
            output[key] = [value]
            return 
        if not values_of:
            output[key] = [k for k, v in value.items()]
            values_of = key
        else:
            output[values_of] = output.get(values_of,[]) + [k for k, v in value.items()]

        return recursive_func(value, values_of)


recursive_func(input_dict)
print("output:- " , output)
