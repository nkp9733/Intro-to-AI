import inspect
import sys
from math import log

statistic = []
stat_ar = []
stat_avg_down_len = []

'''
Raise a "not defined" exception as a reminder 
'''
def _raise_not_defined():
    print "Method not implemented: %s" % inspect.stack()[1][3]
    sys.exit(1)


'''
Extract 'basic' features, i.e., whether a pixel is background or
forground (part of the digit) 
'''
def extract_basic_features(digit_data, width, height):
    features=[]
    for i in range(0,len(digit_data)):
        for j in range(0,len(digit_data[i])):
            if digit_data[i][j] == 0:
                features.append(0)
            else:
                features.append(1)
    #_raise_not_defined()
    #print(digit_data)
    #print(features)
    return features

'''
Extract advanced features that you will come up with 
'''
def extract_advanced_features(digit_data, width, height):
    features=[]
    #print digit_data
    '''
    top = -1
    bottom = -1
    left = 100
    right = -1
    for i in range(0,len(digit_data)):
        if 1 in digit_data[i] or 2 in digit_data[i]:
            top = i-1
            break
    for j in range((len(digit_data)-1),0,-1):
        if 1 in digit_data[j] or 2 in digit_data[j]:
            bottom = j
            break
    for k in range(0,len(digit_data)):
        for l in range(0,len(digit_data[k])):
            if digit_data[k][l] == 1 or digit_data[k][l] == 2:
                if l < left:
                    left = l-1
                if l > right:
                    right = l
    w = right - left
    h = bottom - top
    aspect_ratio = float(w)/h
    #print(aspect_ratio)
    features.append(aspect_ratio)  
    '''
    for m in range(0,len(digit_data)):
        for n in range(0,len(digit_data)):
            counter = 0
            if digit_data[m][n] == 1 or digit_data[m][n] == 2:
                if m == len(digit_data)-1:
                    features.append(1)
                    continue
                z = m
                while digit_data[z][n] == 1 or digit_data[z][n] == 2:
                    if z == len(digit_data)-1:
                        break
                    counter+=1
                    z+=1
            features.append(counter)
            

    #print features
    #_raise_not_defined()
    return features

'''
Extract the final features that you would like to use
'''
def extract_final_features(digit_data, width, height):
    features=[]
    # Your code starts here 
    # You should remove _raise_not_defined() after you complete your code
    # Your code ends here 
    _raise_not_defined()
    return features

'''
Compupte the parameters including the prior and and all the P(x_i|y). Note
that the features to be used must be computed using the passed in method
feature_extractor, which takes in a single digit data along with the width
and height of the image. For example, the method extract_basic_features
defined above is a function than be passed in as a feature_extractor
implementation.

The percentage parameter controls what percentage of the example data
should be used for training. 
'''
def compute_statistics(data, label, width, height, feature_extractor, percentage=100.0):
    
    dec = percentage/100.0
    num_count = [0,0,0,0,0,0,0,0,0,0]
    total_count = 0
    prior_prob = [0,0,0,0,0,0,0,0,0,0]
    for n in range(0,len(label)):
        num_count[label[n]]+=1
        total_count+=1
        prior_prob[label[n]] = float(num_count[label[n]])/total_count
    print(num_count)
    print(total_count)
    print(prior_prob)
    '''
    c = []
    count = []
    total = len(data)
    conditional_prob = []

    for a in range(0,10):
        for b in range(0,(width*height)):
            c.append(0)
        count.append(c)
        conditional_prob.append(c)

    for i in range(0,int(dec*len(data))):
        lbl = label[i]
        feature = extract_basic_features(data[i], width, height)
        for j in range(0, len(feature)):
            if feature[j] == 1:
                count[lbl][j]+=1
    print count
    for x in range(0,len(count)):
        for y in range(0,len(count[x])):
            conditional_prob[x][y] = float(count[x][y]+1)/(num_count[x]+1)
    #print conditional_prob

    global statistic
    for k in range(0,len(prior_prob)):
        prior = log(prior_prob[k])
        temp = 0
        for l in range(0,len(conditional_prob[0])):
            temp += log(conditional_prob[k][l])
        statistic.append(prior+temp)
    print statistic
  
    sum_ar = [0,0,0,0,0,0,0,0,0,0]
    aspect_ratios = [0,0,0,0,0,0,0,0,0,0]
    for i in range(0,int(dec*len(data))):
        lbl = label[i]
        feature = extract_advanced_features(data[i], width, height)
        sum_ar[lbl] = sum_ar[lbl]+feature[0]
        aspect_ratios[lbl] = sum_ar[lbl]/num_count[lbl]
    global stat_ar
    stat_ar = aspect_ratios[:]
    print aspect_ratios
    '''

    avg_down_len = []
    sum_adl = []
    for a in range(0,10):
        ab = []
        for b in range(0,int(dec*width*height)):
            ab.append(0)
        avg_down_len.append(ab)
        sum_adl.append(ab)

    for c in range(0,int(dec*len(data))):
        lbl = label[c]
        feature = extract_advanced_features(data[c], width, height)
        for d in range(0,len(feature)):
            sum_adl[lbl][d] = sum_adl[lbl][d] + feature[d]
    for e in range(0,int(dec*len(data))):
        lbl = label[e]
        for f in range(0,len(feature)):
            avg_down_len[lbl][f] = sum_adl[lbl][f]/num_count[lbl]    
    global stat_avg_down_len
    stat_avg_down_len = avg_down_len[:]
    print sum_adl
    print avg_down_len
    _raise_not_defined()

'''
For the given features for a single digit image, compute the class 
'''
def compute_class(features):
    predicted = -1
    ar = features[0]
    mini = 100
    for i in range(0,len(stat_ar)):
        val = stat_ar[i] - ar
        if val < mini:
            mini = i 
    predicted = mini
    #_raise_not_defined()
    return predicted

'''
Compute joint probaility for all the classes and make predictions for a list
of data
'''
def classify(data, width, height, feature_extractor):

    predicted=[]
    for i in range(0, len(data)):
        features = feature_extractor(data[i],width,height)
        predicted.append(compute_class(features))

    #_raise_not_defined()
    return predicted







        
    
