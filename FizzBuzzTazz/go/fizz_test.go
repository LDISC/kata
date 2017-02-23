package fizzbuzz

import (
	"strconv"
	"testing"
)

func Test_fizzbuzz(t *testing.T) {
	tests := []struct {
		in   int
		want string
	}{
		{0, ""},
		{1, ""},
		{2, ""},
		{4, ""},
		{3, "Fizz"},
		{6, "Fizz"},
		{5, "Buzz"},
		{10, "Buzz"},
		{7, "Tazz"},
		{14, "Tazz"},
		{15, "FizzBuzz"},
		{30, "FizzBuzz"},
		{21, "FizzTazz"},
		{42, "FizzTazz"},
		{35, "BuzzTazz"},
		{70, "BuzzTazz"},
		{105, "FizzBuzzTazz"},
		{210, "FizzBuzzTazz"},
		{11, "Mozz"},
		{22, "Mozz"},
		{33, "FizzMozz"},
		{66, "FizzMozz"},
		{55, "BuzzMozz"},
		{110, "BuzzMozz"},
		{77, "TazzMozz"},
		{154, "TazzMozz"},
		{165, "FizzBuzzMozz"},
		{330, "FizzBuzzMozz"},
		{231, "FizzTazzMozz"},
		{462, "FizzTazzMozz"},
		{385, "BuzzTazzMozz"},
		{770, "BuzzTazzMozz"},
		{1155, "FizzBuzzTazzMozz"},
		{2310, "FizzBuzzTazzMozz"},
		{13, "Vezz"},
		{26, "Vezz"},
		{39, "FizzVezz"},
		{78, "FizzVezz"},
		{65, "BuzzVezz"},
		{130, "BuzzVezz"},
		{91, "TazzVezz"},
		{182, "TazzVezz"},
		{143, "MozzVezz"},
		{286, "MozzVezz"},
		{195, "FizzBuzzVezz"},
		{390, "FizzBuzzVezz"},
		{273, "FizzTazzVezz"},
		{546, "FizzTazzVezz"},
		{429, "FizzMozzVezz"},
		{858, "FizzMozzVezz"},
		{455, "BuzzTazzVezz"},
		{910, "BuzzTazzVezz"},
		{715, "BuzzMozzVezz"},
		{1430, "BuzzMozzVezz"},
		{1001, "TazzMozzVezz"},
		{2002, "TazzMozzVezz"},
		{1365, "FizzBuzzTazzVezz"},
		{2730, "FizzBuzzTazzVezz"},
		{2145, "FizzBuzzMozzVezz"},
		{4290, "FizzBuzzMozzVezz"},
		{3003, "FizzTazzMozzVezz"},
		{6006, "FizzTazzMozzVezz"},
		{5005, "BuzzTazzMozzVezz"},
		{10010, "BuzzTazzMozzVezz"},
		{15015, "FizzBuzzTazzMozzVezz"},
		{30030, "FizzBuzzTazzMozzVezz"},
	}
	for _, tt := range tests {
		t.Run(strconv.Itoa(tt.in), func(t *testing.T) {
			if got := fizzbuzz(tt.in); got != tt.want {
				t.Errorf("fizzbuzz() = %v, want %v", got, tt.want)
			}
		})
	}
}
