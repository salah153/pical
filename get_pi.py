import random

def do_stuff(num_samples):
    list_stuff = []
    for i in range(num_samples):
        list_stuff.append(random.uniform(0, 1))
    return list_stuff

def get_c(s1, s2):
    c = 0
    for i in range(len(s1)):
        if (s1[i]**2 + s2[i]**2) < 1:
            c += 1.0;
    return c

if __name__=="__main__":
    num_samples = 1000

    stuff_1 = do_stuff(num_samples)
    stuff_2 = do_stuff(num_samples)

    c = get_c(stuff_1, stuff_2)

    print(4 * c/num_samples)



