fn fizzbuzz(nums: u16) -> String {
    let mut fizzbuzz_temp: String = String::new();
    for num in 1..nums {
        if num % 3 == 0 && num % 5 == 0 {
            let num_str: &str = &num.to_string();
            fizzbuzz_temp.push('\n');
            // fizzbuzz_temp.push_str(f!("({num_str}) fizzbuzz")); // using fstrings
            fizzbuzz_temp.push_str(&format!("({}) fizzbuzz", num_str));
        } else if num % 5 == 0 {
            let num_str: &str = &num.to_string();
            fizzbuzz_temp.push('\n');
            // fizzbuzz_temp.push_str(f!("({num_str}) buzz")); // using fstrings
            fizzbuzz_temp.push_str(&format!("({}) buzz", num_str));
        } else if num % 3 == 0 {
            let num_str: &str = &num.to_string();
            fizzbuzz_temp.push('\n');
            // fizzbuzz_temp.push_str(f!("({num_str}) fizz")); // using fstrings
            fizzbuzz_temp.push_str(&format!("({}) fizz", num_str));
        } else {
            let num_str: &str = &num.to_string();
            fizzbuzz_temp.push('\n');
            fizzbuzz_temp.push_str(num_str);
        }
    }
    return fizzbuzz_temp;
}

fn main() {
    let num: u16 = 100;
    println! {"{}", fizzbuzz(num)};
}
