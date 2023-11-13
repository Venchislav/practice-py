def rotate_words(str_):
    return ' '.join([i for i in str_.split()][::-1])
	

print(rotate_words('I am coding from phone as electricity is shut down at the moment'))
# moment the at down shut is electricity as phone from coding am I
