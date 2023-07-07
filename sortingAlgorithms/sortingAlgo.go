package main

import "fmt"

type Integer interface {
	int | int8 | int16 | int32 | int64
}

type UInteger interface {
	uint | uint8 | uint16 | uint32 | uint64 | uintptr
}

type Float interface {
	float32 | float64
}

type NumericTypes interface {
	Integer | UInteger | Float
}

type Options struct {
	sortby string
}

type SortAlgorithms[Numeric NumericTypes] struct {
	arr         []Numeric
	first_index int
	last_index  int
	options     *Options
}

func (sort *SortAlgorithms[Numeric]) quickSort(arr []Numeric, first_index int, last_index int) {
	if first_index < last_index {
		pivot := arr[last_index]
		idx := first_index - 1
		for i := first_index; i <= last_index-1; i++ {
			if arr[i] < pivot {
				idx++
				arr[idx], arr[i] = arr[i], arr[idx]
			}
		}
		arr[idx+1], arr[last_index] = arr[last_index], arr[idx+1]
		partition_index := idx + 1
		sort.quickSort(arr, first_index, partition_index-1)
		sort.quickSort(arr, partition_index+1, last_index)
	}
}

func (sort *SortAlgorithms[Numeric]) reverse(arr []Numeric) {
	for i, j := 0, len(arr)-1; i < j; i, j = i+1, j-1 {
		arr[i], arr[j] = arr[j], arr[i]
	}
}

func (sort *SortAlgorithms[Numeric]) reverseQuickSort(arr []Numeric, first_index int, last_index int) {
	sort.quickSort(sort.arr, sort.first_index, sort.last_index)
	sort.reverse(arr)
}

func (sort *SortAlgorithms[Numeric]) QuickSort() {
	switch sort.options.sortby {
	case "asc", "ascending":
		sort.quickSort(sort.arr, sort.first_index, sort.last_index)
	case "desc", "descending":
		sort.reverseQuickSort(sort.arr, sort.first_index, sort.last_index)
	default:
		sort.quickSort(sort.arr, sort.first_index, sort.last_index)
	}
}

func Sort[Numeric NumericTypes](arr []Numeric, options Options) *SortAlgorithms[Numeric] {
	sort := &SortAlgorithms[Numeric]{
		arr:         arr,
		first_index: 0,
		last_index:  len(arr) - 1,
		options:     &options,
	}
	return sort
}

func main() {
	arr := []int{10, 7, 8, 9, 1, 5}
	opt := Options{}
	newArr := Sort[int](arr, opt)
	newArr.QuickSort()
	fmt.Println(arr)

	arr2 := []float32{10, 7, 8, 9, 1, 5, 0, -10, -12, 10.003, 10.75, 11.21, -19.33}
	newArr2 := Sort[float32](arr2, opt)
	newArr2.QuickSort()
	fmt.Println(arr2)

	arr3 := []float32{10, 7, 8, 9, 1, 5, 0, -10, -12, 10.003, 10.75, 11.21, -19.33}
	optDesc := Options{sortby: "desc"}
	newArr3 := Sort[float32](arr3, optDesc)
	newArr3.QuickSort()
	fmt.Println(arr3)
}
