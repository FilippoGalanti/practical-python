def bouncy (height, bounces):
    
    bouncesNumber = 0
    maxHeight = height
    
    while bouncesNumber <= bounces:
        
        maxHeight = maxHeight * (0.6)
        bouncesNumber += 1
        print(round(maxHeight,2), 'meters.')

    return 'ended'

bouncy(100,10)
