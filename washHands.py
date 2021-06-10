N=7
nM=9

def wash_hands(N,nM):
    min = int((N*21*30*nM)/60)
    sec = ((N*21*30*nM))%(24*3600)
    return f'{min} minutes and {sec} seconds'

print(min, ' minutes and', sec, ' seconds')


N=7
nM=9

def wash_hands(N,nM):
    x = int((N*21*30*nM)/60)
    y = (N*21*30*nM) % (24*3600)
    return f'{x} minutes and {y} seconds'




