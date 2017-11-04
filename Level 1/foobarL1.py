import string
def answer(s):
    # your code here
	x = string.ascii_lowercase
	y = x[::-1]
	s = list(s)
	decode ={}
	for i in range(len(x)):
		decode[x[i]] = y[i]

	for i in range(len(s)):
		if s[i] in x:
			s[i] = decode[s[i]]

	s = ''.join(s)
	return s

#answer("Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!")
