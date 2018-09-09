import numpy as np
def outliers_whiskers(feature_name=None, df=None, l_whis=1.5, u_whis=1.5):
    # apply after cluster but w/o exclude bad range
    Throw_Feature = df[feature_name]
    quartile_1, median, quartile_3 = 25 , 50, 75
    Q1, median, Q3 = np.percentile(np.asarray(Throw_Feature), [quartile_1, median, quartile_3])
    IQR = Q3 - Q1
    loval = Q1 - 1.5 * IQR
    hival = Q3 + 1.5 * IQR
    wisklo = np.compress(Throw_Feature >= loval, Throw_Feature)
    wiskhi = np.compress(Throw_Feature <= hival, Throw_Feature)
    lower_bound = np.min(wisklo)
    upper_bound = np.max(wiskhi)
    return (lower_bound, upper_bound)
