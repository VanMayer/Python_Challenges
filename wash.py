def wash_hands(N,nM):
    minutes = 0
    seconds = 0
    time = (N*21*30*nM)
    minutes = time //60
    seconds = time - minutes*60
    return f'{minutes} minutes and {seconds} seconds'

print(wash_hands(7,9))
