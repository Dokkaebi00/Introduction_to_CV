# if filter is even number this cant run
img = [[1,2,3,4,5,6],[4,5,6,7,8,9], [7,8,9,1,2,3], [1,2,3,4,5,6],[4,5,6,7,8,9], [7,8,9,1,2,3]]
filter = [[1,2,3], [4,5,6], [7,8,9]]
# get the sub-matrix to multiply with the filter
def getMatrix (img, filter):
    # get width, heigth of the filter 
    filter_heigth = len(filter)
    filter_width = len(filter[0])
    # get width, heigth of the image
    heigth = len(img)
    width = len(img[0])
    # constant variable to ignore the excess of the image that dont fit with the filter (filter have odd size 2k+1)
    k = int (((len(filter[0]) - 1) / 2))
    # variable to store the result
    result_filter = 0 # calculate
    re = []
    count0 = 0 # variable to store the current column position of the filter
    count1 = 0 # variable to store the current row position of the filter
    count3 = 0 # variable to store the current position of the result 
    for i in range (k, (width - k)):
        re.append ([])
        for j in range (k, (heigth - k)):
            result_filter = 0
            for m in range (i - k, i + k + 1):
                for n in range (j - k, j + k + 1):
                    result_filter += img[m][n] * filter[count1][count0]
                    count0 += 1
                    if (count0 == len(filter[0])):
                        count1 += 1
                        count0 = 0
                    if (count1 == len(filter[0])):
                        count1 = 0
            re[count3].append (result_filter)
        count3+=1
    print (re)
getMatrix (img, filter)