package fizzbuzz

func fizzbuzz(n int) (str string) {
	str = fizzbuzzNaive(n)
	str = fizzbuzzBetter(n)

	return
}

func fizzbuzzBetter(n int) (str string) {
	if n == 0 {
		return
	}

	fizzDuo := []struct {
		divider int
		str     string
	}{
		{3, "Fizz"},
		{5, "Buzz"},
		{7, "Tazz"},
		{11, "Mozz"},
		{13, "Vezz"},
	}

	for _, element := range fizzDuo {
		if n%element.divider == 0 {
			str += element.str
		}
	}

	return
}

func fizzbuzzNaive(n int) string {
	str := ""
	if n == 0 {
		return str
	}
	if n%3 == 0 {
		str += "Fizz"
	}
	if n%5 == 0 {
		str += "Buzz"
	}
	if n%7 == 0 {
		str += "Tazz"
	}
	if n%11 == 0 {
		str += "Mozz"
	}
	if n%13 == 0 {
		str += "Vezz"
	}
	return str
}
