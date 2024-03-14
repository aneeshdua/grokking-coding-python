memoize = {}
def SegmentString(input, lookup):
    # for i in range(len(input)):
    #     prefix = input[:i]
    #     if prefix in lookup.keys():
    #         suffix = input[i:]
    #         if prefix in lookup.keys():
    #             return prefix + " " + suffix
    ######################################################################
    
    # if input in lookup:
    #     return input
    # for i in range(len(input)):
    #     prefix = input[:i]
    #     if prefix in lookup:
    #         segmented = SegmentString(input[i:],lookup)
    #         if segmented:    
    #             return prefix + segmented
    
    # return None
    ######################################################################
    
    if input in lookup:
        return input
    elif input in memoize:
        return memoize[input]
    for i in range(len(input)):
        prefix = input[:i]
        if prefix in lookup:
            segmented = SegmentString(input[i:],lookup):
            if segmented:    
                return prefix + segmented

    memoize[input] = None
    return None
