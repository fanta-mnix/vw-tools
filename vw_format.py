def formatter(tagger, label=None, numerical=None, categorical=None, boolean=None):
    numerical = numerical or ()
    categorical = categorical or ()
    boolean = boolean or ()
    
    n_num = len(numerical)
    n_cat = len(categorical)
    
    def to_vw(row):
        lhs = "{} {}".format(row[label], tagger(row)) if label else tagger(row)
        num = ' '.join("|{} {}:{}".format(chr(ord('a') + i), name, row[name]) for i, name in enumerate(numerical))
        cat = ' '.join("|{} {}={}".format(chr(ord('a') + n_num + i), name, row[name]) for i, name in enumerate(categorical))
        bol = ' '.join("|{} {}".format(chr(ord('a') + n_num + n_cat + i), name) for i, name in enumerate(boolean) if row[name])
        return lhs + ' '.join(one for one in [num, cat, bol] if one)
    
    return to_vw
