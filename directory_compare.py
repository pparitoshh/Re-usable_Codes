from filecmp import dircmp
def print_diff_files(dcmp):
    for name in dcmp.diff_files:
        print("diff_file %s found in %s and %s" % (name, dcmp.left,dcmp.right))
    for sub_dcmp in dcmp.subdirs.values():
        print_diff_files(sub_dcmp)

dcmp = dircmp('D:/py_proj/vqa-winner-cvprw-2017-master_v2/data', 'D:/py_proj/vqa-winner-cvprw-2017-master/data') 
print_diff_files(dcmp) 
