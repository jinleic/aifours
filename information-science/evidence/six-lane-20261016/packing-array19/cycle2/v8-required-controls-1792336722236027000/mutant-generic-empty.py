def structural_acceptance(c, ca):
    if not (type(ca['b_index']) is int and True and (type(ca['list']['n']) is int) and (ca['list']['n'] == 0) and (c['skeleton_sha256'] == SKELETON_SHA) and (ca['list']['sha256'] == B3.EXPECTED['empty_list_receipt']['sha256'])):
        return {'accepted': False, 'scope': 'no generic empty-cover acceptance'}
    return B3.verify()
