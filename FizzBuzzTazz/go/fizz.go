package fizzbuzz

func fizzbuzz(n int) string {
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
