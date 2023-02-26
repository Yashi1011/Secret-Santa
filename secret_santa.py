import random 

def read_names(file_name):
    names = file_name.read().replace(' ', '').split('\r\n')
    names = list(filter(('').__ne__, names))
    print(names)
    return names

def file_write_list(result):
    with open('result.txt', 'wt') as myfile:
        [myfile.write('%s - %s\n' % (i['from'], i['to'])) for i in result]

def file_write_dict(result):
    with open('result.txt', 'wt') as myfile:
        [myfile.write('%s - %s\n' % (key, value)) for key, value in result.items()]

def shuffle_names(names):
    random.shuffle(names)
    return names

def secret_santa_to_dict(names):
    givers, result = set(names), {}
    for name in names:
        givers.discard(name)
        receiver = random.choice(list(givers))
        givers.remove(receiver)
        givers.add(name)
        result[name] = receiver
    return result

def secret_santa_to_list(names):
    givers, result = set(names), []
    for name in names:
        givers.discard(name)
        receiver = random.choice(list(givers))
        givers.remove(receiver)
        givers.add(name)
        result.append({'from': name, 'to': receiver})
    return result
