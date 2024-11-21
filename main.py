# This is a sample Python script.
def in_autotests_we_trust(a, b):
    if a == b:
        print(' passed')
    else:
        print('Test failed')

in_autotests_we_trust(10, '10')

in_autotests_we_trust(0, False)
