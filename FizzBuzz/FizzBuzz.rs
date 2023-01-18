fn fizzbuzz(nums: u16) -> String {
    let mut fizzbuzz_temp: String = String::new();
    for num in 1..nums {
        if num % 3 == 0 && num % 5 == 0 {
            fizzbuzz_temp.push_str(" FizzBuzz ");
        } else if num % 3 == 0 {
            fizzbuzz_temp.push_str(" Fizz ");
        } else if num % 5 == 0 {
            fizzbuzz_temp.push_str(" Buzz ");
        } else {
            fizzbuzz_temp.push_str(&format!(" {} ", &num.to_string()));
        }
    }
    return fizzbuzz_temp.trim().to_string();
}

fn main() {
    let num: u16 = 100;
    println! {"{}", fizzbuzz(num)};
}
